"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class PppoeClientBlockStatistic(Result):
    def __init__(self, **kwargs):
        self._PppoeClientBlockId = ''  # PPPoE Client Block Name, not editable
        self._IpcpState = 'None'  # IPCP Block State, not editable
        self._Ipv6cpState = 'None'  # IPv6CP Block State, not editable
        self._SessionCount = 0  # Session Count, not editable
        self._SessionsUp = 0  # Sessions Up, not editable
        self._SessionsRetried = 0  # Sessions Retried, not editable
        self._AttemptedConnects = 0  # Attempted Connections, not editable
        self._SuccessfulConnects = 0  # Successful Connections, not editable
        self._FailedConnects = 0  # Failed Connections, not editable
        self._SucessfulDisconnects = 0  # Successful Disconnections, not editable
        self._FailedDisconnects = 0  # Failed Disconnections, not editable
        self._MaxSetupTime = 0  # Maximum Setup Time (ms), not editable
        self._MinSetupTime = 0  # Minimum Setup Time (ms), not editable
        self._AverageSetupTime = 0  # Average Setup Time (ms), not editable
        self._SuccessfulSetupRate = 0  # Successful Setup Rate(sessions/sec), not editable
        self._TxPadi = 0  # Tx PADI, not editable
        self._RxPado = 0  # Rx PADO, not editable
        self._TxPadr = 0  # Tx PADR, not editable
        self._RxPads = 0  # Rx PADS, not editable
        self._TxPadt = 0  # Tx PADT, not editable
        self._RxPadt = 0  # Rx PADT, not editable
        self._TxLcpConfigRequest = 0  # Tx LCP Configure Request, not editable
        self._RxLcpConfigRequest = 0  # Rx LCP Configure Request, not editable
        self._TxLcpConfigAck = 0  # Tx LCP Configure Ack, not editable
        self._RxLcpConfigAck = 0  # Rx LCP Configure Ack, not editable
        self._TxLcpConfigNak = 0  # Tx LCP Configure Nak, not editable
        self._RxLcpConfigNak = 0  # Rx LCP Configure Nak, not editable
        self._TxLcpConfigReject = 0  # Tx LCP Configure Reject, not editable
        self._RxLcpConfigReject = 0  # Rx LCP Configure Reject, not editable
        self._TxLcpEchoRequest = 0  # Tx LCP Echo Request, not editable
        self._RxLcpEchoRequest = 0  # Rx LCP Echo Request, not editable
        self._TxLcpEchoReply = 0  # Tx LCP Echo Reply, not editable
        self._RxLcpEchoReply = 0  # Rx LCP Echo Reply, not editable
        self._TxLcpTerminateRequest = 0  # Tx LCP Terminate Request, not editable
        self._RxLcpTerminateRequest = 0  # Rx LCP Terminate Request, not editable
        self._TxLcpTerminateAck = 0  # Tx LCP Terminate Ack, not editable
        self._RxLcpTerminateAck = 0  # Rx LCP Terminate Ack, not editable
        self._TxChap = 0  # Tx CHAP, not editable
        self._RxChap = 0  # Rx CHAP, not editable
        self._TxPap = 0  # Tx PAP, not editable
        self._RxPap = 0  # Rx PAP, not editable
        self._TxIpcp = 0  # Tx IPCP, not editable
        self._RxIpcp = 0  # Rx IPCP, not editable
        self._TxIpv6cp = 0  # Tx IPv6CP, not editable
        self._RxIpv6cp = 0  # Rx IPv6CP, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(PppoeClientBlockStatistic, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def PppoeClientBlockId(self):
        """
        get the value of property _PppoeClientBlockId
        """
        if self.force_auto_sync:
            self.get('PppoeClientBlockId')
        return self._PppoeClientBlockId

    @property
    def IpcpState(self):
        """
        get the value of property _IpcpState
        """
        if self.force_auto_sync:
            self.get('IpcpState')
        return self._IpcpState

    @property
    def Ipv6cpState(self):
        """
        get the value of property _Ipv6cpState
        """
        if self.force_auto_sync:
            self.get('Ipv6cpState')
        return self._Ipv6cpState

    @property
    def SessionCount(self):
        """
        get the value of property _SessionCount
        """
        if self.force_auto_sync:
            self.get('SessionCount')
        return self._SessionCount

    @property
    def SessionsUp(self):
        """
        get the value of property _SessionsUp
        """
        if self.force_auto_sync:
            self.get('SessionsUp')
        return self._SessionsUp

    @property
    def SessionsRetried(self):
        """
        get the value of property _SessionsRetried
        """
        if self.force_auto_sync:
            self.get('SessionsRetried')
        return self._SessionsRetried

    @property
    def AttemptedConnects(self):
        """
        get the value of property _AttemptedConnects
        """
        if self.force_auto_sync:
            self.get('AttemptedConnects')
        return self._AttemptedConnects

    @property
    def SuccessfulConnects(self):
        """
        get the value of property _SuccessfulConnects
        """
        if self.force_auto_sync:
            self.get('SuccessfulConnects')
        return self._SuccessfulConnects

    @property
    def FailedConnects(self):
        """
        get the value of property _FailedConnects
        """
        if self.force_auto_sync:
            self.get('FailedConnects')
        return self._FailedConnects

    @property
    def SucessfulDisconnects(self):
        """
        get the value of property _SucessfulDisconnects
        """
        if self.force_auto_sync:
            self.get('SucessfulDisconnects')
        return self._SucessfulDisconnects

    @property
    def FailedDisconnects(self):
        """
        get the value of property _FailedDisconnects
        """
        if self.force_auto_sync:
            self.get('FailedDisconnects')
        return self._FailedDisconnects

    @property
    def MaxSetupTime(self):
        """
        get the value of property _MaxSetupTime
        """
        if self.force_auto_sync:
            self.get('MaxSetupTime')
        return self._MaxSetupTime

    @property
    def MinSetupTime(self):
        """
        get the value of property _MinSetupTime
        """
        if self.force_auto_sync:
            self.get('MinSetupTime')
        return self._MinSetupTime

    @property
    def AverageSetupTime(self):
        """
        get the value of property _AverageSetupTime
        """
        if self.force_auto_sync:
            self.get('AverageSetupTime')
        return self._AverageSetupTime

    @property
    def SuccessfulSetupRate(self):
        """
        get the value of property _SuccessfulSetupRate
        """
        if self.force_auto_sync:
            self.get('SuccessfulSetupRate')
        return self._SuccessfulSetupRate

    @property
    def TxPadi(self):
        """
        get the value of property _TxPadi
        """
        if self.force_auto_sync:
            self.get('TxPadi')
        return self._TxPadi

    @property
    def RxPado(self):
        """
        get the value of property _RxPado
        """
        if self.force_auto_sync:
            self.get('RxPado')
        return self._RxPado

    @property
    def TxPadr(self):
        """
        get the value of property _TxPadr
        """
        if self.force_auto_sync:
            self.get('TxPadr')
        return self._TxPadr

    @property
    def RxPads(self):
        """
        get the value of property _RxPads
        """
        if self.force_auto_sync:
            self.get('RxPads')
        return self._RxPads

    @property
    def TxPadt(self):
        """
        get the value of property _TxPadt
        """
        if self.force_auto_sync:
            self.get('TxPadt')
        return self._TxPadt

    @property
    def RxPadt(self):
        """
        get the value of property _RxPadt
        """
        if self.force_auto_sync:
            self.get('RxPadt')
        return self._RxPadt

    @property
    def TxLcpConfigRequest(self):
        """
        get the value of property _TxLcpConfigRequest
        """
        if self.force_auto_sync:
            self.get('TxLcpConfigRequest')
        return self._TxLcpConfigRequest

    @property
    def RxLcpConfigRequest(self):
        """
        get the value of property _RxLcpConfigRequest
        """
        if self.force_auto_sync:
            self.get('RxLcpConfigRequest')
        return self._RxLcpConfigRequest

    @property
    def TxLcpConfigAck(self):
        """
        get the value of property _TxLcpConfigAck
        """
        if self.force_auto_sync:
            self.get('TxLcpConfigAck')
        return self._TxLcpConfigAck

    @property
    def RxLcpConfigAck(self):
        """
        get the value of property _RxLcpConfigAck
        """
        if self.force_auto_sync:
            self.get('RxLcpConfigAck')
        return self._RxLcpConfigAck

    @property
    def TxLcpConfigNak(self):
        """
        get the value of property _TxLcpConfigNak
        """
        if self.force_auto_sync:
            self.get('TxLcpConfigNak')
        return self._TxLcpConfigNak

    @property
    def RxLcpConfigNak(self):
        """
        get the value of property _RxLcpConfigNak
        """
        if self.force_auto_sync:
            self.get('RxLcpConfigNak')
        return self._RxLcpConfigNak

    @property
    def TxLcpConfigReject(self):
        """
        get the value of property _TxLcpConfigReject
        """
        if self.force_auto_sync:
            self.get('TxLcpConfigReject')
        return self._TxLcpConfigReject

    @property
    def RxLcpConfigReject(self):
        """
        get the value of property _RxLcpConfigReject
        """
        if self.force_auto_sync:
            self.get('RxLcpConfigReject')
        return self._RxLcpConfigReject

    @property
    def TxLcpEchoRequest(self):
        """
        get the value of property _TxLcpEchoRequest
        """
        if self.force_auto_sync:
            self.get('TxLcpEchoRequest')
        return self._TxLcpEchoRequest

    @property
    def RxLcpEchoRequest(self):
        """
        get the value of property _RxLcpEchoRequest
        """
        if self.force_auto_sync:
            self.get('RxLcpEchoRequest')
        return self._RxLcpEchoRequest

    @property
    def TxLcpEchoReply(self):
        """
        get the value of property _TxLcpEchoReply
        """
        if self.force_auto_sync:
            self.get('TxLcpEchoReply')
        return self._TxLcpEchoReply

    @property
    def RxLcpEchoReply(self):
        """
        get the value of property _RxLcpEchoReply
        """
        if self.force_auto_sync:
            self.get('RxLcpEchoReply')
        return self._RxLcpEchoReply

    @property
    def TxLcpTerminateRequest(self):
        """
        get the value of property _TxLcpTerminateRequest
        """
        if self.force_auto_sync:
            self.get('TxLcpTerminateRequest')
        return self._TxLcpTerminateRequest

    @property
    def RxLcpTerminateRequest(self):
        """
        get the value of property _RxLcpTerminateRequest
        """
        if self.force_auto_sync:
            self.get('RxLcpTerminateRequest')
        return self._RxLcpTerminateRequest

    @property
    def TxLcpTerminateAck(self):
        """
        get the value of property _TxLcpTerminateAck
        """
        if self.force_auto_sync:
            self.get('TxLcpTerminateAck')
        return self._TxLcpTerminateAck

    @property
    def RxLcpTerminateAck(self):
        """
        get the value of property _RxLcpTerminateAck
        """
        if self.force_auto_sync:
            self.get('RxLcpTerminateAck')
        return self._RxLcpTerminateAck

    @property
    def TxChap(self):
        """
        get the value of property _TxChap
        """
        if self.force_auto_sync:
            self.get('TxChap')
        return self._TxChap

    @property
    def RxChap(self):
        """
        get the value of property _RxChap
        """
        if self.force_auto_sync:
            self.get('RxChap')
        return self._RxChap

    @property
    def TxPap(self):
        """
        get the value of property _TxPap
        """
        if self.force_auto_sync:
            self.get('TxPap')
        return self._TxPap

    @property
    def RxPap(self):
        """
        get the value of property _RxPap
        """
        if self.force_auto_sync:
            self.get('RxPap')
        return self._RxPap

    @property
    def TxIpcp(self):
        """
        get the value of property _TxIpcp
        """
        if self.force_auto_sync:
            self.get('TxIpcp')
        return self._TxIpcp

    @property
    def RxIpcp(self):
        """
        get the value of property _RxIpcp
        """
        if self.force_auto_sync:
            self.get('RxIpcp')
        return self._RxIpcp

    @property
    def TxIpv6cp(self):
        """
        get the value of property _TxIpv6cp
        """
        if self.force_auto_sync:
            self.get('TxIpv6cp')
        return self._TxIpv6cp

    @property
    def RxIpv6cp(self):
        """
        get the value of property _RxIpv6cp
        """
        if self.force_auto_sync:
            self.get('RxIpv6cp')
        return self._RxIpv6cp

    def _set_pppoeclientblockid_with_str(self, value):
        self._PppoeClientBlockId = value

    def _set_ipcpstate_with_str(self, value):
        self._IpcpState = value

    def _set_ipv6cpstate_with_str(self, value):
        self._Ipv6cpState = value

    def _set_sessioncount_with_str(self, value):
        try:
            self._SessionCount = int(value)
        except ValueError:
            self._SessionCount = hex(int(value, 16))

    def _set_sessionsup_with_str(self, value):
        try:
            self._SessionsUp = int(value)
        except ValueError:
            self._SessionsUp = hex(int(value, 16))

    def _set_sessionsretried_with_str(self, value):
        try:
            self._SessionsRetried = int(value)
        except ValueError:
            self._SessionsRetried = hex(int(value, 16))

    def _set_attemptedconnects_with_str(self, value):
        try:
            self._AttemptedConnects = int(value)
        except ValueError:
            self._AttemptedConnects = hex(int(value, 16))

    def _set_successfulconnects_with_str(self, value):
        try:
            self._SuccessfulConnects = int(value)
        except ValueError:
            self._SuccessfulConnects = hex(int(value, 16))

    def _set_failedconnects_with_str(self, value):
        try:
            self._FailedConnects = int(value)
        except ValueError:
            self._FailedConnects = hex(int(value, 16))

    def _set_sucessfuldisconnects_with_str(self, value):
        try:
            self._SucessfulDisconnects = int(value)
        except ValueError:
            self._SucessfulDisconnects = hex(int(value, 16))

    def _set_faileddisconnects_with_str(self, value):
        try:
            self._FailedDisconnects = int(value)
        except ValueError:
            self._FailedDisconnects = hex(int(value, 16))

    def _set_maxsetuptime_with_str(self, value):
        try:
            self._MaxSetupTime = int(value)
        except ValueError:
            self._MaxSetupTime = hex(int(value, 16))

    def _set_minsetuptime_with_str(self, value):
        try:
            self._MinSetupTime = int(value)
        except ValueError:
            self._MinSetupTime = hex(int(value, 16))

    def _set_averagesetuptime_with_str(self, value):
        self._AverageSetupTime = float(value)

    def _set_successfulsetuprate_with_str(self, value):
        self._SuccessfulSetupRate = float(value)

    def _set_txpadi_with_str(self, value):
        try:
            self._TxPadi = int(value)
        except ValueError:
            self._TxPadi = hex(int(value, 16))

    def _set_rxpado_with_str(self, value):
        try:
            self._RxPado = int(value)
        except ValueError:
            self._RxPado = hex(int(value, 16))

    def _set_txpadr_with_str(self, value):
        try:
            self._TxPadr = int(value)
        except ValueError:
            self._TxPadr = hex(int(value, 16))

    def _set_rxpads_with_str(self, value):
        try:
            self._RxPads = int(value)
        except ValueError:
            self._RxPads = hex(int(value, 16))

    def _set_txpadt_with_str(self, value):
        try:
            self._TxPadt = int(value)
        except ValueError:
            self._TxPadt = hex(int(value, 16))

    def _set_rxpadt_with_str(self, value):
        try:
            self._RxPadt = int(value)
        except ValueError:
            self._RxPadt = hex(int(value, 16))

    def _set_txlcpconfigrequest_with_str(self, value):
        try:
            self._TxLcpConfigRequest = int(value)
        except ValueError:
            self._TxLcpConfigRequest = hex(int(value, 16))

    def _set_rxlcpconfigrequest_with_str(self, value):
        try:
            self._RxLcpConfigRequest = int(value)
        except ValueError:
            self._RxLcpConfigRequest = hex(int(value, 16))

    def _set_txlcpconfigack_with_str(self, value):
        try:
            self._TxLcpConfigAck = int(value)
        except ValueError:
            self._TxLcpConfigAck = hex(int(value, 16))

    def _set_rxlcpconfigack_with_str(self, value):
        try:
            self._RxLcpConfigAck = int(value)
        except ValueError:
            self._RxLcpConfigAck = hex(int(value, 16))

    def _set_txlcpconfignak_with_str(self, value):
        try:
            self._TxLcpConfigNak = int(value)
        except ValueError:
            self._TxLcpConfigNak = hex(int(value, 16))

    def _set_rxlcpconfignak_with_str(self, value):
        try:
            self._RxLcpConfigNak = int(value)
        except ValueError:
            self._RxLcpConfigNak = hex(int(value, 16))

    def _set_txlcpconfigreject_with_str(self, value):
        try:
            self._TxLcpConfigReject = int(value)
        except ValueError:
            self._TxLcpConfigReject = hex(int(value, 16))

    def _set_rxlcpconfigreject_with_str(self, value):
        try:
            self._RxLcpConfigReject = int(value)
        except ValueError:
            self._RxLcpConfigReject = hex(int(value, 16))

    def _set_txlcpechorequest_with_str(self, value):
        try:
            self._TxLcpEchoRequest = int(value)
        except ValueError:
            self._TxLcpEchoRequest = hex(int(value, 16))

    def _set_rxlcpechorequest_with_str(self, value):
        try:
            self._RxLcpEchoRequest = int(value)
        except ValueError:
            self._RxLcpEchoRequest = hex(int(value, 16))

    def _set_txlcpechoreply_with_str(self, value):
        try:
            self._TxLcpEchoReply = int(value)
        except ValueError:
            self._TxLcpEchoReply = hex(int(value, 16))

    def _set_rxlcpechoreply_with_str(self, value):
        try:
            self._RxLcpEchoReply = int(value)
        except ValueError:
            self._RxLcpEchoReply = hex(int(value, 16))

    def _set_txlcpterminaterequest_with_str(self, value):
        try:
            self._TxLcpTerminateRequest = int(value)
        except ValueError:
            self._TxLcpTerminateRequest = hex(int(value, 16))

    def _set_rxlcpterminaterequest_with_str(self, value):
        try:
            self._RxLcpTerminateRequest = int(value)
        except ValueError:
            self._RxLcpTerminateRequest = hex(int(value, 16))

    def _set_txlcpterminateack_with_str(self, value):
        try:
            self._TxLcpTerminateAck = int(value)
        except ValueError:
            self._TxLcpTerminateAck = hex(int(value, 16))

    def _set_rxlcpterminateack_with_str(self, value):
        try:
            self._RxLcpTerminateAck = int(value)
        except ValueError:
            self._RxLcpTerminateAck = hex(int(value, 16))

    def _set_txchap_with_str(self, value):
        try:
            self._TxChap = int(value)
        except ValueError:
            self._TxChap = hex(int(value, 16))

    def _set_rxchap_with_str(self, value):
        try:
            self._RxChap = int(value)
        except ValueError:
            self._RxChap = hex(int(value, 16))

    def _set_txpap_with_str(self, value):
        try:
            self._TxPap = int(value)
        except ValueError:
            self._TxPap = hex(int(value, 16))

    def _set_rxpap_with_str(self, value):
        try:
            self._RxPap = int(value)
        except ValueError:
            self._RxPap = hex(int(value, 16))

    def _set_txipcp_with_str(self, value):
        try:
            self._TxIpcp = int(value)
        except ValueError:
            self._TxIpcp = hex(int(value, 16))

    def _set_rxipcp_with_str(self, value):
        try:
            self._RxIpcp = int(value)
        except ValueError:
            self._RxIpcp = hex(int(value, 16))

    def _set_txipv6cp_with_str(self, value):
        try:
            self._TxIpv6cp = int(value)
        except ValueError:
            self._TxIpv6cp = hex(int(value, 16))

    def _set_rxipv6cp_with_str(self, value):
        try:
            self._RxIpv6cp = int(value)
        except ValueError:
            self._RxIpv6cp = hex(int(value, 16))

