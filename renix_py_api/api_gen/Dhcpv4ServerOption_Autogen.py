"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Dhcpv4Option_Autogen import Dhcpv4Option


@rom_manager.rom
class Dhcpv4ServerOption(Dhcpv4Option):
    def __init__(self, MessageType=None, **kwargs):
        self._MessageType = swap_int_to_enum_flag(MessageType, EnumDhcpv4ServerMessageType)  # Message Type

        properties = kwargs.copy()
        if MessageType is not None:
            if isinstance(MessageType, Flag):
                properties['MessageType'] = MessageType.value
            else:
                properties['MessageType'] = MessageType

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4ServerOption, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, MessageType=None, **kwargs):
        properties = kwargs.copy()
        if MessageType is not None:
            self._MessageType = swap_int_to_enum_flag(MessageType, EnumDhcpv4ServerMessageType)
            if isinstance(MessageType, Flag):
                properties['MessageType'] = MessageType.value
            else:
                properties['MessageType'] = MessageType

        super(Dhcpv4ServerOption, self).edit(**properties)

    @property
    def MessageType(self):
        """
        get the value of property _MessageType
        """
        if self.force_auto_sync:
            self.get('MessageType')
        return self._MessageType

    @MessageType.setter
    def MessageType(self, value):
        self._MessageType = swap_int_to_enum_flag(value, EnumDhcpv4ServerMessageType)
        if isinstance(value, Flag):
            self.edit(MessageType=value.value)
        else:
            self.edit(MessageType=value)

    def _set_messagetype_with_str(self, value):
        seperate = value.find(':')
        self._MessageType = swap_int_to_enum_flag(int(value[seperate+1:]), EnumDhcpv4ServerMessageType)

