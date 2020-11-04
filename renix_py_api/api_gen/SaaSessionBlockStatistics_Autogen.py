"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class SaaSessionBlockStatistics(Result):
    def __init__(self, **kwargs):
        self._SaaSessionBlockId = ''  # Session Block Name, not editable
        self._BindingState = 'None'  # Binding State, not editable
        self._BlockSessionState = 'Disabled'  # Block State, not editable
        self._CurrentlyAttempting = 0  # Currently Attempting, not editable
        self._CurrentlyIdle = 0  # Currently Idle, not editable
        self._CurrentlyBound = 0  # Currently Bound, not editable
        self._AttemptRate = 0  # Attempt Rate (sessions/sec), not editable
        self._BindRate = 0  # Bind Rate (sessions/sec), not editable
        self._TxNeighborSolicitation = 0  # Tx Neighbor Solicitations (Autoconfiguration), not editable
        self._RxNeighborSolicitation = 0  # Rx Neighbor Solicitations (Autoconfiguration), not editable
        self._TxNeighborAdvertisement = 0  # Tx Neighbor Advertisements (Autoconfiguration), not editable
        self._RxNeighborAdvertisement = 0  # Rx Neighbor Advertisements (Autoconfiguration), not editable
        self._TxRouterSolicitation = 0  # Tx Router Solicitations (Autoconfiguration), not editable
        self._RxRouterAdvertisement = 0  # Rx Router Advertisements (Autoconfiguration), not editable
        self._TotalAttempted = 0  # Total Attempted, not editable
        self._TotalBound = 0  # Total Bound, not editable
        self._TotalDADFailed = 0  # Total DAD Failed, not editable
        self._TotalRATimeoutFailed = 0  # Total RA Timeout Failed, not editable
        self._TotalFailed = 0  # Total Failed, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(SaaSessionBlockStatistics, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def SaaSessionBlockId(self):
        """
        get the value of property _SaaSessionBlockId
        """
        if self.force_auto_sync:
            self.get('SaaSessionBlockId')
        return self._SaaSessionBlockId

    @property
    def BindingState(self):
        """
        get the value of property _BindingState
        """
        if self.force_auto_sync:
            self.get('BindingState')
        return self._BindingState

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
    def CurrentlyIdle(self):
        """
        get the value of property _CurrentlyIdle
        """
        if self.force_auto_sync:
            self.get('CurrentlyIdle')
        return self._CurrentlyIdle

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
    def TxNeighborSolicitation(self):
        """
        get the value of property _TxNeighborSolicitation
        """
        if self.force_auto_sync:
            self.get('TxNeighborSolicitation')
        return self._TxNeighborSolicitation

    @property
    def RxNeighborSolicitation(self):
        """
        get the value of property _RxNeighborSolicitation
        """
        if self.force_auto_sync:
            self.get('RxNeighborSolicitation')
        return self._RxNeighborSolicitation

    @property
    def TxNeighborAdvertisement(self):
        """
        get the value of property _TxNeighborAdvertisement
        """
        if self.force_auto_sync:
            self.get('TxNeighborAdvertisement')
        return self._TxNeighborAdvertisement

    @property
    def RxNeighborAdvertisement(self):
        """
        get the value of property _RxNeighborAdvertisement
        """
        if self.force_auto_sync:
            self.get('RxNeighborAdvertisement')
        return self._RxNeighborAdvertisement

    @property
    def TxRouterSolicitation(self):
        """
        get the value of property _TxRouterSolicitation
        """
        if self.force_auto_sync:
            self.get('TxRouterSolicitation')
        return self._TxRouterSolicitation

    @property
    def RxRouterAdvertisement(self):
        """
        get the value of property _RxRouterAdvertisement
        """
        if self.force_auto_sync:
            self.get('RxRouterAdvertisement')
        return self._RxRouterAdvertisement

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
    def TotalDADFailed(self):
        """
        get the value of property _TotalDADFailed
        """
        if self.force_auto_sync:
            self.get('TotalDADFailed')
        return self._TotalDADFailed

    @property
    def TotalRATimeoutFailed(self):
        """
        get the value of property _TotalRATimeoutFailed
        """
        if self.force_auto_sync:
            self.get('TotalRATimeoutFailed')
        return self._TotalRATimeoutFailed

    @property
    def TotalFailed(self):
        """
        get the value of property _TotalFailed
        """
        if self.force_auto_sync:
            self.get('TotalFailed')
        return self._TotalFailed

    def _set_saasessionblockid_with_str(self, value):
        self._SaaSessionBlockId = value

    def _set_bindingstate_with_str(self, value):
        self._BindingState = value

    def _set_blocksessionstate_with_str(self, value):
        self._BlockSessionState = value

    def _set_currentlyattempting_with_str(self, value):
        try:
            self._CurrentlyAttempting = int(value)
        except ValueError:
            self._CurrentlyAttempting = hex(int(value, 16))

    def _set_currentlyidle_with_str(self, value):
        try:
            self._CurrentlyIdle = int(value)
        except ValueError:
            self._CurrentlyIdle = hex(int(value, 16))

    def _set_currentlybound_with_str(self, value):
        try:
            self._CurrentlyBound = int(value)
        except ValueError:
            self._CurrentlyBound = hex(int(value, 16))

    def _set_attemptrate_with_str(self, value):
        self._AttemptRate = float(value)

    def _set_bindrate_with_str(self, value):
        self._BindRate = float(value)

    def _set_txneighborsolicitation_with_str(self, value):
        try:
            self._TxNeighborSolicitation = int(value)
        except ValueError:
            self._TxNeighborSolicitation = hex(int(value, 16))

    def _set_rxneighborsolicitation_with_str(self, value):
        try:
            self._RxNeighborSolicitation = int(value)
        except ValueError:
            self._RxNeighborSolicitation = hex(int(value, 16))

    def _set_txneighboradvertisement_with_str(self, value):
        try:
            self._TxNeighborAdvertisement = int(value)
        except ValueError:
            self._TxNeighborAdvertisement = hex(int(value, 16))

    def _set_rxneighboradvertisement_with_str(self, value):
        try:
            self._RxNeighborAdvertisement = int(value)
        except ValueError:
            self._RxNeighborAdvertisement = hex(int(value, 16))

    def _set_txroutersolicitation_with_str(self, value):
        try:
            self._TxRouterSolicitation = int(value)
        except ValueError:
            self._TxRouterSolicitation = hex(int(value, 16))

    def _set_rxrouteradvertisement_with_str(self, value):
        try:
            self._RxRouterAdvertisement = int(value)
        except ValueError:
            self._RxRouterAdvertisement = hex(int(value, 16))

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

    def _set_totaldadfailed_with_str(self, value):
        try:
            self._TotalDADFailed = int(value)
        except ValueError:
            self._TotalDADFailed = hex(int(value, 16))

    def _set_totalratimeoutfailed_with_str(self, value):
        try:
            self._TotalRATimeoutFailed = int(value)
        except ValueError:
            self._TotalRATimeoutFailed = hex(int(value, 16))

    def _set_totalfailed_with_str(self, value):
        try:
            self._TotalFailed = int(value)
        except ValueError:
            self._TotalFailed = hex(int(value, 16))

