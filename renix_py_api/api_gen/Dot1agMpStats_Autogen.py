"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Dot1agMpStats(Result):
    def __init__(self, **kwargs):
        self._MepHandle = ''  # MEP Name, not editable
        self._SessionHandle = ''  # 802.1ag Session Name, not editable
        self._MepId = 0  # MEP ID, not editable
        self._RemoteMeps = 0  # Remote MEPs, not editable
        self._CcmTimeout = 0  # CCM Timeouts, not editable
        self._CcmUnexpectMaid = 0  # CCMs from Unexpected MAID , not editable
        self._CcmUnexpectMdLevel = 0  # CCMs from Unexpected MD Level, not editable
        self._TxCcm300Hz = 0  # Tx 3.33 ms CCMs, not editable
        self._TxCcm10ms = 0  # Tx 10 ms CCMs, not editable
        self._TxCcm100ms = 0  # Tx 100 ms CCMs, not editable
        self._TxCcm1s = 0  # Tx 1 sec CCMs, not editable
        self._TxCcm10s = 0  # Tx 10 secs CCMs, not editable
        self._TxCcm1min = 0  # Tx 1 min CCMs, not editable
        self._TxCcm10min = 0  # Tx 10 mins CCMs, not editable
        self._RxCcm = 0  # Rx CCMs, not editable
        self._LastTxCcmSeqNum = 0  # Last Tx CCM Sequence Number, not editable
        self._LbTimeout = 0  # Timeout LBMs, not editable
        self._LbTransIdMismatch = 0  # LB Transaction ID Mismatches, not editable
        self._TxLbm = 0  # Tx LBMs, not editable
        self._RxLbm = 0  # Rx LBMs, not editable
        self._TxLbr = 0  # Tx LBRs, not editable
        self._RxLbr = 0  # Rx LBRs, not editable
        self._TxLtm = 0  # Tx LTMs, not editable
        self._RxLtm = 0  # Rx LTMs, not editable
        self._TxLtr = 0  # Tx LTRs, not editable
        self._RxLtr = 0  # Rx LTRs, not editable
        self._LtTimeout = 0  # Timeout LTMs, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Dot1agMpStats, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def MepHandle(self):
        """
        get the value of property _MepHandle
        """
        if self.force_auto_sync:
            self.get('MepHandle')
        return self._MepHandle

    @property
    def SessionHandle(self):
        """
        get the value of property _SessionHandle
        """
        if self.force_auto_sync:
            self.get('SessionHandle')
        return self._SessionHandle

    @property
    def MepId(self):
        """
        get the value of property _MepId
        """
        if self.force_auto_sync:
            self.get('MepId')
        return self._MepId

    @property
    def RemoteMeps(self):
        """
        get the value of property _RemoteMeps
        """
        if self.force_auto_sync:
            self.get('RemoteMeps')
        return self._RemoteMeps

    @property
    def CcmTimeout(self):
        """
        get the value of property _CcmTimeout
        """
        if self.force_auto_sync:
            self.get('CcmTimeout')
        return self._CcmTimeout

    @property
    def CcmUnexpectMaid(self):
        """
        get the value of property _CcmUnexpectMaid
        """
        if self.force_auto_sync:
            self.get('CcmUnexpectMaid')
        return self._CcmUnexpectMaid

    @property
    def CcmUnexpectMdLevel(self):
        """
        get the value of property _CcmUnexpectMdLevel
        """
        if self.force_auto_sync:
            self.get('CcmUnexpectMdLevel')
        return self._CcmUnexpectMdLevel

    @property
    def TxCcm300Hz(self):
        """
        get the value of property _TxCcm300Hz
        """
        if self.force_auto_sync:
            self.get('TxCcm300Hz')
        return self._TxCcm300Hz

    @property
    def TxCcm10ms(self):
        """
        get the value of property _TxCcm10ms
        """
        if self.force_auto_sync:
            self.get('TxCcm10ms')
        return self._TxCcm10ms

    @property
    def TxCcm100ms(self):
        """
        get the value of property _TxCcm100ms
        """
        if self.force_auto_sync:
            self.get('TxCcm100ms')
        return self._TxCcm100ms

    @property
    def TxCcm1s(self):
        """
        get the value of property _TxCcm1s
        """
        if self.force_auto_sync:
            self.get('TxCcm1s')
        return self._TxCcm1s

    @property
    def TxCcm10s(self):
        """
        get the value of property _TxCcm10s
        """
        if self.force_auto_sync:
            self.get('TxCcm10s')
        return self._TxCcm10s

    @property
    def TxCcm1min(self):
        """
        get the value of property _TxCcm1min
        """
        if self.force_auto_sync:
            self.get('TxCcm1min')
        return self._TxCcm1min

    @property
    def TxCcm10min(self):
        """
        get the value of property _TxCcm10min
        """
        if self.force_auto_sync:
            self.get('TxCcm10min')
        return self._TxCcm10min

    @property
    def RxCcm(self):
        """
        get the value of property _RxCcm
        """
        if self.force_auto_sync:
            self.get('RxCcm')
        return self._RxCcm

    @property
    def LastTxCcmSeqNum(self):
        """
        get the value of property _LastTxCcmSeqNum
        """
        if self.force_auto_sync:
            self.get('LastTxCcmSeqNum')
        return self._LastTxCcmSeqNum

    @property
    def LbTimeout(self):
        """
        get the value of property _LbTimeout
        """
        if self.force_auto_sync:
            self.get('LbTimeout')
        return self._LbTimeout

    @property
    def LbTransIdMismatch(self):
        """
        get the value of property _LbTransIdMismatch
        """
        if self.force_auto_sync:
            self.get('LbTransIdMismatch')
        return self._LbTransIdMismatch

    @property
    def TxLbm(self):
        """
        get the value of property _TxLbm
        """
        if self.force_auto_sync:
            self.get('TxLbm')
        return self._TxLbm

    @property
    def RxLbm(self):
        """
        get the value of property _RxLbm
        """
        if self.force_auto_sync:
            self.get('RxLbm')
        return self._RxLbm

    @property
    def TxLbr(self):
        """
        get the value of property _TxLbr
        """
        if self.force_auto_sync:
            self.get('TxLbr')
        return self._TxLbr

    @property
    def RxLbr(self):
        """
        get the value of property _RxLbr
        """
        if self.force_auto_sync:
            self.get('RxLbr')
        return self._RxLbr

    @property
    def TxLtm(self):
        """
        get the value of property _TxLtm
        """
        if self.force_auto_sync:
            self.get('TxLtm')
        return self._TxLtm

    @property
    def RxLtm(self):
        """
        get the value of property _RxLtm
        """
        if self.force_auto_sync:
            self.get('RxLtm')
        return self._RxLtm

    @property
    def TxLtr(self):
        """
        get the value of property _TxLtr
        """
        if self.force_auto_sync:
            self.get('TxLtr')
        return self._TxLtr

    @property
    def RxLtr(self):
        """
        get the value of property _RxLtr
        """
        if self.force_auto_sync:
            self.get('RxLtr')
        return self._RxLtr

    @property
    def LtTimeout(self):
        """
        get the value of property _LtTimeout
        """
        if self.force_auto_sync:
            self.get('LtTimeout')
        return self._LtTimeout

    def _set_mephandle_with_str(self, value):
        self._MepHandle = value

    def _set_sessionhandle_with_str(self, value):
        self._SessionHandle = value

    def _set_mepid_with_str(self, value):
        try:
            self._MepId = int(value)
        except ValueError:
            self._MepId = hex(int(value, 16))

    def _set_remotemeps_with_str(self, value):
        try:
            self._RemoteMeps = int(value)
        except ValueError:
            self._RemoteMeps = hex(int(value, 16))

    def _set_ccmtimeout_with_str(self, value):
        try:
            self._CcmTimeout = int(value)
        except ValueError:
            self._CcmTimeout = hex(int(value, 16))

    def _set_ccmunexpectmaid_with_str(self, value):
        try:
            self._CcmUnexpectMaid = int(value)
        except ValueError:
            self._CcmUnexpectMaid = hex(int(value, 16))

    def _set_ccmunexpectmdlevel_with_str(self, value):
        try:
            self._CcmUnexpectMdLevel = int(value)
        except ValueError:
            self._CcmUnexpectMdLevel = hex(int(value, 16))

    def _set_txccm300hz_with_str(self, value):
        try:
            self._TxCcm300Hz = int(value)
        except ValueError:
            self._TxCcm300Hz = hex(int(value, 16))

    def _set_txccm10ms_with_str(self, value):
        try:
            self._TxCcm10ms = int(value)
        except ValueError:
            self._TxCcm10ms = hex(int(value, 16))

    def _set_txccm100ms_with_str(self, value):
        try:
            self._TxCcm100ms = int(value)
        except ValueError:
            self._TxCcm100ms = hex(int(value, 16))

    def _set_txccm1s_with_str(self, value):
        try:
            self._TxCcm1s = int(value)
        except ValueError:
            self._TxCcm1s = hex(int(value, 16))

    def _set_txccm10s_with_str(self, value):
        try:
            self._TxCcm10s = int(value)
        except ValueError:
            self._TxCcm10s = hex(int(value, 16))

    def _set_txccm1min_with_str(self, value):
        try:
            self._TxCcm1min = int(value)
        except ValueError:
            self._TxCcm1min = hex(int(value, 16))

    def _set_txccm10min_with_str(self, value):
        try:
            self._TxCcm10min = int(value)
        except ValueError:
            self._TxCcm10min = hex(int(value, 16))

    def _set_rxccm_with_str(self, value):
        try:
            self._RxCcm = int(value)
        except ValueError:
            self._RxCcm = hex(int(value, 16))

    def _set_lasttxccmseqnum_with_str(self, value):
        try:
            self._LastTxCcmSeqNum = int(value)
        except ValueError:
            self._LastTxCcmSeqNum = hex(int(value, 16))

    def _set_lbtimeout_with_str(self, value):
        try:
            self._LbTimeout = int(value)
        except ValueError:
            self._LbTimeout = hex(int(value, 16))

    def _set_lbtransidmismatch_with_str(self, value):
        try:
            self._LbTransIdMismatch = int(value)
        except ValueError:
            self._LbTransIdMismatch = hex(int(value, 16))

    def _set_txlbm_with_str(self, value):
        try:
            self._TxLbm = int(value)
        except ValueError:
            self._TxLbm = hex(int(value, 16))

    def _set_rxlbm_with_str(self, value):
        try:
            self._RxLbm = int(value)
        except ValueError:
            self._RxLbm = hex(int(value, 16))

    def _set_txlbr_with_str(self, value):
        try:
            self._TxLbr = int(value)
        except ValueError:
            self._TxLbr = hex(int(value, 16))

    def _set_rxlbr_with_str(self, value):
        try:
            self._RxLbr = int(value)
        except ValueError:
            self._RxLbr = hex(int(value, 16))

    def _set_txltm_with_str(self, value):
        try:
            self._TxLtm = int(value)
        except ValueError:
            self._TxLtm = hex(int(value, 16))

    def _set_rxltm_with_str(self, value):
        try:
            self._RxLtm = int(value)
        except ValueError:
            self._RxLtm = hex(int(value, 16))

    def _set_txltr_with_str(self, value):
        try:
            self._TxLtr = int(value)
        except ValueError:
            self._TxLtr = hex(int(value, 16))

    def _set_rxltr_with_str(self, value):
        try:
            self._RxLtr = int(value)
        except ValueError:
            self._RxLtr = hex(int(value, 16))

    def _set_lttimeout_with_str(self, value):
        try:
            self._LtTimeout = int(value)
        except ValueError:
            self._LtTimeout = hex(int(value, 16))

