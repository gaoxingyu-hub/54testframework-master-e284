"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Dhcpv4ClientStats(Result):
    def __init__(self, **kwargs):
        self._ClientHandle = ''  # Client Name, not editable
        self._SessionIndex = 0  # Session Index, not editable
        self._ClientState = ''  # Client State, not editable
        self._IpAddress = '0.0.0.0'  # IP Address, not editable
        self._LeaseTime = 0  # Lease Time (sec), not editable
        self._LeaseLeft = 0  # Lease Left (sec), not editable
        self._ErrorStatus = ''  # Error Status, not editable
        self._DiscoverResponseTime = 0  # Discover Response Time (us), not editable
        self._RequestResponseTime = 0  # Request Response Time (us), not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4ClientStats, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def ClientHandle(self):
        """
        get the value of property _ClientHandle
        """
        if self.force_auto_sync:
            self.get('ClientHandle')
        return self._ClientHandle

    @property
    def SessionIndex(self):
        """
        get the value of property _SessionIndex
        """
        if self.force_auto_sync:
            self.get('SessionIndex')
        return self._SessionIndex

    @property
    def ClientState(self):
        """
        get the value of property _ClientState
        """
        if self.force_auto_sync:
            self.get('ClientState')
        return self._ClientState

    @property
    def IpAddress(self):
        """
        get the value of property _IpAddress
        """
        if self.force_auto_sync:
            self.get('IpAddress')
        return self._IpAddress

    @property
    def LeaseTime(self):
        """
        get the value of property _LeaseTime
        """
        if self.force_auto_sync:
            self.get('LeaseTime')
        return self._LeaseTime

    @property
    def LeaseLeft(self):
        """
        get the value of property _LeaseLeft
        """
        if self.force_auto_sync:
            self.get('LeaseLeft')
        return self._LeaseLeft

    @property
    def ErrorStatus(self):
        """
        get the value of property _ErrorStatus
        """
        if self.force_auto_sync:
            self.get('ErrorStatus')
        return self._ErrorStatus

    @property
    def DiscoverResponseTime(self):
        """
        get the value of property _DiscoverResponseTime
        """
        if self.force_auto_sync:
            self.get('DiscoverResponseTime')
        return self._DiscoverResponseTime

    @property
    def RequestResponseTime(self):
        """
        get the value of property _RequestResponseTime
        """
        if self.force_auto_sync:
            self.get('RequestResponseTime')
        return self._RequestResponseTime

    def _set_clienthandle_with_str(self, value):
        self._ClientHandle = value

    def _set_sessionindex_with_str(self, value):
        try:
            self._SessionIndex = int(value)
        except ValueError:
            self._SessionIndex = hex(int(value, 16))

    def _set_clientstate_with_str(self, value):
        self._ClientState = value

    def _set_ipaddress_with_str(self, value):
        self._IpAddress = value

    def _set_leasetime_with_str(self, value):
        try:
            self._LeaseTime = int(value)
        except ValueError:
            self._LeaseTime = hex(int(value, 16))

    def _set_leaseleft_with_str(self, value):
        try:
            self._LeaseLeft = int(value)
        except ValueError:
            self._LeaseLeft = hex(int(value, 16))

    def _set_errorstatus_with_str(self, value):
        self._ErrorStatus = value

    def _set_discoverresponsetime_with_str(self, value):
        self._DiscoverResponseTime = float(value)

    def _set_requestresponsetime_with_str(self, value):
        self._RequestResponseTime = float(value)

