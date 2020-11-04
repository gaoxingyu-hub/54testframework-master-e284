from .renix_common_api import *
from .rom_manager import ROMManager
from gevent import socket
import gevent
from enum import Enum
try:
    from enum import Flag
except:
    from .renix_enum import Flag


class EnumRelationDirection(Enum):
    SOURCE = 1
    TARGET = 2


def return_str(obj):
    ret = ""
    if isinstance(obj, list):
        for o in obj:
            ret = ret + return_str(o) + " "
        ret = '{' + ret + '}'
    elif isinstance(obj, tuple):
        for o in obj:
            ret = ret + return_str(o) + " "
    elif isinstance(obj, dict):
        for k, v in obj.items():
            ret = ret + return_str(k) + " "
            ret = ret + return_str(v) + " "
    elif isinstance(obj, str):
        ret = str(obj).strip()
        if ret.find(' ') > 0:
            ret = '{' + ret + '}'
        if ret == '':
            ret = '{}'
    elif isinstance(obj, Flag):
        pass
    elif isinstance(obj, Enum):
        ret = str(obj).strip()
        rets = ret.split('.')
        ret = rets[1]
    else:
        ret = str(obj)

    return ret


class Core(object):
    def __init__(self, force_auto_sync=True, handle=None, upper=None, **kwargs):
        """
        create an ROM-Object
        :param handle: inform CL to create an object,if handle is '', or get the object with handle if handle is not ''
        :param kwargs: tuple of property name and property value
        """
        self.force_auto_sync = force_auto_sync
        self.handle = handle
        self.lower = []
        self.upper = upper
        self.relatives = {}

        if self.handle is None:
            prop_list = []
            for prop_name, prop_value in kwargs.items():
                tmp_msg = ' -{} {}'.format(prop_name, return_str(prop_value))
                prop_list.append(tmp_msg)

            prop_str = ' '.join(prop_list)
            if self.upper is None:
                msg = 'xet-create {} {}'.format(self.cls_name(), prop_str)
            else:
                msg = 'xet-create {} -upper {} {}'.format(self.cls_name(), self.upper.handle, prop_str)

            ret, data = self._send_msg(msg)
            if ret and data:
                self.handle = data
                renix_debug('Create {} successfully with handle {}'.format(self.cls_name(), self.handle))
            else:
                renix_error('Create {} failed, {}'.format(self.cls_name(), data))
                raise NotImplementedError('Create {} failed, {}'.format(self.cls_name(), data))

        self.get()
        ROMManager.add_object(self.handle, self)

    def _finalize(self):
        msg = 'xet-remove {}'.format(self.handle)
        ret, data = self._send_msg(msg)
        if ret:
            ROMManager.remove_object(self.handle)
            renix_debug('Delete {} successfully'.format(self.handle))
            for child in self.lower:
                ROMManager.remove_object(child.handle)

            return True, ''
        else:
            renix_error('Failed to delete {}.'.format(self.handle))
            return False, data

    def delete(self):
        """
        call to delete itself, its child nodes will be delete at the same time
        :return:
        """
        renix_info('Delete {}, its child nodes will be delete.'.format(self.handle))
        return self._finalize()

    def edit(self, **kwargs):
        """
        modify properties of Renix Python API class
        :param kwargs: it contains properties to modify,
        :return:
        """
        # modify property value
        # Check if there are properties in the edit list.
        if len(kwargs) <= 0:
            renix_warn('No properties in the edit list.')
            return

        prop_list = []
        for prop_name, prop_value in kwargs.items():
            tmp_msg = ' -{} {}'.format(prop_name, return_str(prop_value))
            prop_list.append(tmp_msg)

        prop_str = ' '.join(prop_list)
        msg = 'xet-edit {} {}'.format(self.handle, prop_str)
        renix_debug('{} with handle({}) edit properties'.format(self.cls_name(), self.handle))
        ret, data = self._send_msg(msg)
        if not ret:
            raise ValueError('{} edit properties failed with properties list[{}], {}'.format(self.handle, prop_str, data))

    def get(self, *args, update_child=True):
        """
        get properties of this class
        :param args:  the properties name of this renix python api class
        :param update_child: if True, update its children
        :return: properties values associate with properties name in parameter args
        """
        renix_debug('Get properties of {}'.format(self.handle))
        msg = 'xet-get {}'.format(self.handle)

        if len(args) > 0:
            # get one or more of properties of this rom-object
            for prop in args:
                tmp_str = '{} -{}'.format(msg, str(prop))
                ret, data = self._send_msg(tmp_str)
                if ret is not False:
                    try:
                        func = getattr(self, '_set_{}_with_str'.format(str(prop).lower()))
                        func(data)
                    except Exception:
                        renix_error('{} has no property named {}'.format(self.cls_name(), str(prop)))
                else:
                    raise ValueError('{}get property: {} failed, {}'.format(self.handle, str(prop), data))
            else:
                return True
        else:
            # get all properties of this rom-object
            ret, data = self._send_msg(msg)
            if ret:
                self.__set_properties_value_with_str(data, update_child)
                return True
            else:
                raise ValueError('{} get properties failed, data'.format(self.handle, data))

    def __set_properties_value_with_str(self, msg, update_child):
        """
        used to set property value
        :param msg: message received from Renix server which consist of property name and proeprty value
        :return:
        """
        values = msg.strip().split()
        i = 0
        while i < len(values):
            prop_name = values[i].replace('-', '', 1)
            val = values[i + 1].strip()
            prop_value = val
            i += 2
            if val.startswith('"'):
                if len(val) > 1 and val[-1] == '"':  # value is ""
                    prop_value = prop_value[1:-1].strip()  # remove ""
                else:  # prop value is a list
                    val_list = []
                    val_list.append(val[1:].strip())  # remove " in the prop_value begin position
                    while i < len(values):
                        val = values[i].strip()
                        i += 1
                        if val[-1] == '"' and (i >= len(values) or values[i].startswith('-')):
                            val_list.append(val[:-1].strip())
                            break
                        val_list.append(val)

                    prop_value = ' '.join(val_list)

            if prop_name == 'lower':
                if update_child:
                    relative_handles = prop_value.split()
                    self.lower = []
                    for relative_handle in relative_handles:
                        relative = self.__create_relative_object_from_handle(relative_handle, update_child)
                        if relative:
                            relative.upper = self
                            self.lower.append(relative)
                        else:
                            renix_error('Cannot find lower node with handle{} for '.format(relative_handle, self.handle))
                            raise RuntimeError(
                                'Cannot find lower node with handle{} for '.format(relative_handle, self.handle))
                else:
                    renix_info('{} has lower: {}'.format(self.handle, prop_value))
            else:
                try:
                    func = getattr(self, '_set_{}_with_str'.format(str(prop_name).lower()))
                    func(prop_value)
                except Exception:
                    renix_error('{} has no property named {}'.format(self.cls_name(), str(prop_name)))

    def get_handle(self):
        """
        get the handle of the renix api class
        :return: return the handle of this renix python api class
        """
        return self.handle

    def _get_target_objects(self, relation_name, relative_name=None):
        """
        get all target relatives that match the relation name and relative name
        :param relation_name:
        :param relative_name: target relative class name
        :return: return all target relatives that match the relation name, or False if failed to get target relatives
        """
        msg = 'xet-get {} -{}-to'.format(self.handle, relation_name)
        if relative_name and relative_name != '':
            msg = '{}-{}'.format(msg, relative_name)
        ret, data = self._send_msg(msg)
        if ret:
            relative_handles = data.strip().split()
            ret_relatives = []
            if not relative_name or relative_name not in self.relatives:
                self.relatives[relation_name] = []
            for relative_handle in relative_handles:
                relative = self.__create_relative_object_from_handle(relative_handle, False)
                if not relative:
                    raise ValueError('{} cannot find target object with handle{}'.format(self.handle, relative_handle))
                ret_relatives.append(relative)
                if relative not in self.relatives[relation_name]:
                    self.relatives[relation_name].append(relative)

            return ret_relatives
        else:
            raise RuntimeError('{} failed get target object with relation-name: {}, {}'.format(self.handle, relation_name, data))

    def _get_source_objects(self, relation_name, relative_name=None):
        """
        get all source relatives that match the relation name
        :param relation_name:
        :param relative_name: source relatives class name
        :return: return all source relatives that match the relation name, or False if failed to get source relatives
        """
        msg = 'xet-get {} -{}-from'.format(self.handle, relation_name)
        if relative_name:
            msg = '{}-{}'.format(msg, relative_name)
        ret, data = self._send_msg(msg)
        if ret:
            relative_handles = data.strip().split()
            ret_relatives = []
            if not relative_name or relative_name not in self.relatives:
                self.relatives[relation_name] = []
            for relative_handle in relative_handles:
                relative = self.__create_relative_object_from_handle(relative_handle, False)
                if not relative:
                    raise ValueError('{} cannot find source object with handle{}'.format(self.handle, relative_handle))
                ret_relatives.append(relative)
                if relative not in self.relatives[relation_name]:
                    self.relatives[relation_name].append(relative)
            return ret_relatives
        else:
            raise RuntimeError('{} failed get source object with relation-name: {}, {}'.format(self.handle, relation_name, data))

    def get_children(self, relative_name=None):
        """
        get child nodes
        :param relative_name: child class name
        :return: return all child nodes, or False if failed to get child nodes
        """
        msg = 'xet-get {} -lower'.format(self.handle)
        if relative_name:
            msg = '{}-{}'.format(msg, relative_name)
        ret, data = self._send_msg(msg)
        if ret:
            relative_handles = data.strip().split()
            if not relative_name:
                self.lower = []
            ret_childen = []
            for relative_handle in relative_handles:
                relative = self.__create_relative_object_from_handle(relative_handle, False)
                if not relative:
                    raise ValueError('Cannot find child with handle{} for {}'.format(relative_handle, self.handle))

                ret_childen.append(relative)
                if relative not in self.lower:
                    self.lower.append(relative)

            return ret_childen
        else:
            raise RuntimeError('{}Failed get child nodes'.format(self.handle))

    def get_parent(self):
        """
        get upper node
        :return: return parent node,or False if failed to get parent node
        """
        msg = 'xet-get {} -upper'.format(self.handle)
        ret, data = self._send_msg(msg)
        if ret:
            relative_handles = data.strip().split()
            if len(relative_handles) > 1:
                raise RuntimeError('{} get one more parent: {}'.format(self.handle, data))
            relative = self.__create_relative_object_from_handle(relative_handles[0], False)
            if relative:
                self.upper = relative
                return self.upper
            else:
                raise ValueError('Cannot find upper node with handle{} for {}'.format(relative_handles[0], self.handle))
        else:
            raise RuntimeError('{} failed get upper node, {}'.format(self.handle, data))

    def get_relatives(self, relation_name, direction=EnumRelationDirection.TARGET, relative_name=None):
        """
        get all relatives that match the relation name and direction
        :param relation_name:
        :param direction: 'to' if want to get target relatives, or 'from' if want to get source relatives
        :param relative_name:
        :return: return all source/target that match the relation name and direction
        """
        if relation_name.lower() == 'lower':
            return self.get_children(relative_name)
        elif relation_name.lower() == 'upper':
            return self.get_parent()
        if direction == EnumRelationDirection.TARGET:
            return self._get_target_objects(relation_name, relative_name)
        elif direction == EnumRelationDirection.SOURCE:
            return self._get_source_objects(relation_name, relative_name)
        else:
            raise RuntimeError('{} get {} with wrong direction {}.'.format(self.handle, relation_name, direction))

    def set_relatives(self, relation_name, relation_obj, direction=EnumRelationDirection.TARGET):
        """
        establish relation shown by relation name and direction between this class and another one
        :param relation_name:
        :param relation_obj:
        :param direction:
        :return:
        """
        msg = 'xet-edit {} -{}-'.format(self.handle, relation_name)
        if direction == EnumRelationDirection.SOURCE:
            msg = '{}from {}'.format(msg, relation_obj.handle)
        else:
            msg = '{}to {}'.format(msg, relation_obj.handle)
        ret, data = self._send_msg(msg)
        if not ret:
            raise RuntimeError('{} set relation: {} with {} {}failed, {}'.format(self.handle, relation_name, str(direction.name), relation_obj.handle, data))
        else:
            self.relatives[relation_name] = relation_obj
            return True

    def __create_relative_object_from_handle(self, relative_handle, update_child):
        """
        create an relative object with handle if object with handle does not exist
        :param relative_handle:
        :return:
        """
        relative = ROMManager.get_object(relative_handle, update_child)
        return relative

    def _send_msg(self, msg):
        RenixApiManager.send_msg(msg)

        return RenixApiManager.recv_msg()

    def set_force_auto_sync(self, value):
        self.force_auto_sync = value

    @classmethod
    def cls_name(cls):
        return cls.__name__


