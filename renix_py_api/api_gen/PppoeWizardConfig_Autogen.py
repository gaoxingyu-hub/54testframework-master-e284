"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ProtocolWizardConfig_Autogen import ProtocolWizardConfig


@rom_manager.rom
class PppoeWizardConfig(ProtocolWizardConfig):
    def __init__(self, EmulationMode=None, IpVersion=None, AuthenticationType=None, Username=None, Password=None, ServiceName=None, AcName=None, EnableMaxPayloadTag=None, MaxPayloadBytes=None, PadiTimeout=None, PadiMaxAttempts=None, PadrTimeout=None, PadrMaxAttempts=None, EnableAutoRetry=None, AutoRetryCount=None, EnableEchoRequest=None, EchoRequestInterval=None, EchoRequestMaxAttempts=None, Ipv4Start=None, Ipv4Step=None, Ipv4Count=None, Ipv6InterfaceId=None, Ipv6InterfaceIdStep=None, Ipv6PrefixStart=None, Ipv6PrefixStep=None, Ipv6Count=None, **kwargs):
        self._EmulationMode = EmulationMode  # Emulation Mode
        self._IpVersion = IpVersion  # IPCP encapsulation
        self._AuthenticationType = AuthenticationType  # Authentication
        self._Username = Username  # Username
        self._Password = Password  # Password
        self._ServiceName = ServiceName  # Service Name
        self._AcName = AcName  # AC-Name
        self._EnableMaxPayloadTag = EnableMaxPayloadTag  # Enable Max Payload Tag
        self._MaxPayloadBytes = MaxPayloadBytes  # Max Payload Bytes
        self._PadiTimeout = PadiTimeout  # PADI Timeout (sec)
        self._PadiMaxAttempts = PadiMaxAttempts  # PADI Max Attempts
        self._PadrTimeout = PadrTimeout  # PADR Timeout (sec)
        self._PadrMaxAttempts = PadrMaxAttempts  # PADR Max Attempts
        self._EnableAutoRetry = EnableAutoRetry  # Enable Auto Retry
        self._AutoRetryCount = AutoRetryCount  # Auto Retry Count
        self._EnableEchoRequest = EnableEchoRequest  # Enable Echo-Request
        self._EchoRequestInterval = EchoRequestInterval  # Echo-Request Interval(sec)
        self._EchoRequestMaxAttempts = EchoRequestMaxAttempts  # Echo-Request Max Attempts
        self._Ipv4Start = Ipv4Start  # IPv4 Address Start
        self._Ipv4Step = Ipv4Step  # IPv4 Address Step
        self._Ipv4Count = Ipv4Count  # IPv4 Address Count
        self._Ipv6InterfaceId = Ipv6InterfaceId  # IPv6 Interface ID
        self._Ipv6InterfaceIdStep = Ipv6InterfaceIdStep  # IPv6 Interface ID Step
        self._Ipv6PrefixStart = Ipv6PrefixStart  # IPv6 Prefix Start
        self._Ipv6PrefixStep = Ipv6PrefixStep  # IPv6 Prefix Step
        self._Ipv6Count = Ipv6Count  # IPv6 Address Count

        properties = kwargs.copy()
        if EmulationMode is not None:
            properties['EmulationMode'] = EmulationMode
        if IpVersion is not None:
            properties['IpVersion'] = IpVersion
        if AuthenticationType is not None:
            properties['AuthenticationType'] = AuthenticationType
        if Username is not None:
            properties['Username'] = Username
        if Password is not None:
            properties['Password'] = Password
        if ServiceName is not None:
            properties['ServiceName'] = ServiceName
        if AcName is not None:
            properties['AcName'] = AcName
        if EnableMaxPayloadTag is not None:
            properties['EnableMaxPayloadTag'] = EnableMaxPayloadTag
        if MaxPayloadBytes is not None:
            properties['MaxPayloadBytes'] = MaxPayloadBytes
        if PadiTimeout is not None:
            properties['PadiTimeout'] = PadiTimeout
        if PadiMaxAttempts is not None:
            properties['PadiMaxAttempts'] = PadiMaxAttempts
        if PadrTimeout is not None:
            properties['PadrTimeout'] = PadrTimeout
        if PadrMaxAttempts is not None:
            properties['PadrMaxAttempts'] = PadrMaxAttempts
        if EnableAutoRetry is not None:
            properties['EnableAutoRetry'] = EnableAutoRetry
        if AutoRetryCount is not None:
            properties['AutoRetryCount'] = AutoRetryCount
        if EnableEchoRequest is not None:
            properties['EnableEchoRequest'] = EnableEchoRequest
        if EchoRequestInterval is not None:
            properties['EchoRequestInterval'] = EchoRequestInterval
        if EchoRequestMaxAttempts is not None:
            properties['EchoRequestMaxAttempts'] = EchoRequestMaxAttempts
        if Ipv4Start is not None:
            properties['Ipv4Start'] = Ipv4Start
        if Ipv4Step is not None:
            properties['Ipv4Step'] = Ipv4Step
        if Ipv4Count is not None:
            properties['Ipv4Count'] = Ipv4Count
        if Ipv6InterfaceId is not None:
            properties['Ipv6InterfaceId'] = Ipv6InterfaceId
        if Ipv6InterfaceIdStep is not None:
            properties['Ipv6InterfaceIdStep'] = Ipv6InterfaceIdStep
        if Ipv6PrefixStart is not None:
            properties['Ipv6PrefixStart'] = Ipv6PrefixStart
        if Ipv6PrefixStep is not None:
            properties['Ipv6PrefixStep'] = Ipv6PrefixStep
        if Ipv6Count is not None:
            properties['Ipv6Count'] = Ipv6Count

        # call base class function, and it will send message to renix server to create a class.
        super(PppoeWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EmulationMode=None, IpVersion=None, AuthenticationType=None, Username=None, Password=None, ServiceName=None, AcName=None, EnableMaxPayloadTag=None, MaxPayloadBytes=None, PadiTimeout=None, PadiMaxAttempts=None, PadrTimeout=None, PadrMaxAttempts=None, EnableAutoRetry=None, AutoRetryCount=None, EnableEchoRequest=None, EchoRequestInterval=None, EchoRequestMaxAttempts=None, Ipv4Start=None, Ipv4Step=None, Ipv4Count=None, Ipv6InterfaceId=None, Ipv6InterfaceIdStep=None, Ipv6PrefixStart=None, Ipv6PrefixStep=None, Ipv6Count=None, **kwargs):
        properties = kwargs.copy()
        if EmulationMode is not None:
            self._EmulationMode = EmulationMode
            properties['EmulationMode'] = EmulationMode
        if IpVersion is not None:
            self._IpVersion = IpVersion
            properties['IpVersion'] = IpVersion
        if AuthenticationType is not None:
            self._AuthenticationType = AuthenticationType
            properties['AuthenticationType'] = AuthenticationType
        if Username is not None:
            self._Username = Username
            properties['Username'] = Username
        if Password is not None:
            self._Password = Password
            properties['Password'] = Password
        if ServiceName is not None:
            self._ServiceName = ServiceName
            properties['ServiceName'] = ServiceName
        if AcName is not None:
            self._AcName = AcName
            properties['AcName'] = AcName
        if EnableMaxPayloadTag is not None:
            self._EnableMaxPayloadTag = EnableMaxPayloadTag
            properties['EnableMaxPayloadTag'] = EnableMaxPayloadTag
        if MaxPayloadBytes is not None:
            self._MaxPayloadBytes = MaxPayloadBytes
            properties['MaxPayloadBytes'] = MaxPayloadBytes
        if PadiTimeout is not None:
            self._PadiTimeout = PadiTimeout
            properties['PadiTimeout'] = PadiTimeout
        if PadiMaxAttempts is not None:
            self._PadiMaxAttempts = PadiMaxAttempts
            properties['PadiMaxAttempts'] = PadiMaxAttempts
        if PadrTimeout is not None:
            self._PadrTimeout = PadrTimeout
            properties['PadrTimeout'] = PadrTimeout
        if PadrMaxAttempts is not None:
            self._PadrMaxAttempts = PadrMaxAttempts
            properties['PadrMaxAttempts'] = PadrMaxAttempts
        if EnableAutoRetry is not None:
            self._EnableAutoRetry = EnableAutoRetry
            properties['EnableAutoRetry'] = EnableAutoRetry
        if AutoRetryCount is not None:
            self._AutoRetryCount = AutoRetryCount
            properties['AutoRetryCount'] = AutoRetryCount
        if EnableEchoRequest is not None:
            self._EnableEchoRequest = EnableEchoRequest
            properties['EnableEchoRequest'] = EnableEchoRequest
        if EchoRequestInterval is not None:
            self._EchoRequestInterval = EchoRequestInterval
            properties['EchoRequestInterval'] = EchoRequestInterval
        if EchoRequestMaxAttempts is not None:
            self._EchoRequestMaxAttempts = EchoRequestMaxAttempts
            properties['EchoRequestMaxAttempts'] = EchoRequestMaxAttempts
        if Ipv4Start is not None:
            self._Ipv4Start = Ipv4Start
            properties['Ipv4Start'] = Ipv4Start
        if Ipv4Step is not None:
            self._Ipv4Step = Ipv4Step
            properties['Ipv4Step'] = Ipv4Step
        if Ipv4Count is not None:
            self._Ipv4Count = Ipv4Count
            properties['Ipv4Count'] = Ipv4Count
        if Ipv6InterfaceId is not None:
            self._Ipv6InterfaceId = Ipv6InterfaceId
            properties['Ipv6InterfaceId'] = Ipv6InterfaceId
        if Ipv6InterfaceIdStep is not None:
            self._Ipv6InterfaceIdStep = Ipv6InterfaceIdStep
            properties['Ipv6InterfaceIdStep'] = Ipv6InterfaceIdStep
        if Ipv6PrefixStart is not None:
            self._Ipv6PrefixStart = Ipv6PrefixStart
            properties['Ipv6PrefixStart'] = Ipv6PrefixStart
        if Ipv6PrefixStep is not None:
            self._Ipv6PrefixStep = Ipv6PrefixStep
            properties['Ipv6PrefixStep'] = Ipv6PrefixStep
        if Ipv6Count is not None:
            self._Ipv6Count = Ipv6Count
            properties['Ipv6Count'] = Ipv6Count

        super(PppoeWizardConfig, self).edit(**properties)

    @property
    def EmulationMode(self):
        """
        get the value of property _EmulationMode
        """
        if self.force_auto_sync:
            self.get('EmulationMode')
        return self._EmulationMode

    @property
    def IpVersion(self):
        """
        get the value of property _IpVersion
        """
        if self.force_auto_sync:
            self.get('IpVersion')
        return self._IpVersion

    @property
    def AuthenticationType(self):
        """
        get the value of property _AuthenticationType
        """
        if self.force_auto_sync:
            self.get('AuthenticationType')
        return self._AuthenticationType

    @property
    def Username(self):
        """
        get the value of property _Username
        """
        if self.force_auto_sync:
            self.get('Username')
        return self._Username

    @property
    def Password(self):
        """
        get the value of property _Password
        """
        if self.force_auto_sync:
            self.get('Password')
        return self._Password

    @property
    def ServiceName(self):
        """
        get the value of property _ServiceName
        """
        if self.force_auto_sync:
            self.get('ServiceName')
        return self._ServiceName

    @property
    def AcName(self):
        """
        get the value of property _AcName
        """
        if self.force_auto_sync:
            self.get('AcName')
        return self._AcName

    @property
    def EnableMaxPayloadTag(self):
        """
        get the value of property _EnableMaxPayloadTag
        """
        if self.force_auto_sync:
            self.get('EnableMaxPayloadTag')
        return self._EnableMaxPayloadTag

    @property
    def MaxPayloadBytes(self):
        """
        get the value of property _MaxPayloadBytes
        """
        if self.force_auto_sync:
            self.get('MaxPayloadBytes')
        return self._MaxPayloadBytes

    @property
    def PadiTimeout(self):
        """
        get the value of property _PadiTimeout
        """
        if self.force_auto_sync:
            self.get('PadiTimeout')
        return self._PadiTimeout

    @property
    def PadiMaxAttempts(self):
        """
        get the value of property _PadiMaxAttempts
        """
        if self.force_auto_sync:
            self.get('PadiMaxAttempts')
        return self._PadiMaxAttempts

    @property
    def PadrTimeout(self):
        """
        get the value of property _PadrTimeout
        """
        if self.force_auto_sync:
            self.get('PadrTimeout')
        return self._PadrTimeout

    @property
    def PadrMaxAttempts(self):
        """
        get the value of property _PadrMaxAttempts
        """
        if self.force_auto_sync:
            self.get('PadrMaxAttempts')
        return self._PadrMaxAttempts

    @property
    def EnableAutoRetry(self):
        """
        get the value of property _EnableAutoRetry
        """
        if self.force_auto_sync:
            self.get('EnableAutoRetry')
        return self._EnableAutoRetry

    @property
    def AutoRetryCount(self):
        """
        get the value of property _AutoRetryCount
        """
        if self.force_auto_sync:
            self.get('AutoRetryCount')
        return self._AutoRetryCount

    @property
    def EnableEchoRequest(self):
        """
        get the value of property _EnableEchoRequest
        """
        if self.force_auto_sync:
            self.get('EnableEchoRequest')
        return self._EnableEchoRequest

    @property
    def EchoRequestInterval(self):
        """
        get the value of property _EchoRequestInterval
        """
        if self.force_auto_sync:
            self.get('EchoRequestInterval')
        return self._EchoRequestInterval

    @property
    def EchoRequestMaxAttempts(self):
        """
        get the value of property _EchoRequestMaxAttempts
        """
        if self.force_auto_sync:
            self.get('EchoRequestMaxAttempts')
        return self._EchoRequestMaxAttempts

    @property
    def Ipv4Start(self):
        """
        get the value of property _Ipv4Start
        """
        if self.force_auto_sync:
            self.get('Ipv4Start')
        return self._Ipv4Start

    @property
    def Ipv4Step(self):
        """
        get the value of property _Ipv4Step
        """
        if self.force_auto_sync:
            self.get('Ipv4Step')
        return self._Ipv4Step

    @property
    def Ipv4Count(self):
        """
        get the value of property _Ipv4Count
        """
        if self.force_auto_sync:
            self.get('Ipv4Count')
        return self._Ipv4Count

    @property
    def Ipv6InterfaceId(self):
        """
        get the value of property _Ipv6InterfaceId
        """
        if self.force_auto_sync:
            self.get('Ipv6InterfaceId')
        return self._Ipv6InterfaceId

    @property
    def Ipv6InterfaceIdStep(self):
        """
        get the value of property _Ipv6InterfaceIdStep
        """
        if self.force_auto_sync:
            self.get('Ipv6InterfaceIdStep')
        return self._Ipv6InterfaceIdStep

    @property
    def Ipv6PrefixStart(self):
        """
        get the value of property _Ipv6PrefixStart
        """
        if self.force_auto_sync:
            self.get('Ipv6PrefixStart')
        return self._Ipv6PrefixStart

    @property
    def Ipv6PrefixStep(self):
        """
        get the value of property _Ipv6PrefixStep
        """
        if self.force_auto_sync:
            self.get('Ipv6PrefixStep')
        return self._Ipv6PrefixStep

    @property
    def Ipv6Count(self):
        """
        get the value of property _Ipv6Count
        """
        if self.force_auto_sync:
            self.get('Ipv6Count')
        return self._Ipv6Count

    @EmulationMode.setter
    def EmulationMode(self, value):
        self._EmulationMode = value
        self.edit(EmulationMode=value)

    @IpVersion.setter
    def IpVersion(self, value):
        self._IpVersion = value
        self.edit(IpVersion=value)

    @AuthenticationType.setter
    def AuthenticationType(self, value):
        self._AuthenticationType = value
        self.edit(AuthenticationType=value)

    @Username.setter
    def Username(self, value):
        self._Username = value
        self.edit(Username=value)

    @Password.setter
    def Password(self, value):
        self._Password = value
        self.edit(Password=value)

    @ServiceName.setter
    def ServiceName(self, value):
        self._ServiceName = value
        self.edit(ServiceName=value)

    @AcName.setter
    def AcName(self, value):
        self._AcName = value
        self.edit(AcName=value)

    @EnableMaxPayloadTag.setter
    def EnableMaxPayloadTag(self, value):
        self._EnableMaxPayloadTag = value
        self.edit(EnableMaxPayloadTag=value)

    @MaxPayloadBytes.setter
    def MaxPayloadBytes(self, value):
        self._MaxPayloadBytes = value
        self.edit(MaxPayloadBytes=value)

    @PadiTimeout.setter
    def PadiTimeout(self, value):
        self._PadiTimeout = value
        self.edit(PadiTimeout=value)

    @PadiMaxAttempts.setter
    def PadiMaxAttempts(self, value):
        self._PadiMaxAttempts = value
        self.edit(PadiMaxAttempts=value)

    @PadrTimeout.setter
    def PadrTimeout(self, value):
        self._PadrTimeout = value
        self.edit(PadrTimeout=value)

    @PadrMaxAttempts.setter
    def PadrMaxAttempts(self, value):
        self._PadrMaxAttempts = value
        self.edit(PadrMaxAttempts=value)

    @EnableAutoRetry.setter
    def EnableAutoRetry(self, value):
        self._EnableAutoRetry = value
        self.edit(EnableAutoRetry=value)

    @AutoRetryCount.setter
    def AutoRetryCount(self, value):
        self._AutoRetryCount = value
        self.edit(AutoRetryCount=value)

    @EnableEchoRequest.setter
    def EnableEchoRequest(self, value):
        self._EnableEchoRequest = value
        self.edit(EnableEchoRequest=value)

    @EchoRequestInterval.setter
    def EchoRequestInterval(self, value):
        self._EchoRequestInterval = value
        self.edit(EchoRequestInterval=value)

    @EchoRequestMaxAttempts.setter
    def EchoRequestMaxAttempts(self, value):
        self._EchoRequestMaxAttempts = value
        self.edit(EchoRequestMaxAttempts=value)

    @Ipv4Start.setter
    def Ipv4Start(self, value):
        self._Ipv4Start = value
        self.edit(Ipv4Start=value)

    @Ipv4Step.setter
    def Ipv4Step(self, value):
        self._Ipv4Step = value
        self.edit(Ipv4Step=value)

    @Ipv4Count.setter
    def Ipv4Count(self, value):
        self._Ipv4Count = value
        self.edit(Ipv4Count=value)

    @Ipv6InterfaceId.setter
    def Ipv6InterfaceId(self, value):
        self._Ipv6InterfaceId = value
        self.edit(Ipv6InterfaceId=value)

    @Ipv6InterfaceIdStep.setter
    def Ipv6InterfaceIdStep(self, value):
        self._Ipv6InterfaceIdStep = value
        self.edit(Ipv6InterfaceIdStep=value)

    @Ipv6PrefixStart.setter
    def Ipv6PrefixStart(self, value):
        self._Ipv6PrefixStart = value
        self.edit(Ipv6PrefixStart=value)

    @Ipv6PrefixStep.setter
    def Ipv6PrefixStep(self, value):
        self._Ipv6PrefixStep = value
        self.edit(Ipv6PrefixStep=value)

    @Ipv6Count.setter
    def Ipv6Count(self, value):
        self._Ipv6Count = value
        self.edit(Ipv6Count=value)

    def _set_emulationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._EmulationMode = EnumWizardPppoeMode.%s' % value[:seperate])

    def _set_ipversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._IpVersion = EnumPppoeIpVersion.%s' % value[:seperate])

    def _set_authenticationtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._AuthenticationType = EnumPppoeAuthenticationType.%s' % value[:seperate])

    def _set_username_with_str(self, value):
        self._Username = value

    def _set_password_with_str(self, value):
        self._Password = value

    def _set_servicename_with_str(self, value):
        self._ServiceName = value

    def _set_acname_with_str(self, value):
        self._AcName = value

    def _set_enablemaxpayloadtag_with_str(self, value):
        self._EnableMaxPayloadTag = (value == 'True')

    def _set_maxpayloadbytes_with_str(self, value):
        try:
            self._MaxPayloadBytes = int(value)
        except ValueError:
            self._MaxPayloadBytes = hex(int(value, 16))

    def _set_paditimeout_with_str(self, value):
        try:
            self._PadiTimeout = int(value)
        except ValueError:
            self._PadiTimeout = hex(int(value, 16))

    def _set_padimaxattempts_with_str(self, value):
        try:
            self._PadiMaxAttempts = int(value)
        except ValueError:
            self._PadiMaxAttempts = hex(int(value, 16))

    def _set_padrtimeout_with_str(self, value):
        try:
            self._PadrTimeout = int(value)
        except ValueError:
            self._PadrTimeout = hex(int(value, 16))

    def _set_padrmaxattempts_with_str(self, value):
        try:
            self._PadrMaxAttempts = int(value)
        except ValueError:
            self._PadrMaxAttempts = hex(int(value, 16))

    def _set_enableautoretry_with_str(self, value):
        self._EnableAutoRetry = (value == 'True')

    def _set_autoretrycount_with_str(self, value):
        try:
            self._AutoRetryCount = int(value)
        except ValueError:
            self._AutoRetryCount = hex(int(value, 16))

    def _set_enableechorequest_with_str(self, value):
        self._EnableEchoRequest = (value == 'True')

    def _set_echorequestinterval_with_str(self, value):
        try:
            self._EchoRequestInterval = int(value)
        except ValueError:
            self._EchoRequestInterval = hex(int(value, 16))

    def _set_echorequestmaxattempts_with_str(self, value):
        try:
            self._EchoRequestMaxAttempts = int(value)
        except ValueError:
            self._EchoRequestMaxAttempts = hex(int(value, 16))

    def _set_ipv4start_with_str(self, value):
        self._Ipv4Start = value

    def _set_ipv4step_with_str(self, value):
        self._Ipv4Step = value

    def _set_ipv4count_with_str(self, value):
        try:
            self._Ipv4Count = int(value)
        except ValueError:
            self._Ipv4Count = hex(int(value, 16))

    def _set_ipv6interfaceid_with_str(self, value):
        self._Ipv6InterfaceId = value

    def _set_ipv6interfaceidstep_with_str(self, value):
        self._Ipv6InterfaceIdStep = value

    def _set_ipv6prefixstart_with_str(self, value):
        self._Ipv6PrefixStart = value

    def _set_ipv6prefixstep_with_str(self, value):
        self._Ipv6PrefixStep = value

    def _set_ipv6count_with_str(self, value):
        try:
            self._Ipv6Count = int(value)
        except ValueError:
            self._Ipv6Count = hex(int(value, 16))

