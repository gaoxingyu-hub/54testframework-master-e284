"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class PimSessionStats(Result):
    def __init__(self, **kwargs):
        self._SessionID = ''  # Session Name, not editable
        self._NeighborNum = 0  # Neighbor Num, not editable
        self._TxHello = 0  # Tx Hello, not editable
        self._RxHello = 0  # Rx Hello, not editable
        self._TxJoin = 0  # Tx Join/Prune, not editable
        self._RxJoin = 0  # Rx Join/Prune, not editable
        self._TxAnyG = 0  # Tx AnyG, not editable
        self._RxAnyG = 0  # Rx AnyG, not editable
        self._TxSG = 0  # Tx SG, not editable
        self._RxSG = 0  # Rx SG, not editable
        self._TxRP = 0  # Tx RP, not editable
        self._RxRP = 0  # Rx RP, not editable
        self._TxRpt = 0  # Tx RPT, not editable
        self._RxRpt = 0  # Rx RPT, not editable
        self._TxBsr = 0  # Tx BSR, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(PimSessionStats, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def SessionID(self):
        """
        get the value of property _SessionID
        """
        if self.force_auto_sync:
            self.get('SessionID')
        return self._SessionID

    @property
    def NeighborNum(self):
        """
        get the value of property _NeighborNum
        """
        if self.force_auto_sync:
            self.get('NeighborNum')
        return self._NeighborNum

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
    def TxJoin(self):
        """
        get the value of property _TxJoin
        """
        if self.force_auto_sync:
            self.get('TxJoin')
        return self._TxJoin

    @property
    def RxJoin(self):
        """
        get the value of property _RxJoin
        """
        if self.force_auto_sync:
            self.get('RxJoin')
        return self._RxJoin

    @property
    def TxAnyG(self):
        """
        get the value of property _TxAnyG
        """
        if self.force_auto_sync:
            self.get('TxAnyG')
        return self._TxAnyG

    @property
    def RxAnyG(self):
        """
        get the value of property _RxAnyG
        """
        if self.force_auto_sync:
            self.get('RxAnyG')
        return self._RxAnyG

    @property
    def TxSG(self):
        """
        get the value of property _TxSG
        """
        if self.force_auto_sync:
            self.get('TxSG')
        return self._TxSG

    @property
    def RxSG(self):
        """
        get the value of property _RxSG
        """
        if self.force_auto_sync:
            self.get('RxSG')
        return self._RxSG

    @property
    def TxRP(self):
        """
        get the value of property _TxRP
        """
        if self.force_auto_sync:
            self.get('TxRP')
        return self._TxRP

    @property
    def RxRP(self):
        """
        get the value of property _RxRP
        """
        if self.force_auto_sync:
            self.get('RxRP')
        return self._RxRP

    @property
    def TxRpt(self):
        """
        get the value of property _TxRpt
        """
        if self.force_auto_sync:
            self.get('TxRpt')
        return self._TxRpt

    @property
    def RxRpt(self):
        """
        get the value of property _RxRpt
        """
        if self.force_auto_sync:
            self.get('RxRpt')
        return self._RxRpt

    @property
    def TxBsr(self):
        """
        get the value of property _TxBsr
        """
        if self.force_auto_sync:
            self.get('TxBsr')
        return self._TxBsr

    def _set_sessionid_with_str(self, value):
        self._SessionID = value

    def _set_neighbornum_with_str(self, value):
        try:
            self._NeighborNum = int(value)
        except ValueError:
            self._NeighborNum = hex(int(value, 16))

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

    def _set_txjoin_with_str(self, value):
        try:
            self._TxJoin = int(value)
        except ValueError:
            self._TxJoin = hex(int(value, 16))

    def _set_rxjoin_with_str(self, value):
        try:
            self._RxJoin = int(value)
        except ValueError:
            self._RxJoin = hex(int(value, 16))

    def _set_txanyg_with_str(self, value):
        try:
            self._TxAnyG = int(value)
        except ValueError:
            self._TxAnyG = hex(int(value, 16))

    def _set_rxanyg_with_str(self, value):
        try:
            self._RxAnyG = int(value)
        except ValueError:
            self._RxAnyG = hex(int(value, 16))

    def _set_txsg_with_str(self, value):
        try:
            self._TxSG = int(value)
        except ValueError:
            self._TxSG = hex(int(value, 16))

    def _set_rxsg_with_str(self, value):
        try:
            self._RxSG = int(value)
        except ValueError:
            self._RxSG = hex(int(value, 16))

    def _set_txrp_with_str(self, value):
        try:
            self._TxRP = int(value)
        except ValueError:
            self._TxRP = hex(int(value, 16))

    def _set_rxrp_with_str(self, value):
        try:
            self._RxRP = int(value)
        except ValueError:
            self._RxRP = hex(int(value, 16))

    def _set_txrpt_with_str(self, value):
        try:
            self._TxRpt = int(value)
        except ValueError:
            self._TxRpt = hex(int(value, 16))

    def _set_rxrpt_with_str(self, value):
        try:
            self._RxRpt = int(value)
        except ValueError:
            self._RxRpt = hex(int(value, 16))

    def _set_txbsr_with_str(self, value):
        try:
            self._TxBsr = int(value)
        except ValueError:
            self._TxBsr = hex(int(value, 16))