class Command:
    """
    base class of all command classes.
    """
    def __init__(self, show_return_value=False, **kwargs):
        self.args = []
        self.show_return_value = show_return_value

        for (prop_name, prop_value) in kwargs.items():
            tmp_arg = '-{} {}'.format(prop_name, return_str(prop_value))
            self.args.append(tmp_arg)

    def _send_msg(self, msg):
        RenixApiManager.send_msg(msg)
        return RenixApiManager.recv_msg()

    def execute(self):
        args_str = ' '.join(self.args)
        msg = 'xet-execute {} {}'.format(self.cls_name(), args_str)
        ret, ret_msg = self._send_msg(msg)
        if not ret:
            raise RuntimeError('Issue {} {} failed: {}'.format(self.cls_name(), args_str, ret_msg))
        else:
            if self.show_return_value:
                renix_info('{} return value : {}'.format(self.cls_name(), ret_msg if ret_msg else 'success'))
            if ret_msg:
                self._set_properties(ret_msg)

    def _set_properties(self, msg):
        if msg.find('-') != -1:
            values = msg.strip().split('-')
            values.remove('')
            for value in values:
                value = value.strip()
                separate = value.find(' ')
                prop_name = value[:separate].strip()
                prop_value = value[separate:].strip()
                if prop_value.startswith('"') and prop_value.endswith('"'):
                    prop_value = prop_value[1:-1].strip()  # remove ""
                if prop_value == '':
                    # renix_debug('{} is \'\''.format(prop_name))
                    continue
                try:
                    func = getattr(self, '_set_{}_with_str'.format(prop_name.lower()))
                    func(prop_value)
                except Exception:
                    renix_error('{} has no property named {}'.format(self.cls_name(), prop_name))

        else:
            self._set_output_property(msg.strip())

    def _set_output_property(self, value):
        pass

    @classmethod
    def cls_name(cls):
        return cls.__name__


