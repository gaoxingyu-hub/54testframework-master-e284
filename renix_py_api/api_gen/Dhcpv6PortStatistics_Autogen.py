"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Dhcpv6PortStatistics(Result):
    def __init__(self, **kwargs):
        self._Dhcpv6PortId = ''  # Port Name, not editable
        self._CurrentlyAttempting = 0  # Currently Attempting, not editable
        self._CurrentlyIdl = 0  # Currently Idle, not editable
        self._CurrentlyBound = 0  # Currently Bound, not editable
        self._AverageSetupTime = 0  # Average Setup Time (ms), not editable
        self._MaxSetupTime = 0  # Maximum Setup Time (ms), not editable
        self._MinSetupTime = 0  # Minimum Setup Time (ms), not editable
        self._SolicitTxCount = 0  # Solicit Tx Count, not editable
        self._RequestTxCount = 0  # Request Tx Count, not editable
        self._ReleaseTxCount = 0  # Release Tx Count, not editable
        self._RenewTxCount = 0  # Renew Tx Count, not editable
        self._RebindTxCount = 0  # Rebind Tx Count, not editable
        self._ConfirmTxCount = 0  # Confirm Tx Count, not editable
        self._InfoRequestTxCount = 0  # Infomation-Request Tx Count, not editable
        self._AdvertiseRxCount = 0  # Advertise Rx Count, not editable
        self._ReconfigureRxCount = 0  # Reconfigure Rx Count, not editable
        self._ReplyRxCount = 0  # Reply Rx Count, not editable
        self._SuccessPercentage = 0  # Success Percentage (%), not editable
        self._TotalAttempted = 0  # Total Attempted, not editable
        self._TotalBound = 0  # Total Bound, not editable
        self._TotalBoundFailed = 0  # Total Bound Failed, not editable
        self._TotalRebound = 0  # Total Rebound, not editable
        self._TotalReleased = 0  # Total Released, not editable
        self._TotalReleaseRetried = 0  # Total Release Retried, not editable
        self._TotalRenewed = 0  # Total Renewed, not editable
        self._TotalRenewedRetried = 0  # Total Renewed Retried, not editable
        self._TotalRetired = 0  # Total Retried, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv6PortStatistics, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def Dhcpv6PortId(self):
        """
        get the value of property _Dhcpv6PortId
        """
        if self.force_auto_sync:
            self.get('Dhcpv6PortId')
        return self._Dhcpv6PortId

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
    def AverageSetupTime(self):
        """
        get the value of property _AverageSetupTime
        """
        if self.force_auto_sync:
            self.get('AverageSetupTime')
        return self._AverageSetupTime

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
    def AdvertiseRxCount(self):
        """
        get the value of property _AdvertiseRxCount
        """
        if self.force_auto_sync:
            self.get('AdvertiseRxCount')
        return self._AdvertiseRxCount

    @property
    def ReconfigureRxCount(self):
        """
        get the value of property _ReconfigureRxCount
        """
        if self.force_auto_sync:
            self.get('ReconfigureRxCount')
        return self._ReconfigureRxCount

    @property
    def ReplyRxCount(self):
        """
        get the value of property _ReplyRxCount
        """
        if self.force_auto_sync:
            self.get('ReplyRxCount')
        return self._ReplyRxCount

    @property
    def SuccessPercentage(self):
        """
        get the value of property _SuccessPercentage
        """
        if self.force_auto_sync:
            self.get('SuccessPercentage')
        return self._SuccessPercentage

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
    def TotalBoundFailed(self):
        """
        get the value of property _TotalBoundFailed
        """
        if self.force_auto_sync:
            self.get('TotalBoundFailed')
        return self._TotalBoundFailed

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

    def _set_dhcpv6portid_with_str(self, value):
        self._Dhcpv6PortId = value

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

    def _set_averagesetuptime_with_str(self, value):
        try:
            self._AverageSetupTime = int(value)
        except ValueError:
            self._AverageSetupTime = hex(int(value, 16))

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

    def _set_advertiserxcount_with_str(self, value):
        try:
            self._AdvertiseRxCount = int(value)
        except ValueError:
            self._AdvertiseRxCount = hex(int(value, 16))

    def _set_reconfigurerxcount_with_str(self, value):
        try:
            self._ReconfigureRxCount = int(value)
        except ValueError:
            self._ReconfigureRxCount = hex(int(value, 16))

    def _set_replyrxcount_with_str(self, value):
        try:
            self._ReplyRxCount = int(value)
        except ValueError:
            self._ReplyRxCount = hex(int(value, 16))

    def _set_successpercentage_with_str(self, value):
        self._SuccessPercentage = float(value)

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

    def _set_totalboundfailed_with_str(self, value):
        try:
            self._TotalBoundFailed = int(value)
        except ValueError:
            self._TotalBoundFailed = hex(int(value, 16))

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

