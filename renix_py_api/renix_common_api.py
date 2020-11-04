from os import sys
import os
import subprocess
import logging
import logging.handlers
import datetime
import platform
from gevent.socket import create_connection
import traceback
import struct
import importlib
import atexit
import enum

from common.logConfig import Logger


logger = Logger.module_logger("renix")
# logger = None
sys_entry = None


class LogHandle(enum.Enum):
    LOG_FILE = 0
    LOG_CONSOLE = 1
    LOG_FILE_AND_CONSOLE = 2


def init_log(log_level, log_handle):
    """
    crate log file and set log level
    :param log_level:
    :param log_handle:
    :return:
    """
    log_fmt = logging.Formatter("[%(levelname)s] %(asctime)s  %(message)s")
    current_path = '/var/log/renix_py_api'
    current_file_name = 'script'
    # create logs in user script folder, sys.argv[0] is the script path
    script_path = os.path.abspath(sys.argv[0])
    if os.path.isfile(script_path):
        current_path, current_file_name_ext = os.path.split(script_path)
        current_file_name, extention_name = current_file_name_ext.split('.')
    global logger
    logger = logging.getLogger(current_file_name)
    logger.setLevel(log_level)
    if log_handle == LogHandle.LOG_FILE or log_handle == LogHandle.LOG_FILE_AND_CONSOLE:
        log_folder_path = os.path.join(current_path, "logs")

        if not os.path.exists(log_folder_path):
            os.makedirs(log_folder_path)

        file_name = "%s_%s.log" % (current_file_name, datetime.datetime.now().strftime('%b_%d_%y_%H_%M_%S'))
        log_file_path = os.path.join(log_folder_path, file_name)

        log_file_handler = logging.handlers.RotatingFileHandler(log_file_path,
                                                                maxBytes=10 * 1024 * 1024,
                                                                backupCount=5)
        # log_file_handler.setLevel(log_level)
        log_file_handler.setFormatter(log_fmt)
        logger.addHandler(log_file_handler)

    if log_handle == LogHandle.LOG_CONSOLE or log_handle == LogHandle.LOG_FILE_AND_CONSOLE:
        control_handler = logging.StreamHandler()
        control_handler.setFormatter(log_fmt)

        logger.addHandler(control_handler)


def get_sys_entry():
    return sys_entry


def renix_error(msg):
    if logger:
        logger.error(msg)


def renix_warn(msg):
    if logger:
        logger.warning(msg)


def renix_info(msg):
    if logger:
        logger.info(msg)


def renix_debug(msg):
    if logger:
        logger.debug(msg)


