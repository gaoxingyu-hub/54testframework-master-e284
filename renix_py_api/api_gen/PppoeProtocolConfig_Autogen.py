"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class PppoeProtocolConfig(L23ProtocolConfig):
    def __init__(self, EmulationMode=None, AuthenticationType=None, Username=None, Password=None, ServiceName=None, EnableMaxPayloadTag=None, MaxPayloadBytes=None, LcpConfigReqTimeout=None, LcpConfigReqMaxAttempts=None, LcpTermReqTimeout=None, LcpTermReqMaxAttempts=None, NcpConfigReqTimeout=None, NcpConfigReqMaxAttempts=None, LcpNcpMaxNak=None, EnableMruNegotiation=None, MruSize=None, EnableEchoRequest=None, EchoRequestInterval=None, EchoRequestMaxAttempts=None, EnableMagicNumber=None, **kwargs):
        self._EmulationMode = EmulationMode  # Emulation Mode
        self._IpcpState = EnumPppoeCpState.NONE  # IPCP Block State, not editable
        self._Ipv6cpState = EnumPppoeCpState.NONE  # IPv6CP Block State, not editable
        self._IpVersion = EnumPppoeIpVersion.NONE  # IP Version, not editable
        self._PppSessionCount = 1  # PPPoL2TP session total count, not editable
        self._AuthenticationType = AuthenticationType  # Authentication
        self._Username = Username  # Username
        self._Password = Password  # Password
        self._ServiceName = ServiceName  # Service Name
        self._EnableMaxPayloadTag = EnableMaxPayloadTag  # Enable Max Payload Tag
        self._MaxPayloadBytes = MaxPayloadBytes  # Max Payload Bytes
        self._LcpConfigReqTimeout = LcpConfigReqTimeout  # LCP Configure-Request Timeout(sec)
        self._LcpConfigReqMaxAttempts = LcpConfigReqMaxAttempts  # LCP Configure-Request Max Attempts
        self._LcpTermReqTimeout = LcpTermReqTimeout  # LCP Terminate-Request Timeout(sec)
        self._LcpTermReqMaxAttempts = LcpTermReqMaxAttempts  # LCP Terminate-Request Max Attempts
        self._NcpConfigReqTimeout = NcpConfigReqTimeout  # NCP Configure-Request Timeout(sec)
        self._NcpConfigReqMaxAttempts = NcpConfigReqMaxAttempts  # NCP Configure-Request Max Attempts
        self._LcpNcpMaxNak = LcpNcpMaxNak  # LCP/NCP Max Naks
        self._EnableMruNegotiation = EnableMruNegotiation  # Enable MRU Negotiation
        self._MruSize = MruSize  # MRU Size
        self._EnableEchoRequest = EnableEchoRequest  # Enable Echo-Request
        self._EchoRequestInterval = EchoRequestInterval  # Echo-Request Interval(sec)
        self._EchoRequestMaxAttempts = EchoRequestMaxAttempts  # Echo-Request Max Attempts
        self._EnableMagicNumber = EnableMagicNumber  # Enable Magic-Number

        properties = kwargs.copy()
        if EmulationMode is not None:
            properties['EmulationMode'] = EmulationMode
        if AuthenticationType is not None:
            properties['AuthenticationType'] = AuthenticationType
        if Username is not None:
            properties['Username'] = Username
        if Password is not None:
            properties['Password'] = Password
        if ServiceName is not None:
            properties['ServiceName'] = ServiceName
        if EnableMaxPayloadTag is not None:
            properties['EnableMaxPayloadTag'] = EnableMaxPayloadTag
        if MaxPayloadBytes is not None:
            properties['MaxPayloadBytes'] = MaxPayloadBytes
        if LcpConfigReqTimeout is not None:
            properties['LcpConfigReqTimeout'] = LcpConfigReqTimeout
        if LcpConfigReqMaxAttempts is not None:
            properties['LcpConfigReqMaxAttempts'] = LcpConfigReqMaxAttempts
        if LcpTermReqTimeout is not None:
            properties['LcpTermReqTimeout'] = LcpTermReqTimeout
        if LcpTermReqMaxAttempts is not None:
            properties['LcpTermReqMaxAttempts'] = LcpTermReqMaxAttempts
        if NcpConfigReqTimeout is not None:
            properties['NcpConfigReqTimeout'] = NcpConfigReqTimeout
        if NcpConfigReqMaxAttempts is not None:
            properties['NcpConfigReqMaxAttempts'] = NcpConfigReqMaxAttempts
        if LcpNcpMaxNak is not None:
            properties['LcpNcpMaxNak'] = LcpNcpMaxNak
        if EnableMruNegotiation is not None:
            properties['EnableMruNegotiation'] = EnableMruNegotiation
        if MruSize is not None:
            properties['MruSize'] = MruSize
        if EnableEchoRequest is not None:
            properties['EnableEchoRequest'] = EnableEchoRequest
        if EchoRequestInterval is not None:
            properties['EchoRequestInterval'] = EchoRequestInterval
        if EchoRequestMaxAttempts is not None:
            properties['EchoRequestMaxAttempts'] = EchoRequestMaxAttempts
        if EnableMagicNumber is not None:
            properties['EnableMagicNumber'] = EnableMagicNumber

        # call base class function, and it will send message to renix server to create a class.
        super(PppoeProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EmulationMode=None, AuthenticationType=None, Username=None, Password=None, ServiceName=None, EnableMaxPayloadTag=None, MaxPayloadBytes=None, LcpConfigReqTimeout=None, LcpConfigReqMaxAttempts=None, LcpTermReqTimeout=None, LcpTermReqMaxAttempts=None, NcpConfigReqTimeout=None, NcpConfigReqMaxAttempts=None, LcpNcpMaxNak=None, EnableMruNegotiation=None, MruSize=None, EnableEchoRequest=None, EchoRequestInterval=None, EchoRequestMaxAttempts=None, EnableMagicNumber=None, **kwargs):
        properties = kwargs.copy()
        if EmulationMode is not None:
            self._EmulationMode = EmulationMode
            properties['EmulationMode'] = EmulationMode
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
        if EnableMaxPayloadTag is not None:
            self._EnableMaxPayloadTag = EnableMaxPayloadTag
            properties['EnableMaxPayloadTag'] = EnableMaxPayloadTag
        if MaxPayloadBytes is not None:
            self._MaxPayloadBytes = MaxPayloadBytes
            properties['MaxPayloadBytes'] = MaxPayloadBytes
        if LcpConfigReqTimeout is not None:
            self._LcpConfigReqTimeout = LcpConfigReqTimeout
            properties['LcpConfigReqTimeout'] = LcpConfigReqTimeout
        if LcpConfigReqMaxAttempts is not None:
            self._LcpConfigReqMaxAttempts = LcpConfigReqMaxAttempts
            properties['LcpConfigReqMaxAttempts'] = LcpConfigReqMaxAttempts
        if LcpTermReqTimeout is not None:
            self._LcpTermReqTimeout = LcpTermReqTimeout
            properties['LcpTermReqTimeout'] = LcpTermReqTimeout
        if LcpTermReqMaxAttempts is not None:
            self._LcpTermReqMaxAttempts = LcpTermReqMaxAttempts
            properties['LcpTermReqMaxAttempts'] = LcpTermReqMaxAttempts
        if NcpConfigReqTimeout is not None:
            self._NcpConfigReqTimeout = NcpConfigReqTimeout
            properties['NcpConfigReqTimeout'] = NcpConfigReqTimeout
        if NcpConfigReqMaxAttempts is not None:
            self._NcpConfigReqMaxAttempts = NcpConfigReqMaxAttempts
            properties['NcpConfigReqMaxAttempts'] = NcpConfigReqMaxAttempts
        if LcpNcpMaxNak is not None:
            self._LcpNcpMaxNak = LcpNcpMaxNak
            properties['LcpNcpMaxNak'] = LcpNcpMaxNak
        if EnableMruNegotiation is not None:
            self._EnableMruNegotiation = EnableMruNegotiation
            properties['EnableMruNegotiation'] = EnableMruNegotiation
        if MruSize is not None:
            self._MruSize = MruSize
            properties['MruSize'] = MruSize
        if EnableEchoRequest is not None:
            self._EnableEchoRequest = EnableEchoRequest
            properties['EnableEchoRequest'] = EnableEchoRequest
        if EchoRequestInterval is not None:
            self._EchoRequestInterval = EchoRequestInterval
            properties['EchoRequestInterval'] = EchoRequestInterval
        if EchoRequestMaxAttempts is not None:
            self._EchoRequestMaxAttempts = EchoRequestMaxAttempts
            properties['EchoRequestMaxAttempts'] = EchoRequestMaxAttempts
        if EnableMagicNumber is not None:
            self._EnableMagicNumber = EnableMagicNumber
            properties['EnableMagicNumber'] = EnableMagicNumber

        super(PppoeProtocolConfig, self).edit(**properties)

    @property
    def EmulationMode(self):
        """
        get the value of property _EmulationMode
        """
        if self.force_auto_sync:
            self.get('EmulationMode')
        return self._EmulationMode

    @property
    def IpcpState(self):
        """
        get the value of property _IpcpState
        """
        if self.force_auto_sync:
            self.get('IpcpState')
        return self._IpcpState

    @property
    def Ipv6cpState(self):
        """
        get the value of property _Ipv6cpState
        """
        if self.force_auto_sync:
            self.get('Ipv6cpState')
        return self._Ipv6cpState

    @property
    def IpVersion(self):
        """
        get the value of property _IpVersion
        """
        if self.force_auto_sync:
            self.get('IpVersion')
        return self._IpVersion

    @property
    def PppSessionCount(self):
        """
        get the value of property _PppSessionCount
        """
        if self.force_auto_sync:
            self.get('PppSessionCount')
        return self._PppSessionCount

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
    def LcpConfigReqTimeout(self):
        """
        get the value of property _LcpConfigReqTimeout
        """
        if self.force_auto_sync:
            self.get('LcpConfigReqTimeout')
        return self._LcpConfigReqTimeout

    @property
    def LcpConfigReqMaxAttempts(self):
        """
        get the value of property _LcpConfigReqMaxAttempts
        """
        if self.force_auto_sync:
            self.get('LcpConfigReqMaxAttempts')
        return self._LcpConfigReqMaxAttempts

    @property
    def LcpTermReqTimeout(self):
        """
        get the value of property _LcpTermReqTimeout
        """
        if self.force_auto_sync:
            self.get('LcpTermReqTimeout')
        return self._LcpTermReqTimeout

    @property
    def LcpTermReqMaxAttempts(self):
        """
        get the value of property _LcpTermReqMaxAttempts
        """
        if self.force_auto_sync:
            self.get('LcpTermReqMaxAttempts')
        return self._LcpTermReqMaxAttempts

    @property
    def NcpConfigReqTimeout(self):
        """
        get the value of property _NcpConfigReqTimeout
        """
        if self.force_auto_sync:
            self.get('NcpConfigReqTimeout')
        return self._NcpConfigReqTimeout

    @property
    def NcpConfigReqMaxAttempts(self):
        """
        get the value of property _NcpConfigReqMaxAttempts
        """
        if self.force_auto_sync:
            self.get('NcpConfigReqMaxAttempts')
        return self._NcpConfigReqMaxAttempts

    @property
    def LcpNcpMaxNak(self):
        """
        get the value of property _LcpNcpMaxNak
        """
        if self.force_auto_sync:
            self.get('LcpNcpMaxNak')
        return self._LcpNcpMaxNak

    @property
    def EnableMruNegotiation(self):
        """
        get the value of property _EnableMruNegotiation
        """
        if self.force_auto_sync:
            self.get('EnableMruNegotiation')
        return self._EnableMruNegotiation

    @property
    def MruSize(self):
        """
        get the value of property _MruSize
        """
        if self.force_auto_sync:
            self.get('MruSize')
        return self._MruSize

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
    def EnableMagicNumber(self):
        """
        get the value of property _EnableMagicNumber
        """
        if self.force_auto_sync:
            self.get('EnableMagicNumber')
        return self._EnableMagicNumber

    @EmulationMode.setter
    def EmulationMode(self, value):
        self._EmulationMode = value
        self.edit(EmulationMode=value)

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

    @EnableMaxPayloadTag.setter
    def EnableMaxPayloadTag(self, value):
        self._EnableMaxPayloadTag = value
        self.edit(EnableMaxPayloadTag=value)

    @MaxPayloadBytes.setter
    def MaxPayloadBytes(self, value):
        self._MaxPayloadBytes = value
        self.edit(MaxPayloadBytes=value)

    @LcpConfigReqTimeout.setter
    def LcpConfigReqTimeout(self, value):
        self._LcpConfigReqTimeout = value
        self.edit(LcpConfigReqTimeout=value)

    @LcpConfigReqMaxAttempts.setter
    def LcpConfigReqMaxAttempts(self, value):
        self._LcpConfigReqMaxAttempts = value
        self.edit(LcpConfigReqMaxAttempts=value)

    @LcpTermReqTimeout.setter
    def LcpTermReqTimeout(self, value):
        self._LcpTermReqTimeout = value
        self.edit(LcpTermReqTimeout=value)

    @LcpTermReqMaxAttempts.setter
    def LcpTermReqMaxAttempts(self, value):
        self._LcpTermReqMaxAttempts = value
        self.edit(LcpTermReqMaxAttempts=value)

    @NcpConfigReqTimeout.setter
    def NcpConfigReqTimeout(self, value):
        self._NcpConfigReqTimeout = value
        self.edit(NcpConfigReqTimeout=value)

    @NcpConfigReqMaxAttempts.setter
    def NcpConfigReqMaxAttempts(self, value):
        self._NcpConfigReqMaxAttempts = value
        self.edit(NcpConfigReqMaxAttempts=value)

    @LcpNcpMaxNak.setter
    def LcpNcpMaxNak(self, value):
        self._LcpNcpMaxNak = value
        self.edit(LcpNcpMaxNak=value)

    @EnableMruNegotiation.setter
    def EnableMruNegotiation(self, value):
        self._EnableMruNegotiation = value
        self.edit(EnableMruNegotiation=value)

    @MruSize.setter
    def MruSize(self, value):
        self._MruSize = value
        self.edit(MruSize=value)

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

    @EnableMagicNumber.setter
    def EnableMagicNumber(self, value):
        self._EnableMagicNumber = value
        self.edit(EnableMagicNumber=value)

    def _set_emulationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._EmulationMode = EnumPppoeMode.%s' % value[:seperate])

    def _set_ipcpstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._IpcpState = EnumPppoeCpState.%s' % value[:seperate])

    def _set_ipv6cpstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._Ipv6cpState = EnumPppoeCpState.%s' % value[:seperate])

    def _set_ipversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._IpVersion = EnumPppoeIpVersion.%s' % value[:seperate])

    def _set_pppsessioncount_with_str(self, value):
        try:
            self._PppSessionCount = int(value)
        except ValueError:
            self._PppSessionCount = hex(int(value, 16))

    def _set_authenticationtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._AuthenticationType = EnumPppoeAuthenticationType.%s' % value[:seperate])

    def _set_username_with_str(self, value):
        self._Username = value

    def _set_password_with_str(self, value):
        self._Password = value

    def _set_servicename_with_str(self, value):
        self._ServiceName = value

    def _set_enablemaxpayloadtag_with_str(self, value):
        self._EnableMaxPayloadTag = (value == 'True')

    def _set_maxpayloadbytes_with_str(self, value):
        try:
            self._MaxPayloadBytes = int(value)
        except ValueError:
            self._MaxPayloadBytes = hex(int(value, 16))

    def _set_lcpconfigreqtimeout_with_str(self, value):
        try:
            self._LcpConfigReqTimeout = int(value)
        except ValueError:
            self._LcpConfigReqTimeout = hex(int(value, 16))

    def _set_lcpconfigreqmaxattempts_with_str(self, value):
        try:
            self._LcpConfigReqMaxAttempts = int(value)
        except ValueError:
            self._LcpConfigReqMaxAttempts = hex(int(value, 16))

    def _set_lcptermreqtimeout_with_str(self, value):
        try:
            self._LcpTermReqTimeout = int(value)
        except ValueError:
            self._LcpTermReqTimeout = hex(int(value, 16))

    def _set_lcptermreqmaxattempts_with_str(self, value):
        try:
            self._LcpTermReqMaxAttempts = int(value)
        except ValueError:
            self._LcpTermReqMaxAttempts = hex(int(value, 16))

    def _set_ncpconfigreqtimeout_with_str(self, value):
        try:
            self._NcpConfigReqTimeout = int(value)
        except ValueError:
            self._NcpConfigReqTimeout = hex(int(value, 16))

    def _set_ncpconfigreqmaxattempts_with_str(self, value):
        try:
            self._NcpConfigReqMaxAttempts = int(value)
        except ValueError:
            self._NcpConfigReqMaxAttempts = hex(int(value, 16))

    def _set_lcpncpmaxnak_with_str(self, value):
        try:
            self._LcpNcpMaxNak = int(value)
        except ValueError:
            self._LcpNcpMaxNak = hex(int(value, 16))

    def _set_enablemrunegotiation_with_str(self, value):
        self._EnableMruNegotiation = (value == 'True')

    def _set_mrusize_with_str(self, value):
        try:
            self._MruSize = int(value)
        except ValueError:
            self._MruSize = hex(int(value, 16))

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

    def _set_enablemagicnumber_with_str(self, value):
        self._EnableMagicNumber = (value == 'True')

