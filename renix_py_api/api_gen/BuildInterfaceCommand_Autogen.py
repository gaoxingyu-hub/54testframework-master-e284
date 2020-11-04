"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class BuildInterfaceCommand(ROMCommand):
    def __init__(self, InterfaceList=None, NetworkLayers=None, TopLayers=None, **kwargs):
        self._InterfaceList = InterfaceList  # Interfaces
        self._NetworkLayers = NetworkLayers  # Network Layer String List
        self._TopLayers = TopLayers  # Top Layer String List

        properties = kwargs.copy()
        if InterfaceList is not None:
            properties['InterfaceList'] = InterfaceList
        if NetworkLayers is not None:
            properties['NetworkLayers'] = NetworkLayers
        if TopLayers is not None:
            properties['TopLayers'] = TopLayers

        # call base class function, and it will send message to renix server to create a class.
        super(BuildInterfaceCommand, self).__init__(**properties)

    @property
    def InterfaceList(self):
        """
        get the value of property _InterfaceList
        """
        return self._InterfaceList

    @property
    def NetworkLayers(self):
        """
        get the value of property _NetworkLayers
        """
        return self._NetworkLayers

    @property
    def TopLayers(self):
        """
        get the value of property _TopLayers
        """
        return self._TopLayers

    @InterfaceList.setter
    def InterfaceList(self, value):
        self._InterfaceList = value

    @NetworkLayers.setter
    def NetworkLayers(self, value):
        self._NetworkLayers = value

    @TopLayers.setter
    def TopLayers(self, value):
        self._TopLayers = value

    def _set_interfacelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._InterfaceList = tmp_value.split()

    def _set_networklayers_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._NetworkLayers = tmp_value.split()

    def _set_toplayers_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._TopLayers = tmp_value.split()

