"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class RestartAutoNegotiationCommand(ROMCommand):
    def __init__(self, PortList=None, **kwargs):
        self._PortList = PortList  # Port Handles

        properties = kwargs.copy()
        if PortList is not None:
            properties['PortList'] = PortList

        # call base class function, and it will send message to renix server to create a class.
        super(RestartAutoNegotiationCommand, self).__init__(**properties)

    @property
    def PortList(self):
        """
        get the value of property _PortList
        """
        return self._PortList

    @PortList.setter
    def PortList(self, value):
        self._PortList = value

    def _set_portlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PortList = tmp_value.split()