class CaptureDataListener(object):
    _sock = None
    _started = False
    listen_port = 20000
    listen_task = None
    buffer = bytearray()
    position = 0
    callback = None

    @classmethod
    def start_listen(cls):
        if not cls._started:
            cls._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while 1:
                try:
                    cls._sock.bind(('127.0.0.1', cls.listen_port))
                    break
                except:
                    cls.listen_port += 1

            cls._started = True
            cls.listen_task = gevent.spawn(cls.run)

    @classmethod
    def stop(cls):
        try:
            cls._started = False
            if cls._sock:
                cls._sock.close()
            if cls.listen_task:
                cls.listen_task.kill()
        except:
            pass

    @classmethod
    def run(cls):
        try:
            while cls._started:
                cls.read_total_length()
                total_length = cls.read_u32()
                cls.read_body(total_length)
        except Exception as e:
            renix_error('Process real-time capture data fail: {}'.format(e))

    @classmethod
    def read_total_length(cls):
        to_read = 4
        while to_read > 0:
            data = cls._sock.recv(to_read)
            to_read -= len(data)
            cls.buffer.extend(data)
            cls.notify_data()

    @classmethod
    def notify_data(cls):
        if not cls.callback:
            return

        port_name_len = cls.read_u8()
        port_name = cls.read_buffer(''.join((str(port_name_len), 'B')), port_name_len)
        port_name = port_name.decode('utf-8')
        packet_count = cls.read_u16()
        packet_list = list()
        while packet_count > 0:
            sec = cls.read_u32()
            nsec = cls.read_u32()
            length = cls.read_u32()
            packet_data = cls.read_buffer(''.join((str(length), 'B')), port_name_len)
            packet_list.append((sec, nsec, length, packet_data))

        cls.callback(port_name, packet_list)

    @classmethod
    def read_body(cls, total_length):
        while total_length > 0:
            data = cls._sock.recv(total_length)
            total_length -= len(data)
            cls.buffer.extend(data)

    @classmethod
    def read(cls, pattern, length):
        s = struct.Struct(pattern)
        data, = s.unpack_from(cls.buffer, cls.position)
        cls.position += length
        return data

    @classmethod
    def read_buffer(cls, pattern, length):
        s = struct.Struct(pattern)
        data = s.unpack_from(cls.buffer, cls.position)
        cls.position += length
        return data

    @classmethod
    def read_u8(cls):
        return cls.read('B', 1)

    @classmethod
    def read_i8(cls):
        return cls.read('b', 1)

    @classmethod
    def read_u16(cls):
        return cls.read('!H', 2)

    @classmethod
    def read_i16(cls):
        return cls.read('!h', 2)

    @classmethod
    def read_u32(cls):
        return cls.read('!I', 4)

    @classmethod
    def read_i32(cls):
        return cls.read('!i', 4)

    @classmethod
    def read_u64(cls):
        return cls.read('!Q', 8)

    @classmethod
    def read_i64(cls):
        return cls.read('!q', 8)

    @classmethod
    def read_bool(cls):
        return cls.read('?', 1)

    @classmethod
    def read_double(cls):
        return cls.read('!d', 8)


