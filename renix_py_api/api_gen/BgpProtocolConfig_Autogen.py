"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class BgpProtocolConfig(L23ProtocolConfig):
    def __init__(self, BgpInitiator=None, AsNumber=None, AsNumberStep=None, Enable4ByteAs=None, AsNumber4Byte=None, AsNumber4ByteStep=None, DutAsNumber=None, DutAsNumberStep=None, Enable4ByteDutAs=None, Dut4ByteAsNumber=None, Dut4ByteAsNumberStep=None, UseGatewayAsDutIp=None, BgpSessionIpAddressType=None, DutIpv4Address=None, DutIpv4AddressStep=None, DutIpv6Address=None, DutIpv6AddressStep=None, HoldTime=None, KeepaliveTime=None, ConnectRetryCount=None, ConnectRetryInterval=None, MaxRoutesPerUpdateMessage=None, RouteRefreshMode=None, EnableGracefulRestart=None, RestartTime=None, EnableViewRoutes=None, Password=None, EnableBfd=None, **kwargs):
        self._BgpProtocolState = EnumBgpProtocolState.DISABLED  # BGP Protocol State, not editable
        self._IpVersion = EnumBgpIpVersion.IPV4  # IP Version, not editable
        self._BgpInitiator = BgpInitiator  # BGP Initiator
        self._AsNumber = AsNumber  # AS Number
        self._AsNumberStep = AsNumberStep  # AS Number Step
        self._Enable4ByteAs = Enable4ByteAs  # Enable 4-Byte AS Number
        self._AsNumber4Byte = AsNumber4Byte  # 4-Bytes AS Number
        self._AsNumber4ByteStep = AsNumber4ByteStep  # 4-Bytes AS Number Step
        self._DutAsNumber = DutAsNumber  # DUT AS Number
        self._DutAsNumberStep = DutAsNumberStep  # DUT AS Number Step
        self._Enable4ByteDutAs = Enable4ByteDutAs  # Enable 4-Byte DUT AS Number
        self._Dut4ByteAsNumber = Dut4ByteAsNumber  # DUT 4-Bytes AS Number
        self._Dut4ByteAsNumberStep = Dut4ByteAsNumberStep  # DUT 4-Bytes AS Number Step
        self._BgpType = EnumBgpType.IBGP  # BGP Type, not editable
        self._UseGatewayAsDutIp = UseGatewayAsDutIp  # Use Gateway as DUT IP
        self._BgpSessionIpAddressType = BgpSessionIpAddressType  # BGP Session IP Address Type
        self._DutIpv4Address = DutIpv4Address  # DUT IPv4 address
        self._DutIpv4AddressStep = DutIpv4AddressStep  # DUT IPv4 address step
        self._DutIpv6Address = DutIpv6Address  # DUT IPv6 address
        self._DutIpv6AddressStep = DutIpv6AddressStep  # DUT IPv6 address step
        self._HoldTime = HoldTime  # Hold Time Interval (sec)
        self._KeepaliveTime = KeepaliveTime  # Keep Alive Interval (sec)
        self._ConnectRetryCount = ConnectRetryCount  # Connection Retry Count
        self._ConnectRetryInterval = ConnectRetryInterval  # Connection Retry Interval (sec)
        self._MaxRoutesPerUpdateMessage = MaxRoutesPerUpdateMessage  # Max Routes per Update Message
        self._RouteRefreshMode = RouteRefreshMode  # Route Refresh Mode
        self._EnableGracefulRestart = EnableGracefulRestart  # Enable Graceful Restart
        self._RestartTime = RestartTime  # Restart Time (sec)
        self._EnableViewRoutes = EnableViewRoutes  # Enable View Routes
        self._Authentication = EnumBgpAuthentication.NONE  # Authentication, not editable
        self._Password = Password  # Password
        self._EnableBfd = EnableBfd  # Enable BFD

        properties = kwargs.copy()
        if BgpInitiator is not None:
            properties['BgpInitiator'] = BgpInitiator
        if AsNumber is not None:
            properties['AsNumber'] = AsNumber
        if AsNumberStep is not None:
            properties['AsNumberStep'] = AsNumberStep
        if Enable4ByteAs is not None:
            properties['Enable4ByteAs'] = Enable4ByteAs
        if AsNumber4Byte is not None:
            properties['AsNumber4Byte'] = AsNumber4Byte
        if AsNumber4ByteStep is not None:
            properties['AsNumber4ByteStep'] = AsNumber4ByteStep
        if DutAsNumber is not None:
            properties['DutAsNumber'] = DutAsNumber
        if DutAsNumberStep is not None:
            properties['DutAsNumberStep'] = DutAsNumberStep
        if Enable4ByteDutAs is not None:
            properties['Enable4ByteDutAs'] = Enable4ByteDutAs
        if Dut4ByteAsNumber is not None:
            properties['Dut4ByteAsNumber'] = Dut4ByteAsNumber
        if Dut4ByteAsNumberStep is not None:
            properties['Dut4ByteAsNumberStep'] = Dut4ByteAsNumberStep
        if UseGatewayAsDutIp is not None:
            properties['UseGatewayAsDutIp'] = UseGatewayAsDutIp
        if BgpSessionIpAddressType is not None:
            properties['BgpSessionIpAddressType'] = BgpSessionIpAddressType
        if DutIpv4Address is not None:
            properties['DutIpv4Address'] = DutIpv4Address
        if DutIpv4AddressStep is not None:
            properties['DutIpv4AddressStep'] = DutIpv4AddressStep
        if DutIpv6Address is not None:
            properties['DutIpv6Address'] = DutIpv6Address
        if DutIpv6AddressStep is not None:
            properties['DutIpv6AddressStep'] = DutIpv6AddressStep
        if HoldTime is not None:
            properties['HoldTime'] = HoldTime
        if KeepaliveTime is not None:
            properties['KeepaliveTime'] = KeepaliveTime
        if ConnectRetryCount is not None:
            properties['ConnectRetryCount'] = ConnectRetryCount
        if ConnectRetryInterval is not None:
            properties['ConnectRetryInterval'] = ConnectRetryInterval
        if MaxRoutesPerUpdateMessage is not None:
            properties['MaxRoutesPerUpdateMessage'] = MaxRoutesPerUpdateMessage
        if RouteRefreshMode is not None:
            properties['RouteRefreshMode'] = RouteRefreshMode
        if EnableGracefulRestart is not None:
            properties['EnableGracefulRestart'] = EnableGracefulRestart
        if RestartTime is not None:
            properties['RestartTime'] = RestartTime
        if EnableViewRoutes is not None:
            properties['EnableViewRoutes'] = EnableViewRoutes
        if Password is not None:
            properties['Password'] = Password
        if EnableBfd is not None:
            properties['EnableBfd'] = EnableBfd

        # call base class function, and it will send message to renix server to create a class.
        super(BgpProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, BgpInitiator=None, AsNumber=None, AsNumberStep=None, Enable4ByteAs=None, AsNumber4Byte=None, AsNumber4ByteStep=None, DutAsNumber=None, DutAsNumberStep=None, Enable4ByteDutAs=None, Dut4ByteAsNumber=None, Dut4ByteAsNumberStep=None, UseGatewayAsDutIp=None, BgpSessionIpAddressType=None, DutIpv4Address=None, DutIpv4AddressStep=None, DutIpv6Address=None, DutIpv6AddressStep=None, HoldTime=None, KeepaliveTime=None, ConnectRetryCount=None, ConnectRetryInterval=None, MaxRoutesPerUpdateMessage=None, RouteRefreshMode=None, EnableGracefulRestart=None, RestartTime=None, EnableViewRoutes=None, Password=None, EnableBfd=None, **kwargs):
        properties = kwargs.copy()
        if BgpInitiator is not None:
            self._BgpInitiator = BgpInitiator
            properties['BgpInitiator'] = BgpInitiator
        if AsNumber is not None:
            self._AsNumber = AsNumber
            properties['AsNumber'] = AsNumber
        if AsNumberStep is not None:
            self._AsNumberStep = AsNumberStep
            properties['AsNumberStep'] = AsNumberStep
        if Enable4ByteAs is not None:
            self._Enable4ByteAs = Enable4ByteAs
            properties['Enable4ByteAs'] = Enable4ByteAs
        if AsNumber4Byte is not None:
            self._AsNumber4Byte = AsNumber4Byte
            properties['AsNumber4Byte'] = AsNumber4Byte
        if AsNumber4ByteStep is not None:
            self._AsNumber4ByteStep = AsNumber4ByteStep
            properties['AsNumber4ByteStep'] = AsNumber4ByteStep
        if DutAsNumber is not None:
            self._DutAsNumber = DutAsNumber
            properties['DutAsNumber'] = DutAsNumber
        if DutAsNumberStep is not None:
            self._DutAsNumberStep = DutAsNumberStep
            properties['DutAsNumberStep'] = DutAsNumberStep
        if Enable4ByteDutAs is not None:
            self._Enable4ByteDutAs = Enable4ByteDutAs
            properties['Enable4ByteDutAs'] = Enable4ByteDutAs
        if Dut4ByteAsNumber is not None:
            self._Dut4ByteAsNumber = Dut4ByteAsNumber
            properties['Dut4ByteAsNumber'] = Dut4ByteAsNumber
        if Dut4ByteAsNumberStep is not None:
            self._Dut4ByteAsNumberStep = Dut4ByteAsNumberStep
            properties['Dut4ByteAsNumberStep'] = Dut4ByteAsNumberStep
        if UseGatewayAsDutIp is not None:
            self._UseGatewayAsDutIp = UseGatewayAsDutIp
            properties['UseGatewayAsDutIp'] = UseGatewayAsDutIp
        if BgpSessionIpAddressType is not None:
            self._BgpSessionIpAddressType = BgpSessionIpAddressType
            properties['BgpSessionIpAddressType'] = BgpSessionIpAddressType
        if DutIpv4Address is not None:
            self._DutIpv4Address = DutIpv4Address
            properties['DutIpv4Address'] = DutIpv4Address
        if DutIpv4AddressStep is not None:
            self._DutIpv4AddressStep = DutIpv4AddressStep
            properties['DutIpv4AddressStep'] = DutIpv4AddressStep
        if DutIpv6Address is not None:
            self._DutIpv6Address = DutIpv6Address
            properties['DutIpv6Address'] = DutIpv6Address
        if DutIpv6AddressStep is not None:
            self._DutIpv6AddressStep = DutIpv6AddressStep
            properties['DutIpv6AddressStep'] = DutIpv6AddressStep
        if HoldTime is not None:
            self._HoldTime = HoldTime
            properties['HoldTime'] = HoldTime
        if KeepaliveTime is not None:
            self._KeepaliveTime = KeepaliveTime
            properties['KeepaliveTime'] = KeepaliveTime
        if ConnectRetryCount is not None:
            self._ConnectRetryCount = ConnectRetryCount
            properties['ConnectRetryCount'] = ConnectRetryCount
        if ConnectRetryInterval is not None:
            self._ConnectRetryInterval = ConnectRetryInterval
            properties['ConnectRetryInterval'] = ConnectRetryInterval
        if MaxRoutesPerUpdateMessage is not None:
            self._MaxRoutesPerUpdateMessage = MaxRoutesPerUpdateMessage
            properties['MaxRoutesPerUpdateMessage'] = MaxRoutesPerUpdateMessage
        if RouteRefreshMode is not None:
            self._RouteRefreshMode = RouteRefreshMode
            properties['RouteRefreshMode'] = RouteRefreshMode
        if EnableGracefulRestart is not None:
            self._EnableGracefulRestart = EnableGracefulRestart
            properties['EnableGracefulRestart'] = EnableGracefulRestart
        if RestartTime is not None:
            self._RestartTime = RestartTime
            properties['RestartTime'] = RestartTime
        if EnableViewRoutes is not None:
            self._EnableViewRoutes = EnableViewRoutes
            properties['EnableViewRoutes'] = EnableViewRoutes
        if Password is not None:
            self._Password = Password
            properties['Password'] = Password
        if EnableBfd is not None:
            self._EnableBfd = EnableBfd
            properties['EnableBfd'] = EnableBfd

        super(BgpProtocolConfig, self).edit(**properties)

    @property
    def BgpProtocolState(self):
        """
        get the value of property _BgpProtocolState
        """
        if self.force_auto_sync:
            self.get('BgpProtocolState')
        return self._BgpProtocolState

    @property
    def IpVersion(self):
        """
        get the value of property _IpVersion
        """
        if self.force_auto_sync:
            self.get('IpVersion')
        return self._IpVersion

    @property
    def BgpInitiator(self):
        """
        get the value of property _BgpInitiator
        """
        if self.force_auto_sync:
            self.get('BgpInitiator')
        return self._BgpInitiator

    @property
    def AsNumber(self):
        """
        get the value of property _AsNumber
        """
        if self.force_auto_sync:
            self.get('AsNumber')
        return self._AsNumber

    @property
    def AsNumberStep(self):
        """
        get the value of property _AsNumberStep
        """
        if self.force_auto_sync:
            self.get('AsNumberStep')
        return self._AsNumberStep

    @property
    def Enable4ByteAs(self):
        """
        get the value of property _Enable4ByteAs
        """
        if self.force_auto_sync:
            self.get('Enable4ByteAs')
        return self._Enable4ByteAs

    @property
    def AsNumber4Byte(self):
        """
        get the value of property _AsNumber4Byte
        """
        if self.force_auto_sync:
            self.get('AsNumber4Byte')
        return self._AsNumber4Byte

    @property
    def AsNumber4ByteStep(self):
        """
        get the value of property _AsNumber4ByteStep
        """
        if self.force_auto_sync:
            self.get('AsNumber4ByteStep')
        return self._AsNumber4ByteStep

    @property
    def DutAsNumber(self):
        """
        get the value of property _DutAsNumber
        """
        if self.force_auto_sync:
            self.get('DutAsNumber')
        return self._DutAsNumber

    @property
    def DutAsNumberStep(self):
        """
        get the value of property _DutAsNumberStep
        """
        if self.force_auto_sync:
            self.get('DutAsNumberStep')
        return self._DutAsNumberStep

    @property
    def Enable4ByteDutAs(self):
        """
        get the value of property _Enable4ByteDutAs
        """
        if self.force_auto_sync:
            self.get('Enable4ByteDutAs')
        return self._Enable4ByteDutAs

    @property
    def Dut4ByteAsNumber(self):
        """
        get the value of property _Dut4ByteAsNumber
        """
        if self.force_auto_sync:
            self.get('Dut4ByteAsNumber')
        return self._Dut4ByteAsNumber

    @property
    def Dut4ByteAsNumberStep(self):
        """
        get the value of property _Dut4ByteAsNumberStep
        """
        if self.force_auto_sync:
            self.get('Dut4ByteAsNumberStep')
        return self._Dut4ByteAsNumberStep

    @property
    def BgpType(self):
        """
        get the value of property _BgpType
        """
        if self.force_auto_sync:
            self.get('BgpType')
        return self._BgpType

    @property
    def UseGatewayAsDutIp(self):
        """
        get the value of property _UseGatewayAsDutIp
        """
        if self.force_auto_sync:
            self.get('UseGatewayAsDutIp')
        return self._UseGatewayAsDutIp

    @property
    def BgpSessionIpAddressType(self):
        """
        get the value of property _BgpSessionIpAddressType
        """
        if self.force_auto_sync:
            self.get('BgpSessionIpAddressType')
        return self._BgpSessionIpAddressType

    @property
    def DutIpv4Address(self):
        """
        get the value of property _DutIpv4Address
        """
        if self.force_auto_sync:
            self.get('DutIpv4Address')
        return self._DutIpv4Address

    @property
    def DutIpv4AddressStep(self):
        """
        get the value of property _DutIpv4AddressStep
        """
        if self.force_auto_sync:
            self.get('DutIpv4AddressStep')
        return self._DutIpv4AddressStep

    @property
    def DutIpv6Address(self):
        """
        get the value of property _DutIpv6Address
        """
        if self.force_auto_sync:
            self.get('DutIpv6Address')
        return self._DutIpv6Address

    @property
    def DutIpv6AddressStep(self):
        """
        get the value of property _DutIpv6AddressStep
        """
        if self.force_auto_sync:
            self.get('DutIpv6AddressStep')
        return self._DutIpv6AddressStep

    @property
    def HoldTime(self):
        """
        get the value of property _HoldTime
        """
        if self.force_auto_sync:
            self.get('HoldTime')
        return self._HoldTime

    @property
    def KeepaliveTime(self):
        """
        get the value of property _KeepaliveTime
        """
        if self.force_auto_sync:
            self.get('KeepaliveTime')
        return self._KeepaliveTime

    @property
    def ConnectRetryCount(self):
        """
        get the value of property _ConnectRetryCount
        """
        if self.force_auto_sync:
            self.get('ConnectRetryCount')
        return self._ConnectRetryCount

    @property
    def ConnectRetryInterval(self):
        """
        get the value of property _ConnectRetryInterval
        """
        if self.force_auto_sync:
            self.get('ConnectRetryInterval')
        return self._ConnectRetryInterval

    @property
    def MaxRoutesPerUpdateMessage(self):
        """
        get the value of property _MaxRoutesPerUpdateMessage
        """
        if self.force_auto_sync:
            self.get('MaxRoutesPerUpdateMessage')
        return self._MaxRoutesPerUpdateMessage

    @property
    def RouteRefreshMode(self):
        """
        get the value of property _RouteRefreshMode
        """
        if self.force_auto_sync:
            self.get('RouteRefreshMode')
        return self._RouteRefreshMode

    @property
    def EnableGracefulRestart(self):
        """
        get the value of property _EnableGracefulRestart
        """
        if self.force_auto_sync:
            self.get('EnableGracefulRestart')
        return self._EnableGracefulRestart

    @property
    def RestartTime(self):
        """
        get the value of property _RestartTime
        """
        if self.force_auto_sync:
            self.get('RestartTime')
        return self._RestartTime

    @property
    def EnableViewRoutes(self):
        """
        get the value of property _EnableViewRoutes
        """
        if self.force_auto_sync:
            self.get('EnableViewRoutes')
        return self._EnableViewRoutes

    @property
    def Authentication(self):
        """
        get the value of property _Authentication
        """
        if self.force_auto_sync:
            self.get('Authentication')
        return self._Authentication

    @property
    def Password(self):
        """
        get the value of property _Password
        """
        if self.force_auto_sync:
            self.get('Password')
        return self._Password

    @property
    def EnableBfd(self):
        """
        get the value of property _EnableBfd
        """
        if self.force_auto_sync:
            self.get('EnableBfd')
        return self._EnableBfd

    @BgpInitiator.setter
    def BgpInitiator(self, value):
        self._BgpInitiator = value
        self.edit(BgpInitiator=value)

    @AsNumber.setter
    def AsNumber(self, value):
        self._AsNumber = value
        self.edit(AsNumber=value)

    @AsNumberStep.setter
    def AsNumberStep(self, value):
        self._AsNumberStep = value
        self.edit(AsNumberStep=value)

    @Enable4ByteAs.setter
    def Enable4ByteAs(self, value):
        self._Enable4ByteAs = value
        self.edit(Enable4ByteAs=value)

    @AsNumber4Byte.setter
    def AsNumber4Byte(self, value):
        self._AsNumber4Byte = value
        self.edit(AsNumber4Byte=value)

    @AsNumber4ByteStep.setter
    def AsNumber4ByteStep(self, value):
        self._AsNumber4ByteStep = value
        self.edit(AsNumber4ByteStep=value)

    @DutAsNumber.setter
    def DutAsNumber(self, value):
        self._DutAsNumber = value
        self.edit(DutAsNumber=value)

    @DutAsNumberStep.setter
    def DutAsNumberStep(self, value):
        self._DutAsNumberStep = value
        self.edit(DutAsNumberStep=value)

    @Enable4ByteDutAs.setter
    def Enable4ByteDutAs(self, value):
        self._Enable4ByteDutAs = value
        self.edit(Enable4ByteDutAs=value)

    @Dut4ByteAsNumber.setter
    def Dut4ByteAsNumber(self, value):
        self._Dut4ByteAsNumber = value
        self.edit(Dut4ByteAsNumber=value)

    @Dut4ByteAsNumberStep.setter
    def Dut4ByteAsNumberStep(self, value):
        self._Dut4ByteAsNumberStep = value
        self.edit(Dut4ByteAsNumberStep=value)

    @UseGatewayAsDutIp.setter
    def UseGatewayAsDutIp(self, value):
        self._UseGatewayAsDutIp = value
        self.edit(UseGatewayAsDutIp=value)

    @BgpSessionIpAddressType.setter
    def BgpSessionIpAddressType(self, value):
        self._BgpSessionIpAddressType = value
        self.edit(BgpSessionIpAddressType=value)

    @DutIpv4Address.setter
    def DutIpv4Address(self, value):
        self._DutIpv4Address = value
        self.edit(DutIpv4Address=value)

    @DutIpv4AddressStep.setter
    def DutIpv4AddressStep(self, value):
        self._DutIpv4AddressStep = value
        self.edit(DutIpv4AddressStep=value)

    @DutIpv6Address.setter
    def DutIpv6Address(self, value):
        self._DutIpv6Address = value
        self.edit(DutIpv6Address=value)

    @DutIpv6AddressStep.setter
    def DutIpv6AddressStep(self, value):
        self._DutIpv6AddressStep = value
        self.edit(DutIpv6AddressStep=value)

    @HoldTime.setter
    def HoldTime(self, value):
        self._HoldTime = value
        self.edit(HoldTime=value)

    @KeepaliveTime.setter
    def KeepaliveTime(self, value):
        self._KeepaliveTime = value
        self.edit(KeepaliveTime=value)

    @ConnectRetryCount.setter
    def ConnectRetryCount(self, value):
        self._ConnectRetryCount = value
        self.edit(ConnectRetryCount=value)

    @ConnectRetryInterval.setter
    def ConnectRetryInterval(self, value):
        self._ConnectRetryInterval = value
        self.edit(ConnectRetryInterval=value)

    @MaxRoutesPerUpdateMessage.setter
    def MaxRoutesPerUpdateMessage(self, value):
        self._MaxRoutesPerUpdateMessage = value
        self.edit(MaxRoutesPerUpdateMessage=value)

    @RouteRefreshMode.setter
    def RouteRefreshMode(self, value):
        self._RouteRefreshMode = value
        self.edit(RouteRefreshMode=value)

    @EnableGracefulRestart.setter
    def EnableGracefulRestart(self, value):
        self._EnableGracefulRestart = value
        self.edit(EnableGracefulRestart=value)

    @RestartTime.setter
    def RestartTime(self, value):
        self._RestartTime = value
        self.edit(RestartTime=value)

    @EnableViewRoutes.setter
    def EnableViewRoutes(self, value):
        self._EnableViewRoutes = value
        self.edit(EnableViewRoutes=value)

    @Password.setter
    def Password(self, value):
        self._Password = value
        self.edit(Password=value)

    @EnableBfd.setter
    def EnableBfd(self, value):
        self._EnableBfd = value
        self.edit(EnableBfd=value)

    def _set_bgpprotocolstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._BgpProtocolState = EnumBgpProtocolState.%s' % value[:seperate])

    def _set_ipversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._IpVersion = EnumBgpIpVersion.%s' % value[:seperate])

    def _set_bgpinitiator_with_str(self, value):
        self._BgpInitiator = (value == 'True')

    def _set_asnumber_with_str(self, value):
        try:
            self._AsNumber = int(value)
        except ValueError:
            self._AsNumber = hex(int(value, 16))

    def _set_asnumberstep_with_str(self, value):
        try:
            self._AsNumberStep = int(value)
        except ValueError:
            self._AsNumberStep = hex(int(value, 16))

    def _set_enable4byteas_with_str(self, value):
        self._Enable4ByteAs = (value == 'True')

    def _set_asnumber4byte_with_str(self, value):
        self._AsNumber4Byte = value

    def _set_asnumber4bytestep_with_str(self, value):
        self._AsNumber4ByteStep = value

    def _set_dutasnumber_with_str(self, value):
        try:
            self._DutAsNumber = int(value)
        except ValueError:
            self._DutAsNumber = hex(int(value, 16))

    def _set_dutasnumberstep_with_str(self, value):
        try:
            self._DutAsNumberStep = int(value)
        except ValueError:
            self._DutAsNumberStep = hex(int(value, 16))

    def _set_enable4bytedutas_with_str(self, value):
        self._Enable4ByteDutAs = (value == 'True')

    def _set_dut4byteasnumber_with_str(self, value):
        self._Dut4ByteAsNumber = value

    def _set_dut4byteasnumberstep_with_str(self, value):
        self._Dut4ByteAsNumberStep = value

    def _set_bgptype_with_str(self, value):
        seperate = value.find(':')
        exec('self._BgpType = EnumBgpType.%s' % value[:seperate])

    def _set_usegatewayasdutip_with_str(self, value):
        self._UseGatewayAsDutIp = (value == 'True')

    def _set_bgpsessionipaddresstype_with_str(self, value):
        seperate = value.find(':')
        exec('self._BgpSessionIpAddressType = EnumBgpSessionIpAddress.%s' % value[:seperate])

    def _set_dutipv4address_with_str(self, value):
        self._DutIpv4Address = value

    def _set_dutipv4addressstep_with_str(self, value):
        self._DutIpv4AddressStep = value

    def _set_dutipv6address_with_str(self, value):
        self._DutIpv6Address = value

    def _set_dutipv6addressstep_with_str(self, value):
        self._DutIpv6AddressStep = value

    def _set_holdtime_with_str(self, value):
        try:
            self._HoldTime = int(value)
        except ValueError:
            self._HoldTime = hex(int(value, 16))

    def _set_keepalivetime_with_str(self, value):
        try:
            self._KeepaliveTime = int(value)
        except ValueError:
            self._KeepaliveTime = hex(int(value, 16))

    def _set_connectretrycount_with_str(self, value):
        try:
            self._ConnectRetryCount = int(value)
        except ValueError:
            self._ConnectRetryCount = hex(int(value, 16))

    def _set_connectretryinterval_with_str(self, value):
        try:
            self._ConnectRetryInterval = int(value)
        except ValueError:
            self._ConnectRetryInterval = hex(int(value, 16))

    def _set_maxroutesperupdatemessage_with_str(self, value):
        try:
            self._MaxRoutesPerUpdateMessage = int(value)
        except ValueError:
            self._MaxRoutesPerUpdateMessage = hex(int(value, 16))

    def _set_routerefreshmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._RouteRefreshMode = EnumBgpRouteRefreshMode.%s' % value[:seperate])

    def _set_enablegracefulrestart_with_str(self, value):
        self._EnableGracefulRestart = (value == 'True')

    def _set_restarttime_with_str(self, value):
        try:
            self._RestartTime = int(value)
        except ValueError:
            self._RestartTime = hex(int(value, 16))

    def _set_enableviewroutes_with_str(self, value):
        self._EnableViewRoutes = (value == 'True')

    def _set_authentication_with_str(self, value):
        seperate = value.find(':')
        exec('self._Authentication = EnumBgpAuthentication.%s' % value[:seperate])

    def _set_password_with_str(self, value):
        self._Password = value

    def _set_enablebfd_with_str(self, value):
        self._EnableBfd = (value == 'True')

