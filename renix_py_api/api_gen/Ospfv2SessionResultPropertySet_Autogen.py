"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Ospfv2SessionResultPropertySet(Result):
    def __init__(self, **kwargs):
        self._SessionHandle = ''  # Session Name, not editable
        self._RouterState = 'Not Start'  # Router State, not editable
        self._AdjacencyState = 'Down'  # Adjacency Status, not editable
        self._TxHello = 0  # Tx Hello, not editable
        self._RxHello = 0  # Rx Hello, not editable
        self._TxDd = 0  # Tx DD, not editable
        self._RxDd = 0  # Rx DD, not editable
        self._TxRouterLsa = 0  # Tx Router LSA, not editable
        self._RxRouterLsa = 0  # Rx Router LSA, not editable
        self._TxNetworkLsa = 0  # Tx Network LSA, not editable
        self._RxNetworkLsa = 0  # Rx Network LSA, not editable
        self._TxSummaryLsa = 0  # Tx Network Summary LSA, not editable
        self._RxSummaryLsa = 0  # Rx Network Summary LSA, not editable
        self._TxAsbrSummaryLsa = 0  # Tx ASBR Summary LSA, not editable
        self._RxAsbrSummaryLsa = 0  # Rx ASBR Summary LSA, not editable
        self._TxAsExternalLsa = 0  # Tx AS External LSA, not editable
        self._RxAsExternalLsa = 0  # Rx AS External LSA, not editable
        self._TxNssaLsa = 0  # Tx NSSA LSA, not editable
        self._RxNssaLsa = 0  # Rx NSSA LSA, not editable
        self._TxTeLsa = 0  # Tx TE LSA, not editable
        self._RxTeLsa = 0  # Rx TE LSA, not editable
        self._TxRequest = 0  # Tx Request, not editable
        self._RxRequest = 0  # Rx Request, not editable
        self._TxUpdate = 0  # Tx Update, not editable
        self._RxUpdate = 0  # Rx Update, not editable
        self._TxAck = 0  # Tx Ack, not editable
        self._RxAck = 0  # Rx Ack, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv2SessionResultPropertySet, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def SessionHandle(self):
        """
        get the value of property _SessionHandle
        """
        if self.force_auto_sync:
            self.get('SessionHandle')
        return self._SessionHandle

    @property
    def RouterState(self):
        """
        get the value of property _RouterState
        """
        if self.force_auto_sync:
            self.get('RouterState')
        return self._RouterState

    @property
    def AdjacencyState(self):
        """
        get the value of property _AdjacencyState
        """
        if self.force_auto_sync:
            self.get('AdjacencyState')
        return self._AdjacencyState

    @property
    def TxHello(self):
        """
        get the value of property _TxHello
        """
        if self.force_auto_sync:
            self.get('TxHello')
        return self._TxHello

    @property
    def RxHello(self):
        """
        get the value of property _RxHello
        """
        if self.force_auto_sync:
            self.get('RxHello')
        return self._RxHello

    @property
    def TxDd(self):
        """
        get the value of property _TxDd
        """
        if self.force_auto_sync:
            self.get('TxDd')
        return self._TxDd

    @property
    def RxDd(self):
        """
        get the value of property _RxDd
        """
        if self.force_auto_sync:
            self.get('RxDd')
        return self._RxDd

    @property
    def TxRouterLsa(self):
        """
        get the value of property _TxRouterLsa
        """
        if self.force_auto_sync:
            self.get('TxRouterLsa')
        return self._TxRouterLsa

    @property
    def RxRouterLsa(self):
        """
        get the value of property _RxRouterLsa
        """
        if self.force_auto_sync:
            self.get('RxRouterLsa')
        return self._RxRouterLsa

    @property
    def TxNetworkLsa(self):
        """
        get the value of property _TxNetworkLsa
        """
        if self.force_auto_sync:
            self.get('TxNetworkLsa')
        return self._TxNetworkLsa

    @property
    def RxNetworkLsa(self):
        """
        get the value of property _RxNetworkLsa
        """
        if self.force_auto_sync:
            self.get('RxNetworkLsa')
        return self._RxNetworkLsa

    @property
    def TxSummaryLsa(self):
        """
        get the value of property _TxSummaryLsa
        """
        if self.force_auto_sync:
            self.get('TxSummaryLsa')
        return self._TxSummaryLsa

    @property
    def RxSummaryLsa(self):
        """
        get the value of property _RxSummaryLsa
        """
        if self.force_auto_sync:
            self.get('RxSummaryLsa')
        return self._RxSummaryLsa

    @property
    def TxAsbrSummaryLsa(self):
        """
        get the value of property _TxAsbrSummaryLsa
        """
        if self.force_auto_sync:
            self.get('TxAsbrSummaryLsa')
        return self._TxAsbrSummaryLsa

    @property
    def RxAsbrSummaryLsa(self):
        """
        get the value of property _RxAsbrSummaryLsa
        """
        if self.force_auto_sync:
            self.get('RxAsbrSummaryLsa')
        return self._RxAsbrSummaryLsa

    @property
    def TxAsExternalLsa(self):
        """
        get the value of property _TxAsExternalLsa
        """
        if self.force_auto_sync:
            self.get('TxAsExternalLsa')
        return self._TxAsExternalLsa

    @property
    def RxAsExternalLsa(self):
        """
        get the value of property _RxAsExternalLsa
        """
        if self.force_auto_sync:
            self.get('RxAsExternalLsa')
        return self._RxAsExternalLsa

    @property
    def TxNssaLsa(self):
        """
        get the value of property _TxNssaLsa
        """
        if self.force_auto_sync:
            self.get('TxNssaLsa')
        return self._TxNssaLsa

    @property
    def RxNssaLsa(self):
        """
        get the value of property _RxNssaLsa
        """
        if self.force_auto_sync:
            self.get('RxNssaLsa')
        return self._RxNssaLsa

    @property
    def TxTeLsa(self):
        """
        get the value of property _TxTeLsa
        """
        if self.force_auto_sync:
            self.get('TxTeLsa')
        return self._TxTeLsa

    @property
    def RxTeLsa(self):
        """
        get the value of property _RxTeLsa
        """
        if self.force_auto_sync:
            self.get('RxTeLsa')
        return self._RxTeLsa

    @property
    def TxRequest(self):
        """
        get the value of property _TxRequest
        """
        if self.force_auto_sync:
            self.get('TxRequest')
        return self._TxRequest

    @property
    def RxRequest(self):
        """
        get the value of property _RxRequest
        """
        if self.force_auto_sync:
            self.get('RxRequest')
        return self._RxRequest

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
    def TxAck(self):
        """
        get the value of property _TxAck
        """
        if self.force_auto_sync:
            self.get('TxAck')
        return self._TxAck

    @property
    def RxAck(self):
        """
        get the value of property _RxAck
        """
        if self.force_auto_sync:
            self.get('RxAck')
        return self._RxAck

    def _set_sessionhandle_with_str(self, value):
        self._SessionHandle = value

    def _set_routerstate_with_str(self, value):
        self._RouterState = value

    def _set_adjacencystate_with_str(self, value):
        self._AdjacencyState = value

    def _set_txhello_with_str(self, value):
        try:
            self._TxHello = int(value)
        except ValueError:
            self._TxHello = hex(int(value, 16))

    def _set_rxhello_with_str(self, value):
        try:
            self._RxHello = int(value)
        except ValueError:
            self._RxHello = hex(int(value, 16))

    def _set_txdd_with_str(self, value):
        try:
            self._TxDd = int(value)
        except ValueError:
            self._TxDd = hex(int(value, 16))

    def _set_rxdd_with_str(self, value):
        try:
            self._RxDd = int(value)
        except ValueError:
            self._RxDd = hex(int(value, 16))

    def _set_txrouterlsa_with_str(self, value):
        try:
            self._TxRouterLsa = int(value)
        except ValueError:
            self._TxRouterLsa = hex(int(value, 16))

    def _set_rxrouterlsa_with_str(self, value):
        try:
            self._RxRouterLsa = int(value)
        except ValueError:
            self._RxRouterLsa = hex(int(value, 16))

    def _set_txnetworklsa_with_str(self, value):
        try:
            self._TxNetworkLsa = int(value)
        except ValueError:
            self._TxNetworkLsa = hex(int(value, 16))

    def _set_rxnetworklsa_with_str(self, value):
        try:
            self._RxNetworkLsa = int(value)
        except ValueError:
            self._RxNetworkLsa = hex(int(value, 16))

    def _set_txsummarylsa_with_str(self, value):
        try:
            self._TxSummaryLsa = int(value)
        except ValueError:
            self._TxSummaryLsa = hex(int(value, 16))

    def _set_rxsummarylsa_with_str(self, value):
        try:
            self._RxSummaryLsa = int(value)
        except ValueError:
            self._RxSummaryLsa = hex(int(value, 16))

    def _set_txasbrsummarylsa_with_str(self, value):
        try:
            self._TxAsbrSummaryLsa = int(value)
        except ValueError:
            self._TxAsbrSummaryLsa = hex(int(value, 16))

    def _set_rxasbrsummarylsa_with_str(self, value):
        try:
            self._RxAsbrSummaryLsa = int(value)
        except ValueError:
            self._RxAsbrSummaryLsa = hex(int(value, 16))

    def _set_txasexternallsa_with_str(self, value):
        try:
            self._TxAsExternalLsa = int(value)
        except ValueError:
            self._TxAsExternalLsa = hex(int(value, 16))

    def _set_rxasexternallsa_with_str(self, value):
        try:
            self._RxAsExternalLsa = int(value)
        except ValueError:
            self._RxAsExternalLsa = hex(int(value, 16))

    def _set_txnssalsa_with_str(self, value):
        try:
            self._TxNssaLsa = int(value)
        except ValueError:
            self._TxNssaLsa = hex(int(value, 16))

    def _set_rxnssalsa_with_str(self, value):
        try:
            self._RxNssaLsa = int(value)
        except ValueError:
            self._RxNssaLsa = hex(int(value, 16))

    def _set_txtelsa_with_str(self, value):
        try:
            self._TxTeLsa = int(value)
        except ValueError:
            self._TxTeLsa = hex(int(value, 16))

    def _set_rxtelsa_with_str(self, value):
        try:
            self._RxTeLsa = int(value)
        except ValueError:
            self._RxTeLsa = hex(int(value, 16))

    def _set_txrequest_with_str(self, value):
        try:
            self._TxRequest = int(value)
        except ValueError:
            self._TxRequest = hex(int(value, 16))

    def _set_rxrequest_with_str(self, value):
        try:
            self._RxRequest = int(value)
        except ValueError:
            self._RxRequest = hex(int(value, 16))

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

    def _set_txack_with_str(self, value):
        try:
            self._TxAck = int(value)
        except ValueError:
            self._TxAck = hex(int(value, 16))

    def _set_rxack_with_str(self, value):
        try:
            self._RxAck = int(value)
        except ValueError:
            self._RxAck = hex(int(value, 16))

