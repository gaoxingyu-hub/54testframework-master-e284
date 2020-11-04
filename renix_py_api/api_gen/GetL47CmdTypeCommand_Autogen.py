"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class GetL47CmdTypeCommand(ROMCommand):
    def __init__(self, ProtocolType=None, **kwargs):
        self._ProtocolType = ProtocolType  # Protocol Type
        self._CommandTypes = None  # Available command types, not editable

        properties = kwargs.copy()
        if ProtocolType is not None:
            properties['ProtocolType'] = ProtocolType

        # call base class function, and it will send message to renix server to create a class.
        super(GetL47CmdTypeCommand, self).__init__(**properties)

    @property
    def ProtocolType(self):
        """
        get the value of property _ProtocolType
        """
        return self._ProtocolType

    @property
    def CommandTypes(self):
        """
        get the value of property _CommandTypes
        """
        return self._CommandTypes

    @ProtocolType.setter
    def ProtocolType(self, value):
        self._ProtocolType = value

    def _set_protocoltype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ProtocolType = ProtocolType.%s' % value[:seperate])

    def _set_commandtypes_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._CommandTypes = tmp_value.split()

    def _set_output_property(self, value):
        self._set_commandtypes_with_str(value)

