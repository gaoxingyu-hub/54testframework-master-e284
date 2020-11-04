"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Dot1xPortStatistics(Result):
    def __init__(self, **kwargs):
        self._PortHandle = ''  # Port Name, not editable
        self._CurrentAuthenticatedAttempt = 0  # Currently Attempt, not editable
        self._CurrentAuthenticated = 0  # Currently Authenticated, not editable
        self._CurrentFailed = 0  # Currently Failed, not editable
        self._CurrentLogoff = 0  # Currently Logoff, not editable
        self._TotalAttempt = 0  # Total Attempt, not editable
        self._TotalAuthenticated = 0  # Total Authenticated, not editable
        self._TotalFailed = 0  # Total Fail, not editable
        self._TotalLogoff = 0  # Total Logoff, not editable
        self._TotalRetry = 0  # Total Retry Authenticated, not editable
        self._TotalRetransmit = 0  # Total Retransmit, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Dot1xPortStatistics, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def PortHandle(self):
        """
        get the value of property _PortHandle
        """
        if self.force_auto_sync:
            self.get('PortHandle')
        return self._PortHandle

    @property
    def CurrentAuthenticatedAttempt(self):
        """
        get the value of property _CurrentAuthenticatedAttempt
        """
        if self.force_auto_sync:
            self.get('CurrentAuthenticatedAttempt')
        return self._CurrentAuthenticatedAttempt

    @property
    def CurrentAuthenticated(self):
        """
        get the value of property _CurrentAuthenticated
        """
        if self.force_auto_sync:
            self.get('CurrentAuthenticated')
        return self._CurrentAuthenticated

    @property
    def CurrentFailed(self):
        """
        get the value of property _CurrentFailed
        """
        if self.force_auto_sync:
            self.get('CurrentFailed')
        return self._CurrentFailed

    @property
    def CurrentLogoff(self):
        """
        get the value of property _CurrentLogoff
        """
        if self.force_auto_sync:
            self.get('CurrentLogoff')
        return self._CurrentLogoff

    @property
    def TotalAttempt(self):
        """
        get the value of property _TotalAttempt
        """
        if self.force_auto_sync:
            self.get('TotalAttempt')
        return self._TotalAttempt

    @property
    def TotalAuthenticated(self):
        """
        get the value of property _TotalAuthenticated
        """
        if self.force_auto_sync:
            self.get('TotalAuthenticated')
        return self._TotalAuthenticated

    @property
    def TotalFailed(self):
        """
        get the value of property _TotalFailed
        """
        if self.force_auto_sync:
            self.get('TotalFailed')
        return self._TotalFailed

    @property
    def TotalLogoff(self):
        """
        get the value of property _TotalLogoff
        """
        if self.force_auto_sync:
            self.get('TotalLogoff')
        return self._TotalLogoff

    @property
    def TotalRetry(self):
        """
        get the value of property _TotalRetry
        """
        if self.force_auto_sync:
            self.get('TotalRetry')
        return self._TotalRetry

    @property
    def TotalRetransmit(self):
        """
        get the value of property _TotalRetransmit
        """
        if self.force_auto_sync:
            self.get('TotalRetransmit')
        return self._TotalRetransmit

    def _set_porthandle_with_str(self, value):
        self._PortHandle = value

    def _set_currentauthenticatedattempt_with_str(self, value):
        try:
            self._CurrentAuthenticatedAttempt = int(value)
        except ValueError:
            self._CurrentAuthenticatedAttempt = hex(int(value, 16))

    def _set_currentauthenticated_with_str(self, value):
        try:
            self._CurrentAuthenticated = int(value)
        except ValueError:
            self._CurrentAuthenticated = hex(int(value, 16))

    def _set_currentfailed_with_str(self, value):
        try:
            self._CurrentFailed = int(value)
        except ValueError:
            self._CurrentFailed = hex(int(value, 16))

    def _set_currentlogoff_with_str(self, value):
        try:
            self._CurrentLogoff = int(value)
        except ValueError:
            self._CurrentLogoff = hex(int(value, 16))

    def _set_totalattempt_with_str(self, value):
        try:
            self._TotalAttempt = int(value)
        except ValueError:
            self._TotalAttempt = hex(int(value, 16))

    def _set_totalauthenticated_with_str(self, value):
        try:
            self._TotalAuthenticated = int(value)
        except ValueError:
            self._TotalAuthenticated = hex(int(value, 16))

    def _set_totalfailed_with_str(self, value):
        try:
            self._TotalFailed = int(value)
        except ValueError:
            self._TotalFailed = hex(int(value, 16))

    def _set_totallogoff_with_str(self, value):
        try:
            self._TotalLogoff = int(value)
        except ValueError:
            self._TotalLogoff = hex(int(value, 16))

    def _set_totalretry_with_str(self, value):
        try:
            self._TotalRetry = int(value)
        except ValueError:
            self._TotalRetry = hex(int(value, 16))

    def _set_totalretransmit_with_str(self, value):
        try:
            self._TotalRetransmit = int(value)
        except ValueError:
            self._TotalRetransmit = hex(int(value, 16))

