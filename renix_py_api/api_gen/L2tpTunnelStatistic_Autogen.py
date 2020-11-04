"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class L2tpTunnelStatistic(Result):
    def __init__(self, **kwargs):
        self._L2tpBlockId = ''  # L2TP Block Name, not editable
        self._NodeIndexInBlock = 1  # Index in LAC/LNS Block, not editable
        self._LocalTunnelId = 0  # Local Tunnel ID, not editable
        self._RemoteTunnelId = 0  # Remote Tunnel ID, not editable
        self._TunnelState = 'Idle'  # Tunnel State, not editable
        self._UdpSourcePort = 1701  # UDP Source Port, not editable
        self._UdpDestinationPort = 1701  # UDP Destination Port, not editable
        self._LocalIpAddress = ''  # Local IPv4 Address, not editable
        self._RemoteIpAddress = ''  # Remote IPv4 Address, not editable
        self._LocalIpv6Address = ''  # Local IPv6 Address, not editable
        self._RemoteIpv6Address = ''  # Remote IPv6 Address, not editable
        self._SessionCount = 0  # Session Count, not editable
        self._SessionUp = 0  # Session Up, not editable
        self._SessionDown = 0  # Session Down, not editable
        self._TxPackets = 0  # Tx Packets, not editable
        self._RxPackets = 0  # Rx Packets, not editable
        self._TxSccrq = 0  # Tx SCCRQ, not editable
        self._RxSccrq = 0  # Rx SCCRQ, not editable
        self._TxSccrp = 0  # Tx SCCRP, not editable
        self._RxSccrp = 0  # Rx SCCRP, not editable
        self._TxScccn = 0  # Tx SCCCN, not editable
        self._RxScccn = 0  # Rx SCCCN, not editable
        self._TxSli = 0  # Tx SLI, not editable
        self._RxSli = 0  # Rx SLI, not editable
        self._TxStopCcn = 0  # Tx StopCCN, not editable
        self._RxStopCcn = 0  # Rx StopCCN, not editable
        self._TxWen = 0  # Tx WEN, not editable
        self._RxWen = 0  # Rx WEN, not editable
        self._TxHello = 0  # Tx Hello, not editable
        self._RxHello = 0  # Rx Hello, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(L2tpTunnelStatistic, self).__init__(**properties)

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
    def NodeIndexInBlock(self):
        """
        get the value of property _NodeIndexInBlock
        """
        if self.force_auto_sync:
            self.get('NodeIndexInBlock')
        return self._NodeIndexInBlock

    @property
    def LocalTunnelId(self):
        """
        get the value of property _LocalTunnelId
        """
        if self.force_auto_sync:
            self.get('LocalTunnelId')
        return self._LocalTunnelId

    @property
    def RemoteTunnelId(self):
        """
        get the value of property _RemoteTunnelId
        """
        if self.force_auto_sync:
            self.get('RemoteTunnelId')
        return self._RemoteTunnelId

    @property
    def TunnelState(self):
        """
        get the value of property _TunnelState
        """
        if self.force_auto_sync:
            self.get('TunnelState')
        return self._TunnelState

    @property
    def UdpSourcePort(self):
        """
        get the value of property _UdpSourcePort
        """
        if self.force_auto_sync:
            self.get('UdpSourcePort')
        return self._UdpSourcePort

    @property
    def UdpDestinationPort(self):
        """
        get the value of property _UdpDestinationPort
        """
        if self.force_auto_sync:
            self.get('UdpDestinationPort')
        return self._UdpDestinationPort

    @property
    def LocalIpAddress(self):
        """
        get the value of property _LocalIpAddress
        """
        if self.force_auto_sync:
            self.get('LocalIpAddress')
        return self._LocalIpAddress

    @property
    def RemoteIpAddress(self):
        """
        get the value of property _RemoteIpAddress
        """
        if self.force_auto_sync:
            self.get('RemoteIpAddress')
        return self._RemoteIpAddress

    @property
    def LocalIpv6Address(self):
        """
        get the value of property _LocalIpv6Address
        """
        if self.force_auto_sync:
            self.get('LocalIpv6Address')
        return self._LocalIpv6Address

    @property
    def RemoteIpv6Address(self):
        """
        get the value of property _RemoteIpv6Address
        """
        if self.force_auto_sync:
            self.get('RemoteIpv6Address')
        return self._RemoteIpv6Address

    @property
    def SessionCount(self):
        """
        get the value of property _SessionCount
        """
        if self.force_auto_sync:
            self.get('SessionCount')
        return self._SessionCount

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

    def _set_l2tpblockid_with_str(self, value):
        self._L2tpBlockId = value

    def _set_nodeindexinblock_with_str(self, value):
        try:
            self._NodeIndexInBlock = int(value)
        except ValueError:
            self._NodeIndexInBlock = hex(int(value, 16))

    def _set_localtunnelid_with_str(self, value):
        try:
            self._LocalTunnelId = int(value)
        except ValueError:
            self._LocalTunnelId = hex(int(value, 16))

    def _set_remotetunnelid_with_str(self, value):
        try:
            self._RemoteTunnelId = int(value)
        except ValueError:
            self._RemoteTunnelId = hex(int(value, 16))

    def _set_tunnelstate_with_str(self, value):
        self._TunnelState = value

    def _set_udpsourceport_with_str(self, value):
        try:
            self._UdpSourcePort = int(value)
        except ValueError:
            self._UdpSourcePort = hex(int(value, 16))

    def _set_udpdestinationport_with_str(self, value):
        try:
            self._UdpDestinationPort = int(value)
        except ValueError:
            self._UdpDestinationPort = hex(int(value, 16))

    def _set_localipaddress_with_str(self, value):
        self._LocalIpAddress = value

    def _set_remoteipaddress_with_str(self, value):
        self._RemoteIpAddress = value

    def _set_localipv6address_with_str(self, value):
        self._LocalIpv6Address = value

    def _set_remoteipv6address_with_str(self, value):
        self._RemoteIpv6Address = value

    def _set_sessioncount_with_str(self, value):
        try:
            self._SessionCount = int(value)
        except ValueError:
            self._SessionCount = hex(int(value, 16))

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

