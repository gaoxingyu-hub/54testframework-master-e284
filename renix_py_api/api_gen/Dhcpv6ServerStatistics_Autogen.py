"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Dhcpv6ServerStatistics(Result):
    def __init__(self, **kwargs):
        self._Dhcpv6ServerId = ''  # DHCPv6/PD Server Session, not editable
        self._ServerState = 'Down'  # Server State, not editable
        self._CurrentlyBound = 0  # Currently Bound, not editable
        self._ReconfigureRebindTxCount = 0  # Reconfigure Rebind Tx Count, not editable
        self._ReconfigureRenewTxCount = 0  # Reconfigure Renew Tx Count, not editable
        self._ReconfigureTxCount = 0  # Reconfigure Tx Count, not editable
        self._AdvertiseTxCount = 0  # Advertise Tx Count, not editable
        self._ReplyTxCount = 0  # Reply Tx Count, not editable
        self._SolicitRxCount = 0  # Solicit Rx Count, not editable
        self._RequestRxCount = 0  # Request Rx Count, not editable
        self._ReleaseRxCount = 0  # Release Rx Count, not editable
        self._RenewRxCount = 0  # Renew Rx Count, not editable
        self._RebindRxCount = 0  # Rebind Rx Count, not editable
        self._TotalBound = 0  # Total Bound, not editable
        self._TotalExpired = 0  # Total Expired, not editable
        self._TotalReleased = 0  # Total Released, not editable
        self._TotalRenewed = 0  # Total Renewed, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv6ServerStatistics, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def Dhcpv6ServerId(self):
        """
        get the value of property _Dhcpv6ServerId
        """
        if self.force_auto_sync:
            self.get('Dhcpv6ServerId')
        return self._Dhcpv6ServerId

    @property
    def ServerState(self):
        """
        get the value of property _ServerState
        """
        if self.force_auto_sync:
            self.get('ServerState')
        return self._ServerState

    @property
    def CurrentlyBound(self):
        """
        get the value of property _CurrentlyBound
        """
        if self.force_auto_sync:
            self.get('CurrentlyBound')
        return self._CurrentlyBound

    @property
    def ReconfigureRebindTxCount(self):
        """
        get the value of property _ReconfigureRebindTxCount
        """
        if self.force_auto_sync:
            self.get('ReconfigureRebindTxCount')
        return self._ReconfigureRebindTxCount

    @property
    def ReconfigureRenewTxCount(self):
        """
        get the value of property _ReconfigureRenewTxCount
        """
        if self.force_auto_sync:
            self.get('ReconfigureRenewTxCount')
        return self._ReconfigureRenewTxCount

    @property
    def ReconfigureTxCount(self):
        """
        get the value of property _ReconfigureTxCount
        """
        if self.force_auto_sync:
            self.get('ReconfigureTxCount')
        return self._ReconfigureTxCount

    @property
    def AdvertiseTxCount(self):
        """
        get the value of property _AdvertiseTxCount
        """
        if self.force_auto_sync:
            self.get('AdvertiseTxCount')
        return self._AdvertiseTxCount

    @property
    def ReplyTxCount(self):
        """
        get the value of property _ReplyTxCount
        """
        if self.force_auto_sync:
            self.get('ReplyTxCount')
        return self._ReplyTxCount

    @property
    def SolicitRxCount(self):
        """
        get the value of property _SolicitRxCount
        """
        if self.force_auto_sync:
            self.get('SolicitRxCount')
        return self._SolicitRxCount

    @property
    def RequestRxCount(self):
        """
        get the value of property _RequestRxCount
        """
        if self.force_auto_sync:
            self.get('RequestRxCount')
        return self._RequestRxCount

    @property
    def ReleaseRxCount(self):
        """
        get the value of property _ReleaseRxCount
        """
        if self.force_auto_sync:
            self.get('ReleaseRxCount')
        return self._ReleaseRxCount

    @property
    def RenewRxCount(self):
        """
        get the value of property _RenewRxCount
        """
        if self.force_auto_sync:
            self.get('RenewRxCount')
        return self._RenewRxCount

    @property
    def RebindRxCount(self):
        """
        get the value of property _RebindRxCount
        """
        if self.force_auto_sync:
            self.get('RebindRxCount')
        return self._RebindRxCount

    @property
    def TotalBound(self):
        """
        get the value of property _TotalBound
        """
        if self.force_auto_sync:
            self.get('TotalBound')
        return self._TotalBound

    @property
    def TotalExpired(self):
        """
        get the value of property _TotalExpired
        """
        if self.force_auto_sync:
            self.get('TotalExpired')
        return self._TotalExpired

    @property
    def TotalReleased(self):
        """
        get the value of property _TotalReleased
        """
        if self.force_auto_sync:
            self.get('TotalReleased')
        return self._TotalReleased

    @property
    def TotalRenewed(self):
        """
        get the value of property _TotalRenewed
        """
        if self.force_auto_sync:
            self.get('TotalRenewed')
        return self._TotalRenewed

    def _set_dhcpv6serverid_with_str(self, value):
        self._Dhcpv6ServerId = value

    def _set_serverstate_with_str(self, value):
        self._ServerState = value

    def _set_currentlybound_with_str(self, value):
        try:
            self._CurrentlyBound = int(value)
        except ValueError:
            self._CurrentlyBound = hex(int(value, 16))

    def _set_reconfigurerebindtxcount_with_str(self, value):
        try:
            self._ReconfigureRebindTxCount = int(value)
        except ValueError:
            self._ReconfigureRebindTxCount = hex(int(value, 16))

    def _set_reconfigurerenewtxcount_with_str(self, value):
        try:
            self._ReconfigureRenewTxCount = int(value)
        except ValueError:
            self._ReconfigureRenewTxCount = hex(int(value, 16))

    def _set_reconfiguretxcount_with_str(self, value):
        try:
            self._ReconfigureTxCount = int(value)
        except ValueError:
            self._ReconfigureTxCount = hex(int(value, 16))

    def _set_advertisetxcount_with_str(self, value):
        try:
            self._AdvertiseTxCount = int(value)
        except ValueError:
            self._AdvertiseTxCount = hex(int(value, 16))

    def _set_replytxcount_with_str(self, value):
        try:
            self._ReplyTxCount = int(value)
        except ValueError:
            self._ReplyTxCount = hex(int(value, 16))

    def _set_solicitrxcount_with_str(self, value):
        try:
            self._SolicitRxCount = int(value)
        except ValueError:
            self._SolicitRxCount = hex(int(value, 16))

    def _set_requestrxcount_with_str(self, value):
        try:
            self._RequestRxCount = int(value)
        except ValueError:
            self._RequestRxCount = hex(int(value, 16))

    def _set_releaserxcount_with_str(self, value):
        try:
            self._ReleaseRxCount = int(value)
        except ValueError:
            self._ReleaseRxCount = hex(int(value, 16))

    def _set_renewrxcount_with_str(self, value):
        try:
            self._RenewRxCount = int(value)
        except ValueError:
            self._RenewRxCount = hex(int(value, 16))

    def _set_rebindrxcount_with_str(self, value):
        try:
            self._RebindRxCount = int(value)
        except ValueError:
            self._RebindRxCount = hex(int(value, 16))

    def _set_totalbound_with_str(self, value):
        try:
            self._TotalBound = int(value)
        except ValueError:
            self._TotalBound = hex(int(value, 16))

    def _set_totalexpired_with_str(self, value):
        try:
            self._TotalExpired = int(value)
        except ValueError:
            self._TotalExpired = hex(int(value, 16))

    def _set_totalreleased_with_str(self, value):
        try:
            self._TotalReleased = int(value)
        except ValueError:
            self._TotalReleased = hex(int(value, 16))

    def _set_totalrenewed_with_str(self, value):
        try:
            self._TotalRenewed = int(value)
        except ValueError:
            self._TotalRenewed = hex(int(value, 16))

