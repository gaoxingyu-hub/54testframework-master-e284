"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SetPlConnectionToClCommand(ROMCommand):
    def __init__(self, PlAddress=None, PlPortToCl=None, ClListenPort=None, TestCaseName=None, LinkStatus=None, **kwargs):
        self._PlAddress = PlAddress  # Renix Client IP address
        self._PlPortToCl = PlPortToCl  # Renix Client connection port to renix server
        self._ClListenPort = ClListenPort  # Renix server listen port
        self._TestCaseName = TestCaseName  # Test Case Name
        self._LinkStatus = LinkStatus  # Link Status

        properties = kwargs.copy()
        if PlAddress is not None:
            properties['PlAddress'] = PlAddress
        if PlPortToCl is not None:
            properties['PlPortToCl'] = PlPortToCl
        if ClListenPort is not None:
            properties['ClListenPort'] = ClListenPort
        if TestCaseName is not None:
            properties['TestCaseName'] = TestCaseName
        if LinkStatus is not None:
            properties['LinkStatus'] = LinkStatus

        # call base class function, and it will send message to renix server to create a class.
        super(SetPlConnectionToClCommand, self).__init__(**properties)

    @property
    def PlAddress(self):
        """
        get the value of property _PlAddress
        """
        return self._PlAddress

    @property
    def PlPortToCl(self):
        """
        get the value of property _PlPortToCl
        """
        return self._PlPortToCl

    @property
    def ClListenPort(self):
        """
        get the value of property _ClListenPort
        """
        return self._ClListenPort

    @property
    def TestCaseName(self):
        """
        get the value of property _TestCaseName
        """
        return self._TestCaseName

    @property
    def LinkStatus(self):
        """
        get the value of property _LinkStatus
        """
        return self._LinkStatus

    @PlAddress.setter
    def PlAddress(self, value):
        self._PlAddress = value

    @PlPortToCl.setter
    def PlPortToCl(self, value):
        self._PlPortToCl = value

    @ClListenPort.setter
    def ClListenPort(self, value):
        self._ClListenPort = value

    @TestCaseName.setter
    def TestCaseName(self, value):
        self._TestCaseName = value

    @LinkStatus.setter
    def LinkStatus(self, value):
        self._LinkStatus = value

    def _set_pladdress_with_str(self, value):
        self._PlAddress = value

    def _set_plporttocl_with_str(self, value):
        try:
            self._PlPortToCl = int(value)
        except ValueError:
            self._PlPortToCl = hex(int(value, 16))

    def _set_cllistenport_with_str(self, value):
        try:
            self._ClListenPort = int(value)
        except ValueError:
            self._ClListenPort = hex(int(value, 16))

    def _set_testcasename_with_str(self, value):
        self._TestCaseName = value

    def _set_linkstatus_with_str(self, value):
        self._LinkStatus = (value == 'True')

