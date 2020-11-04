"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ConfigPortsLinkCommand(ROMCommand):
    def __init__(self, PortList=None, EnableLink=None, **kwargs):
        self._PortList = PortList  # Port Handles
        self._EnableLink = EnableLink  # Link

        properties = kwargs.copy()
        if PortList is not None:
            properties['PortList'] = PortList
        if EnableLink is not None:
            properties['EnableLink'] = EnableLink

        # call base class function, and it will send message to renix server to create a class.
        super(ConfigPortsLinkCommand, self).__init__(**properties)

    @property
    def PortList(self):
        """
        get the value of property _PortList
        """
        return self._PortList

    @property
    def EnableLink(self):
        """
        get the value of property _EnableLink
        """
        return self._EnableLink

    @PortList.setter
    def PortList(self, value):
        self._PortList = value

    @EnableLink.setter
    def EnableLink(self, value):
        self._EnableLink = value

    def _set_portlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PortList = tmp_value.split()

    def _set_enablelink_with_str(self, value):
        self._EnableLink = (value == 'True')

