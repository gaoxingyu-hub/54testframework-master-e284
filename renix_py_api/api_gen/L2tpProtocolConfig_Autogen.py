"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class L2tpProtocolConfig(L23ProtocolConfig):
    def __init__(self, EmulationMode=None, TunnelCountPerNode=None, SessionCountPerTunnel=None, TunnelStartingId=None, SessionStartingId=None, UdpSourcePort=None, UdpChecksumEnabled=None, RetryTunnelCreationEnabled=None, TunnelCreationTimeout=None, MaxTunnelCreationTimes=None, HostName=None, EnableAuthentication=None, IncomingTunnelPassword=None, OutgoingTunnelPassword=None, HelloEnabled=None, HelloInterval=None, TxBitRate=None, BearerCapabilities=None, BearerType=None, FrameCapabilities=None, FrameType=None, CallingNumberEnabled=None, CallingNumber=None, RxWindowSize=None, UseGatewayAsRemoteIp=None, RemoteIpv4Address=None, RemoteIpv4AddressStep=None, RemoteIpv6Address=None, RemoteIpv6AddressStep=None, LcpProxyMode=None, ForceLcpRenegotiation=None, Ipv4TosValue=None, Ipv6TrafficClassValue=None, HideFramingCapabilities=None, HideBearerCapabilities=None, HideAssignedTunnelId=None, HideChallenge=None, HideChallengeResponse=None, HideAssignedSessionId=None, HideCallSerialNumber=None, HideFramingType=None, HideCallingNumber=None, HideTxConnectSpeed=None, HideLastSentLcpConfReq=None, HideLastReceivedLcpConfReq=None, HideProxyAuthenType=None, HideProxyAuthenName=None, HideProxyAuthenChallenge=None, HideProxyAuthenId=None, HideProxyAuthenResponse=None, **kwargs):
        self._L2tpBlockState = EnumL2tpState.NONE  # L2TP Block State, not editable
        self._L2tpVersion = EnumL2tpVersion.L2TPV2  # L2TP Version, not editable
        self._EmulationMode = EmulationMode  # Emulation Mode
        self._IpEncapsulation = EnumL2tpIpEncapsulation.IPV4  # IP Encapsulation, not editable
        self._TunnelCountPerNode = TunnelCountPerNode  # Tunnel Count per LAC/LNS
        self._SessionCountPerTunnel = SessionCountPerTunnel  # Session Count per Tunnel
        self._TunnelStartingId = TunnelStartingId  # Tunnel Starting ID
        self._SessionStartingId = SessionStartingId  # Session Starting ID
        self._UdpSourcePort = UdpSourcePort  # UDP Source Port
        self._UdpChecksumEnabled = UdpChecksumEnabled  # Enable UDP Checksum
        self._RetryTunnelCreationEnabled = RetryTunnelCreationEnabled  # Enable Retry Tunnel Creation
        self._TunnelCreationTimeout = TunnelCreationTimeout  # Tunnel Creation Timeout(secs)
        self._MaxTunnelCreationTimes = MaxTunnelCreationTimes  # Maximum Tunnel Creation Times
        self._HostName = HostName  # Host Name
        self._EnableAuthentication = EnableAuthentication  # Enable Authentication
        self._IncomingTunnelPassword = IncomingTunnelPassword  # Incoming Tunnel Password
        self._OutgoingTunnelPassword = OutgoingTunnelPassword  # Outgoing Tunnel Password
        self._HelloEnabled = HelloEnabled  # Enable Hello
        self._HelloInterval = HelloInterval  # Hello Interval (secs)
        self._TxBitRate = TxBitRate  # Tx Bit Rate (bits/sec)
        self._BearerCapabilities = BearerCapabilities  # Bearer Capabilities
        self._BearerType = BearerType  # Bearer Type
        self._FrameCapabilities = FrameCapabilities  # Frame Capabilities
        self._FrameType = FrameType  # Frame Type
        self._CallingNumberEnabled = CallingNumberEnabled  # Enable Calling Number
        self._CallingNumber = CallingNumber  # Calling Number
        self._RxWindowSize = RxWindowSize  # Rx Window Size
        self._UseGatewayAsRemoteIp = UseGatewayAsRemoteIp  # Use Gateway Address as Remote Address
        self._RemoteIpv4Address = RemoteIpv4Address  # Remote IPv4 Address
        self._RemoteIpv4AddressStep = RemoteIpv4AddressStep  # Remote IPv4 Address Step
        self._RemoteIpv6Address = RemoteIpv6Address  # Remote IPv6 Address
        self._RemoteIpv6AddressStep = RemoteIpv6AddressStep  # Remote IPv6 Address Step
        self._LcpProxyMode = LcpProxyMode  # LCP Proxy Mode
        self._ForceLcpRenegotiation = ForceLcpRenegotiation  # Force LCP Renegotiation
        self._Ipv4TosValue = Ipv4TosValue  # IPv4 TOS value(Hex)
        self._Ipv6TrafficClassValue = Ipv6TrafficClassValue  # IPv6 Traffic Class Value
        self._HideFramingCapabilities = HideFramingCapabilities  # Hidden Framing Capabilities(3)
        self._HideBearerCapabilities = HideBearerCapabilities  # Hidden Bearer Capabilities(4)
        self._HideFirmwareRevision = False  # Hidden Firmware Revision(6), not editable
        self._HideVendorName = False  # Hidden Vendor Name(8), not editable
        self._HideAssignedTunnelId = HideAssignedTunnelId  # Hidden Assigned Tunnel ID(9)
        self._HideChallenge = HideChallenge  # Hidden Challenge(11)
        self._HideChallengeResponse = HideChallengeResponse  # Hidden Challenge Response(13)
        self._HideAssignedSessionId = HideAssignedSessionId  # Hidden Assigned Session ID(14)
        self._HideCallSerialNumber = HideCallSerialNumber  # Hidden Call Serial Number(15)
        self._HideMinBps = False  # Hidden Minimum BPS(16), not editable
        self._HideMaxBps = False  # Hidden Maximum BPS(17), not editable
        self._HideBearerType = False  # Hidden Bearer Type(18), not editable
        self._HideFramingType = HideFramingType  # Hidden Framing Type(19)
        self._HideCalledNumber = False  # Hidden Called Number(21), not editable
        self._HideCallingNumber = HideCallingNumber  # Hidden Calling Number(22)
        self._HideSubAddress = False  # Hidden Sub-Address(23), not editable
        self._HideTxConnectSpeed = HideTxConnectSpeed  # Hidden Tx Connect Speed(24)
        self._HidePhysicalChannelId = False  # Hidden Physical Channel ID(25), not editable
        self._HidePrivateGroupId = False  # Hidden Private Group ID(37), not editable
        self._HideRxConnectSpeed = False  # Hidden Rx Connect Speed(38), not editable
        self._HideInitialReceivedLcpConfReq = False  # Hidden Initial Received LCP CONFREQ(26), not editable
        self._HideLastSentLcpConfReq = HideLastSentLcpConfReq  # Hidden Last Sent LCP CONFREQ(27)
        self._HideLastReceivedLcpConfReq = HideLastReceivedLcpConfReq  # Hidden Last Received LCP CONFREQ(28)
        self._HideProxyAuthenType = HideProxyAuthenType  # Hidden Proxy Authen Type(29)
        self._HideProxyAuthenName = HideProxyAuthenName  # Hidden Proxy Authen Name(30)
        self._HideProxyAuthenChallenge = HideProxyAuthenChallenge  # Hidden Proxy Authen Challenge(31)
        self._HideProxyAuthenId = HideProxyAuthenId  # Hidden Proxy Authen ID(32)
        self._HideProxyAuthenResponse = HideProxyAuthenResponse  # Hidden Proxy Authen Response(33)
        self._HideCallErrors = False  # Hidden Call Errors(34), not editable
        self._HideAccm = False  # Hidden ACCM(35), not editable

        properties = kwargs.copy()
        if EmulationMode is not None:
            properties['EmulationMode'] = EmulationMode
        if TunnelCountPerNode is not None:
            properties['TunnelCountPerNode'] = TunnelCountPerNode
        if SessionCountPerTunnel is not None:
            properties['SessionCountPerTunnel'] = SessionCountPerTunnel
        if TunnelStartingId is not None:
            properties['TunnelStartingId'] = TunnelStartingId
        if SessionStartingId is not None:
            properties['SessionStartingId'] = SessionStartingId
        if UdpSourcePort is not None:
            properties['UdpSourcePort'] = UdpSourcePort
        if UdpChecksumEnabled is not None:
            properties['UdpChecksumEnabled'] = UdpChecksumEnabled
        if RetryTunnelCreationEnabled is not None:
            properties['RetryTunnelCreationEnabled'] = RetryTunnelCreationEnabled
        if TunnelCreationTimeout is not None:
            properties['TunnelCreationTimeout'] = TunnelCreationTimeout
        if MaxTunnelCreationTimes is not None:
            properties['MaxTunnelCreationTimes'] = MaxTunnelCreationTimes
        if HostName is not None:
            properties['HostName'] = HostName
        if EnableAuthentication is not None:
            properties['EnableAuthentication'] = EnableAuthentication
        if IncomingTunnelPassword is not None:
            properties['IncomingTunnelPassword'] = IncomingTunnelPassword
        if OutgoingTunnelPassword is not None:
            properties['OutgoingTunnelPassword'] = OutgoingTunnelPassword
        if HelloEnabled is not None:
            properties['HelloEnabled'] = HelloEnabled
        if HelloInterval is not None:
            properties['HelloInterval'] = HelloInterval
        if TxBitRate is not None:
            properties['TxBitRate'] = TxBitRate
        if BearerCapabilities is not None:
            properties['BearerCapabilities'] = BearerCapabilities
        if BearerType is not None:
            properties['BearerType'] = BearerType
        if FrameCapabilities is not None:
            properties['FrameCapabilities'] = FrameCapabilities
        if FrameType is not None:
            properties['FrameType'] = FrameType
        if CallingNumberEnabled is not None:
            properties['CallingNumberEnabled'] = CallingNumberEnabled
        if CallingNumber is not None:
            properties['CallingNumber'] = CallingNumber
        if RxWindowSize is not None:
            properties['RxWindowSize'] = RxWindowSize
        if UseGatewayAsRemoteIp is not None:
            properties['UseGatewayAsRemoteIp'] = UseGatewayAsRemoteIp
        if RemoteIpv4Address is not None:
            properties['RemoteIpv4Address'] = RemoteIpv4Address
        if RemoteIpv4AddressStep is not None:
            properties['RemoteIpv4AddressStep'] = RemoteIpv4AddressStep
        if RemoteIpv6Address is not None:
            properties['RemoteIpv6Address'] = RemoteIpv6Address
        if RemoteIpv6AddressStep is not None:
            properties['RemoteIpv6AddressStep'] = RemoteIpv6AddressStep
        if LcpProxyMode is not None:
            properties['LcpProxyMode'] = LcpProxyMode
        if ForceLcpRenegotiation is not None:
            properties['ForceLcpRenegotiation'] = ForceLcpRenegotiation
        if Ipv4TosValue is not None:
            properties['Ipv4TosValue'] = Ipv4TosValue
        if Ipv6TrafficClassValue is not None:
            properties['Ipv6TrafficClassValue'] = Ipv6TrafficClassValue
        if HideFramingCapabilities is not None:
            properties['HideFramingCapabilities'] = HideFramingCapabilities
        if HideBearerCapabilities is not None:
            properties['HideBearerCapabilities'] = HideBearerCapabilities
        if HideAssignedTunnelId is not None:
            properties['HideAssignedTunnelId'] = HideAssignedTunnelId
        if HideChallenge is not None:
            properties['HideChallenge'] = HideChallenge
        if HideChallengeResponse is not None:
            properties['HideChallengeResponse'] = HideChallengeResponse
        if HideAssignedSessionId is not None:
            properties['HideAssignedSessionId'] = HideAssignedSessionId
        if HideCallSerialNumber is not None:
            properties['HideCallSerialNumber'] = HideCallSerialNumber
        if HideFramingType is not None:
            properties['HideFramingType'] = HideFramingType
        if HideCallingNumber is not None:
            properties['HideCallingNumber'] = HideCallingNumber
        if HideTxConnectSpeed is not None:
            properties['HideTxConnectSpeed'] = HideTxConnectSpeed
        if HideLastSentLcpConfReq is not None:
            properties['HideLastSentLcpConfReq'] = HideLastSentLcpConfReq
        if HideLastReceivedLcpConfReq is not None:
            properties['HideLastReceivedLcpConfReq'] = HideLastReceivedLcpConfReq
        if HideProxyAuthenType is not None:
            properties['HideProxyAuthenType'] = HideProxyAuthenType
        if HideProxyAuthenName is not None:
            properties['HideProxyAuthenName'] = HideProxyAuthenName
        if HideProxyAuthenChallenge is not None:
            properties['HideProxyAuthenChallenge'] = HideProxyAuthenChallenge
        if HideProxyAuthenId is not None:
            properties['HideProxyAuthenId'] = HideProxyAuthenId
        if HideProxyAuthenResponse is not None:
            properties['HideProxyAuthenResponse'] = HideProxyAuthenResponse

        # call base class function, and it will send message to renix server to create a class.
        super(L2tpProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EmulationMode=None, TunnelCountPerNode=None, SessionCountPerTunnel=None, TunnelStartingId=None, SessionStartingId=None, UdpSourcePort=None, UdpChecksumEnabled=None, RetryTunnelCreationEnabled=None, TunnelCreationTimeout=None, MaxTunnelCreationTimes=None, HostName=None, EnableAuthentication=None, IncomingTunnelPassword=None, OutgoingTunnelPassword=None, HelloEnabled=None, HelloInterval=None, TxBitRate=None, BearerCapabilities=None, BearerType=None, FrameCapabilities=None, FrameType=None, CallingNumberEnabled=None, CallingNumber=None, RxWindowSize=None, UseGatewayAsRemoteIp=None, RemoteIpv4Address=None, RemoteIpv4AddressStep=None, RemoteIpv6Address=None, RemoteIpv6AddressStep=None, LcpProxyMode=None, ForceLcpRenegotiation=None, Ipv4TosValue=None, Ipv6TrafficClassValue=None, HideFramingCapabilities=None, HideBearerCapabilities=None, HideAssignedTunnelId=None, HideChallenge=None, HideChallengeResponse=None, HideAssignedSessionId=None, HideCallSerialNumber=None, HideFramingType=None, HideCallingNumber=None, HideTxConnectSpeed=None, HideLastSentLcpConfReq=None, HideLastReceivedLcpConfReq=None, HideProxyAuthenType=None, HideProxyAuthenName=None, HideProxyAuthenChallenge=None, HideProxyAuthenId=None, HideProxyAuthenResponse=None, **kwargs):
        properties = kwargs.copy()
        if EmulationMode is not None:
            self._EmulationMode = EmulationMode
            properties['EmulationMode'] = EmulationMode
        if TunnelCountPerNode is not None:
            self._TunnelCountPerNode = TunnelCountPerNode
            properties['TunnelCountPerNode'] = TunnelCountPerNode
        if SessionCountPerTunnel is not None:
            self._SessionCountPerTunnel = SessionCountPerTunnel
            properties['SessionCountPerTunnel'] = SessionCountPerTunnel
        if TunnelStartingId is not None:
            self._TunnelStartingId = TunnelStartingId
            properties['TunnelStartingId'] = TunnelStartingId
        if SessionStartingId is not None:
            self._SessionStartingId = SessionStartingId
            properties['SessionStartingId'] = SessionStartingId
        if UdpSourcePort is not None:
            self._UdpSourcePort = UdpSourcePort
            properties['UdpSourcePort'] = UdpSourcePort
        if UdpChecksumEnabled is not None:
            self._UdpChecksumEnabled = UdpChecksumEnabled
            properties['UdpChecksumEnabled'] = UdpChecksumEnabled
        if RetryTunnelCreationEnabled is not None:
            self._RetryTunnelCreationEnabled = RetryTunnelCreationEnabled
            properties['RetryTunnelCreationEnabled'] = RetryTunnelCreationEnabled
        if TunnelCreationTimeout is not None:
            self._TunnelCreationTimeout = TunnelCreationTimeout
            properties['TunnelCreationTimeout'] = TunnelCreationTimeout
        if MaxTunnelCreationTimes is not None:
            self._MaxTunnelCreationTimes = MaxTunnelCreationTimes
            properties['MaxTunnelCreationTimes'] = MaxTunnelCreationTimes
        if HostName is not None:
            self._HostName = HostName
            properties['HostName'] = HostName
        if EnableAuthentication is not None:
            self._EnableAuthentication = EnableAuthentication
            properties['EnableAuthentication'] = EnableAuthentication
        if IncomingTunnelPassword is not None:
            self._IncomingTunnelPassword = IncomingTunnelPassword
            properties['IncomingTunnelPassword'] = IncomingTunnelPassword
        if OutgoingTunnelPassword is not None:
            self._OutgoingTunnelPassword = OutgoingTunnelPassword
            properties['OutgoingTunnelPassword'] = OutgoingTunnelPassword
        if HelloEnabled is not None:
            self._HelloEnabled = HelloEnabled
            properties['HelloEnabled'] = HelloEnabled
        if HelloInterval is not None:
            self._HelloInterval = HelloInterval
            properties['HelloInterval'] = HelloInterval
        if TxBitRate is not None:
            self._TxBitRate = TxBitRate
            properties['TxBitRate'] = TxBitRate
        if BearerCapabilities is not None:
            self._BearerCapabilities = BearerCapabilities
            properties['BearerCapabilities'] = BearerCapabilities
        if BearerType is not None:
            self._BearerType = BearerType
            properties['BearerType'] = BearerType
        if FrameCapabilities is not None:
            self._FrameCapabilities = FrameCapabilities
            properties['FrameCapabilities'] = FrameCapabilities
        if FrameType is not None:
            self._FrameType = FrameType
            properties['FrameType'] = FrameType
        if CallingNumberEnabled is not None:
            self._CallingNumberEnabled = CallingNumberEnabled
            properties['CallingNumberEnabled'] = CallingNumberEnabled
        if CallingNumber is not None:
            self._CallingNumber = CallingNumber
            properties['CallingNumber'] = CallingNumber
        if RxWindowSize is not None:
            self._RxWindowSize = RxWindowSize
            properties['RxWindowSize'] = RxWindowSize
        if UseGatewayAsRemoteIp is not None:
            self._UseGatewayAsRemoteIp = UseGatewayAsRemoteIp
            properties['UseGatewayAsRemoteIp'] = UseGatewayAsRemoteIp
        if RemoteIpv4Address is not None:
            self._RemoteIpv4Address = RemoteIpv4Address
            properties['RemoteIpv4Address'] = RemoteIpv4Address
        if RemoteIpv4AddressStep is not None:
            self._RemoteIpv4AddressStep = RemoteIpv4AddressStep
            properties['RemoteIpv4AddressStep'] = RemoteIpv4AddressStep
        if RemoteIpv6Address is not None:
            self._RemoteIpv6Address = RemoteIpv6Address
            properties['RemoteIpv6Address'] = RemoteIpv6Address
        if RemoteIpv6AddressStep is not None:
            self._RemoteIpv6AddressStep = RemoteIpv6AddressStep
            properties['RemoteIpv6AddressStep'] = RemoteIpv6AddressStep
        if LcpProxyMode is not None:
            self._LcpProxyMode = LcpProxyMode
            properties['LcpProxyMode'] = LcpProxyMode
        if ForceLcpRenegotiation is not None:
            self._ForceLcpRenegotiation = ForceLcpRenegotiation
            properties['ForceLcpRenegotiation'] = ForceLcpRenegotiation
        if Ipv4TosValue is not None:
            self._Ipv4TosValue = Ipv4TosValue
            properties['Ipv4TosValue'] = Ipv4TosValue
        if Ipv6TrafficClassValue is not None:
            self._Ipv6TrafficClassValue = Ipv6TrafficClassValue
            properties['Ipv6TrafficClassValue'] = Ipv6TrafficClassValue
        if HideFramingCapabilities is not None:
            self._HideFramingCapabilities = HideFramingCapabilities
            properties['HideFramingCapabilities'] = HideFramingCapabilities
        if HideBearerCapabilities is not None:
            self._HideBearerCapabilities = HideBearerCapabilities
            properties['HideBearerCapabilities'] = HideBearerCapabilities
        if HideAssignedTunnelId is not None:
            self._HideAssignedTunnelId = HideAssignedTunnelId
            properties['HideAssignedTunnelId'] = HideAssignedTunnelId
        if HideChallenge is not None:
            self._HideChallenge = HideChallenge
            properties['HideChallenge'] = HideChallenge
        if HideChallengeResponse is not None:
            self._HideChallengeResponse = HideChallengeResponse
            properties['HideChallengeResponse'] = HideChallengeResponse
        if HideAssignedSessionId is not None:
            self._HideAssignedSessionId = HideAssignedSessionId
            properties['HideAssignedSessionId'] = HideAssignedSessionId
        if HideCallSerialNumber is not None:
            self._HideCallSerialNumber = HideCallSerialNumber
            properties['HideCallSerialNumber'] = HideCallSerialNumber
        if HideFramingType is not None:
            self._HideFramingType = HideFramingType
            properties['HideFramingType'] = HideFramingType
        if HideCallingNumber is not None:
            self._HideCallingNumber = HideCallingNumber
            properties['HideCallingNumber'] = HideCallingNumber
        if HideTxConnectSpeed is not None:
            self._HideTxConnectSpeed = HideTxConnectSpeed
            properties['HideTxConnectSpeed'] = HideTxConnectSpeed
        if HideLastSentLcpConfReq is not None:
            self._HideLastSentLcpConfReq = HideLastSentLcpConfReq
            properties['HideLastSentLcpConfReq'] = HideLastSentLcpConfReq
        if HideLastReceivedLcpConfReq is not None:
            self._HideLastReceivedLcpConfReq = HideLastReceivedLcpConfReq
            properties['HideLastReceivedLcpConfReq'] = HideLastReceivedLcpConfReq
        if HideProxyAuthenType is not None:
            self._HideProxyAuthenType = HideProxyAuthenType
            properties['HideProxyAuthenType'] = HideProxyAuthenType
        if HideProxyAuthenName is not None:
            self._HideProxyAuthenName = HideProxyAuthenName
            properties['HideProxyAuthenName'] = HideProxyAuthenName
        if HideProxyAuthenChallenge is not None:
            self._HideProxyAuthenChallenge = HideProxyAuthenChallenge
            properties['HideProxyAuthenChallenge'] = HideProxyAuthenChallenge
        if HideProxyAuthenId is not None:
            self._HideProxyAuthenId = HideProxyAuthenId
            properties['HideProxyAuthenId'] = HideProxyAuthenId
        if HideProxyAuthenResponse is not None:
            self._HideProxyAuthenResponse = HideProxyAuthenResponse
            properties['HideProxyAuthenResponse'] = HideProxyAuthenResponse

        super(L2tpProtocolConfig, self).edit(**properties)

    @property
    def L2tpBlockState(self):
        """
        get the value of property _L2tpBlockState
        """
        if self.force_auto_sync:
            self.get('L2tpBlockState')
        return self._L2tpBlockState

    @property
    def L2tpVersion(self):
        """
        get the value of property _L2tpVersion
        """
        if self.force_auto_sync:
            self.get('L2tpVersion')
        return self._L2tpVersion

    @property
    def EmulationMode(self):
        """
        get the value of property _EmulationMode
        """
        if self.force_auto_sync:
            self.get('EmulationMode')
        return self._EmulationMode

    @property
    def IpEncapsulation(self):
        """
        get the value of property _IpEncapsulation
        """
        if self.force_auto_sync:
            self.get('IpEncapsulation')
        return self._IpEncapsulation

    @property
    def TunnelCountPerNode(self):
        """
        get the value of property _TunnelCountPerNode
        """
        if self.force_auto_sync:
            self.get('TunnelCountPerNode')
        return self._TunnelCountPerNode

    @property
    def SessionCountPerTunnel(self):
        """
        get the value of property _SessionCountPerTunnel
        """
        if self.force_auto_sync:
            self.get('SessionCountPerTunnel')
        return self._SessionCountPerTunnel

    @property
    def TunnelStartingId(self):
        """
        get the value of property _TunnelStartingId
        """
        if self.force_auto_sync:
            self.get('TunnelStartingId')
        return self._TunnelStartingId

    @property
    def SessionStartingId(self):
        """
        get the value of property _SessionStartingId
        """
        if self.force_auto_sync:
            self.get('SessionStartingId')
        return self._SessionStartingId

    @property
    def UdpSourcePort(self):
        """
        get the value of property _UdpSourcePort
        """
        if self.force_auto_sync:
            self.get('UdpSourcePort')
        return self._UdpSourcePort

    @property
    def UdpChecksumEnabled(self):
        """
        get the value of property _UdpChecksumEnabled
        """
        if self.force_auto_sync:
            self.get('UdpChecksumEnabled')
        return self._UdpChecksumEnabled

    @property
    def RetryTunnelCreationEnabled(self):
        """
        get the value of property _RetryTunnelCreationEnabled
        """
        if self.force_auto_sync:
            self.get('RetryTunnelCreationEnabled')
        return self._RetryTunnelCreationEnabled

    @property
    def TunnelCreationTimeout(self):
        """
        get the value of property _TunnelCreationTimeout
        """
        if self.force_auto_sync:
            self.get('TunnelCreationTimeout')
        return self._TunnelCreationTimeout

    @property
    def MaxTunnelCreationTimes(self):
        """
        get the value of property _MaxTunnelCreationTimes
        """
        if self.force_auto_sync:
            self.get('MaxTunnelCreationTimes')
        return self._MaxTunnelCreationTimes

    @property
    def HostName(self):
        """
        get the value of property _HostName
        """
        if self.force_auto_sync:
            self.get('HostName')
        return self._HostName

    @property
    def EnableAuthentication(self):
        """
        get the value of property _EnableAuthentication
        """
        if self.force_auto_sync:
            self.get('EnableAuthentication')
        return self._EnableAuthentication

    @property
    def IncomingTunnelPassword(self):
        """
        get the value of property _IncomingTunnelPassword
        """
        if self.force_auto_sync:
            self.get('IncomingTunnelPassword')
        return self._IncomingTunnelPassword

    @property
    def OutgoingTunnelPassword(self):
        """
        get the value of property _OutgoingTunnelPassword
        """
        if self.force_auto_sync:
            self.get('OutgoingTunnelPassword')
        return self._OutgoingTunnelPassword

    @property
    def HelloEnabled(self):
        """
        get the value of property _HelloEnabled
        """
        if self.force_auto_sync:
            self.get('HelloEnabled')
        return self._HelloEnabled

    @property
    def HelloInterval(self):
        """
        get the value of property _HelloInterval
        """
        if self.force_auto_sync:
            self.get('HelloInterval')
        return self._HelloInterval

    @property
    def TxBitRate(self):
        """
        get the value of property _TxBitRate
        """
        if self.force_auto_sync:
            self.get('TxBitRate')
        return self._TxBitRate

    @property
    def BearerCapabilities(self):
        """
        get the value of property _BearerCapabilities
        """
        if self.force_auto_sync:
            self.get('BearerCapabilities')
        return self._BearerCapabilities

    @property
    def BearerType(self):
        """
        get the value of property _BearerType
        """
        if self.force_auto_sync:
            self.get('BearerType')
        return self._BearerType

    @property
    def FrameCapabilities(self):
        """
        get the value of property _FrameCapabilities
        """
        if self.force_auto_sync:
            self.get('FrameCapabilities')
        return self._FrameCapabilities

    @property
    def FrameType(self):
        """
        get the value of property _FrameType
        """
        if self.force_auto_sync:
            self.get('FrameType')
        return self._FrameType

    @property
    def CallingNumberEnabled(self):
        """
        get the value of property _CallingNumberEnabled
        """
        if self.force_auto_sync:
            self.get('CallingNumberEnabled')
        return self._CallingNumberEnabled

    @property
    def CallingNumber(self):
        """
        get the value of property _CallingNumber
        """
        if self.force_auto_sync:
            self.get('CallingNumber')
        return self._CallingNumber

    @property
    def RxWindowSize(self):
        """
        get the value of property _RxWindowSize
        """
        if self.force_auto_sync:
            self.get('RxWindowSize')
        return self._RxWindowSize

    @property
    def UseGatewayAsRemoteIp(self):
        """
        get the value of property _UseGatewayAsRemoteIp
        """
        if self.force_auto_sync:
            self.get('UseGatewayAsRemoteIp')
        return self._UseGatewayAsRemoteIp

    @property
    def RemoteIpv4Address(self):
        """
        get the value of property _RemoteIpv4Address
        """
        if self.force_auto_sync:
            self.get('RemoteIpv4Address')
        return self._RemoteIpv4Address

    @property
    def RemoteIpv4AddressStep(self):
        """
        get the value of property _RemoteIpv4AddressStep
        """
        if self.force_auto_sync:
            self.get('RemoteIpv4AddressStep')
        return self._RemoteIpv4AddressStep

    @property
    def RemoteIpv6Address(self):
        """
        get the value of property _RemoteIpv6Address
        """
        if self.force_auto_sync:
            self.get('RemoteIpv6Address')
        return self._RemoteIpv6Address

    @property
    def RemoteIpv6AddressStep(self):
        """
        get the value of property _RemoteIpv6AddressStep
        """
        if self.force_auto_sync:
            self.get('RemoteIpv6AddressStep')
        return self._RemoteIpv6AddressStep

    @property
    def LcpProxyMode(self):
        """
        get the value of property _LcpProxyMode
        """
        if self.force_auto_sync:
            self.get('LcpProxyMode')
        return self._LcpProxyMode

    @property
    def ForceLcpRenegotiation(self):
        """
        get the value of property _ForceLcpRenegotiation
        """
        if self.force_auto_sync:
            self.get('ForceLcpRenegotiation')
        return self._ForceLcpRenegotiation

    @property
    def Ipv4TosValue(self):
        """
        get the value of property _Ipv4TosValue
        """
        if self.force_auto_sync:
            self.get('Ipv4TosValue')
        return self._Ipv4TosValue

    @property
    def Ipv6TrafficClassValue(self):
        """
        get the value of property _Ipv6TrafficClassValue
        """
        if self.force_auto_sync:
            self.get('Ipv6TrafficClassValue')
        return self._Ipv6TrafficClassValue

    @property
    def HideFramingCapabilities(self):
        """
        get the value of property _HideFramingCapabilities
        """
        if self.force_auto_sync:
            self.get('HideFramingCapabilities')
        return self._HideFramingCapabilities

    @property
    def HideBearerCapabilities(self):
        """
        get the value of property _HideBearerCapabilities
        """
        if self.force_auto_sync:
            self.get('HideBearerCapabilities')
        return self._HideBearerCapabilities

    @property
    def HideFirmwareRevision(self):
        """
        get the value of property _HideFirmwareRevision
        """
        if self.force_auto_sync:
            self.get('HideFirmwareRevision')
        return self._HideFirmwareRevision

    @property
    def HideVendorName(self):
        """
        get the value of property _HideVendorName
        """
        if self.force_auto_sync:
            self.get('HideVendorName')
        return self._HideVendorName

    @property
    def HideAssignedTunnelId(self):
        """
        get the value of property _HideAssignedTunnelId
        """
        if self.force_auto_sync:
            self.get('HideAssignedTunnelId')
        return self._HideAssignedTunnelId

    @property
    def HideChallenge(self):
        """
        get the value of property _HideChallenge
        """
        if self.force_auto_sync:
            self.get('HideChallenge')
        return self._HideChallenge

    @property
    def HideChallengeResponse(self):
        """
        get the value of property _HideChallengeResponse
        """
        if self.force_auto_sync:
            self.get('HideChallengeResponse')
        return self._HideChallengeResponse

    @property
    def HideAssignedSessionId(self):
        """
        get the value of property _HideAssignedSessionId
        """
        if self.force_auto_sync:
            self.get('HideAssignedSessionId')
        return self._HideAssignedSessionId

    @property
    def HideCallSerialNumber(self):
        """
        get the value of property _HideCallSerialNumber
        """
        if self.force_auto_sync:
            self.get('HideCallSerialNumber')
        return self._HideCallSerialNumber

    @property
    def HideMinBps(self):
        """
        get the value of property _HideMinBps
        """
        if self.force_auto_sync:
            self.get('HideMinBps')
        return self._HideMinBps

    @property
    def HideMaxBps(self):
        """
        get the value of property _HideMaxBps
        """
        if self.force_auto_sync:
            self.get('HideMaxBps')
        return self._HideMaxBps

    @property
    def HideBearerType(self):
        """
        get the value of property _HideBearerType
        """
        if self.force_auto_sync:
            self.get('HideBearerType')
        return self._HideBearerType

    @property
    def HideFramingType(self):
        """
        get the value of property _HideFramingType
        """
        if self.force_auto_sync:
            self.get('HideFramingType')
        return self._HideFramingType

    @property
    def HideCalledNumber(self):
        """
        get the value of property _HideCalledNumber
        """
        if self.force_auto_sync:
            self.get('HideCalledNumber')
        return self._HideCalledNumber

    @property
    def HideCallingNumber(self):
        """
        get the value of property _HideCallingNumber
        """
        if self.force_auto_sync:
            self.get('HideCallingNumber')
        return self._HideCallingNumber

    @property
    def HideSubAddress(self):
        """
        get the value of property _HideSubAddress
        """
        if self.force_auto_sync:
            self.get('HideSubAddress')
        return self._HideSubAddress

    @property
    def HideTxConnectSpeed(self):
        """
        get the value of property _HideTxConnectSpeed
        """
        if self.force_auto_sync:
            self.get('HideTxConnectSpeed')
        return self._HideTxConnectSpeed

    @property
    def HidePhysicalChannelId(self):
        """
        get the value of property _HidePhysicalChannelId
        """
        if self.force_auto_sync:
            self.get('HidePhysicalChannelId')
        return self._HidePhysicalChannelId

    @property
    def HidePrivateGroupId(self):
        """
        get the value of property _HidePrivateGroupId
        """
        if self.force_auto_sync:
            self.get('HidePrivateGroupId')
        return self._HidePrivateGroupId

    @property
    def HideRxConnectSpeed(self):
        """
        get the value of property _HideRxConnectSpeed
        """
        if self.force_auto_sync:
            self.get('HideRxConnectSpeed')
        return self._HideRxConnectSpeed

    @property
    def HideInitialReceivedLcpConfReq(self):
        """
        get the value of property _HideInitialReceivedLcpConfReq
        """
        if self.force_auto_sync:
            self.get('HideInitialReceivedLcpConfReq')
        return self._HideInitialReceivedLcpConfReq

    @property
    def HideLastSentLcpConfReq(self):
        """
        get the value of property _HideLastSentLcpConfReq
        """
        if self.force_auto_sync:
            self.get('HideLastSentLcpConfReq')
        return self._HideLastSentLcpConfReq

    @property
    def HideLastReceivedLcpConfReq(self):
        """
        get the value of property _HideLastReceivedLcpConfReq
        """
        if self.force_auto_sync:
            self.get('HideLastReceivedLcpConfReq')
        return self._HideLastReceivedLcpConfReq

    @property
    def HideProxyAuthenType(self):
        """
        get the value of property _HideProxyAuthenType
        """
        if self.force_auto_sync:
            self.get('HideProxyAuthenType')
        return self._HideProxyAuthenType

    @property
    def HideProxyAuthenName(self):
        """
        get the value of property _HideProxyAuthenName
        """
        if self.force_auto_sync:
            self.get('HideProxyAuthenName')
        return self._HideProxyAuthenName

    @property
    def HideProxyAuthenChallenge(self):
        """
        get the value of property _HideProxyAuthenChallenge
        """
        if self.force_auto_sync:
            self.get('HideProxyAuthenChallenge')
        return self._HideProxyAuthenChallenge

    @property
    def HideProxyAuthenId(self):
        """
        get the value of property _HideProxyAuthenId
        """
        if self.force_auto_sync:
            self.get('HideProxyAuthenId')
        return self._HideProxyAuthenId

    @property
    def HideProxyAuthenResponse(self):
        """
        get the value of property _HideProxyAuthenResponse
        """
        if self.force_auto_sync:
            self.get('HideProxyAuthenResponse')
        return self._HideProxyAuthenResponse

    @property
    def HideCallErrors(self):
        """
        get the value of property _HideCallErrors
        """
        if self.force_auto_sync:
            self.get('HideCallErrors')
        return self._HideCallErrors

    @property
    def HideAccm(self):
        """
        get the value of property _HideAccm
        """
        if self.force_auto_sync:
            self.get('HideAccm')
        return self._HideAccm

    @EmulationMode.setter
    def EmulationMode(self, value):
        self._EmulationMode = value
        self.edit(EmulationMode=value)

    @TunnelCountPerNode.setter
    def TunnelCountPerNode(self, value):
        self._TunnelCountPerNode = value
        self.edit(TunnelCountPerNode=value)

    @SessionCountPerTunnel.setter
    def SessionCountPerTunnel(self, value):
        self._SessionCountPerTunnel = value
        self.edit(SessionCountPerTunnel=value)

    @TunnelStartingId.setter
    def TunnelStartingId(self, value):
        self._TunnelStartingId = value
        self.edit(TunnelStartingId=value)

    @SessionStartingId.setter
    def SessionStartingId(self, value):
        self._SessionStartingId = value
        self.edit(SessionStartingId=value)

    @UdpSourcePort.setter
    def UdpSourcePort(self, value):
        self._UdpSourcePort = value
        self.edit(UdpSourcePort=value)

    @UdpChecksumEnabled.setter
    def UdpChecksumEnabled(self, value):
        self._UdpChecksumEnabled = value
        self.edit(UdpChecksumEnabled=value)

    @RetryTunnelCreationEnabled.setter
    def RetryTunnelCreationEnabled(self, value):
        self._RetryTunnelCreationEnabled = value
        self.edit(RetryTunnelCreationEnabled=value)

    @TunnelCreationTimeout.setter
    def TunnelCreationTimeout(self, value):
        self._TunnelCreationTimeout = value
        self.edit(TunnelCreationTimeout=value)

    @MaxTunnelCreationTimes.setter
    def MaxTunnelCreationTimes(self, value):
        self._MaxTunnelCreationTimes = value
        self.edit(MaxTunnelCreationTimes=value)

    @HostName.setter
    def HostName(self, value):
        self._HostName = value
        self.edit(HostName=value)

    @EnableAuthentication.setter
    def EnableAuthentication(self, value):
        self._EnableAuthentication = value
        self.edit(EnableAuthentication=value)

    @IncomingTunnelPassword.setter
    def IncomingTunnelPassword(self, value):
        self._IncomingTunnelPassword = value
        self.edit(IncomingTunnelPassword=value)

    @OutgoingTunnelPassword.setter
    def OutgoingTunnelPassword(self, value):
        self._OutgoingTunnelPassword = value
        self.edit(OutgoingTunnelPassword=value)

    @HelloEnabled.setter
    def HelloEnabled(self, value):
        self._HelloEnabled = value
        self.edit(HelloEnabled=value)

    @HelloInterval.setter
    def HelloInterval(self, value):
        self._HelloInterval = value
        self.edit(HelloInterval=value)

    @TxBitRate.setter
    def TxBitRate(self, value):
        self._TxBitRate = value
        self.edit(TxBitRate=value)

    @BearerCapabilities.setter
    def BearerCapabilities(self, value):
        self._BearerCapabilities = value
        self.edit(BearerCapabilities=value)

    @BearerType.setter
    def BearerType(self, value):
        self._BearerType = value
        self.edit(BearerType=value)

    @FrameCapabilities.setter
    def FrameCapabilities(self, value):
        self._FrameCapabilities = value
        self.edit(FrameCapabilities=value)

    @FrameType.setter
    def FrameType(self, value):
        self._FrameType = value
        self.edit(FrameType=value)

    @CallingNumberEnabled.setter
    def CallingNumberEnabled(self, value):
        self._CallingNumberEnabled = value
        self.edit(CallingNumberEnabled=value)

    @CallingNumber.setter
    def CallingNumber(self, value):
        self._CallingNumber = value
        self.edit(CallingNumber=value)

    @RxWindowSize.setter
    def RxWindowSize(self, value):
        self._RxWindowSize = value
        self.edit(RxWindowSize=value)

    @UseGatewayAsRemoteIp.setter
    def UseGatewayAsRemoteIp(self, value):
        self._UseGatewayAsRemoteIp = value
        self.edit(UseGatewayAsRemoteIp=value)

    @RemoteIpv4Address.setter
    def RemoteIpv4Address(self, value):
        self._RemoteIpv4Address = value
        self.edit(RemoteIpv4Address=value)

    @RemoteIpv4AddressStep.setter
    def RemoteIpv4AddressStep(self, value):
        self._RemoteIpv4AddressStep = value
        self.edit(RemoteIpv4AddressStep=value)

    @RemoteIpv6Address.setter
    def RemoteIpv6Address(self, value):
        self._RemoteIpv6Address = value
        self.edit(RemoteIpv6Address=value)

    @RemoteIpv6AddressStep.setter
    def RemoteIpv6AddressStep(self, value):
        self._RemoteIpv6AddressStep = value
        self.edit(RemoteIpv6AddressStep=value)

    @LcpProxyMode.setter
    def LcpProxyMode(self, value):
        self._LcpProxyMode = value
        self.edit(LcpProxyMode=value)

    @ForceLcpRenegotiation.setter
    def ForceLcpRenegotiation(self, value):
        self._ForceLcpRenegotiation = value
        self.edit(ForceLcpRenegotiation=value)

    @Ipv4TosValue.setter
    def Ipv4TosValue(self, value):
        self._Ipv4TosValue = value
        self.edit(Ipv4TosValue=value)

    @Ipv6TrafficClassValue.setter
    def Ipv6TrafficClassValue(self, value):
        self._Ipv6TrafficClassValue = value
        self.edit(Ipv6TrafficClassValue=value)

    @HideFramingCapabilities.setter
    def HideFramingCapabilities(self, value):
        self._HideFramingCapabilities = value
        self.edit(HideFramingCapabilities=value)

    @HideBearerCapabilities.setter
    def HideBearerCapabilities(self, value):
        self._HideBearerCapabilities = value
        self.edit(HideBearerCapabilities=value)

    @HideAssignedTunnelId.setter
    def HideAssignedTunnelId(self, value):
        self._HideAssignedTunnelId = value
        self.edit(HideAssignedTunnelId=value)

    @HideChallenge.setter
    def HideChallenge(self, value):
        self._HideChallenge = value
        self.edit(HideChallenge=value)

    @HideChallengeResponse.setter
    def HideChallengeResponse(self, value):
        self._HideChallengeResponse = value
        self.edit(HideChallengeResponse=value)

    @HideAssignedSessionId.setter
    def HideAssignedSessionId(self, value):
        self._HideAssignedSessionId = value
        self.edit(HideAssignedSessionId=value)

    @HideCallSerialNumber.setter
    def HideCallSerialNumber(self, value):
        self._HideCallSerialNumber = value
        self.edit(HideCallSerialNumber=value)

    @HideFramingType.setter
    def HideFramingType(self, value):
        self._HideFramingType = value
        self.edit(HideFramingType=value)

    @HideCallingNumber.setter
    def HideCallingNumber(self, value):
        self._HideCallingNumber = value
        self.edit(HideCallingNumber=value)

    @HideTxConnectSpeed.setter
    def HideTxConnectSpeed(self, value):
        self._HideTxConnectSpeed = value
        self.edit(HideTxConnectSpeed=value)

    @HideLastSentLcpConfReq.setter
    def HideLastSentLcpConfReq(self, value):
        self._HideLastSentLcpConfReq = value
        self.edit(HideLastSentLcpConfReq=value)

    @HideLastReceivedLcpConfReq.setter
    def HideLastReceivedLcpConfReq(self, value):
        self._HideLastReceivedLcpConfReq = value
        self.edit(HideLastReceivedLcpConfReq=value)

    @HideProxyAuthenType.setter
    def HideProxyAuthenType(self, value):
        self._HideProxyAuthenType = value
        self.edit(HideProxyAuthenType=value)

    @HideProxyAuthenName.setter
    def HideProxyAuthenName(self, value):
        self._HideProxyAuthenName = value
        self.edit(HideProxyAuthenName=value)

    @HideProxyAuthenChallenge.setter
    def HideProxyAuthenChallenge(self, value):
        self._HideProxyAuthenChallenge = value
        self.edit(HideProxyAuthenChallenge=value)

    @HideProxyAuthenId.setter
    def HideProxyAuthenId(self, value):
        self._HideProxyAuthenId = value
        self.edit(HideProxyAuthenId=value)

    @HideProxyAuthenResponse.setter
    def HideProxyAuthenResponse(self, value):
        self._HideProxyAuthenResponse = value
        self.edit(HideProxyAuthenResponse=value)

    def _set_l2tpblockstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._L2tpBlockState = EnumL2tpState.%s' % value[:seperate])

    def _set_l2tpversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._L2tpVersion = EnumL2tpVersion.%s' % value[:seperate])

    def _set_emulationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._EmulationMode = EnumL2tpEmulationMode.%s' % value[:seperate])

    def _set_ipencapsulation_with_str(self, value):
        seperate = value.find(':')
        exec('self._IpEncapsulation = EnumL2tpIpEncapsulation.%s' % value[:seperate])

    def _set_tunnelcountpernode_with_str(self, value):
        try:
            self._TunnelCountPerNode = int(value)
        except ValueError:
            self._TunnelCountPerNode = hex(int(value, 16))

    def _set_sessioncountpertunnel_with_str(self, value):
        try:
            self._SessionCountPerTunnel = int(value)
        except ValueError:
            self._SessionCountPerTunnel = hex(int(value, 16))

    def _set_tunnelstartingid_with_str(self, value):
        try:
            self._TunnelStartingId = int(value)
        except ValueError:
            self._TunnelStartingId = hex(int(value, 16))

    def _set_sessionstartingid_with_str(self, value):
        try:
            self._SessionStartingId = int(value)
        except ValueError:
            self._SessionStartingId = hex(int(value, 16))

    def _set_udpsourceport_with_str(self, value):
        try:
            self._UdpSourcePort = int(value)
        except ValueError:
            self._UdpSourcePort = hex(int(value, 16))

    def _set_udpchecksumenabled_with_str(self, value):
        self._UdpChecksumEnabled = (value == 'True')

    def _set_retrytunnelcreationenabled_with_str(self, value):
        self._RetryTunnelCreationEnabled = (value == 'True')

    def _set_tunnelcreationtimeout_with_str(self, value):
        try:
            self._TunnelCreationTimeout = int(value)
        except ValueError:
            self._TunnelCreationTimeout = hex(int(value, 16))

    def _set_maxtunnelcreationtimes_with_str(self, value):
        try:
            self._MaxTunnelCreationTimes = int(value)
        except ValueError:
            self._MaxTunnelCreationTimes = hex(int(value, 16))

    def _set_hostname_with_str(self, value):
        self._HostName = value

    def _set_enableauthentication_with_str(self, value):
        self._EnableAuthentication = (value == 'True')

    def _set_incomingtunnelpassword_with_str(self, value):
        self._IncomingTunnelPassword = value

    def _set_outgoingtunnelpassword_with_str(self, value):
        self._OutgoingTunnelPassword = value

    def _set_helloenabled_with_str(self, value):
        self._HelloEnabled = (value == 'True')

    def _set_hellointerval_with_str(self, value):
        try:
            self._HelloInterval = int(value)
        except ValueError:
            self._HelloInterval = hex(int(value, 16))

    def _set_txbitrate_with_str(self, value):
        try:
            self._TxBitRate = int(value)
        except ValueError:
            self._TxBitRate = hex(int(value, 16))

    def _set_bearercapabilities_with_str(self, value):
        seperate = value.find(':')
        exec('self._BearerCapabilities = EnumL2tpBearCapabilities.%s' % value[:seperate])

    def _set_bearertype_with_str(self, value):
        seperate = value.find(':')
        exec('self._BearerType = EnumL2tpBearType.%s' % value[:seperate])

    def _set_framecapabilities_with_str(self, value):
        seperate = value.find(':')
        exec('self._FrameCapabilities = EnumL2tpFrameCapabilities.%s' % value[:seperate])

    def _set_frametype_with_str(self, value):
        seperate = value.find(':')
        exec('self._FrameType = EnumL2tpFrameType.%s' % value[:seperate])

    def _set_callingnumberenabled_with_str(self, value):
        self._CallingNumberEnabled = (value == 'True')

    def _set_callingnumber_with_str(self, value):
        self._CallingNumber = value

    def _set_rxwindowsize_with_str(self, value):
        try:
            self._RxWindowSize = int(value)
        except ValueError:
            self._RxWindowSize = hex(int(value, 16))

    def _set_usegatewayasremoteip_with_str(self, value):
        self._UseGatewayAsRemoteIp = (value == 'True')

    def _set_remoteipv4address_with_str(self, value):
        self._RemoteIpv4Address = value

    def _set_remoteipv4addressstep_with_str(self, value):
        self._RemoteIpv4AddressStep = value

    def _set_remoteipv6address_with_str(self, value):
        self._RemoteIpv6Address = value

    def _set_remoteipv6addressstep_with_str(self, value):
        self._RemoteIpv6AddressStep = value

    def _set_lcpproxymode_with_str(self, value):
        seperate = value.find(':')
        exec('self._LcpProxyMode = EnumL2tpLcpProxyMode.%s' % value[:seperate])

    def _set_forcelcprenegotiation_with_str(self, value):
        self._ForceLcpRenegotiation = (value == 'True')

    def _set_ipv4tosvalue_with_str(self, value):
        try:
            self._Ipv4TosValue = int(value)
        except ValueError:
            self._Ipv4TosValue = hex(int(value, 16))

    def _set_ipv6trafficclassvalue_with_str(self, value):
        try:
            self._Ipv6TrafficClassValue = int(value)
        except ValueError:
            self._Ipv6TrafficClassValue = hex(int(value, 16))

    def _set_hideframingcapabilities_with_str(self, value):
        self._HideFramingCapabilities = (value == 'True')

    def _set_hidebearercapabilities_with_str(self, value):
        self._HideBearerCapabilities = (value == 'True')

    def _set_hidefirmwarerevision_with_str(self, value):
        self._HideFirmwareRevision = (value == 'True')

    def _set_hidevendorname_with_str(self, value):
        self._HideVendorName = (value == 'True')

    def _set_hideassignedtunnelid_with_str(self, value):
        self._HideAssignedTunnelId = (value == 'True')

    def _set_hidechallenge_with_str(self, value):
        self._HideChallenge = (value == 'True')

    def _set_hidechallengeresponse_with_str(self, value):
        self._HideChallengeResponse = (value == 'True')

    def _set_hideassignedsessionid_with_str(self, value):
        self._HideAssignedSessionId = (value == 'True')

    def _set_hidecallserialnumber_with_str(self, value):
        self._HideCallSerialNumber = (value == 'True')

    def _set_hideminbps_with_str(self, value):
        self._HideMinBps = (value == 'True')

    def _set_hidemaxbps_with_str(self, value):
        self._HideMaxBps = (value == 'True')

    def _set_hidebearertype_with_str(self, value):
        self._HideBearerType = (value == 'True')

    def _set_hideframingtype_with_str(self, value):
        self._HideFramingType = (value == 'True')

    def _set_hidecallednumber_with_str(self, value):
        self._HideCalledNumber = (value == 'True')

    def _set_hidecallingnumber_with_str(self, value):
        self._HideCallingNumber = (value == 'True')

    def _set_hidesubaddress_with_str(self, value):
        self._HideSubAddress = (value == 'True')

    def _set_hidetxconnectspeed_with_str(self, value):
        self._HideTxConnectSpeed = (value == 'True')

    def _set_hidephysicalchannelid_with_str(self, value):
        self._HidePhysicalChannelId = (value == 'True')

    def _set_hideprivategroupid_with_str(self, value):
        self._HidePrivateGroupId = (value == 'True')

    def _set_hiderxconnectspeed_with_str(self, value):
        self._HideRxConnectSpeed = (value == 'True')

    def _set_hideinitialreceivedlcpconfreq_with_str(self, value):
        self._HideInitialReceivedLcpConfReq = (value == 'True')

    def _set_hidelastsentlcpconfreq_with_str(self, value):
        self._HideLastSentLcpConfReq = (value == 'True')

    def _set_hidelastreceivedlcpconfreq_with_str(self, value):
        self._HideLastReceivedLcpConfReq = (value == 'True')

    def _set_hideproxyauthentype_with_str(self, value):
        self._HideProxyAuthenType = (value == 'True')

    def _set_hideproxyauthenname_with_str(self, value):
        self._HideProxyAuthenName = (value == 'True')

    def _set_hideproxyauthenchallenge_with_str(self, value):
        self._HideProxyAuthenChallenge = (value == 'True')

    def _set_hideproxyauthenid_with_str(self, value):
        self._HideProxyAuthenId = (value == 'True')

    def _set_hideproxyauthenresponse_with_str(self, value):
        self._HideProxyAuthenResponse = (value == 'True')

    def _set_hidecallerrors_with_str(self, value):
        self._HideCallErrors = (value == 'True')

    def _set_hideaccm_with_str(self, value):
        self._HideAccm = (value == 'True')

