"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class Dhcpv6ClientConfig(L23ProtocolConfig):
    def __init__(self, EmulationMode=None, EnableRenewMsg=None, EnableRebindMsg=None, EnableReconfigAccept=None, T1Timer=None, T2Timer=None, PreferredLifetime=None, ValidLifetime=None, RapidCommitOptMode=None, DuidType=None, DuidCustomValue=None, DuidEnterpriseNumber=None, DuidStartValue=None, DuidStepValue=None, DestinationAddress=None, EnableRelayAgent=None, RelayAgentIp=None, ServerIp=None, EnableUseRelayAgentMacForTraffic=None, RequestPrefixLength=None, RequestPrefixStartAddress=None, ControlPlaneSrcIPv6Addr=None, RequestStartAddress=None, EnableAuthentication=None, AuthenticationProtocol=None, DhcpRealm=None, AuthenticationKeyId=None, AuthenticationKey=None, AuthenticationKeyType=None, EnableDad=None, DadTimeout=None, DadTransmits=None, **kwargs):
        self._EmulationMode = EmulationMode  # Emulation Mode
        self._Dhcpv6BlockState = EnumDhcpv6BlockSessionState.IDLE  # DHCPv6 Block State, not editable
        self._Dhcpv6PdBlockState = EnumDhcpv6BlockSessionState.IDLE  # DHCPv6-PD Block State, not editable
        self._EnableRenewMsg = EnableRenewMsg  # Enable Renew Messages
        self._EnableRebindMsg = EnableRebindMsg  # Enable Rebind Messages
        self._EnableReconfigAccept = EnableReconfigAccept  # Enable Reconfigure Accept
        self._T1Timer = T1Timer  # T1 Timer (sec)
        self._T2Timer = T2Timer  # T2 Timer (sec)
        self._PreferredLifetime = PreferredLifetime  # Preferred Lifetime (sec)
        self._ValidLifetime = ValidLifetime  # Valid Lifetime (sec)
        self._RapidCommitOptMode = RapidCommitOptMode  # Rapid Commit Operation Mode
        self._DuidType = DuidType  # DUID Type
        self._DuidCustomValue = DuidCustomValue  # Custom DUID Value
        self._DuidEnterpriseNumber = DuidEnterpriseNumber  # DUID Enterprise Number
        self._DuidStartValue = DuidStartValue  # Starting DUID Value
        self._DuidStepValue = DuidStepValue  # DUID Step Value
        self._DestinationAddress = DestinationAddress  # Destination Address
        self._EnableRelayAgent = EnableRelayAgent  # Enable Relay Agent
        self._RelayAgentIp = RelayAgentIp  # Relay Agent IP
        self._ServerIp = ServerIp  # Server IP
        self._EnableUseRelayAgentMacForTraffic = EnableUseRelayAgentMacForTraffic  # Use Relay Agent MAC Address for Traffic
        self._RequestPrefixLength = RequestPrefixLength  # Request Prefix Length
        self._RequestPrefixStartAddress = RequestPrefixStartAddress  # Request Prefix Starting Address
        self._ControlPlaneSrcIPv6Addr = ControlPlaneSrcIPv6Addr  # Control Plane Source IPv6 Address
        self._RequestStartAddress = RequestStartAddress  # Request Starting Address
        self._EnableAuthentication = EnableAuthentication  # Enable Authentication
        self._AuthenticationProtocol = AuthenticationProtocol  # Authentication Protocol
        self._DhcpRealm = DhcpRealm  # DHCP Realm
        self._AuthenticationKeyId = AuthenticationKeyId  # Authentication Key ID
        self._AuthenticationKey = AuthenticationKey  # Authentication Key
        self._AuthenticationKeyType = AuthenticationKeyType  # Authentication Key Type
        self._EnableDad = EnableDad  # Enable DAD
        self._DadTimeout = DadTimeout  # DAD Timeout (sec)
        self._DadTransmits = DadTransmits  # DAD Transmits

        properties = kwargs.copy()
        if EmulationMode is not None:
            properties['EmulationMode'] = EmulationMode
        if EnableRenewMsg is not None:
            properties['EnableRenewMsg'] = EnableRenewMsg
        if EnableRebindMsg is not None:
            properties['EnableRebindMsg'] = EnableRebindMsg
        if EnableReconfigAccept is not None:
            properties['EnableReconfigAccept'] = EnableReconfigAccept
        if T1Timer is not None:
            properties['T1Timer'] = T1Timer
        if T2Timer is not None:
            properties['T2Timer'] = T2Timer
        if PreferredLifetime is not None:
            properties['PreferredLifetime'] = PreferredLifetime
        if ValidLifetime is not None:
            properties['ValidLifetime'] = ValidLifetime
        if RapidCommitOptMode is not None:
            properties['RapidCommitOptMode'] = RapidCommitOptMode
        if DuidType is not None:
            properties['DuidType'] = DuidType
        if DuidCustomValue is not None:
            properties['DuidCustomValue'] = DuidCustomValue
        if DuidEnterpriseNumber is not None:
            properties['DuidEnterpriseNumber'] = DuidEnterpriseNumber
        if DuidStartValue is not None:
            properties['DuidStartValue'] = DuidStartValue
        if DuidStepValue is not None:
            properties['DuidStepValue'] = DuidStepValue
        if DestinationAddress is not None:
            properties['DestinationAddress'] = DestinationAddress
        if EnableRelayAgent is not None:
            properties['EnableRelayAgent'] = EnableRelayAgent
        if RelayAgentIp is not None:
            properties['RelayAgentIp'] = RelayAgentIp
        if ServerIp is not None:
            properties['ServerIp'] = ServerIp
        if EnableUseRelayAgentMacForTraffic is not None:
            properties['EnableUseRelayAgentMacForTraffic'] = EnableUseRelayAgentMacForTraffic
        if RequestPrefixLength is not None:
            properties['RequestPrefixLength'] = RequestPrefixLength
        if RequestPrefixStartAddress is not None:
            properties['RequestPrefixStartAddress'] = RequestPrefixStartAddress
        if ControlPlaneSrcIPv6Addr is not None:
            properties['ControlPlaneSrcIPv6Addr'] = ControlPlaneSrcIPv6Addr
        if RequestStartAddress is not None:
            properties['RequestStartAddress'] = RequestStartAddress
        if EnableAuthentication is not None:
            properties['EnableAuthentication'] = EnableAuthentication
        if AuthenticationProtocol is not None:
            properties['AuthenticationProtocol'] = AuthenticationProtocol
        if DhcpRealm is not None:
            properties['DhcpRealm'] = DhcpRealm
        if AuthenticationKeyId is not None:
            properties['AuthenticationKeyId'] = AuthenticationKeyId
        if AuthenticationKey is not None:
            properties['AuthenticationKey'] = AuthenticationKey
        if AuthenticationKeyType is not None:
            properties['AuthenticationKeyType'] = AuthenticationKeyType
        if EnableDad is not None:
            properties['EnableDad'] = EnableDad
        if DadTimeout is not None:
            properties['DadTimeout'] = DadTimeout
        if DadTransmits is not None:
            properties['DadTransmits'] = DadTransmits

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv6ClientConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EmulationMode=None, EnableRenewMsg=None, EnableRebindMsg=None, EnableReconfigAccept=None, T1Timer=None, T2Timer=None, PreferredLifetime=None, ValidLifetime=None, RapidCommitOptMode=None, DuidType=None, DuidCustomValue=None, DuidEnterpriseNumber=None, DuidStartValue=None, DuidStepValue=None, DestinationAddress=None, EnableRelayAgent=None, RelayAgentIp=None, ServerIp=None, EnableUseRelayAgentMacForTraffic=None, RequestPrefixLength=None, RequestPrefixStartAddress=None, ControlPlaneSrcIPv6Addr=None, RequestStartAddress=None, EnableAuthentication=None, AuthenticationProtocol=None, DhcpRealm=None, AuthenticationKeyId=None, AuthenticationKey=None, AuthenticationKeyType=None, EnableDad=None, DadTimeout=None, DadTransmits=None, **kwargs):
        properties = kwargs.copy()
        if EmulationMode is not None:
            self._EmulationMode = EmulationMode
            properties['EmulationMode'] = EmulationMode
        if EnableRenewMsg is not None:
            self._EnableRenewMsg = EnableRenewMsg
            properties['EnableRenewMsg'] = EnableRenewMsg
        if EnableRebindMsg is not None:
            self._EnableRebindMsg = EnableRebindMsg
            properties['EnableRebindMsg'] = EnableRebindMsg
        if EnableReconfigAccept is not None:
            self._EnableReconfigAccept = EnableReconfigAccept
            properties['EnableReconfigAccept'] = EnableReconfigAccept
        if T1Timer is not None:
            self._T1Timer = T1Timer
            properties['T1Timer'] = T1Timer
        if T2Timer is not None:
            self._T2Timer = T2Timer
            properties['T2Timer'] = T2Timer
        if PreferredLifetime is not None:
            self._PreferredLifetime = PreferredLifetime
            properties['PreferredLifetime'] = PreferredLifetime
        if ValidLifetime is not None:
            self._ValidLifetime = ValidLifetime
            properties['ValidLifetime'] = ValidLifetime
        if RapidCommitOptMode is not None:
            self._RapidCommitOptMode = RapidCommitOptMode
            properties['RapidCommitOptMode'] = RapidCommitOptMode
        if DuidType is not None:
            self._DuidType = DuidType
            properties['DuidType'] = DuidType
        if DuidCustomValue is not None:
            self._DuidCustomValue = DuidCustomValue
            properties['DuidCustomValue'] = DuidCustomValue
        if DuidEnterpriseNumber is not None:
            self._DuidEnterpriseNumber = DuidEnterpriseNumber
            properties['DuidEnterpriseNumber'] = DuidEnterpriseNumber
        if DuidStartValue is not None:
            self._DuidStartValue = DuidStartValue
            properties['DuidStartValue'] = DuidStartValue
        if DuidStepValue is not None:
            self._DuidStepValue = DuidStepValue
            properties['DuidStepValue'] = DuidStepValue
        if DestinationAddress is not None:
            self._DestinationAddress = DestinationAddress
            properties['DestinationAddress'] = DestinationAddress
        if EnableRelayAgent is not None:
            self._EnableRelayAgent = EnableRelayAgent
            properties['EnableRelayAgent'] = EnableRelayAgent
        if RelayAgentIp is not None:
            self._RelayAgentIp = RelayAgentIp
            properties['RelayAgentIp'] = RelayAgentIp
        if ServerIp is not None:
            self._ServerIp = ServerIp
            properties['ServerIp'] = ServerIp
        if EnableUseRelayAgentMacForTraffic is not None:
            self._EnableUseRelayAgentMacForTraffic = EnableUseRelayAgentMacForTraffic
            properties['EnableUseRelayAgentMacForTraffic'] = EnableUseRelayAgentMacForTraffic
        if RequestPrefixLength is not None:
            self._RequestPrefixLength = RequestPrefixLength
            properties['RequestPrefixLength'] = RequestPrefixLength
        if RequestPrefixStartAddress is not None:
            self._RequestPrefixStartAddress = RequestPrefixStartAddress
            properties['RequestPrefixStartAddress'] = RequestPrefixStartAddress
        if ControlPlaneSrcIPv6Addr is not None:
            self._ControlPlaneSrcIPv6Addr = ControlPlaneSrcIPv6Addr
            properties['ControlPlaneSrcIPv6Addr'] = ControlPlaneSrcIPv6Addr
        if RequestStartAddress is not None:
            self._RequestStartAddress = RequestStartAddress
            properties['RequestStartAddress'] = RequestStartAddress
        if EnableAuthentication is not None:
            self._EnableAuthentication = EnableAuthentication
            properties['EnableAuthentication'] = EnableAuthentication
        if AuthenticationProtocol is not None:
            self._AuthenticationProtocol = AuthenticationProtocol
            properties['AuthenticationProtocol'] = AuthenticationProtocol
        if DhcpRealm is not None:
            self._DhcpRealm = DhcpRealm
            properties['DhcpRealm'] = DhcpRealm
        if AuthenticationKeyId is not None:
            self._AuthenticationKeyId = AuthenticationKeyId
            properties['AuthenticationKeyId'] = AuthenticationKeyId
        if AuthenticationKey is not None:
            self._AuthenticationKey = AuthenticationKey
            properties['AuthenticationKey'] = AuthenticationKey
        if AuthenticationKeyType is not None:
            self._AuthenticationKeyType = AuthenticationKeyType
            properties['AuthenticationKeyType'] = AuthenticationKeyType
        if EnableDad is not None:
            self._EnableDad = EnableDad
            properties['EnableDad'] = EnableDad
        if DadTimeout is not None:
            self._DadTimeout = DadTimeout
            properties['DadTimeout'] = DadTimeout
        if DadTransmits is not None:
            self._DadTransmits = DadTransmits
            properties['DadTransmits'] = DadTransmits

        super(Dhcpv6ClientConfig, self).edit(**properties)

    @property
    def EmulationMode(self):
        """
        get the value of property _EmulationMode
        """
        if self.force_auto_sync:
            self.get('EmulationMode')
        return self._EmulationMode

    @property
    def Dhcpv6BlockState(self):
        """
        get the value of property _Dhcpv6BlockState
        """
        if self.force_auto_sync:
            self.get('Dhcpv6BlockState')
        return self._Dhcpv6BlockState

    @property
    def Dhcpv6PdBlockState(self):
        """
        get the value of property _Dhcpv6PdBlockState
        """
        if self.force_auto_sync:
            self.get('Dhcpv6PdBlockState')
        return self._Dhcpv6PdBlockState

    @property
    def EnableRenewMsg(self):
        """
        get the value of property _EnableRenewMsg
        """
        if self.force_auto_sync:
            self.get('EnableRenewMsg')
        return self._EnableRenewMsg

    @property
    def EnableRebindMsg(self):
        """
        get the value of property _EnableRebindMsg
        """
        if self.force_auto_sync:
            self.get('EnableRebindMsg')
        return self._EnableRebindMsg

    @property
    def EnableReconfigAccept(self):
        """
        get the value of property _EnableReconfigAccept
        """
        if self.force_auto_sync:
            self.get('EnableReconfigAccept')
        return self._EnableReconfigAccept

    @property
    def T1Timer(self):
        """
        get the value of property _T1Timer
        """
        if self.force_auto_sync:
            self.get('T1Timer')
        return self._T1Timer

    @property
    def T2Timer(self):
        """
        get the value of property _T2Timer
        """
        if self.force_auto_sync:
            self.get('T2Timer')
        return self._T2Timer

    @property
    def PreferredLifetime(self):
        """
        get the value of property _PreferredLifetime
        """
        if self.force_auto_sync:
            self.get('PreferredLifetime')
        return self._PreferredLifetime

    @property
    def ValidLifetime(self):
        """
        get the value of property _ValidLifetime
        """
        if self.force_auto_sync:
            self.get('ValidLifetime')
        return self._ValidLifetime

    @property
    def RapidCommitOptMode(self):
        """
        get the value of property _RapidCommitOptMode
        """
        if self.force_auto_sync:
            self.get('RapidCommitOptMode')
        return self._RapidCommitOptMode

    @property
    def DuidType(self):
        """
        get the value of property _DuidType
        """
        if self.force_auto_sync:
            self.get('DuidType')
        return self._DuidType

    @property
    def DuidCustomValue(self):
        """
        get the value of property _DuidCustomValue
        """
        if self.force_auto_sync:
            self.get('DuidCustomValue')
        return self._DuidCustomValue

    @property
    def DuidEnterpriseNumber(self):
        """
        get the value of property _DuidEnterpriseNumber
        """
        if self.force_auto_sync:
            self.get('DuidEnterpriseNumber')
        return self._DuidEnterpriseNumber

    @property
    def DuidStartValue(self):
        """
        get the value of property _DuidStartValue
        """
        if self.force_auto_sync:
            self.get('DuidStartValue')
        return self._DuidStartValue

    @property
    def DuidStepValue(self):
        """
        get the value of property _DuidStepValue
        """
        if self.force_auto_sync:
            self.get('DuidStepValue')
        return self._DuidStepValue

    @property
    def DestinationAddress(self):
        """
        get the value of property _DestinationAddress
        """
        if self.force_auto_sync:
            self.get('DestinationAddress')
        return self._DestinationAddress

    @property
    def EnableRelayAgent(self):
        """
        get the value of property _EnableRelayAgent
        """
        if self.force_auto_sync:
            self.get('EnableRelayAgent')
        return self._EnableRelayAgent

    @property
    def RelayAgentIp(self):
        """
        get the value of property _RelayAgentIp
        """
        if self.force_auto_sync:
            self.get('RelayAgentIp')
        return self._RelayAgentIp

    @property
    def ServerIp(self):
        """
        get the value of property _ServerIp
        """
        if self.force_auto_sync:
            self.get('ServerIp')
        return self._ServerIp

    @property
    def EnableUseRelayAgentMacForTraffic(self):
        """
        get the value of property _EnableUseRelayAgentMacForTraffic
        """
        if self.force_auto_sync:
            self.get('EnableUseRelayAgentMacForTraffic')
        return self._EnableUseRelayAgentMacForTraffic

    @property
    def RequestPrefixLength(self):
        """
        get the value of property _RequestPrefixLength
        """
        if self.force_auto_sync:
            self.get('RequestPrefixLength')
        return self._RequestPrefixLength

    @property
    def RequestPrefixStartAddress(self):
        """
        get the value of property _RequestPrefixStartAddress
        """
        if self.force_auto_sync:
            self.get('RequestPrefixStartAddress')
        return self._RequestPrefixStartAddress

    @property
    def ControlPlaneSrcIPv6Addr(self):
        """
        get the value of property _ControlPlaneSrcIPv6Addr
        """
        if self.force_auto_sync:
            self.get('ControlPlaneSrcIPv6Addr')
        return self._ControlPlaneSrcIPv6Addr

    @property
    def RequestStartAddress(self):
        """
        get the value of property _RequestStartAddress
        """
        if self.force_auto_sync:
            self.get('RequestStartAddress')
        return self._RequestStartAddress

    @property
    def EnableAuthentication(self):
        """
        get the value of property _EnableAuthentication
        """
        if self.force_auto_sync:
            self.get('EnableAuthentication')
        return self._EnableAuthentication

    @property
    def AuthenticationProtocol(self):
        """
        get the value of property _AuthenticationProtocol
        """
        if self.force_auto_sync:
            self.get('AuthenticationProtocol')
        return self._AuthenticationProtocol

    @property
    def DhcpRealm(self):
        """
        get the value of property _DhcpRealm
        """
        if self.force_auto_sync:
            self.get('DhcpRealm')
        return self._DhcpRealm

    @property
    def AuthenticationKeyId(self):
        """
        get the value of property _AuthenticationKeyId
        """
        if self.force_auto_sync:
            self.get('AuthenticationKeyId')
        return self._AuthenticationKeyId

    @property
    def AuthenticationKey(self):
        """
        get the value of property _AuthenticationKey
        """
        if self.force_auto_sync:
            self.get('AuthenticationKey')
        return self._AuthenticationKey

    @property
    def AuthenticationKeyType(self):
        """
        get the value of property _AuthenticationKeyType
        """
        if self.force_auto_sync:
            self.get('AuthenticationKeyType')
        return self._AuthenticationKeyType

    @property
    def EnableDad(self):
        """
        get the value of property _EnableDad
        """
        if self.force_auto_sync:
            self.get('EnableDad')
        return self._EnableDad

    @property
    def DadTimeout(self):
        """
        get the value of property _DadTimeout
        """
        if self.force_auto_sync:
            self.get('DadTimeout')
        return self._DadTimeout

    @property
    def DadTransmits(self):
        """
        get the value of property _DadTransmits
        """
        if self.force_auto_sync:
            self.get('DadTransmits')
        return self._DadTransmits

    @EmulationMode.setter
    def EmulationMode(self, value):
        self._EmulationMode = value
        self.edit(EmulationMode=value)

    @EnableRenewMsg.setter
    def EnableRenewMsg(self, value):
        self._EnableRenewMsg = value
        self.edit(EnableRenewMsg=value)

    @EnableRebindMsg.setter
    def EnableRebindMsg(self, value):
        self._EnableRebindMsg = value
        self.edit(EnableRebindMsg=value)

    @EnableReconfigAccept.setter
    def EnableReconfigAccept(self, value):
        self._EnableReconfigAccept = value
        self.edit(EnableReconfigAccept=value)

    @T1Timer.setter
    def T1Timer(self, value):
        self._T1Timer = value
        self.edit(T1Timer=value)

    @T2Timer.setter
    def T2Timer(self, value):
        self._T2Timer = value
        self.edit(T2Timer=value)

    @PreferredLifetime.setter
    def PreferredLifetime(self, value):
        self._PreferredLifetime = value
        self.edit(PreferredLifetime=value)

    @ValidLifetime.setter
    def ValidLifetime(self, value):
        self._ValidLifetime = value
        self.edit(ValidLifetime=value)

    @RapidCommitOptMode.setter
    def RapidCommitOptMode(self, value):
        self._RapidCommitOptMode = value
        self.edit(RapidCommitOptMode=value)

    @DuidType.setter
    def DuidType(self, value):
        self._DuidType = value
        self.edit(DuidType=value)

    @DuidCustomValue.setter
    def DuidCustomValue(self, value):
        self._DuidCustomValue = value
        self.edit(DuidCustomValue=value)

    @DuidEnterpriseNumber.setter
    def DuidEnterpriseNumber(self, value):
        self._DuidEnterpriseNumber = value
        self.edit(DuidEnterpriseNumber=value)

    @DuidStartValue.setter
    def DuidStartValue(self, value):
        self._DuidStartValue = value
        self.edit(DuidStartValue=value)

    @DuidStepValue.setter
    def DuidStepValue(self, value):
        self._DuidStepValue = value
        self.edit(DuidStepValue=value)

    @DestinationAddress.setter
    def DestinationAddress(self, value):
        self._DestinationAddress = value
        self.edit(DestinationAddress=value)

    @EnableRelayAgent.setter
    def EnableRelayAgent(self, value):
        self._EnableRelayAgent = value
        self.edit(EnableRelayAgent=value)

    @RelayAgentIp.setter
    def RelayAgentIp(self, value):
        self._RelayAgentIp = value
        self.edit(RelayAgentIp=value)

    @ServerIp.setter
    def ServerIp(self, value):
        self._ServerIp = value
        self.edit(ServerIp=value)

    @EnableUseRelayAgentMacForTraffic.setter
    def EnableUseRelayAgentMacForTraffic(self, value):
        self._EnableUseRelayAgentMacForTraffic = value
        self.edit(EnableUseRelayAgentMacForTraffic=value)

    @RequestPrefixLength.setter
    def RequestPrefixLength(self, value):
        self._RequestPrefixLength = value
        self.edit(RequestPrefixLength=value)

    @RequestPrefixStartAddress.setter
    def RequestPrefixStartAddress(self, value):
        self._RequestPrefixStartAddress = value
        self.edit(RequestPrefixStartAddress=value)

    @ControlPlaneSrcIPv6Addr.setter
    def ControlPlaneSrcIPv6Addr(self, value):
        self._ControlPlaneSrcIPv6Addr = value
        self.edit(ControlPlaneSrcIPv6Addr=value)

    @RequestStartAddress.setter
    def RequestStartAddress(self, value):
        self._RequestStartAddress = value
        self.edit(RequestStartAddress=value)

    @EnableAuthentication.setter
    def EnableAuthentication(self, value):
        self._EnableAuthentication = value
        self.edit(EnableAuthentication=value)

    @AuthenticationProtocol.setter
    def AuthenticationProtocol(self, value):
        self._AuthenticationProtocol = value
        self.edit(AuthenticationProtocol=value)

    @DhcpRealm.setter
    def DhcpRealm(self, value):
        self._DhcpRealm = value
        self.edit(DhcpRealm=value)

    @AuthenticationKeyId.setter
    def AuthenticationKeyId(self, value):
        self._AuthenticationKeyId = value
        self.edit(AuthenticationKeyId=value)

    @AuthenticationKey.setter
    def AuthenticationKey(self, value):
        self._AuthenticationKey = value
        self.edit(AuthenticationKey=value)

    @AuthenticationKeyType.setter
    def AuthenticationKeyType(self, value):
        self._AuthenticationKeyType = value
        self.edit(AuthenticationKeyType=value)

    @EnableDad.setter
    def EnableDad(self, value):
        self._EnableDad = value
        self.edit(EnableDad=value)

    @DadTimeout.setter
    def DadTimeout(self, value):
        self._DadTimeout = value
        self.edit(DadTimeout=value)

    @DadTransmits.setter
    def DadTransmits(self, value):
        self._DadTransmits = value
        self.edit(DadTransmits=value)

    def _set_emulationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._EmulationMode = EnumDhcpv6EmulationMode.%s' % value[:seperate])

    def _set_dhcpv6blockstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._Dhcpv6BlockState = EnumDhcpv6BlockSessionState.%s' % value[:seperate])

    def _set_dhcpv6pdblockstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._Dhcpv6PdBlockState = EnumDhcpv6BlockSessionState.%s' % value[:seperate])

    def _set_enablerenewmsg_with_str(self, value):
        self._EnableRenewMsg = (value == 'True')

    def _set_enablerebindmsg_with_str(self, value):
        self._EnableRebindMsg = (value == 'True')

    def _set_enablereconfigaccept_with_str(self, value):
        self._EnableReconfigAccept = (value == 'True')

    def _set_t1timer_with_str(self, value):
        try:
            self._T1Timer = int(value)
        except ValueError:
            self._T1Timer = hex(int(value, 16))

    def _set_t2timer_with_str(self, value):
        try:
            self._T2Timer = int(value)
        except ValueError:
            self._T2Timer = hex(int(value, 16))

    def _set_preferredlifetime_with_str(self, value):
        try:
            self._PreferredLifetime = int(value)
        except ValueError:
            self._PreferredLifetime = hex(int(value, 16))

    def _set_validlifetime_with_str(self, value):
        try:
            self._ValidLifetime = int(value)
        except ValueError:
            self._ValidLifetime = hex(int(value, 16))

    def _set_rapidcommitoptmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._RapidCommitOptMode = EnumDhcpv6RapidCommitOptMode.%s' % value[:seperate])

    def _set_duidtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._DuidType = EnumDhcpv6DuidType.%s' % value[:seperate])

    def _set_duidcustomvalue_with_str(self, value):
        try:
            self._DuidCustomValue = int(value)
        except ValueError:
            self._DuidCustomValue = hex(int(value, 16))

    def _set_duidenterprisenumber_with_str(self, value):
        try:
            self._DuidEnterpriseNumber = int(value)
        except ValueError:
            self._DuidEnterpriseNumber = hex(int(value, 16))

    def _set_duidstartvalue_with_str(self, value):
        self._DuidStartValue = value

    def _set_duidstepvalue_with_str(self, value):
        try:
            self._DuidStepValue = int(value)
        except ValueError:
            self._DuidStepValue = hex(int(value, 16))

    def _set_destinationaddress_with_str(self, value):
        seperate = value.find(':')
        exec('self._DestinationAddress = EnumDhcpv6DestAddress.%s' % value[:seperate])

    def _set_enablerelayagent_with_str(self, value):
        self._EnableRelayAgent = (value == 'True')

    def _set_relayagentip_with_str(self, value):
        self._RelayAgentIp = value

    def _set_serverip_with_str(self, value):
        self._ServerIp = value

    def _set_enableuserelayagentmacfortraffic_with_str(self, value):
        self._EnableUseRelayAgentMacForTraffic = (value == 'True')

    def _set_requestprefixlength_with_str(self, value):
        try:
            self._RequestPrefixLength = int(value)
        except ValueError:
            self._RequestPrefixLength = hex(int(value, 16))

    def _set_requestprefixstartaddress_with_str(self, value):
        self._RequestPrefixStartAddress = value

    def _set_controlplanesrcipv6addr_with_str(self, value):
        seperate = value.find(':')
        exec('self._ControlPlaneSrcIPv6Addr = EnumDhcpv6SourceIPv6Address.%s' % value[:seperate])

    def _set_requeststartaddress_with_str(self, value):
        self._RequestStartAddress = value

    def _set_enableauthentication_with_str(self, value):
        self._EnableAuthentication = (value == 'True')

    def _set_authenticationprotocol_with_str(self, value):
        seperate = value.find(':')
        exec('self._AuthenticationProtocol = EnumDhcpv6AuthenticationProtocol.%s' % value[:seperate])

    def _set_dhcprealm_with_str(self, value):
        self._DhcpRealm = value

    def _set_authenticationkeyid_with_str(self, value):
        try:
            self._AuthenticationKeyId = int(value)
        except ValueError:
            self._AuthenticationKeyId = hex(int(value, 16))

    def _set_authenticationkey_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._AuthenticationKey = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._AuthenticationKey.append(int(str_value))
            except ValueError:
                self._AuthenticationKey.append(hex(int(str_value, 16)))

    def _set_authenticationkeytype_with_str(self, value):
        seperate = value.find(':')
        exec('self._AuthenticationKeyType = EnumDhcpv6KeyType.%s' % value[:seperate])

    def _set_enabledad_with_str(self, value):
        self._EnableDad = (value == 'True')

    def _set_dadtimeout_with_str(self, value):
        try:
            self._DadTimeout = int(value)
        except ValueError:
            self._DadTimeout = hex(int(value, 16))

    def _set_dadtransmits_with_str(self, value):
        try:
            self._DadTransmits = int(value)
        except ValueError:
            self._DadTransmits = hex(int(value, 16))

