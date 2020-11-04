"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SelectInterfaceCommand(ROMCommand):
    def __init__(self, ProtocolList=None, InterfaceList=None, **kwargs):
        self._ProtocolList = ProtocolList  # Protocol Handles
        self._InterfaceList = InterfaceList  # Interface Handles

        properties = kwargs.copy()
        if ProtocolList is not None:
            properties['ProtocolList'] = ProtocolList
        if InterfaceList is not None:
            properties['InterfaceList'] = InterfaceList

        # call base class function, and it will send message to renix server to create a class.
        super(SelectInterfaceCommand, self).__init__(**properties)

    @property
    def ProtocolList(self):
        """
        get the value of property _ProtocolList
        """
        return self._ProtocolList

    @property
    def InterfaceList(self):
        """
        get the value of property _InterfaceList
        """
        return self._InterfaceList

    @ProtocolList.setter
    def ProtocolList(self, value):
        self._ProtocolList = value

    @InterfaceList.setter
    def InterfaceList(self, value):
        self._InterfaceList = value

    def _set_protocollist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ProtocolList = tmp_value.split()

    def _set_interfacelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._InterfaceList = tmp_value.split()

