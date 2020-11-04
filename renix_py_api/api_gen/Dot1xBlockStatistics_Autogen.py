"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Dot1xBlockStatistics(Result):
    def __init__(self, **kwargs):
        self._Dot1xBlockHandle = ''  # 802.1x Block Name, not editable
        self._BlockState = ''  # Block State, not editable
        self._CurrentAuthenticatedAttempt = 0  # Currently Authenticated Attempt, not editable
        self._CurrentAuthenticated = 0  # Currently Authenticated, not editable
        self._CurrentFailed = 0  # Currently Failed, not editable
        self._CurrentLogoff = 0  # Currently Logoff, not editable
        self._AuthenticatedAttemptRate = 0  # Authenticated Attempt Rate (sessions/sec), not editable
        self._AuthenticatedRate = 0  # Authenticated Rate (sessions/sec), not editable
        self._LogoffRate = 0  # Logoff Rate (sessions/sec), not editable
        self._TotalAttempt = 0  # Total Attempt, not editable
        self._TotalAuthenticated = 0  # Total Authenticated, not editable
        self._TotalFailed = 0  # Total Fail, not editable
        self._TotalLogoff = 0  # Total Logoff, not editable
        self._TotalRetry = 0  # Total Retry Authenticated, not editable
        self._TotalRetransmit = 0  # Total Retransmit, not editable
        self._RxEapFailure = 0  # Rx EAP-Failure, not editable
        self._RxEapRequest = 0  # Rx EAP-Request, not editable
        self._RxEapSucess = 0  # Rx EAP-Success, not editable
        self._TxEapResponse = 0  # Tx EAP-Response, not editable
        self._MaxAuthenticatedTime = 0  # Maximum Authenticated Time (ms), not editable
        self._MaxLogoffTime = 0  # Maximum Logoff Time (ms), not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Dot1xBlockStatistics, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def Dot1xBlockHandle(self):
        """
        get the value of property _Dot1xBlockHandle
        """
        if self.force_auto_sync:
            self.get('Dot1xBlockHandle')
        return self._Dot1xBlockHandle

    @property
    def BlockState(self):
        """
        get the value of property _BlockState
        """
        if self.force_auto_sync:
            self.get('BlockState')
        return self._BlockState

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
    def AuthenticatedAttemptRate(self):
        """
        get the value of property _AuthenticatedAttemptRate
        """
        if self.force_auto_sync:
            self.get('AuthenticatedAttemptRate')
        return self._AuthenticatedAttemptRate

    @property
    def AuthenticatedRate(self):
        """
        get the value of property _AuthenticatedRate
        """
        if self.force_auto_sync:
            self.get('AuthenticatedRate')
        return self._AuthenticatedRate

    @property
    def LogoffRate(self):
        """
        get the value of property _LogoffRate
        """
        if self.force_auto_sync:
            self.get('LogoffRate')
        return self._LogoffRate

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

    @property
    def RxEapFailure(self):
        """
        get the value of property _RxEapFailure
        """
        if self.force_auto_sync:
            self.get('RxEapFailure')
        return self._RxEapFailure

    @property
    def RxEapRequest(self):
        """
        get the value of property _RxEapRequest
        """
        if self.force_auto_sync:
            self.get('RxEapRequest')
        return self._RxEapRequest

    @property
    def RxEapSucess(self):
        """
        get the value of property _RxEapSucess
        """
        if self.force_auto_sync:
            self.get('RxEapSucess')
        return self._RxEapSucess

    @property
    def TxEapResponse(self):
        """
        get the value of property _TxEapResponse
        """
        if self.force_auto_sync:
            self.get('TxEapResponse')
        return self._TxEapResponse

    @property
    def MaxAuthenticatedTime(self):
        """
        get the value of property _MaxAuthenticatedTime
        """
        if self.force_auto_sync:
            self.get('MaxAuthenticatedTime')
        return self._MaxAuthenticatedTime

    @property
    def MaxLogoffTime(self):
        """
        get the value of property _MaxLogoffTime
        """
        if self.force_auto_sync:
            self.get('MaxLogoffTime')
        return self._MaxLogoffTime

    def _set_dot1xblockhandle_with_str(self, value):
        self._Dot1xBlockHandle = value

    def _set_blockstate_with_str(self, value):
        self._BlockState = value

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

    def _set_authenticatedattemptrate_with_str(self, value):
        self._AuthenticatedAttemptRate = float(value)

    def _set_authenticatedrate_with_str(self, value):
        self._AuthenticatedRate = float(value)

    def _set_logoffrate_with_str(self, value):
        self._LogoffRate = float(value)

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

    def _set_rxeapfailure_with_str(self, value):
        try:
            self._RxEapFailure = int(value)
        except ValueError:
            self._RxEapFailure = hex(int(value, 16))

    def _set_rxeaprequest_with_str(self, value):
        try:
            self._RxEapRequest = int(value)
        except ValueError:
            self._RxEapRequest = hex(int(value, 16))

    def _set_rxeapsucess_with_str(self, value):
        try:
            self._RxEapSucess = int(value)
        except ValueError:
            self._RxEapSucess = hex(int(value, 16))

    def _set_txeapresponse_with_str(self, value):
        try:
            self._TxEapResponse = int(value)
        except ValueError:
            self._TxEapResponse = hex(int(value, 16))

    def _set_maxauthenticatedtime_with_str(self, value):
        try:
            self._MaxAuthenticatedTime = int(value)
        except ValueError:
            self._MaxAuthenticatedTime = hex(int(value, 16))

    def _set_maxlogofftime_with_str(self, value):
        try:
            self._MaxLogoffTime = int(value)
        except ValueError:
            self._MaxLogoffTime = hex(int(value, 16))

