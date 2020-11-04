"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Dhcpv4PortStats(Result):
    def __init__(self, **kwargs):
        self._PortHandle = ''  # Port Name, not editable
        self._CurrentAttempt = 0  # Currently Attempt, not editable
        self._CurrentBound = 0  # Currently Bound, not editable
        self._TotalAttempt = 0  # Total Attempt, not editable
        self._TotalBound = 0  # Total Bound, not editable
        self._TotalFailed = 0  # Total Fail, not editable
        self._TotalReboot = 0  # Total Init-Reboot, not editable
        self._TotalRenew = 0  # Total Renew, not editable
        self._TotalRebind = 0  # Total Rebind, not editable
        self._TotalRetry = 0  # Total Retry, not editable
        self._TxDiscover = 0  # Tx Discover, not editable
        self._RxOffer = 0  # Rx Offer, not editable
        self._TxRequest = 0  # Tx Request, not editable
        self._RxAck = 0  # Rx ACK, not editable
        self._RxNak = 0  # Rx NAK, not editable
        self._TxRenew = 0  # Tx Renew, not editable
        self._TxRebind = 0  # Tx Rebind, not editable
        self._TxReboot = 0  # Tx Reboot, not editable
        self._TxRelease = 0  # Tx Release, not editable
        self._RxForceRenew = 0  # Rx Force Renew, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4PortStats, self).__init__(**properties)

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
    def CurrentAttempt(self):
        """
        get the value of property _CurrentAttempt
        """
        if self.force_auto_sync:
            self.get('CurrentAttempt')
        return self._CurrentAttempt

    @property
    def CurrentBound(self):
        """
        get the value of property _CurrentBound
        """
        if self.force_auto_sync:
            self.get('CurrentBound')
        return self._CurrentBound

    @property
    def TotalAttempt(self):
        """
        get the value of property _TotalAttempt
        """
        if self.force_auto_sync:
            self.get('TotalAttempt')
        return self._TotalAttempt

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
    def TotalReboot(self):
        """
        get the value of property _TotalReboot
        """
        if self.force_auto_sync:
            self.get('TotalReboot')
        return self._TotalReboot

    @property
    def TotalRenew(self):
        """
        get the value of property _TotalRenew
        """
        if self.force_auto_sync:
            self.get('TotalRenew')
        return self._TotalRenew

    @property
    def TotalRebind(self):
        """
        get the value of property _TotalRebind
        """
        if self.force_auto_sync:
            self.get('TotalRebind')
        return self._TotalRebind

    @property
    def TotalRetry(self):
        """
        get the value of property _TotalRetry
        """
        if self.force_auto_sync:
            self.get('TotalRetry')
        return self._TotalRetry

    @property
    def TxDiscover(self):
        """
        get the value of property _TxDiscover
        """
        if self.force_auto_sync:
            self.get('TxDiscover')
        return self._TxDiscover

    @property
    def RxOffer(self):
        """
        get the value of property _RxOffer
        """
        if self.force_auto_sync:
            self.get('RxOffer')
        return self._RxOffer

    @property
    def TxRequest(self):
        """
        get the value of property _TxRequest
        """
        if self.force_auto_sync:
            self.get('TxRequest')
        return self._TxRequest

    @property
    def RxAck(self):
        """
        get the value of property _RxAck
        """
        if self.force_auto_sync:
            self.get('RxAck')
        return self._RxAck

    @property
    def RxNak(self):
        """
        get the value of property _RxNak
        """
        if self.force_auto_sync:
            self.get('RxNak')
        return self._RxNak

    @property
    def TxRenew(self):
        """
        get the value of property _TxRenew
        """
        if self.force_auto_sync:
            self.get('TxRenew')
        return self._TxRenew

    @property
    def TxRebind(self):
        """
        get the value of property _TxRebind
        """
        if self.force_auto_sync:
            self.get('TxRebind')
        return self._TxRebind

    @property
    def TxReboot(self):
        """
        get the value of property _TxReboot
        """
        if self.force_auto_sync:
            self.get('TxReboot')
        return self._TxReboot

    @property
    def TxRelease(self):
        """
        get the value of property _TxRelease
        """
        if self.force_auto_sync:
            self.get('TxRelease')
        return self._TxRelease

    @property
    def RxForceRenew(self):
        """
        get the value of property _RxForceRenew
        """
        if self.force_auto_sync:
            self.get('RxForceRenew')
        return self._RxForceRenew

    def _set_porthandle_with_str(self, value):
        self._PortHandle = value

    def _set_currentattempt_with_str(self, value):
        try:
            self._CurrentAttempt = int(value)
        except ValueError:
            self._CurrentAttempt = hex(int(value, 16))

    def _set_currentbound_with_str(self, value):
        try:
            self._CurrentBound = int(value)
        except ValueError:
            self._CurrentBound = hex(int(value, 16))

    def _set_totalattempt_with_str(self, value):
        try:
            self._TotalAttempt = int(value)
        except ValueError:
            self._TotalAttempt = hex(int(value, 16))

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

    def _set_totalreboot_with_str(self, value):
        try:
            self._TotalReboot = int(value)
        except ValueError:
            self._TotalReboot = hex(int(value, 16))

    def _set_totalrenew_with_str(self, value):
        try:
            self._TotalRenew = int(value)
        except ValueError:
            self._TotalRenew = hex(int(value, 16))

    def _set_totalrebind_with_str(self, value):
        try:
            self._TotalRebind = int(value)
        except ValueError:
            self._TotalRebind = hex(int(value, 16))

    def _set_totalretry_with_str(self, value):
        try:
            self._TotalRetry = int(value)
        except ValueError:
            self._TotalRetry = hex(int(value, 16))

    def _set_txdiscover_with_str(self, value):
        try:
            self._TxDiscover = int(value)
        except ValueError:
            self._TxDiscover = hex(int(value, 16))

    def _set_rxoffer_with_str(self, value):
        try:
            self._RxOffer = int(value)
        except ValueError:
            self._RxOffer = hex(int(value, 16))

    def _set_txrequest_with_str(self, value):
        try:
            self._TxRequest = int(value)
        except ValueError:
            self._TxRequest = hex(int(value, 16))

    def _set_rxack_with_str(self, value):
        try:
            self._RxAck = int(value)
        except ValueError:
            self._RxAck = hex(int(value, 16))

    def _set_rxnak_with_str(self, value):
        try:
            self._RxNak = int(value)
        except ValueError:
            self._RxNak = hex(int(value, 16))

    def _set_txrenew_with_str(self, value):
        try:
            self._TxRenew = int(value)
        except ValueError:
            self._TxRenew = hex(int(value, 16))

    def _set_txrebind_with_str(self, value):
        try:
            self._TxRebind = int(value)
        except ValueError:
            self._TxRebind = hex(int(value, 16))

    def _set_txreboot_with_str(self, value):
        try:
            self._TxReboot = int(value)
        except ValueError:
            self._TxReboot = hex(int(value, 16))

    def _set_txrelease_with_str(self, value):
        try:
            self._TxRelease = int(value)
        except ValueError:
            self._TxRelease = hex(int(value, 16))

    def _set_rxforcerenew_with_str(self, value):
        try:
            self._RxForceRenew = int(value)
        except ValueError:
            self._RxForceRenew = hex(int(value, 16))

