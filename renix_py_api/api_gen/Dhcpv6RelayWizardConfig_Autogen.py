"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ProtocolWizardConfig_Autogen import ProtocolWizardConfig


@rom_manager.rom
class Dhcpv6RelayWizardConfig(ProtocolWizardConfig):
    def __init__(self, EmulationMode=None, PreferredLifetime=None, ValidLifetime=None, T1Timer=None, T2Timer=None, EnableRenewMsg=None, EnableRebindMsg=None, RapidCommitOptMode=None, DuidType=None, DuidCustomValue=None, DuidEnterpriseNumber=None, DuidStartValue=None, DuidStepValue=None, EthernetAddr=None, EthernetStep=None, PrefixLength=None, ClientCountsPerBlock=None, RelayCounts=None, ClientCounts=None, EnableGateway=None, StartServerIp=None, ServerIpStep=None, RelayAgentIp=None, RelayAgentIpStep=None, **kwargs):
        self._EmulationMode = EmulationMode  # Emulation Mode
        self._PreferredLifetime = PreferredLifetime  # Preferred Lifetime (secs)
        self._ValidLifetime = ValidLifetime  # Valid Lifetime (secs)
        self._T1Timer = T1Timer  # T1 Timer(secs)
        self._T2Timer = T2Timer  # T2 Timer(secs)
        self._EnableRenewMsg = EnableRenewMsg  # Enable Renew Messages
        self._EnableRebindMsg = EnableRebindMsg  # Enable Rebind Messages
        self._RapidCommitOptMode = RapidCommitOptMode  # Rapid Commit Operation Mode
        self._DuidType = DuidType  # DUID Type
        self._DuidCustomValue = DuidCustomValue  # Custom DUID Value
        self._DuidEnterpriseNumber = DuidEnterpriseNumber  # DUID Enterprise Number
        self._DuidStartValue = DuidStartValue  # Starting DUID Value
        self._DuidStepValue = DuidStepValue  # DUID Step Value
        self._EthernetAddr = EthernetAddr  # Client MAC Address
        self._EthernetStep = EthernetStep  # Client MAC Address Step
        self._PrefixLength = PrefixLength  # IPv6 Prefix Length
        self._ClientCountsPerBlock = ClientCountsPerBlock  # Client Counts Per Block
        self._RelayCounts = RelayCounts  # Relay Counts
        self._ClientCounts = ClientCounts  # Client Counts
        self._EnableGateway = EnableGateway  # Enable Gateway As Server Ip
        self._StartServerIp = StartServerIp  # IPv6 Address
        self._ServerIpStep = ServerIpStep  # IPv6 Address Step
        self._RelayAgentIp = RelayAgentIp  # IPv6 Address
        self._RelayAgentIpStep = RelayAgentIpStep  # IPv6 Address Step

        properties = kwargs.copy()
        if EmulationMode is not None:
            properties['EmulationMode'] = EmulationMode
        if PreferredLifetime is not None:
            properties['PreferredLifetime'] = PreferredLifetime
        if ValidLifetime is not None:
            properties['ValidLifetime'] = ValidLifetime
        if T1Timer is not None:
            properties['T1Timer'] = T1Timer
        if T2Timer is not None:
            properties['T2Timer'] = T2Timer
        if EnableRenewMsg is not None:
            properties['EnableRenewMsg'] = EnableRenewMsg
        if EnableRebindMsg is not None:
            properties['EnableRebindMsg'] = EnableRebindMsg
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
        if EthernetAddr is not None:
            properties['EthernetAddr'] = EthernetAddr
        if EthernetStep is not None:
            properties['EthernetStep'] = EthernetStep
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if ClientCountsPerBlock is not None:
            properties['ClientCountsPerBlock'] = ClientCountsPerBlock
        if RelayCounts is not None:
            properties['RelayCounts'] = RelayCounts
        if ClientCounts is not None:
            properties['ClientCounts'] = ClientCounts
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
        super(Dhcpv6RelayWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EmulationMode=None, PreferredLifetime=None, ValidLifetime=None, T1Timer=None, T2Timer=None, EnableRenewMsg=None, EnableRebindMsg=None, RapidCommitOptMode=None, DuidType=None, DuidCustomValue=None, DuidEnterpriseNumber=None, DuidStartValue=None, DuidStepValue=None, EthernetAddr=None, EthernetStep=None, PrefixLength=None, ClientCountsPerBlock=None, RelayCounts=None, ClientCounts=None, EnableGateway=None, StartServerIp=None, ServerIpStep=None, RelayAgentIp=None, RelayAgentIpStep=None, **kwargs):
        properties = kwargs.copy()
        if EmulationMode is not None:
            self._EmulationMode = EmulationMode
            properties['EmulationMode'] = EmulationMode
        if PreferredLifetime is not None:
            self._PreferredLifetime = PreferredLifetime
            properties['PreferredLifetime'] = PreferredLifetime
        if ValidLifetime is not None:
            self._ValidLifetime = ValidLifetime
            properties['ValidLifetime'] = ValidLifetime
        if T1Timer is not None:
            self._T1Timer = T1Timer
            properties['T1Timer'] = T1Timer
        if T2Timer is not None:
            self._T2Timer = T2Timer
            properties['T2Timer'] = T2Timer
        if EnableRenewMsg is not None:
            self._EnableRenewMsg = EnableRenewMsg
            properties['EnableRenewMsg'] = EnableRenewMsg
        if EnableRebindMsg is not None:
            self._EnableRebindMsg = EnableRebindMsg
            properties['EnableRebindMsg'] = EnableRebindMsg
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
        if EthernetAddr is not None:
            self._EthernetAddr = EthernetAddr
            properties['EthernetAddr'] = EthernetAddr
        if EthernetStep is not None:
            self._EthernetStep = EthernetStep
            properties['EthernetStep'] = EthernetStep
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if ClientCountsPerBlock is not None:
            self._ClientCountsPerBlock = ClientCountsPerBlock
            properties['ClientCountsPerBlock'] = ClientCountsPerBlock
        if RelayCounts is not None:
            self._RelayCounts = RelayCounts
            properties['RelayCounts'] = RelayCounts
        if ClientCounts is not None:
            self._ClientCounts = ClientCounts
            properties['ClientCounts'] = ClientCounts
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

        super(Dhcpv6RelayWizardConfig, self).edit(**properties)

    @property
    def EmulationMode(self):
        """
        get the value of property _EmulationMode
        """
        if self.force_auto_sync:
            self.get('EmulationMode')
        return self._EmulationMode

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
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

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

    @EmulationMode.setter
    def EmulationMode(self, value):
        self._EmulationMode = value
        self.edit(EmulationMode=value)

    @PreferredLifetime.setter
    def PreferredLifetime(self, value):
        self._PreferredLifetime = value
        self.edit(PreferredLifetime=value)

    @ValidLifetime.setter
    def ValidLifetime(self, value):
        self._ValidLifetime = value
        self.edit(ValidLifetime=value)

    @T1Timer.setter
    def T1Timer(self, value):
        self._T1Timer = value
        self.edit(T1Timer=value)

    @T2Timer.setter
    def T2Timer(self, value):
        self._T2Timer = value
        self.edit(T2Timer=value)

    @EnableRenewMsg.setter
    def EnableRenewMsg(self, value):
        self._EnableRenewMsg = value
        self.edit(EnableRenewMsg=value)

    @EnableRebindMsg.setter
    def EnableRebindMsg(self, value):
        self._EnableRebindMsg = value
        self.edit(EnableRebindMsg=value)

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

    @EthernetAddr.setter
    def EthernetAddr(self, value):
        self._EthernetAddr = value
        self.edit(EthernetAddr=value)

    @EthernetStep.setter
    def EthernetStep(self, value):
        self._EthernetStep = value
        self.edit(EthernetStep=value)

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

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

    def _set_emulationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._EmulationMode = EnumDhcpv6EmulationMode.%s' % value[:seperate])

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

    def _set_enablerenewmsg_with_str(self, value):
        self._EnableRenewMsg = (value == 'True')

    def _set_enablerebindmsg_with_str(self, value):
        self._EnableRebindMsg = (value == 'True')

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

    def _set_ethernetaddr_with_str(self, value):
        self._EthernetAddr = value

    def _set_ethernetstep_with_str(self, value):
        self._EthernetStep = value

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

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

