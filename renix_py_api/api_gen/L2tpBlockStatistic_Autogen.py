"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class L2tpBlockStatistic(Result):
    def __init__(self, **kwargs):
        self._L2tpBlockId = ''  # L2TP Block Name, not editable
        self._L2tpBlockState = 'Idle'  # L2TP Block State, not editable
        self._TunnelCount = 0  # Tunnel Count, not editable
        self._SessionCount = 0  # Session Count, not editable
        self._TunnelUp = 0  # Tunnel Up, not editable
        self._TunnelDown = 0  # Tunnel Down, not editable
        self._SessionUp = 0  # Session Up, not editable
        self._SessionDown = 0  # Session Down, not editable
        self._TunnelSetupRate = 0.0  # Tunnel Setup Rate(tunnels/sec), not editable
        self._SessionSetupRate = 0.0  # Session Setup Rate(sessions/sec), not editable
        self._AverageTunnelSetupTime = 0.0  # Average Tunnel Setup Time(ms), not editable
        self._MaxTunnelSetupTime = 0  # Maximum Tunnel Setup Time(ms), not editable
        self._MinTunnelSetupTime = 0  # Minimum Tunnel Setup Time(ms), not editable
        self._AverageSessionSetupTime = 0.0  # Average Session Setup Time(ms), not editable
        self._MaxSessionSetupTime = 0  # Maximum Session Setup Time(ms), not editable
        self._MinSessionSetupTime = 0  # Minimum Session Setup Time(ms), not editable
        self._TxPackets = 0  # Tx Packets, not editable
        self._RxPackets = 0  # Rx Packets, not editable
        self._TxSccrq = 0  # Tx SCCRQ, not editable
        self._RxSccrq = 0  # Rx SCCRQ, not editable
        self._TxSccrp = 0  # Tx SCCRP, not editable
        self._RxSccrp = 0  # Rx SCCRP, not editable
        self._TxScccn = 0  # Tx SCCCN, not editable
        self._RxScccn = 0  # Rx SCCCN, not editable
        self._TxIcrq = 0  # Tx ICRQ, not editable
        self._RxIcrq = 0  # Rx ICRQ, not editable
        self._TxIcrp = 0  # Tx ICRP, not editable
        self._RxIcrp = 0  # Rx ICRP, not editable
        self._TxIccn = 0  # Tx ICCN, not editable
        self._RxIccn = 0  # Rx ICCN, not editable
        self._TxSli = 0  # Tx SLI, not editable
        self._RxSli = 0  # Rx SLI, not editable
        self._TxStopCcn = 0  # Tx StopCCN, not editable
        self._RxStopCcn = 0  # Rx StopCCN, not editable
        self._TxWen = 0  # Tx WEN, not editable
        self._RxWen = 0  # Rx WEN, not editable
        self._TxHello = 0  # Tx Hello, not editable
        self._RxHello = 0  # Rx Hello, not editable
        self._TxCdn = 0  # Tx CDN, not editable
        self._RxCdn = 0  # Rx CDN, not editable
        self._TxZlb = 0  # Tx ZLB, not editable
        self._RxZlb = 0  # Rx ZLB, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(L2tpBlockStatistic, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def L2tpBlockId(self):
        """
        get the value of property _L2tpBlockId
        """
        if self.force_auto_sync:
            self.get('L2tpBlockId')
        return self._L2tpBlockId

    @property
    def L2tpBlockState(self):
        """
        get the value of property _L2tpBlockState
        """
        if self.force_auto_sync:
            self.get('L2tpBlockState')
        return self._L2tpBlockState

    @property
    def TunnelCount(self):
        """
        get the value of property _TunnelCount
        """
        if self.force_auto_sync:
            self.get('TunnelCount')
        return self._TunnelCount

    @property
    def SessionCount(self):
        """
        get the value of property _SessionCount
        """
        if self.force_auto_sync:
            self.get('SessionCount')
        return self._SessionCount

    @property
    def TunnelUp(self):
        """
        get the value of property _TunnelUp
        """
        if self.force_auto_sync:
            self.get('TunnelUp')
        return self._TunnelUp

    @property
    def TunnelDown(self):
        """
        get the value of property _TunnelDown
        """
        if self.force_auto_sync:
            self.get('TunnelDown')
        return self._TunnelDown

    @property
    def SessionUp(self):
        """
        get the value of property _SessionUp
        """
        if self.force_auto_sync:
            self.get('SessionUp')
        return self._SessionUp

    @property
    def SessionDown(self):
        """
        get the value of property _SessionDown
        """
        if self.force_auto_sync:
            self.get('SessionDown')
        return self._SessionDown

    @property
    def TunnelSetupRate(self):
        """
        get the value of property _TunnelSetupRate
        """
        if self.force_auto_sync:
            self.get('TunnelSetupRate')
        return self._TunnelSetupRate

    @property
    def SessionSetupRate(self):
        """
        get the value of property _SessionSetupRate
        """
        if self.force_auto_sync:
            self.get('SessionSetupRate')
        return self._SessionSetupRate

    @property
    def AverageTunnelSetupTime(self):
        """
        get the value of property _AverageTunnelSetupTime
        """
        if self.force_auto_sync:
            self.get('AverageTunnelSetupTime')
        return self._AverageTunnelSetupTime

    @property
    def MaxTunnelSetupTime(self):
        """
        get the value of property _MaxTunnelSetupTime
        """
        if self.force_auto_sync:
            self.get('MaxTunnelSetupTime')
        return self._MaxTunnelSetupTime

    @property
    def MinTunnelSetupTime(self):
        """
        get the value of property _MinTunnelSetupTime
        """
        if self.force_auto_sync:
            self.get('MinTunnelSetupTime')
        return self._MinTunnelSetupTime

    @property
    def AverageSessionSetupTime(self):
        """
        get the value of property _AverageSessionSetupTime
        """
        if self.force_auto_sync:
            self.get('AverageSessionSetupTime')
        return self._AverageSessionSetupTime

    @property
    def MaxSessionSetupTime(self):
        """
        get the value of property _MaxSessionSetupTime
        """
        if self.force_auto_sync:
            self.get('MaxSessionSetupTime')
        return self._MaxSessionSetupTime

    @property
    def MinSessionSetupTime(self):
        """
        get the value of property _MinSessionSetupTime
        """
        if self.force_auto_sync:
            self.get('MinSessionSetupTime')
        return self._MinSessionSetupTime

    @property
    def TxPackets(self):
        """
        get the value of property _TxPackets
        """
        if self.force_auto_sync:
            self.get('TxPackets')
        return self._TxPackets

    @property
    def RxPackets(self):
        """
        get the value of property _RxPackets
        """
        if self.force_auto_sync:
            self.get('RxPackets')
        return self._RxPackets

    @property
    def TxSccrq(self):
        """
        get the value of property _TxSccrq
        """
        if self.force_auto_sync:
            self.get('TxSccrq')
        return self._TxSccrq

    @property
    def RxSccrq(self):
        """
        get the value of property _RxSccrq
        """
        if self.force_auto_sync:
            self.get('RxSccrq')
        return self._RxSccrq

    @property
    def TxSccrp(self):
        """
        get the value of property _TxSccrp
        """
        if self.force_auto_sync:
            self.get('TxSccrp')
        return self._TxSccrp

    @property
    def RxSccrp(self):
        """
        get the value of property _RxSccrp
        """
        if self.force_auto_sync:
            self.get('RxSccrp')
        return self._RxSccrp

    @property
    def TxScccn(self):
        """
        get the value of property _TxScccn
        """
        if self.force_auto_sync:
            self.get('TxScccn')
        return self._TxScccn

    @property
    def RxScccn(self):
        """
        get the value of property _RxScccn
        """
        if self.force_auto_sync:
            self.get('RxScccn')
        return self._RxScccn

    @property
    def TxIcrq(self):
        """
        get the value of property _TxIcrq
        """
        if self.force_auto_sync:
            self.get('TxIcrq')
        return self._TxIcrq

    @property
    def RxIcrq(self):
        """
        get the value of property _RxIcrq
        """
        if self.force_auto_sync:
            self.get('RxIcrq')
        return self._RxIcrq

    @property
    def TxIcrp(self):
        """
        get the value of property _TxIcrp
        """
        if self.force_auto_sync:
            self.get('TxIcrp')
        return self._TxIcrp

    @property
    def RxIcrp(self):
        """
        get the value of property _RxIcrp
        """
        if self.force_auto_sync:
            self.get('RxIcrp')
        return self._RxIcrp

    @property
    def TxIccn(self):
        """
        get the value of property _TxIccn
        """
        if self.force_auto_sync:
            self.get('TxIccn')
        return self._TxIccn

    @property
    def RxIccn(self):
        """
        get the value of property _RxIccn
        """
        if self.force_auto_sync:
            self.get('RxIccn')
        return self._RxIccn

    @property
    def TxSli(self):
        """
        get the value of property _TxSli
        """
        if self.force_auto_sync:
            self.get('TxSli')
        return self._TxSli

    @property
    def RxSli(self):
        """
        get the value of property _RxSli
        """
        if self.force_auto_sync:
            self.get('RxSli')
        return self._RxSli

    @property
    def TxStopCcn(self):
        """
        get the value of property _TxStopCcn
        """
        if self.force_auto_sync:
            self.get('TxStopCcn')
        return self._TxStopCcn

    @property
    def RxStopCcn(self):
        """
        get the value of property _RxStopCcn
        """
        if self.force_auto_sync:
            self.get('RxStopCcn')
        return self._RxStopCcn

    @property
    def TxWen(self):
        """
        get the value of property _TxWen
        """
        if self.force_auto_sync:
            self.get('TxWen')
        return self._TxWen

    @property
    def RxWen(self):
        """
        get the value of property _RxWen
        """
        if self.force_auto_sync:
            self.get('RxWen')
        return self._RxWen

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
    def TxCdn(self):
        """
        get the value of property _TxCdn
        """
        if self.force_auto_sync:
            self.get('TxCdn')
        return self._TxCdn

    @property
    def RxCdn(self):
        """
        get the value of property _RxCdn
        """
        if self.force_auto_sync:
            self.get('RxCdn')
        return self._RxCdn

    @property
    def TxZlb(self):
        """
        get the value of property _TxZlb
        """
        if self.force_auto_sync:
            self.get('TxZlb')
        return self._TxZlb

    @property
    def RxZlb(self):
        """
        get the value of property _RxZlb
        """
        if self.force_auto_sync:
            self.get('RxZlb')
        return self._RxZlb

    def _set_l2tpblockid_with_str(self, value):
        self._L2tpBlockId = value

    def _set_l2tpblockstate_with_str(self, value):
        self._L2tpBlockState = value

    def _set_tunnelcount_with_str(self, value):
        try:
            self._TunnelCount = int(value)
        except ValueError:
            self._TunnelCount = hex(int(value, 16))

    def _set_sessioncount_with_str(self, value):
        try:
            self._SessionCount = int(value)
        except ValueError:
            self._SessionCount = hex(int(value, 16))

    def _set_tunnelup_with_str(self, value):
        try:
            self._TunnelUp = int(value)
        except ValueError:
            self._TunnelUp = hex(int(value, 16))

    def _set_tunneldown_with_str(self, value):
        try:
            self._TunnelDown = int(value)
        except ValueError:
            self._TunnelDown = hex(int(value, 16))

    def _set_sessionup_with_str(self, value):
        try:
            self._SessionUp = int(value)
        except ValueError:
            self._SessionUp = hex(int(value, 16))

    def _set_sessiondown_with_str(self, value):
        try:
            self._SessionDown = int(value)
        except ValueError:
            self._SessionDown = hex(int(value, 16))

    def _set_tunnelsetuprate_with_str(self, value):
        self._TunnelSetupRate = float(value)

    def _set_sessionsetuprate_with_str(self, value):
        self._SessionSetupRate = float(value)

    def _set_averagetunnelsetuptime_with_str(self, value):
        self._AverageTunnelSetupTime = float(value)

    def _set_maxtunnelsetuptime_with_str(self, value):
        try:
            self._MaxTunnelSetupTime = int(value)
        except ValueError:
            self._MaxTunnelSetupTime = hex(int(value, 16))

    def _set_mintunnelsetuptime_with_str(self, value):
        try:
            self._MinTunnelSetupTime = int(value)
        except ValueError:
            self._MinTunnelSetupTime = hex(int(value, 16))

    def _set_averagesessionsetuptime_with_str(self, value):
        self._AverageSessionSetupTime = float(value)

    def _set_maxsessionsetuptime_with_str(self, value):
        try:
            self._MaxSessionSetupTime = int(value)
        except ValueError:
            self._MaxSessionSetupTime = hex(int(value, 16))

    def _set_minsessionsetuptime_with_str(self, value):
        try:
            self._MinSessionSetupTime = int(value)
        except ValueError:
            self._MinSessionSetupTime = hex(int(value, 16))

    def _set_txpackets_with_str(self, value):
        try:
            self._TxPackets = int(value)
        except ValueError:
            self._TxPackets = hex(int(value, 16))

    def _set_rxpackets_with_str(self, value):
        try:
            self._RxPackets = int(value)
        except ValueError:
            self._RxPackets = hex(int(value, 16))

    def _set_txsccrq_with_str(self, value):
        try:
            self._TxSccrq = int(value)
        except ValueError:
            self._TxSccrq = hex(int(value, 16))

    def _set_rxsccrq_with_str(self, value):
        try:
            self._RxSccrq = int(value)
        except ValueError:
            self._RxSccrq = hex(int(value, 16))

    def _set_txsccrp_with_str(self, value):
        try:
            self._TxSccrp = int(value)
        except ValueError:
            self._TxSccrp = hex(int(value, 16))

    def _set_rxsccrp_with_str(self, value):
        try:
            self._RxSccrp = int(value)
        except ValueError:
            self._RxSccrp = hex(int(value, 16))

    def _set_txscccn_with_str(self, value):
        try:
            self._TxScccn = int(value)
        except ValueError:
            self._TxScccn = hex(int(value, 16))

    def _set_rxscccn_with_str(self, value):
        try:
            self._RxScccn = int(value)
        except ValueError:
            self._RxScccn = hex(int(value, 16))

    def _set_txicrq_with_str(self, value):
        try:
            self._TxIcrq = int(value)
        except ValueError:
            self._TxIcrq = hex(int(value, 16))

    def _set_rxicrq_with_str(self, value):
        try:
            self._RxIcrq = int(value)
        except ValueError:
            self._RxIcrq = hex(int(value, 16))

    def _set_txicrp_with_str(self, value):
        try:
            self._TxIcrp = int(value)
        except ValueError:
            self._TxIcrp = hex(int(value, 16))

    def _set_rxicrp_with_str(self, value):
        try:
            self._RxIcrp = int(value)
        except ValueError:
            self._RxIcrp = hex(int(value, 16))

    def _set_txiccn_with_str(self, value):
        try:
            self._TxIccn = int(value)
        except ValueError:
            self._TxIccn = hex(int(value, 16))

    def _set_rxiccn_with_str(self, value):
        try:
            self._RxIccn = int(value)
        except ValueError:
            self._RxIccn = hex(int(value, 16))

    def _set_txsli_with_str(self, value):
        try:
            self._TxSli = int(value)
        except ValueError:
            self._TxSli = hex(int(value, 16))

    def _set_rxsli_with_str(self, value):
        try:
            self._RxSli = int(value)
        except ValueError:
            self._RxSli = hex(int(value, 16))

    def _set_txstopccn_with_str(self, value):
        try:
            self._TxStopCcn = int(value)
        except ValueError:
            self._TxStopCcn = hex(int(value, 16))

    def _set_rxstopccn_with_str(self, value):
        try:
            self._RxStopCcn = int(value)
        except ValueError:
            self._RxStopCcn = hex(int(value, 16))

    def _set_txwen_with_str(self, value):
        try:
            self._TxWen = int(value)
        except ValueError:
            self._TxWen = hex(int(value, 16))

    def _set_rxwen_with_str(self, value):
        try:
            self._RxWen = int(value)
        except ValueError:
            self._RxWen = hex(int(value, 16))

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

    def _set_txcdn_with_str(self, value):
        try:
            self._TxCdn = int(value)
        except ValueError:
            self._TxCdn = hex(int(value, 16))

    def _set_rxcdn_with_str(self, value):
        try:
            self._RxCdn = int(value)
        except ValueError:
            self._RxCdn = hex(int(value, 16))

    def _set_txzlb_with_str(self, value):
        try:
            self._TxZlb = int(value)
        except ValueError:
            self._TxZlb = hex(int(value, 16))

    def _set_rxzlb_with_str(self, value):
        try:
            self._RxZlb = int(value)
        except ValueError:
            self._RxZlb = hex(int(value, 16))

