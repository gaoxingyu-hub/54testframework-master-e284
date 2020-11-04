"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Dhcpv4ServerStats(Result):
    def __init__(self, **kwargs):
        self._ServerHandle = ''  # Server Name, not editable
        self._CurrentBound = 0  # Currently Bound, not editable
        self._TotalBound = 0  # Total Bound, not editable
        self._TotalExpire = 0  # Total Expire, not editable
        self._TotalReboot = 0  # Total Init-Reboot, not editable
        self._TotalRenew = 0  # Total Renew, not editable
        self._TotalRebind = 0  # Total Rebind, not editable
        self._TotalRelease = 0  # Total Release, not editable
        self._RxDiscover = 0  # Rx Discover, not editable
        self._TxOffer = 0  # Tx Offer, not editable
        self._RxRequest = 0  # Rx Request, not editable
        self._TxAck = 0  # Tx ACK, not editable
        self._TxNak = 0  # Tx NAK, not editable
        self._RxDecline = 0  # Rx Decline, not editable
        self._RxRelease = 0  # Rx Release, not editable
        self._TxForceRenew = 0  # Tx Force Renew, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4ServerStats, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def ServerHandle(self):
        """
        get the value of property _ServerHandle
        """
        if self.force_auto_sync:
            self.get('ServerHandle')
        return self._ServerHandle

    @property
    def CurrentBound(self):
        """
        get the value of property _CurrentBound
        """
        if self.force_auto_sync:
            self.get('CurrentBound')
        return self._CurrentBound

    @property
    def TotalBound(self):
        """
        get the value of property _TotalBound
        """
        if self.force_auto_sync:
            self.get('TotalBound')
        return self._TotalBound

    @property
    def TotalExpire(self):
        """
        get the value of property _TotalExpire
        """
        if self.force_auto_sync:
            self.get('TotalExpire')
        return self._TotalExpire

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
    def TotalRelease(self):
        """
        get the value of property _TotalRelease
        """
        if self.force_auto_sync:
            self.get('TotalRelease')
        return self._TotalRelease

    @property
    def RxDiscover(self):
        """
        get the value of property _RxDiscover
        """
        if self.force_auto_sync:
            self.get('RxDiscover')
        return self._RxDiscover

    @property
    def TxOffer(self):
        """
        get the value of property _TxOffer
        """
        if self.force_auto_sync:
            self.get('TxOffer')
        return self._TxOffer

    @property
    def RxRequest(self):
        """
        get the value of property _RxRequest
        """
        if self.force_auto_sync:
            self.get('RxRequest')
        return self._RxRequest

    @property
    def TxAck(self):
        """
        get the value of property _TxAck
        """
        if self.force_auto_sync:
            self.get('TxAck')
        return self._TxAck

    @property
    def TxNak(self):
        """
        get the value of property _TxNak
        """
        if self.force_auto_sync:
            self.get('TxNak')
        return self._TxNak

    @property
    def RxDecline(self):
        """
        get the value of property _RxDecline
        """
        if self.force_auto_sync:
            self.get('RxDecline')
        return self._RxDecline

    @property
    def RxRelease(self):
        """
        get the value of property _RxRelease
        """
        if self.force_auto_sync:
            self.get('RxRelease')
        return self._RxRelease

    @property
    def TxForceRenew(self):
        """
        get the value of property _TxForceRenew
        """
        if self.force_auto_sync:
            self.get('TxForceRenew')
        return self._TxForceRenew

    def _set_serverhandle_with_str(self, value):
        self._ServerHandle = value

    def _set_currentbound_with_str(self, value):
        try:
            self._CurrentBound = int(value)
        except ValueError:
            self._CurrentBound = hex(int(value, 16))

    def _set_totalbound_with_str(self, value):
        try:
            self._TotalBound = int(value)
        except ValueError:
            self._TotalBound = hex(int(value, 16))

    def _set_totalexpire_with_str(self, value):
        try:
            self._TotalExpire = int(value)
        except ValueError:
            self._TotalExpire = hex(int(value, 16))

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

    def _set_totalrelease_with_str(self, value):
        try:
            self._TotalRelease = int(value)
        except ValueError:
            self._TotalRelease = hex(int(value, 16))

    def _set_rxdiscover_with_str(self, value):
        try:
            self._RxDiscover = int(value)
        except ValueError:
            self._RxDiscover = hex(int(value, 16))

    def _set_txoffer_with_str(self, value):
        try:
            self._TxOffer = int(value)
        except ValueError:
            self._TxOffer = hex(int(value, 16))

    def _set_rxrequest_with_str(self, value):
        try:
            self._RxRequest = int(value)
        except ValueError:
            self._RxRequest = hex(int(value, 16))

    def _set_txack_with_str(self, value):
        try:
            self._TxAck = int(value)
        except ValueError:
            self._TxAck = hex(int(value, 16))

    def _set_txnak_with_str(self, value):
        try:
            self._TxNak = int(value)
        except ValueError:
            self._TxNak = hex(int(value, 16))

    def _set_rxdecline_with_str(self, value):
        try:
            self._RxDecline = int(value)
        except ValueError:
            self._RxDecline = hex(int(value, 16))

    def _set_rxrelease_with_str(self, value):
        try:
            self._RxRelease = int(value)
        except ValueError:
            self._RxRelease = hex(int(value, 16))

    def _set_txforcerenew_with_str(self, value):
        try:
            self._TxForceRenew = int(value)
        except ValueError:
            self._TxForceRenew = hex(int(value, 16))