class RenixApiManager(object):
    _connect_socket = None
    _connected = False
    _type_str = b'_TCL'

    @classmethod
    def connection_init(cls, host, port, timeout):
        cls._connect_socket = create_connection((host, port), timeout)
        if cls._connect_socket:
            cls._connected = True
        else:
            raise Exception('Connect to renix server timeout')

    @classmethod
    def rom_init(cls):
        importlib.import_module('renix_py_api.api_gen')
        # get sysentry
        from renix_py_api.api_gen.SysEntry_Autogen import SysEntry
        global sys_entry
        sys_entry = SysEntry(handle='SysEntry_1')

    @classmethod
    def close_connection(cls):
        if cls._connect_socket:
            cls._connect_socket.close()
            cls._connect_socket = None
            cls._connected = False
        renix_info('close connection to CL')

    @classmethod
    def _get_executable_name(cls):
        if platform.system() == 'Windows':
            return 'server.exe'
        else:
            return 'server'

    @classmethod
    def start_server(cls):
        # get cl file, server.py or server.exe
        # get module folder, __file__ is the full name of renix.py
        current_path = os.path.dirname(os.path.realpath(__file__))
        server_path = os.path.abspath(os.path.join(current_path, '../server.py'))
        # server_exe_path = os.path.abspath(os.path.join(current_path, '../{}'.format(cls._get_executable_name())))
        server_exe_path = r"D:\opt\renix\server\server.exe"
        renix_server_dir = os.environ.get('RENIX_SERVER_PATH')
        cmd = ''
        if os.path.exists(server_path):
            cmd = 'python -u {} -b -l i'.format(server_path)
        elif os.path.exists(server_exe_path):
            cmd = '\"{}\" -b -l i'.format(server_exe_path)
        elif renix_server_dir:
            renix_server_exe_path = os.path.abspath(os.path.join(renix_server_dir, cls._get_executable_name()))
            renix_server_script_path = os.path.abspath(os.path.join(renix_server_dir, 'server.py'))
            if os.path.exists(renix_server_exe_path):
                cmd = '\"{}\" -b -l i'.format(renix_server_exe_path)
            elif os.path.exists(renix_server_script_path):
                cmd = 'python -u {} -b -l i'.format(renix_server_script_path)
            else:
                raise RuntimeError('Failed to start renix server, cannot find renix server file in {}.'.format(renix_server_dir))
        else:
            raise RuntimeError('Failed to start renix server, cannot find renix server file.')

        # run cl and get listen port
        py_pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf8')
        line = py_pipe.stdout.readline()
        print(line)
        renix_info('Receive Msg: {}'.format(line))
        line = line.strip()
        key = 'listen_port'
        npos = line.find(key)
        if npos != -1:
            line = line[npos + len(key):]
            values = line.split()
            if len(values) > 0:
                port = values[0]
                if port.isdigit():
                    return int(port)
                else:
                    raise RuntimeError('get error listen port {}'.format(port))
            else:
                raise RuntimeError('failed to get listen port value.')
        else:
            raise RuntimeError('cannot find key word :{}'.format(key))

    @classmethod
    def exit(cls):
        """
        close Renix API if CL exit with exception
        :return:
        """
        cls.close_connection()

    @classmethod
    def __reader(cls):
        """
        get raw data received from CL.
        msg start with $$$ and end with ???
        first 4 bytes is the length of message without $$$???
        msg will deliver to function __format_recv_msg
        :return:  data without begin ,end flag($$$, ???) and data length if got useful message

        """
        try:
            data = b''
            while True:
                buf = cls._connect_socket.recv(2048)
                if len(buf) <= 0:
                    renix_error("Socket receive and return a null data")
                    break
                data = data + buf
                if len(data) > (3 + 4 + 3):
                    if data[0:3] == b'$$$':
                        length, = struct.unpack("i", data[3:7])
                        if (length + 3 + 3) <= len(data):
                            if data[(length + 3):(length + 6)] == b'???':
                                msg = data[(3 + 4):(length + 3)]
                                renix_debug('Receive Msg: %s' % data)
                                return cls.__format_recv_msg(msg)
                            else:
                                renix_error("Not end with '???', date is : %s" % data)
                                return False, 'Not end with ???'
                        else:
                            renix_debug('The length of data received is : %d, full data length is: %d, waiting more data ' % (len(data), length))
                    else:
                        renix_error("Error msg not start with $$$, date is : %s" % data)
                        return False, 'Error msg not start with $$$'
                else:
                    renix_debug('receive data length < 7, waiting more data')
        except:
            renix_error('Failed to read data from CL, close connection to CL.')
            cls.exit()

    @classmethod
    def __format_send_msg(cls, msg):
        """
        encode message, add begin and end flag , date length
        :param msg:
        :return:
        """
        data = msg
        if not isinstance(msg, bytes):
            data = bytes(msg, 'ascii')

        data = cls._type_str + data
        format_msg = b'$$$' + struct.pack('i', (len(data) + 4)) + data + b'???'

        return format_msg

    @classmethod
    def __format_recv_msg(cls, msg):
        if msg[0:4] == cls._type_str:
            ret_str = bytes.decode(msg[4:])
            if ret_str.startswith('ERROR'):
                renix_error(msg)
                return False, ret_str
            elif ret_str.startswith('SUCCESS'):
                return True, ''
            else:
                return True, ret_str
        else:
            renix_error("error message type with {new_type,old_type} %s" % {msg[0:4], cls._type_str})
            return False, msg

    @classmethod
    def send_msg(cls, msg):
        """
        send msg to CL
        :param msg: raw message that need send to CL
        :return: format message received from CL
        """
        try:
            if cls._connected:
                data = msg
                if not isinstance(msg, bytes):
                    data = bytes(msg, 'ascii')

                format_msg = cls.__format_send_msg(data)
                cls._connect_socket.sendall(format_msg)
                renix_debug("Send Msg: %s" % format_msg)
            else:
                renix_error('Connection to CL has been shutdown ,failed send msg: {}'.format(msg))
                cls.exit()
        except:
            renix_error('Send msg to CL failed')
            cls.exit()

    @classmethod
    def recv_msg(cls):
        """
        get return data from CL
        :return: False if data begin with 'ERROR', True if date begins with 'SUCCESS', real data if other case.
        """
        if cls._connected:
            return cls.__reader()
        else:
            renix_error('Failed receive message from CL,as connection to CL has been shutdown')
            cls.exit()



