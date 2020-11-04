"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Dhcpv6ClientBlockStatistics(Result):
    def __init__(self, **kwargs):
        self._Dhcpv6ClientBlockId = ''  # DHCPv6/PD Session Block Name, not editable
        self._BlockSessionState = 'Idle'  # Block State, not editable
        self._CurrentlyAttempting = 0  # Currently Attempting, not editable
        self._CurrentlyIdl = 0  # Currently Idle, not editable
        self._CurrentlyBound = 0  # Currently Bound, not editable
        self._AttemptRate = 0  # Attempt Rate (sessions/sec), not editable
        self._BindRate = 0  # Bind Rate (sessions/sec), not editable
        self._RebindRate = 0  # Rebind Rate (sessions/sec), not editable
        self._ReleaseRate = 0  # Release Rate (sessions/sec), not editable
        self._RenewRate = 0  # Renew Rate (sessions/sec), not editable
        self._AverageRebindToReplyTime = 0  # Average Rebind to Reply Time (ms), not editable
        self._AverageReleaseToReplyTime = 0  # Average Release to Reply Time (ms), not editable
        self._AverageRenewToReplyTime = 0  # Average Renew to Reply Time (ms), not editable
        self._AverageRequestToReplyTime = 0  # Average Request to Reply Time (ms), not editable
        self._AverageSolicitToAdvertiseTime = 0  # Average Solicit to Advertise Time (ms), not editable
        self._AverageSolicitToReplyTime = 0  # Average Solicit to Reply Time (ms), not editable
        self._MaxRebindToReplyTime = 0  # Maximum Rebind to Reply Time (ms), not editable
        self._MaxReleaseToReplyTime = 0  # Maximum Release to Reply Time (ms), not editable
        self._MaxRenewToReplyTime = 0  # Maximum Renew to Reply Time (ms), not editable
        self._MaxRequestToReplyTime = 0  # Maximum Request to Reply Time (ms), not editable
        self._MaxSolicitToAdvertiseTime = 0  # Maximum Solicit to Advertise Time (ms), not editable
        self._MaxSolicitToReplyTime = 0  # Maximum Solicit to Reply Time (ms), not editable
        self._MinRebindToReplyTime = 0  # Minimum Rebind to Reply Time (ms), not editable
        self._MinReleaseToReplyTime = 0  # Minimum Release to Reply Time (ms), not editable
        self._MinRenewToReplyTime = 0  # Minimum Renew to Reply Time (ms), not editable
        self._MinRequestToReplyTime = 0  # Minimum Request to Reply Time (ms), not editable
        self._MinSolicitToAdvertiseTime = 0  # Minimum Solicit to Advertise Time (ms), not editable
        self._MinSolicitToReplyTime = 0  # Minimum Solicit to Reply Time (ms), not editable
        self._AdvertiseRxCount = 0  # Advertise Rx Count, not editable
        self._ReplyRxCount = 0  # Reply Rx Count, not editable
        self._ReconfigureRxCount = 0  # Reconfigure Rx Count, not editable
        self._SolicitTxCount = 0  # Solicit Tx Count, not editable
        self._RequestTxCount = 0  # Request Tx Count, not editable
        self._ReleaseTxCount = 0  # Release Tx Count, not editable
        self._RenewTxCount = 0  # Renew Tx Count, not editable
        self._RebindTxCount = 0  # Rebind Tx Count, not editable
        self._ConfirmTxCount = 0  # Confirm Tx Count, not editable
        self._InfoRequestTxCount = 0  # Infomation-Request Tx Count, not editable
        self._TotalAttempted = 0  # Total Attempted, not editable
        self._TotalBound = 0  # Total Bound, not editable
        self._TotalFailed = 0  # Total Failed, not editable
        self._TotalRebound = 0  # Total Rebound, not editable
        self._TotalReleased = 0  # Total Released, not editable
        self._TotalReleaseRetried = 0  # Total Release Retried, not editable
        self._TotalRenewed = 0  # Total Renewed, not editable
        self._TotalRenewedRetried = 0  # Total Renewed Retried, not editable
        self._TotalRetired = 0  # Total Retried, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv6ClientBlockStatistics, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def Dhcpv6ClientBlockId(self):
        """
        get the value of property _Dhcpv6ClientBlockId
        """
        if self.force_auto_sync:
            self.get('Dhcpv6ClientBlockId')
        return self._Dhcpv6ClientBlockId

    @property
    def BlockSessionState(self):
        """
        get the value of property _BlockSessionState
        """
        if self.force_auto_sync:
            self.get('BlockSessionState')
        return self._BlockSessionState

    @property
    def CurrentlyAttempting(self):
        """
        get the value of property _CurrentlyAttempting
        """
        if self.force_auto_sync:
            self.get('CurrentlyAttempting')
        return self._CurrentlyAttempting

    @property
    def CurrentlyIdl(self):
        """
        get the value of property _CurrentlyIdl
        """
        if self.force_auto_sync:
            self.get('CurrentlyIdl')
        return self._CurrentlyIdl

    @property
    def CurrentlyBound(self):
        """
        get the value of property _CurrentlyBound
        """
        if self.force_auto_sync:
            self.get('CurrentlyBound')
        return self._CurrentlyBound

    @property
    def AttemptRate(self):
        """
        get the value of property _AttemptRate
        """
        if self.force_auto_sync:
            self.get('AttemptRate')
        return self._AttemptRate

    @property
    def BindRate(self):
        """
        get the value of property _BindRate
        """
        if self.force_auto_sync:
            self.get('BindRate')
        return self._BindRate

    @property
    def RebindRate(self):
        """
        get the value of property _RebindRate
        """
        if self.force_auto_sync:
            self.get('RebindRate')
        return self._RebindRate

    @property
    def ReleaseRate(self):
        """
        get the value of property _ReleaseRate
        """
        if self.force_auto_sync:
            self.get('ReleaseRate')
        return self._ReleaseRate

    @property
    def RenewRate(self):
        """
        get the value of property _RenewRate
        """
        if self.force_auto_sync:
            self.get('RenewRate')
        return self._RenewRate

    @property
    def AverageRebindToReplyTime(self):
        """
        get the value of property _AverageRebindToReplyTime
        """
        if self.force_auto_sync:
            self.get('AverageRebindToReplyTime')
        return self._AverageRebindToReplyTime

    @property
    def AverageReleaseToReplyTime(self):
        """
        get the value of property _AverageReleaseToReplyTime
        """
        if self.force_auto_sync:
            self.get('AverageReleaseToReplyTime')
        return self._AverageReleaseToReplyTime

    @property
    def AverageRenewToReplyTime(self):
        """
        get the value of property _AverageRenewToReplyTime
        """
        if self.force_auto_sync:
            self.get('AverageRenewToReplyTime')
        return self._AverageRenewToReplyTime

    @property
    def AverageRequestToReplyTime(self):
        """
        get the value of property _AverageRequestToReplyTime
        """
        if self.force_auto_sync:
            self.get('AverageRequestToReplyTime')
        return self._AverageRequestToReplyTime

    @property
    def AverageSolicitToAdvertiseTime(self):
        """
        get the value of property _AverageSolicitToAdvertiseTime
        """
        if self.force_auto_sync:
            self.get('AverageSolicitToAdvertiseTime')
        return self._AverageSolicitToAdvertiseTime

    @property
    def AverageSolicitToReplyTime(self):
        """
        get the value of property _AverageSolicitToReplyTime
        """
        if self.force_auto_sync:
            self.get('AverageSolicitToReplyTime')
        return self._AverageSolicitToReplyTime

    @property
    def MaxRebindToReplyTime(self):
        """
        get the value of property _MaxRebindToReplyTime
        """
        if self.force_auto_sync:
            self.get('MaxRebindToReplyTime')
        return self._MaxRebindToReplyTime

    @property
    def MaxReleaseToReplyTime(self):
        """
        get the value of property _MaxReleaseToReplyTime
        """
        if self.force_auto_sync:
            self.get('MaxReleaseToReplyTime')
        return self._MaxReleaseToReplyTime

    @property
    def MaxRenewToReplyTime(self):
        """
        get the value of property _MaxRenewToReplyTime
        """
        if self.force_auto_sync:
            self.get('MaxRenewToReplyTime')
        return self._MaxRenewToReplyTime

    @property
    def MaxRequestToReplyTime(self):
        """
        get the value of property _MaxRequestToReplyTime
        """
        if self.force_auto_sync:
            self.get('MaxRequestToReplyTime')
        return self._MaxRequestToReplyTime

    @property
    def MaxSolicitToAdvertiseTime(self):
        """
        get the value of property _MaxSolicitToAdvertiseTime
        """
        if self.force_auto_sync:
            self.get('MaxSolicitToAdvertiseTime')
        return self._MaxSolicitToAdvertiseTime

    @property
    def MaxSolicitToReplyTime(self):
        """
        get the value of property _MaxSolicitToReplyTime
        """
        if self.force_auto_sync:
            self.get('MaxSolicitToReplyTime')
        return self._MaxSolicitToReplyTime

    @property
    def MinRebindToReplyTime(self):
        """
        get the value of property _MinRebindToReplyTime
        """
        if self.force_auto_sync:
            self.get('MinRebindToReplyTime')
        return self._MinRebindToReplyTime

    @property
    def MinReleaseToReplyTime(self):
        """
        get the value of property _MinReleaseToReplyTime
        """
        if self.force_auto_sync:
            self.get('MinReleaseToReplyTime')
        return self._MinReleaseToReplyTime

    @property
    def MinRenewToReplyTime(self):
        """
        get the value of property _MinRenewToReplyTime
        """
        if self.force_auto_sync:
            self.get('MinRenewToReplyTime')
        return self._MinRenewToReplyTime

    @property
    def MinRequestToReplyTime(self):
        """
        get the value of property _MinRequestToReplyTime
        """
        if self.force_auto_sync:
            self.get('MinRequestToReplyTime')
        return self._MinRequestToReplyTime

    @property
    def MinSolicitToAdvertiseTime(self):
        """
        get the value of property _MinSolicitToAdvertiseTime
        """
        if self.force_auto_sync:
            self.get('MinSolicitToAdvertiseTime')
        return self._MinSolicitToAdvertiseTime

    @property
    def MinSolicitToReplyTime(self):
        """
        get the value of property _MinSolicitToReplyTime
        """
        if self.force_auto_sync:
            self.get('MinSolicitToReplyTime')
        return self._MinSolicitToReplyTime

    @property
    def AdvertiseRxCount(self):
        """
        get the value of property _AdvertiseRxCount
        """
        if self.force_auto_sync:
            self.get('AdvertiseRxCount')
        return self._AdvertiseRxCount

    @property
    def ReplyRxCount(self):
        """
        get the value of property _ReplyRxCount
        """
        if self.force_auto_sync:
            self.get('ReplyRxCount')
        return self._ReplyRxCount

    @property
    def ReconfigureRxCount(self):
        """
        get the value of property _ReconfigureRxCount
        """
        if self.force_auto_sync:
            self.get('ReconfigureRxCount')
        return self._ReconfigureRxCount

    @property
    def SolicitTxCount(self):
        """
        get the value of property _SolicitTxCount
        """
        if self.force_auto_sync:
            self.get('SolicitTxCount')
        return self._SolicitTxCount

    @property
    def RequestTxCount(self):
        """
        get the value of property _RequestTxCount
        """
        if self.force_auto_sync:
            self.get('RequestTxCount')
        return self._RequestTxCount

    @property
    def ReleaseTxCount(self):
        """
        get the value of property _ReleaseTxCount
        """
        if self.force_auto_sync:
            self.get('ReleaseTxCount')
        return self._ReleaseTxCount

    @property
    def RenewTxCount(self):
        """
        get the value of property _RenewTxCount
        """
        if self.force_auto_sync:
            self.get('RenewTxCount')
        return self._RenewTxCount

    @property
    def RebindTxCount(self):
        """
        get the value of property _RebindTxCount
        """
        if self.force_auto_sync:
            self.get('RebindTxCount')
        return self._RebindTxCount

    @property
    def ConfirmTxCount(self):
        """
        get the value of property _ConfirmTxCount
        """
        if self.force_auto_sync:
            self.get('ConfirmTxCount')
        return self._ConfirmTxCount

    @property
    def InfoRequestTxCount(self):
        """
        get the value of property _InfoRequestTxCount
        """
        if self.force_auto_sync:
            self.get('InfoRequestTxCount')
        return self._InfoRequestTxCount

    @property
    def TotalAttempted(self):
        """
        get the value of property _TotalAttempted
        """
        if self.force_auto_sync:
            self.get('TotalAttempted')
        return self._TotalAttempted

    @property
    def TotalBound(self):
        """
        get the value of property _TotalBound
        """
        if self.force_auto_sync:
            self.get('TotalBound')
        return self._TotalBound

    @property
    def TotalFailed(self):
        """
        get the value of property _TotalFailed
        """
        if self.force_auto_sync:
            self.get('TotalFailed')
        return self._TotalFailed

    @property
    def TotalRebound(self):
        """
        get the value of property _TotalRebound
        """
        if self.force_auto_sync:
            self.get('TotalRebound')
        return self._TotalRebound

    @property
    def TotalReleased(self):
        """
        get the value of property _TotalReleased
        """
        if self.force_auto_sync:
            self.get('TotalReleased')
        return self._TotalReleased

    @property
    def TotalReleaseRetried(self):
        """
        get the value of property _TotalReleaseRetried
        """
        if self.force_auto_sync:
            self.get('TotalReleaseRetried')
        return self._TotalReleaseRetried

    @property
    def TotalRenewed(self):
        """
        get the value of property _TotalRenewed
        """
        if self.force_auto_sync:
            self.get('TotalRenewed')
        return self._TotalRenewed

    @property
    def TotalRenewedRetried(self):
        """
        get the value of property _TotalRenewedRetried
        """
        if self.force_auto_sync:
            self.get('TotalRenewedRetried')
        return self._TotalRenewedRetried

    @property
    def TotalRetired(self):
        """
        get the value of property _TotalRetired
        """
        if self.force_auto_sync:
            self.get('TotalRetired')
        return self._TotalRetired

    def _set_dhcpv6clientblockid_with_str(self, value):
        self._Dhcpv6ClientBlockId = value

    def _set_blocksessionstate_with_str(self, value):
        self._BlockSessionState = value

    def _set_currentlyattempting_with_str(self, value):
        try:
            self._CurrentlyAttempting = int(value)
        except ValueError:
            self._CurrentlyAttempting = hex(int(value, 16))

    def _set_currentlyidl_with_str(self, value):
        try:
            self._CurrentlyIdl = int(value)
        except ValueError:
            self._CurrentlyIdl = hex(int(value, 16))

    def _set_currentlybound_with_str(self, value):
        try:
            self._CurrentlyBound = int(value)
        except ValueError:
            self._CurrentlyBound = hex(int(value, 16))

    def _set_attemptrate_with_str(self, value):
        self._AttemptRate = float(value)

    def _set_bindrate_with_str(self, value):
        self._BindRate = float(value)

    def _set_rebindrate_with_str(self, value):
        self._RebindRate = float(value)

    def _set_releaserate_with_str(self, value):
        self._ReleaseRate = float(value)

    def _set_renewrate_with_str(self, value):
        self._RenewRate = float(value)

    def _set_averagerebindtoreplytime_with_str(self, value):
        try:
            self._AverageRebindToReplyTime = int(value)
        except ValueError:
            self._AverageRebindToReplyTime = hex(int(value, 16))

    def _set_averagereleasetoreplytime_with_str(self, value):
        try:
            self._AverageReleaseToReplyTime = int(value)
        except ValueError:
            self._AverageReleaseToReplyTime = hex(int(value, 16))

    def _set_averagerenewtoreplytime_with_str(self, value):
        try:
            self._AverageRenewToReplyTime = int(value)
        except ValueError:
            self._AverageRenewToReplyTime = hex(int(value, 16))

    def _set_averagerequesttoreplytime_with_str(self, value):
        try:
            self._AverageRequestToReplyTime = int(value)
        except ValueError:
            self._AverageRequestToReplyTime = hex(int(value, 16))

    def _set_averagesolicittoadvertisetime_with_str(self, value):
        try:
            self._AverageSolicitToAdvertiseTime = int(value)
        except ValueError:
            self._AverageSolicitToAdvertiseTime = hex(int(value, 16))

    def _set_averagesolicittoreplytime_with_str(self, value):
        try:
            self._AverageSolicitToReplyTime = int(value)
        except ValueError:
            self._AverageSolicitToReplyTime = hex(int(value, 16))

    def _set_maxrebindtoreplytime_with_str(self, value):
        try:
            self._MaxRebindToReplyTime = int(value)
        except ValueError:
            self._MaxRebindToReplyTime = hex(int(value, 16))

    def _set_maxreleasetoreplytime_with_str(self, value):
        try:
            self._MaxReleaseToReplyTime = int(value)
        except ValueError:
            self._MaxReleaseToReplyTime = hex(int(value, 16))

    def _set_maxrenewtoreplytime_with_str(self, value):
        try:
            self._MaxRenewToReplyTime = int(value)
        except ValueError:
            self._MaxRenewToReplyTime = hex(int(value, 16))

    def _set_maxrequesttoreplytime_with_str(self, value):
        try:
            self._MaxRequestToReplyTime = int(value)
        except ValueError:
            self._MaxRequestToReplyTime = hex(int(value, 16))

    def _set_maxsolicittoadvertisetime_with_str(self, value):
        try:
            self._MaxSolicitToAdvertiseTime = int(value)
        except ValueError:
            self._MaxSolicitToAdvertiseTime = hex(int(value, 16))

    def _set_maxsolicittoreplytime_with_str(self, value):
        try:
            self._MaxSolicitToReplyTime = int(value)
        except ValueError:
            self._MaxSolicitToReplyTime = hex(int(value, 16))

    def _set_minrebindtoreplytime_with_str(self, value):
        try:
            self._MinRebindToReplyTime = int(value)
        except ValueError:
            self._MinRebindToReplyTime = hex(int(value, 16))

    def _set_minreleasetoreplytime_with_str(self, value):
        try:
            self._MinReleaseToReplyTime = int(value)
        except ValueError:
            self._MinReleaseToReplyTime = hex(int(value, 16))

    def _set_minrenewtoreplytime_with_str(self, value):
        try:
            self._MinRenewToReplyTime = int(value)
        except ValueError:
            self._MinRenewToReplyTime = hex(int(value, 16))

    def _set_minrequesttoreplytime_with_str(self, value):
        try:
            self._MinRequestToReplyTime = int(value)
        except ValueError:
            self._MinRequestToReplyTime = hex(int(value, 16))

    def _set_minsolicittoadvertisetime_with_str(self, value):
        try:
            self._MinSolicitToAdvertiseTime = int(value)
        except ValueError:
            self._MinSolicitToAdvertiseTime = hex(int(value, 16))

    def _set_minsolicittoreplytime_with_str(self, value):
        try:
            self._MinSolicitToReplyTime = int(value)
        except ValueError:
            self._MinSolicitToReplyTime = hex(int(value, 16))

    def _set_advertiserxcount_with_str(self, value):
        try:
            self._AdvertiseRxCount = int(value)
        except ValueError:
            self._AdvertiseRxCount = hex(int(value, 16))

    def _set_replyrxcount_with_str(self, value):
        try:
            self._ReplyRxCount = int(value)
        except ValueError:
            self._ReplyRxCount = hex(int(value, 16))

    def _set_reconfigurerxcount_with_str(self, value):
        try:
            self._ReconfigureRxCount = int(value)
        except ValueError:
            self._ReconfigureRxCount = hex(int(value, 16))

    def _set_solicittxcount_with_str(self, value):
        try:
            self._SolicitTxCount = int(value)
        except ValueError:
            self._SolicitTxCount = hex(int(value, 16))

    def _set_requesttxcount_with_str(self, value):
        try:
            self._RequestTxCount = int(value)
        except ValueError:
            self._RequestTxCount = hex(int(value, 16))

    def _set_releasetxcount_with_str(self, value):
        try:
            self._ReleaseTxCount = int(value)
        except ValueError:
            self._ReleaseTxCount = hex(int(value, 16))

    def _set_renewtxcount_with_str(self, value):
        try:
            self._RenewTxCount = int(value)
        except ValueError:
            self._RenewTxCount = hex(int(value, 16))

    def _set_rebindtxcount_with_str(self, value):
        try:
            self._RebindTxCount = int(value)
        except ValueError:
            self._RebindTxCount = hex(int(value, 16))

    def _set_confirmtxcount_with_str(self, value):
        try:
            self._ConfirmTxCount = int(value)
        except ValueError:
            self._ConfirmTxCount = hex(int(value, 16))

    def _set_inforequesttxcount_with_str(self, value):
        try:
            self._InfoRequestTxCount = int(value)
        except ValueError:
            self._InfoRequestTxCount = hex(int(value, 16))

    def _set_totalattempted_with_str(self, value):
        try:
            self._TotalAttempted = int(value)
        except ValueError:
            self._TotalAttempted = hex(int(value, 16))

    def _set_totalbound_with_str(self, value):
        try:
            self._TotalBound = int(value)
        except ValueError:
            self._TotalBound = hex(int(value, 16))

    def _set_totalfailed_with_str(self, value):
        try:
            self._TotalFailed = int(value)
        except ValueError:
            self._TotalFailed = hex(int(value, 16))

    def _set_totalrebound_with_str(self, value):
        try:
            self._TotalRebound = int(value)
        except ValueError:
            self._TotalRebound = hex(int(value, 16))

    def _set_totalreleased_with_str(self, value):
        try:
            self._TotalReleased = int(value)
        except ValueError:
            self._TotalReleased = hex(int(value, 16))

    def _set_totalreleaseretried_with_str(self, value):
        try:
            self._TotalReleaseRetried = int(value)
        except ValueError:
            self._TotalReleaseRetried = hex(int(value, 16))

    def _set_totalrenewed_with_str(self, value):
        try:
            self._TotalRenewed = int(value)
        except ValueError:
            self._TotalRenewed = hex(int(value, 16))

    def _set_totalrenewedretried_with_str(self, value):
        try:
            self._TotalRenewedRetried = int(value)
        except ValueError:
            self._TotalRenewedRetried = hex(int(value, 16))

    def _set_totalretired_with_str(self, value):
        try:
            self._TotalRetired = int(value)
        except ValueError:
            self._TotalRetired = hex(int(value, 16))

