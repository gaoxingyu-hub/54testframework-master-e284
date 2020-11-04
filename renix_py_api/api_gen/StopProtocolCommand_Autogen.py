"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class StopProtocolCommand(ROMCommand):
    def __init__(self, ProtocolList=None, **kwargs):
        self._ProtocolList = ProtocolList  # Protocol Configuration Handles

        properties = kwargs.copy()
        if ProtocolList is not None:
            properties['ProtocolList'] = ProtocolList

        # call base class function, and it will send message to renix server to create a class.
        super(StopProtocolCommand, self).__init__(**properties)

    @property
    def ProtocolList(self):
        """
        get the value of property _ProtocolList
        """
        return self._ProtocolList

    @ProtocolList.setter
    def ProtocolList(self, value):
        self._ProtocolList = value

    def _set_protocollist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ProtocolList = tmp_value.split()

