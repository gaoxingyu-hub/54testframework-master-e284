"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SendPortsLinkFaultCommand(ROMCommand):
    def __init__(self, PortList=None, Start=None, **kwargs):
        self._PortList = PortList  # Port Handles
        self._Start = Start  # Start

        properties = kwargs.copy()
        if PortList is not None:
            properties['PortList'] = PortList
        if Start is not None:
            properties['Start'] = Start

        # call base class function, and it will send message to renix server to create a class.
        super(SendPortsLinkFaultCommand, self).__init__(**properties)

    @property
    def PortList(self):
        """
        get the value of property _PortList
        """
        return self._PortList

    @property
    def Start(self):
        """
        get the value of property _Start
        """
        return self._Start

    @PortList.setter
    def PortList(self, value):
        self._PortList = value

    @Start.setter
    def Start(self, value):
        self._Start = value

    def _set_portlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PortList = tmp_value.split()

    def _set_start_with_str(self, value):
        self._Start = (value == 'True')

