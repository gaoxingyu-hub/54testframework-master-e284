"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class BgpSessionBlockStatistic(Result):
    def __init__(self, **kwargs):
        self._BgpSessionBlockId = ''  # BGP Session Block Name, not editable
        self._PeerCount = 0  # BGP Session Count, not editable
        self._EstablishedPeers = 0  # Established BGP Session Count, not editable
        self._TxOpen = 0  # Tx Open Count, not editable
        self._RxOpen = 0  # Rx Open Count, not editable
        self._TxKeepalive = 0  # Tx Keepalive Count, not editable
        self._RxKeepalive = 0  # Rx Keepalive Count, not editable
        self._TxUpdate = 0  # Tx Update Count, not editable
        self._RxUpdate = 0  # Rx Update Count, not editable
        self._TxAdvertisedUpdate = 0  # Tx Advertised Update Count, not editable
        self._RxAdvertisedUpdate = 0  # Rx Advertised Update Count, not editable
        self._TxWithdrawnUpdate = 0  # Tx Withdrawn Update Count, not editable
        self._RxWithdrawnUpdate = 0  # Rx Withdrawn Update Count, not editable
        self._TxAdvertisedRoutes = 0  # Tx Advertised Routes Count, not editable
        self._RxAdvertisedRoutes = 0  # Rx Advertised Routes Count, not editable
        self._TxWithdrawnRoutes = 0  # Tx Withdrawn Routes Count, not editable
        self._RxWithdrawnRoutes = 0  # Rx Withdrawn Routes Count, not editable
        self._LastTxUpdateRoutes = 0  # Last Tx Update Routes Count, not editable
        self._LastRxUpdateRoutes = 0  # Last Rx Update Routes Count, not editable
        self._TxNotification = 0  # Tx Notification Count, not editable
        self._RxNotification = 0  # Rx Notification Count, not editable
        self._TxRefresh = 0  # Tx Refresh Count, not editable
        self._RxRefresh = 0  # Rx Refresh Count, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(BgpSessionBlockStatistic, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def BgpSessionBlockId(self):
        """
        get the value of property _BgpSessionBlockId
        """
        if self.force_auto_sync:
            self.get('BgpSessionBlockId')
        return self._BgpSessionBlockId

    @property
    def PeerCount(self):
        """
        get the value of property _PeerCount
        """
        if self.force_auto_sync:
            self.get('PeerCount')
        return self._PeerCount

    @property
    def EstablishedPeers(self):
        """
        get the value of property _EstablishedPeers
        """
        if self.force_auto_sync:
            self.get('EstablishedPeers')
        return self._EstablishedPeers

    @property
    def TxOpen(self):
        """
        get the value of property _TxOpen
        """
        if self.force_auto_sync:
            self.get('TxOpen')
        return self._TxOpen

    @property
    def RxOpen(self):
        """
        get the value of property _RxOpen
        """
        if self.force_auto_sync:
            self.get('RxOpen')
        return self._RxOpen

    @property
    def TxKeepalive(self):
        """
        get the value of property _TxKeepalive
        """
        if self.force_auto_sync:
            self.get('TxKeepalive')
        return self._TxKeepalive

    @property
    def RxKeepalive(self):
        """
        get the value of property _RxKeepalive
        """
        if self.force_auto_sync:
            self.get('RxKeepalive')
        return self._RxKeepalive

    @property
    def TxUpdate(self):
        """
        get the value of property _TxUpdate
        """
        if self.force_auto_sync:
            self.get('TxUpdate')
        return self._TxUpdate

    @property
    def RxUpdate(self):
        """
        get the value of property _RxUpdate
        """
        if self.force_auto_sync:
            self.get('RxUpdate')
        return self._RxUpdate

    @property
    def TxAdvertisedUpdate(self):
        """
        get the value of property _TxAdvertisedUpdate
        """
        if self.force_auto_sync:
            self.get('TxAdvertisedUpdate')
        return self._TxAdvertisedUpdate

    @property
    def RxAdvertisedUpdate(self):
        """
        get the value of property _RxAdvertisedUpdate
        """
        if self.force_auto_sync:
            self.get('RxAdvertisedUpdate')
        return self._RxAdvertisedUpdate

    @property
    def TxWithdrawnUpdate(self):
        """
        get the value of property _TxWithdrawnUpdate
        """
        if self.force_auto_sync:
            self.get('TxWithdrawnUpdate')
        return self._TxWithdrawnUpdate

    @property
    def RxWithdrawnUpdate(self):
        """
        get the value of property _RxWithdrawnUpdate
        """
        if self.force_auto_sync:
            self.get('RxWithdrawnUpdate')
        return self._RxWithdrawnUpdate

    @property
    def TxAdvertisedRoutes(self):
        """
        get the value of property _TxAdvertisedRoutes
        """
        if self.force_auto_sync:
            self.get('TxAdvertisedRoutes')
        return self._TxAdvertisedRoutes

    @property
    def RxAdvertisedRoutes(self):
        """
        get the value of property _RxAdvertisedRoutes
        """
        if self.force_auto_sync:
            self.get('RxAdvertisedRoutes')
        return self._RxAdvertisedRoutes

    @property
    def TxWithdrawnRoutes(self):
        """
        get the value of property _TxWithdrawnRoutes
        """
        if self.force_auto_sync:
            self.get('TxWithdrawnRoutes')
        return self._TxWithdrawnRoutes

    @property
    def RxWithdrawnRoutes(self):
        """
        get the value of property _RxWithdrawnRoutes
        """
        if self.force_auto_sync:
            self.get('RxWithdrawnRoutes')
        return self._RxWithdrawnRoutes

    @property
    def LastTxUpdateRoutes(self):
        """
        get the value of property _LastTxUpdateRoutes
        """
        if self.force_auto_sync:
            self.get('LastTxUpdateRoutes')
        return self._LastTxUpdateRoutes

    @property
    def LastRxUpdateRoutes(self):
        """
        get the value of property _LastRxUpdateRoutes
        """
        if self.force_auto_sync:
            self.get('LastRxUpdateRoutes')
        return self._LastRxUpdateRoutes

    @property
    def TxNotification(self):
        """
        get the value of property _TxNotification
        """
        if self.force_auto_sync:
            self.get('TxNotification')
        return self._TxNotification

    @property
    def RxNotification(self):
        """
        get the value of property _RxNotification
        """
        if self.force_auto_sync:
            self.get('RxNotification')
        return self._RxNotification

    @property
    def TxRefresh(self):
        """
        get the value of property _TxRefresh
        """
        if self.force_auto_sync:
            self.get('TxRefresh')
        return self._TxRefresh

    @property
    def RxRefresh(self):
        """
        get the value of property _RxRefresh
        """
        if self.force_auto_sync:
            self.get('RxRefresh')
        return self._RxRefresh

    def _set_bgpsessionblockid_with_str(self, value):
        self._BgpSessionBlockId = value

    def _set_peercount_with_str(self, value):
        try:
            self._PeerCount = int(value)
        except ValueError:
            self._PeerCount = hex(int(value, 16))

    def _set_establishedpeers_with_str(self, value):
        try:
            self._EstablishedPeers = int(value)
        except ValueError:
            self._EstablishedPeers = hex(int(value, 16))

    def _set_txopen_with_str(self, value):
        try:
            self._TxOpen = int(value)
        except ValueError:
            self._TxOpen = hex(int(value, 16))

    def _set_rxopen_with_str(self, value):
        try:
            self._RxOpen = int(value)
        except ValueError:
            self._RxOpen = hex(int(value, 16))

    def _set_txkeepalive_with_str(self, value):
        try:
            self._TxKeepalive = int(value)
        except ValueError:
            self._TxKeepalive = hex(int(value, 16))

    def _set_rxkeepalive_with_str(self, value):
        try:
            self._RxKeepalive = int(value)
        except ValueError:
            self._RxKeepalive = hex(int(value, 16))

    def _set_txupdate_with_str(self, value):
        try:
            self._TxUpdate = int(value)
        except ValueError:
            self._TxUpdate = hex(int(value, 16))

    def _set_rxupdate_with_str(self, value):
        try:
            self._RxUpdate = int(value)
        except ValueError:
            self._RxUpdate = hex(int(value, 16))

    def _set_txadvertisedupdate_with_str(self, value):
        try:
            self._TxAdvertisedUpdate = int(value)
        except ValueError:
            self._TxAdvertisedUpdate = hex(int(value, 16))

    def _set_rxadvertisedupdate_with_str(self, value):
        try:
            self._RxAdvertisedUpdate = int(value)
        except ValueError:
            self._RxAdvertisedUpdate = hex(int(value, 16))

    def _set_txwithdrawnupdate_with_str(self, value):
        try:
            self._TxWithdrawnUpdate = int(value)
        except ValueError:
            self._TxWithdrawnUpdate = hex(int(value, 16))

    def _set_rxwithdrawnupdate_with_str(self, value):
        try:
            self._RxWithdrawnUpdate = int(value)
        except ValueError:
            self._RxWithdrawnUpdate = hex(int(value, 16))

    def _set_txadvertisedroutes_with_str(self, value):
        try:
            self._TxAdvertisedRoutes = int(value)
        except ValueError:
            self._TxAdvertisedRoutes = hex(int(value, 16))

    def _set_rxadvertisedroutes_with_str(self, value):
        try:
            self._RxAdvertisedRoutes = int(value)
        except ValueError:
            self._RxAdvertisedRoutes = hex(int(value, 16))

    def _set_txwithdrawnroutes_with_str(self, value):
        try:
            self._TxWithdrawnRoutes = int(value)
        except ValueError:
            self._TxWithdrawnRoutes = hex(int(value, 16))

    def _set_rxwithdrawnroutes_with_str(self, value):
        try:
            self._RxWithdrawnRoutes = int(value)
        except ValueError:
            self._RxWithdrawnRoutes = hex(int(value, 16))

    def _set_lasttxupdateroutes_with_str(self, value):
        try:
            self._LastTxUpdateRoutes = int(value)
        except ValueError:
            self._LastTxUpdateRoutes = hex(int(value, 16))

    def _set_lastrxupdateroutes_with_str(self, value):
        try:
            self._LastRxUpdateRoutes = int(value)
        except ValueError:
            self._LastRxUpdateRoutes = hex(int(value, 16))

    def _set_txnotification_with_str(self, value):
        try:
            self._TxNotification = int(value)
        except ValueError:
            self._TxNotification = hex(int(value, 16))

    def _set_rxnotification_with_str(self, value):
        try:
            self._RxNotification = int(value)
        except ValueError:
            self._RxNotification = hex(int(value, 16))

    def _set_txrefresh_with_str(self, value):
        try:
            self._TxRefresh = int(value)
        except ValueError:
            self._TxRefresh = hex(int(value, 16))

    def _set_rxrefresh_with_str(self, value):
        try:
            self._RxRefresh = int(value)
        except ValueError:
            self._RxRefresh = hex(int(value, 16))

