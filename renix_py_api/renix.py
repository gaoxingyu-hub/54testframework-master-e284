import time
from .renix_common_api import *
from .core import *
from .api_gen import *
from .rom_manager import *


def initialize(log=True, log_level=logging.INFO, log_handle=LogHandle.LOG_FILE_AND_CONSOLE, host='127.0.0.1', port=9001, timeout=30000):
    """
    Do some initialization work,such as initialize log file and connect to CL
    :param log: record renix api logs to file if log is True
    :param log_level: log level ,info by default
    :param log_handle: write log to file or console, or both
    :param host: the ip address of CL is running
    :param port: the listen port connected to CL
    :param timeout: the time waiting for connect CL successfully
    :return: the time waiting for connect CL successfully
    """
    # print('renix python api init begin')
    try:
        # if log:
        #     init_log(logging.INFO, LogHandle.LOG_FILE_AND_CONSOLE)

        # launch CL if it is not running
        port = RenixApiManager.start_server()
        if not port:
            renix_error('launch CL failed with listen port: '.format(port))
            return

        # connect to cl
        RenixApiManager.connection_init(host, port, timeout)

        # rom init
        RenixApiManager.rom_init()
        renix_info('Renix api initialization finished')
    except Exception as err:
        renix_error(traceback.format_exc())
        shutdown()
        raise RuntimeError(traceback)


@atexit.register
def shutdown():
    CaptureDataListener.stop()
    RenixApiManager.exit()


def register_capture_notify(port, callback):
    if not port:
        return False, 'Port is None'

    if not isinstance(port, Port):
        return False, 'Invalid object type, expect a Port object'

    CaptureDataListener.start_listen()
    if callback != CaptureDataListener.callback:
        CaptureDataListener.callback = callback

    capture_config = port.get_children(relative_name='CaptureConfig')[0]
    capture_config.edit(EnableRealtimeCapture=True)

    cmd = SubscribeRealtimeCaptureDataCommand(CaptureConfig=capture_config.handle,
                                              ListenPort=CaptureDataListener.listen_port,
                                              ListenIp='127.0.0.1')
    cmd.execute()


def wait_stream_stop(stream_cfg, wait_time=1000):
    """
    block until stream_cfg has been stopped after issue stop stream command,
    it will return after wait_time seconds even if stream_cfg is still running
    :param stream_cfg: stream instance
    :param wait_time: wait time for stream stop
    :return:
    """
    if isinstance(stream_cfg, StreamTemplate):
        while wait_time:
            stream_cfg.get('State')
            if stream_cfg.State == EnumState.READY:
                break
            else:
                wait_time -= 1
                time.sleep(1)
        else:
            renix_warn('wait stream {} stop timeout'.format(stream_cfg.Name))
    else:
        renix_warn('{} is not a stream'.format(stream_cfg.Name))
