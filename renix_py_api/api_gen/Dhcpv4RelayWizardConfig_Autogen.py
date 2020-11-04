"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ProtocolWizardConfig_Autogen import ProtocolWizardConfig


@rom_manager.rom
class Dhcpv4RelayWizardConfig(ProtocolWizardConfig):
    def __init__(self, HostName=None, EnableRouterOption=None, SubnetMask=None, RoutersOption=None, DoMainServerOption=None, DomainOption=None, StaticRoutesOption=None, IpLeaseOption=None, ServerIdOption=None, T1Option=None, T2Option=None, VendorClassIdentifier=None, BroadcastFlag=None, ClientCountsPerBlock=None, RelayCounts=None, ClientCounts=None, EthernetAddr=None, EthernetStep=None, EnableGateway=None, StartServerIp=None, ServerIpStep=None, RelayAgentIp=None, RelayAgentIpStep=None, **kwargs):
        self._HostName = HostName  # Host Name
        self._EnableRouterOption = EnableRouterOption  # Enable Router Option
        self._SubnetMask = SubnetMask  # Subnet Mask Option [1]
        self._RoutersOption = RoutersOption  # Routers Option [3]
        self._DoMainServerOption = DoMainServerOption  # Domain Name Server Option [6]
        self._DomainOption = DomainOption  # Domain Name Option [15]
        self._StaticRoutesOption = StaticRoutesOption  # Static Routes Option [33]
        self._IpLeaseOption = IpLeaseOption  # IP Address Lease Time Option [51]
        self._ServerIdOption = ServerIdOption  # Server Identifier Option [54]
        self._T1Option = T1Option  # Renewal Time (T1) Option [58]
        self._T2Option = T2Option  # Rebinding Time (T2) Option [59]
        self._VendorClassIdentifier = VendorClassIdentifier  # Vendor Class Identifier [60]
        self._BroadcastFlag = BroadcastFlag  # Broadcast Flag
        self._ClientCountsPerBlock = ClientCountsPerBlock  # Client Counts Per Block
        self._RelayCounts = RelayCounts  # Relay Counts
        self._ClientCounts = ClientCounts  # Client Counts
        self._EthernetAddr = EthernetAddr  # Client MAC Address
        self._EthernetStep = EthernetStep  # Client MAC Address Step
        self._EnableGateway = EnableGateway  # Use Ipv4 Gateway As Server Ip
        self._StartServerIp = StartServerIp  # Server IPv4 Address
        self._ServerIpStep = ServerIpStep  # Server IPv4 Address Step
        self._RelayAgentIp = RelayAgentIp  # Relay Agent IPv4 Address
        self._RelayAgentIpStep = RelayAgentIpStep  # Relay Agent IPv4 Address Step

        properties = kwargs.copy()
        if HostName is not None:
            properties['HostName'] = HostName
        if EnableRouterOption is not None:
            properties['EnableRouterOption'] = EnableRouterOption
        if SubnetMask is not None:
            properties['SubnetMask'] = SubnetMask
        if RoutersOption is not None:
            properties['RoutersOption'] = RoutersOption
        if DoMainServerOption is not None:
            properties['DoMainServerOption'] = DoMainServerOption
        if DomainOption is not None:
            properties['DomainOption'] = DomainOption
        if StaticRoutesOption is not None:
            properties['StaticRoutesOption'] = StaticRoutesOption
        if IpLeaseOption is not None:
            properties['IpLeaseOption'] = IpLeaseOption
        if ServerIdOption is not None:
            properties['ServerIdOption'] = ServerIdOption
        if T1Option is not None:
            properties['T1Option'] = T1Option
        if T2Option is not None:
            properties['T2Option'] = T2Option
        if VendorClassIdentifier is not None:
            properties['VendorClassIdentifier'] = VendorClassIdentifier
        if BroadcastFlag is not None:
            properties['BroadcastFlag'] = BroadcastFlag
        if ClientCountsPerBlock is not None:
            properties['ClientCountsPerBlock'] = ClientCountsPerBlock
        if RelayCounts is not None:
            properties['RelayCounts'] = RelayCounts
        if ClientCounts is not None:
            properties['ClientCounts'] = ClientCounts
        if EthernetAddr is not None:
            properties['EthernetAddr'] = EthernetAddr
        if EthernetStep is not None:
            properties['EthernetStep'] = EthernetStep
        if EnableGateway is not None:
            properties['EnableGateway'] = EnableGateway
        if StartServerIp is not None:
            properties['StartServerIp'] = StartServerIp
        if ServerIpStep is not None:
            properties['ServerIpStep'] = ServerIpStep
        if RelayAgentIp is not None:
            properties['RelayAgentIp'] = RelayAgentIp
        if RelayAgentIpStep is not None:
            properties['RelayAgentIpStep'] = RelayAgentIpStep

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4RelayWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, HostName=None, EnableRouterOption=None, SubnetMask=None, RoutersOption=None, DoMainServerOption=None, DomainOption=None, StaticRoutesOption=None, IpLeaseOption=None, ServerIdOption=None, T1Option=None, T2Option=None, VendorClassIdentifier=None, BroadcastFlag=None, ClientCountsPerBlock=None, RelayCounts=None, ClientCounts=None, EthernetAddr=None, EthernetStep=None, EnableGateway=None, StartServerIp=None, ServerIpStep=None, RelayAgentIp=None, RelayAgentIpStep=None, **kwargs):
        properties = kwargs.copy()
        if HostName is not None:
            self._HostName = HostName
            properties['HostName'] = HostName
        if EnableRouterOption is not None:
            self._EnableRouterOption = EnableRouterOption
            properties['EnableRouterOption'] = EnableRouterOption
        if SubnetMask is not None:
            self._SubnetMask = SubnetMask
            properties['SubnetMask'] = SubnetMask
        if RoutersOption is not None:
            self._RoutersOption = RoutersOption
            properties['RoutersOption'] = RoutersOption
        if DoMainServerOption is not None:
            self._DoMainServerOption = DoMainServerOption
            properties['DoMainServerOption'] = DoMainServerOption
        if DomainOption is not None:
            self._DomainOption = DomainOption
            properties['DomainOption'] = DomainOption
        if StaticRoutesOption is not None:
            self._StaticRoutesOption = StaticRoutesOption
            properties['StaticRoutesOption'] = StaticRoutesOption
        if IpLeaseOption is not None:
            self._IpLeaseOption = IpLeaseOption
            properties['IpLeaseOption'] = IpLeaseOption
        if ServerIdOption is not None:
            self._ServerIdOption = ServerIdOption
            properties['ServerIdOption'] = ServerIdOption
        if T1Option is not None:
            self._T1Option = T1Option
            properties['T1Option'] = T1Option
        if T2Option is not None:
            self._T2Option = T2Option
            properties['T2Option'] = T2Option
        if VendorClassIdentifier is not None:
            self._VendorClassIdentifier = VendorClassIdentifier
            properties['VendorClassIdentifier'] = VendorClassIdentifier
        if BroadcastFlag is not None:
            self._BroadcastFlag = BroadcastFlag
            properties['BroadcastFlag'] = BroadcastFlag
        if ClientCountsPerBlock is not None:
            self._ClientCountsPerBlock = ClientCountsPerBlock
            properties['ClientCountsPerBlock'] = ClientCountsPerBlock
        if RelayCounts is not None:
            self._RelayCounts = RelayCounts
            properties['RelayCounts'] = RelayCounts
        if ClientCounts is not None:
            self._ClientCounts = ClientCounts
            properties['ClientCounts'] = ClientCounts
        if EthernetAddr is not None:
            self._EthernetAddr = EthernetAddr
            properties['EthernetAddr'] = EthernetAddr
        if EthernetStep is not None:
            self._EthernetStep = EthernetStep
            properties['EthernetStep'] = EthernetStep
        if EnableGateway is not None:
            self._EnableGateway = EnableGateway
            properties['EnableGateway'] = EnableGateway
        if StartServerIp is not None:
            self._StartServerIp = StartServerIp
            properties['StartServerIp'] = StartServerIp
        if ServerIpStep is not None:
            self._ServerIpStep = ServerIpStep
            properties['ServerIpStep'] = ServerIpStep
        if RelayAgentIp is not None:
            self._RelayAgentIp = RelayAgentIp
            properties['RelayAgentIp'] = RelayAgentIp
        if RelayAgentIpStep is not None:
            self._RelayAgentIpStep = RelayAgentIpStep
            properties['RelayAgentIpStep'] = RelayAgentIpStep

        super(Dhcpv4RelayWizardConfig, self).edit(**properties)

    @property
    def HostName(self):
        """
        get the value of property _HostName
        """
        if self.force_auto_sync:
            self.get('HostName')
        return self._HostName

    @property
    def EnableRouterOption(self):
        """
        get the value of property _EnableRouterOption
        """
        if self.force_auto_sync:
            self.get('EnableRouterOption')
        return self._EnableRouterOption

    @property
    def SubnetMask(self):
        """
        get the value of property _SubnetMask
        """
        if self.force_auto_sync:
            self.get('SubnetMask')
        return self._SubnetMask

    @property
    def RoutersOption(self):
        """
        get the value of property _RoutersOption
        """
        if self.force_auto_sync:
            self.get('RoutersOption')
        return self._RoutersOption

    @property
    def DoMainServerOption(self):
        """
        get the value of property _DoMainServerOption
        """
        if self.force_auto_sync:
            self.get('DoMainServerOption')
        return self._DoMainServerOption

    @property
    def DomainOption(self):
        """
        get the value of property _DomainOption
        """
        if self.force_auto_sync:
            self.get('DomainOption')
        return self._DomainOption

    @property
    def StaticRoutesOption(self):
        """
        get the value of property _StaticRoutesOption
        """
        if self.force_auto_sync:
            self.get('StaticRoutesOption')
        return self._StaticRoutesOption

    @property
    def IpLeaseOption(self):
        """
        get the value of property _IpLeaseOption
        """
        if self.force_auto_sync:
            self.get('IpLeaseOption')
        return self._IpLeaseOption

    @property
    def ServerIdOption(self):
        """
        get the value of property _ServerIdOption
        """
        if self.force_auto_sync:
            self.get('ServerIdOption')
        return self._ServerIdOption

    @property
    def T1Option(self):
        """
        get the value of property _T1Option
        """
        if self.force_auto_sync:
            self.get('T1Option')
        return self._T1Option

    @property
    def T2Option(self):
        """
        get the value of property _T2Option
        """
        if self.force_auto_sync:
            self.get('T2Option')
        return self._T2Option

    @property
    def VendorClassIdentifier(self):
        """
        get the value of property _VendorClassIdentifier
        """
        if self.force_auto_sync:
            self.get('VendorClassIdentifier')
        return self._VendorClassIdentifier

    @property
    def BroadcastFlag(self):
        """
        get the value of property _BroadcastFlag
        """
        if self.force_auto_sync:
            self.get('BroadcastFlag')
        return self._BroadcastFlag

    @property
    def ClientCountsPerBlock(self):
        """
        get the value of property _ClientCountsPerBlock
        """
        if self.force_auto_sync:
            self.get('ClientCountsPerBlock')
        return self._ClientCountsPerBlock

    @property
    def RelayCounts(self):
        """
        get the value of property _RelayCounts
        """
        if self.force_auto_sync:
            self.get('RelayCounts')
        return self._RelayCounts

    @property
    def ClientCounts(self):
        """
        get the value of property _ClientCounts
        """
        if self.force_auto_sync:
            self.get('ClientCounts')
        return self._ClientCounts

    @property
    def EthernetAddr(self):
        """
        get the value of property _EthernetAddr
        """
        if self.force_auto_sync:
            self.get('EthernetAddr')
        return self._EthernetAddr

    @property
    def EthernetStep(self):
        """
        get the value of property _EthernetStep
        """
        if self.force_auto_sync:
            self.get('EthernetStep')
        return self._EthernetStep

    @property
    def EnableGateway(self):
        """
        get the value of property _EnableGateway
        """
        if self.force_auto_sync:
            self.get('EnableGateway')
        return self._EnableGateway

    @property
    def StartServerIp(self):
        """
        get the value of property _StartServerIp
        """
        if self.force_auto_sync:
            self.get('StartServerIp')
        return self._StartServerIp

    @property
    def ServerIpStep(self):
        """
        get the value of property _ServerIpStep
        """
        if self.force_auto_sync:
            self.get('ServerIpStep')
        return self._ServerIpStep

    @property
    def RelayAgentIp(self):
        """
        get the value of property _RelayAgentIp
        """
        if self.force_auto_sync:
            self.get('RelayAgentIp')
        return self._RelayAgentIp

    @property
    def RelayAgentIpStep(self):
        """
        get the value of property _RelayAgentIpStep
        """
        if self.force_auto_sync:
            self.get('RelayAgentIpStep')
        return self._RelayAgentIpStep

    @HostName.setter
    def HostName(self, value):
        self._HostName = value
        self.edit(HostName=value)

    @EnableRouterOption.setter
    def EnableRouterOption(self, value):
        self._EnableRouterOption = value
        self.edit(EnableRouterOption=value)

    @SubnetMask.setter
    def SubnetMask(self, value):
        self._SubnetMask = value
        self.edit(SubnetMask=value)

    @RoutersOption.setter
    def RoutersOption(self, value):
        self._RoutersOption = value
        self.edit(RoutersOption=value)

    @DoMainServerOption.setter
    def DoMainServerOption(self, value):
        self._DoMainServerOption = value
        self.edit(DoMainServerOption=value)

    @DomainOption.setter
    def DomainOption(self, value):
        self._DomainOption = value
        self.edit(DomainOption=value)

    @StaticRoutesOption.setter
    def StaticRoutesOption(self, value):
        self._StaticRoutesOption = value
        self.edit(StaticRoutesOption=value)

    @IpLeaseOption.setter
    def IpLeaseOption(self, value):
        self._IpLeaseOption = value
        self.edit(IpLeaseOption=value)

    @ServerIdOption.setter
    def ServerIdOption(self, value):
        self._ServerIdOption = value
        self.edit(ServerIdOption=value)

    @T1Option.setter
    def T1Option(self, value):
        self._T1Option = value
        self.edit(T1Option=value)

    @T2Option.setter
    def T2Option(self, value):
        self._T2Option = value
        self.edit(T2Option=value)

    @VendorClassIdentifier.setter
    def VendorClassIdentifier(self, value):
        self._VendorClassIdentifier = value
        self.edit(VendorClassIdentifier=value)

    @BroadcastFlag.setter
    def BroadcastFlag(self, value):
        self._BroadcastFlag = value
        self.edit(BroadcastFlag=value)

    @ClientCountsPerBlock.setter
    def ClientCountsPerBlock(self, value):
        self._ClientCountsPerBlock = value
        self.edit(ClientCountsPerBlock=value)

    @RelayCounts.setter
    def RelayCounts(self, value):
        self._RelayCounts = value
        self.edit(RelayCounts=value)

    @ClientCounts.setter
    def ClientCounts(self, value):
        self._ClientCounts = value
        self.edit(ClientCounts=value)

    @EthernetAddr.setter
    def EthernetAddr(self, value):
        self._EthernetAddr = value
        self.edit(EthernetAddr=value)

    @EthernetStep.setter
    def EthernetStep(self, value):
        self._EthernetStep = value
        self.edit(EthernetStep=value)

    @EnableGateway.setter
    def EnableGateway(self, value):
        self._EnableGateway = value
        self.edit(EnableGateway=value)

    @StartServerIp.setter
    def StartServerIp(self, value):
        self._StartServerIp = value
        self.edit(StartServerIp=value)

    @ServerIpStep.setter
    def ServerIpStep(self, value):
        self._ServerIpStep = value
        self.edit(ServerIpStep=value)

    @RelayAgentIp.setter
    def RelayAgentIp(self, value):
        self._RelayAgentIp = value
        self.edit(RelayAgentIp=value)

    @RelayAgentIpStep.setter
    def RelayAgentIpStep(self, value):
        self._RelayAgentIpStep = value
        self.edit(RelayAgentIpStep=value)

    def _set_hostname_with_str(self, value):
        self._HostName = value

    def _set_enablerouteroption_with_str(self, value):
        self._EnableRouterOption = (value == 'True')

    def _set_subnetmask_with_str(self, value):
        self._SubnetMask = (value == 'True')

    def _set_routersoption_with_str(self, value):
        self._RoutersOption = (value == 'True')

    def _set_domainserveroption_with_str(self, value):
        self._DoMainServerOption = (value == 'True')

    def _set_domainoption_with_str(self, value):
        self._DomainOption = (value == 'True')

    def _set_staticroutesoption_with_str(self, value):
        self._StaticRoutesOption = (value == 'True')

    def _set_ipleaseoption_with_str(self, value):
        self._IpLeaseOption = (value == 'True')

    def _set_serveridoption_with_str(self, value):
        self._ServerIdOption = (value == 'True')

    def _set_t1option_with_str(self, value):
        self._T1Option = (value == 'True')

    def _set_t2option_with_str(self, value):
        self._T2Option = (value == 'True')

    def _set_vendorclassidentifier_with_str(self, value):
        self._VendorClassIdentifier = value

    def _set_broadcastflag_with_str(self, value):
        seperate = value.find(':')
        exec('self._BroadcastFlag = EnumDhcpv4BroadcastType.%s' % value[:seperate])

    def _set_clientcountsperblock_with_str(self, value):
        try:
            self._ClientCountsPerBlock = int(value)
        except ValueError:
            self._ClientCountsPerBlock = hex(int(value, 16))

    def _set_relaycounts_with_str(self, value):
        try:
            self._RelayCounts = int(value)
        except ValueError:
            self._RelayCounts = hex(int(value, 16))

    def _set_clientcounts_with_str(self, value):
        try:
            self._ClientCounts = int(value)
        except ValueError:
            self._ClientCounts = hex(int(value, 16))

    def _set_ethernetaddr_with_str(self, value):
        self._EthernetAddr = value

    def _set_ethernetstep_with_str(self, value):
        self._EthernetStep = value

    def _set_enablegateway_with_str(self, value):
        self._EnableGateway = (value == 'True')

    def _set_startserverip_with_str(self, value):
        self._StartServerIp = value

    def _set_serveripstep_with_str(self, value):
        self._ServerIpStep = value

    def _set_relayagentip_with_str(self, value):
        self._RelayAgentIp = value

    def _set_relayagentipstep_with_str(self, value):
        self._RelayAgentIpStep = value

