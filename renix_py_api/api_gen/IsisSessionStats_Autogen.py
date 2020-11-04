"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class IsisSessionStats(Result):
    def __init__(self, **kwargs):
        self._SessionHandle = ''  # IS-IS Session Name, not editable
        self._RouterState = 'Init'  # Router State, not editable
        self._P2pThreeWayState = 'Not Started'  # P2P Adjacency State, not editable
        self._L1BroadcastState = 'Not Started'  # Broadcast L1 State, not editable
        self._L2BroadcastState = 'Not Started'  # Broadcast L2 State, not editable
        self._TxP2pHello = 0  # Tx P2P Hello, not editable
        self._RxP2pHello = 0  # Rx P2P Hello, not editable
        self._TxLanL1Hello = 0  # Tx LAN L1 Hello, not editable
        self._RxLanL1Hello = 0  # Rx LAN L1 Hello, not editable
        self._TxLanL2Hello = 0  # Tx LAN L2 Hello, not editable
        self._RxLanL2Hello = 0  # Rx LAN L2 Hello, not editable
        self._TxL1Lsp = 0  # Tx L1 LSP, not editable
        self._RxL1Lsp = 0  # Rx L1 LSP, not editable
        self._TxL2Lsp = 0  # Tx L2 LSP, not editable
        self._RxL2Lsp = 0  # Rx L2 LSP, not editable
        self._TxL1Csnp = 0  # Tx L1 CSNP, not editable
        self._RxL1Csnp = 0  # Rx L1 CSNP, not editable
        self._TxL2Csnp = 0  # Tx L2 CSNP, not editable
        self._RxL2Csnp = 0  # Rx L2 CSNP, not editable
        self._TxL1Psnp = 0  # Tx L1 PSNP, not editable
        self._RxL1Psnp = 0  # Rx L1 PSNP, not editable
        self._TxL2Psnp = 0  # Tx L2 PSNP, not editable
        self._RxL2Psnp = 0  # Rx L2 PSNP, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(IsisSessionStats, self).__init__(**properties)

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
    def P2pThreeWayState(self):
        """
        get the value of property _P2pThreeWayState
        """
        if self.force_auto_sync:
            self.get('P2pThreeWayState')
        return self._P2pThreeWayState

    @property
    def L1BroadcastState(self):
        """
        get the value of property _L1BroadcastState
        """
        if self.force_auto_sync:
            self.get('L1BroadcastState')
        return self._L1BroadcastState

    @property
    def L2BroadcastState(self):
        """
        get the value of property _L2BroadcastState
        """
        if self.force_auto_sync:
            self.get('L2BroadcastState')
        return self._L2BroadcastState

    @property
    def TxP2pHello(self):
        """
        get the value of property _TxP2pHello
        """
        if self.force_auto_sync:
            self.get('TxP2pHello')
        return self._TxP2pHello

    @property
    def RxP2pHello(self):
        """
        get the value of property _RxP2pHello
        """
        if self.force_auto_sync:
            self.get('RxP2pHello')
        return self._RxP2pHello

    @property
    def TxLanL1Hello(self):
        """
        get the value of property _TxLanL1Hello
        """
        if self.force_auto_sync:
            self.get('TxLanL1Hello')
        return self._TxLanL1Hello

    @property
    def RxLanL1Hello(self):
        """
        get the value of property _RxLanL1Hello
        """
        if self.force_auto_sync:
            self.get('RxLanL1Hello')
        return self._RxLanL1Hello

    @property
    def TxLanL2Hello(self):
        """
        get the value of property _TxLanL2Hello
        """
        if self.force_auto_sync:
            self.get('TxLanL2Hello')
        return self._TxLanL2Hello

    @property
    def RxLanL2Hello(self):
        """
        get the value of property _RxLanL2Hello
        """
        if self.force_auto_sync:
            self.get('RxLanL2Hello')
        return self._RxLanL2Hello

    @property
    def TxL1Lsp(self):
        """
        get the value of property _TxL1Lsp
        """
        if self.force_auto_sync:
            self.get('TxL1Lsp')
        return self._TxL1Lsp

    @property
    def RxL1Lsp(self):
        """
        get the value of property _RxL1Lsp
        """
        if self.force_auto_sync:
            self.get('RxL1Lsp')
        return self._RxL1Lsp

    @property
    def TxL2Lsp(self):
        """
        get the value of property _TxL2Lsp
        """
        if self.force_auto_sync:
            self.get('TxL2Lsp')
        return self._TxL2Lsp

    @property
    def RxL2Lsp(self):
        """
        get the value of property _RxL2Lsp
        """
        if self.force_auto_sync:
            self.get('RxL2Lsp')
        return self._RxL2Lsp

    @property
    def TxL1Csnp(self):
        """
        get the value of property _TxL1Csnp
        """
        if self.force_auto_sync:
            self.get('TxL1Csnp')
        return self._TxL1Csnp

    @property
    def RxL1Csnp(self):
        """
        get the value of property _RxL1Csnp
        """
        if self.force_auto_sync:
            self.get('RxL1Csnp')
        return self._RxL1Csnp

    @property
    def TxL2Csnp(self):
        """
        get the value of property _TxL2Csnp
        """
        if self.force_auto_sync:
            self.get('TxL2Csnp')
        return self._TxL2Csnp

    @property
    def RxL2Csnp(self):
        """
        get the value of property _RxL2Csnp
        """
        if self.force_auto_sync:
            self.get('RxL2Csnp')
        return self._RxL2Csnp

    @property
    def TxL1Psnp(self):
        """
        get the value of property _TxL1Psnp
        """
        if self.force_auto_sync:
            self.get('TxL1Psnp')
        return self._TxL1Psnp

    @property
    def RxL1Psnp(self):
        """
        get the value of property _RxL1Psnp
        """
        if self.force_auto_sync:
            self.get('RxL1Psnp')
        return self._RxL1Psnp

    @property
    def TxL2Psnp(self):
        """
        get the value of property _TxL2Psnp
        """
        if self.force_auto_sync:
            self.get('TxL2Psnp')
        return self._TxL2Psnp

    @property
    def RxL2Psnp(self):
        """
        get the value of property _RxL2Psnp
        """
        if self.force_auto_sync:
            self.get('RxL2Psnp')
        return self._RxL2Psnp

    def _set_sessionhandle_with_str(self, value):
        self._SessionHandle = value

    def _set_routerstate_with_str(self, value):
        self._RouterState = value

    def _set_p2pthreewaystate_with_str(self, value):
        self._P2pThreeWayState = value

    def _set_l1broadcaststate_with_str(self, value):
        self._L1BroadcastState = value

    def _set_l2broadcaststate_with_str(self, value):
        self._L2BroadcastState = value

    def _set_txp2phello_with_str(self, value):
        try:
            self._TxP2pHello = int(value)
        except ValueError:
            self._TxP2pHello = hex(int(value, 16))

    def _set_rxp2phello_with_str(self, value):
        try:
            self._RxP2pHello = int(value)
        except ValueError:
            self._RxP2pHello = hex(int(value, 16))

    def _set_txlanl1hello_with_str(self, value):
        try:
            self._TxLanL1Hello = int(value)
        except ValueError:
            self._TxLanL1Hello = hex(int(value, 16))

    def _set_rxlanl1hello_with_str(self, value):
        try:
            self._RxLanL1Hello = int(value)
        except ValueError:
            self._RxLanL1Hello = hex(int(value, 16))

    def _set_txlanl2hello_with_str(self, value):
        try:
            self._TxLanL2Hello = int(value)
        except ValueError:
            self._TxLanL2Hello = hex(int(value, 16))

    def _set_rxlanl2hello_with_str(self, value):
        try:
            self._RxLanL2Hello = int(value)
        except ValueError:
            self._RxLanL2Hello = hex(int(value, 16))

    def _set_txl1lsp_with_str(self, value):
        try:
            self._TxL1Lsp = int(value)
        except ValueError:
            self._TxL1Lsp = hex(int(value, 16))

    def _set_rxl1lsp_with_str(self, value):
        try:
            self._RxL1Lsp = int(value)
        except ValueError:
            self._RxL1Lsp = hex(int(value, 16))

    def _set_txl2lsp_with_str(self, value):
        try:
            self._TxL2Lsp = int(value)
        except ValueError:
            self._TxL2Lsp = hex(int(value, 16))

    def _set_rxl2lsp_with_str(self, value):
        try:
            self._RxL2Lsp = int(value)
        except ValueError:
            self._RxL2Lsp = hex(int(value, 16))

    def _set_txl1csnp_with_str(self, value):
        try:
            self._TxL1Csnp = int(value)
        except ValueError:
            self._TxL1Csnp = hex(int(value, 16))

    def _set_rxl1csnp_with_str(self, value):
        try:
            self._RxL1Csnp = int(value)
        except ValueError:
            self._RxL1Csnp = hex(int(value, 16))

    def _set_txl2csnp_with_str(self, value):
        try:
            self._TxL2Csnp = int(value)
        except ValueError:
            self._TxL2Csnp = hex(int(value, 16))

    def _set_rxl2csnp_with_str(self, value):
        try:
            self._RxL2Csnp = int(value)
        except ValueError:
            self._RxL2Csnp = hex(int(value, 16))

    def _set_txl1psnp_with_str(self, value):
        try:
            self._TxL1Psnp = int(value)
        except ValueError:
            self._TxL1Psnp = hex(int(value, 16))

    def _set_rxl1psnp_with_str(self, value):
        try:
            self._RxL1Psnp = int(value)
        except ValueError:
            self._RxL1Psnp = hex(int(value, 16))

    def _set_txl2psnp_with_str(self, value):
        try:
            self._TxL2Psnp = int(value)
        except ValueError:
            self._TxL2Psnp = hex(int(value, 16))

    def _set_rxl2psnp_with_str(self, value):
        try:
            self._RxL2Psnp = int(value)
        except ValueError:
            self._RxL2Psnp = hex(int(value, 16))

