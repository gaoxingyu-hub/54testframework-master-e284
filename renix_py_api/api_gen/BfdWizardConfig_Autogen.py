"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ProtocolWizardConfig_Autogen import ProtocolWizardConfig


@rom_manager.rom
class BfdWizardConfig(ProtocolWizardConfig):
    def __init__(self, RouterRole=None, TransmitInterval=None, ReceiveInterval=None, DetectMultiplier=None, EchoReceiveInterval=None, AuthenticationType=None, Password=None, KeyID=None, IsControlPlaneIndependentSession=None, Ipv4SessionNumber=None, Ipv4DestinationAddress=None, Ipv4Increment=None, Ipv4StepPerInterface=None, Ipv4StepPerPort=None, Ipv6SessionNumber=None, Ipv6DestinationAddress=None, Ipv6Increment=None, Ipv6StepPerInterface=None, Ipv6StepPerPort=None, **kwargs):
        self._RouterRole = RouterRole  # Router Role
        self._TransmitInterval = TransmitInterval  # Transmit Interval
        self._ReceiveInterval = ReceiveInterval  # Receive Interval
        self._DetectMultiplier = DetectMultiplier  # Detect Multiplier
        self._EchoReceiveInterval = EchoReceiveInterval  # Echo Receive Interval
        self._AuthenticationType = AuthenticationType  # Authentication Type
        self._Password = Password  # Password
        self._KeyID = KeyID  # Key ID
        self._IsControlPlaneIndependentSession = IsControlPlaneIndependentSession  # Control Plane Independent Session
        self._Ipv4SessionNumber = Ipv4SessionNumber  # Number of Sessions
        self._Ipv4DestinationAddress = Ipv4DestinationAddress  # IPv4 Destination Address
        self._Ipv4Increment = Ipv4Increment  # IPv4 Increment
        self._Ipv4StepPerInterface = Ipv4StepPerInterface  # IPv4 Step per Interface
        self._Ipv4StepPerPort = Ipv4StepPerPort  # Destination Address Increment
        self._Ipv6SessionNumber = Ipv6SessionNumber  # Number of Sessions
        self._Ipv6DestinationAddress = Ipv6DestinationAddress  # IPv6 Destination Address
        self._Ipv6Increment = Ipv6Increment  # IPv4 Increment
        self._Ipv6StepPerInterface = Ipv6StepPerInterface  # IPv4 Step per Interface
        self._Ipv6StepPerPort = Ipv6StepPerPort  # Destination Address Increment

        properties = kwargs.copy()
        if RouterRole is not None:
            properties['RouterRole'] = RouterRole
        if TransmitInterval is not None:
            properties['TransmitInterval'] = TransmitInterval
        if ReceiveInterval is not None:
            properties['ReceiveInterval'] = ReceiveInterval
        if DetectMultiplier is not None:
            properties['DetectMultiplier'] = DetectMultiplier
        if EchoReceiveInterval is not None:
            properties['EchoReceiveInterval'] = EchoReceiveInterval
        if AuthenticationType is not None:
            properties['AuthenticationType'] = AuthenticationType
        if Password is not None:
            properties['Password'] = Password
        if KeyID is not None:
            properties['KeyID'] = KeyID
        if IsControlPlaneIndependentSession is not None:
            properties['IsControlPlaneIndependentSession'] = IsControlPlaneIndependentSession
        if Ipv4SessionNumber is not None:
            properties['Ipv4SessionNumber'] = Ipv4SessionNumber
        if Ipv4DestinationAddress is not None:
            properties['Ipv4DestinationAddress'] = Ipv4DestinationAddress
        if Ipv4Increment is not None:
            properties['Ipv4Increment'] = Ipv4Increment
        if Ipv4StepPerInterface is not None:
            properties['Ipv4StepPerInterface'] = Ipv4StepPerInterface
        if Ipv4StepPerPort is not None:
            properties['Ipv4StepPerPort'] = Ipv4StepPerPort
        if Ipv6SessionNumber is not None:
            properties['Ipv6SessionNumber'] = Ipv6SessionNumber
        if Ipv6DestinationAddress is not None:
            properties['Ipv6DestinationAddress'] = Ipv6DestinationAddress
        if Ipv6Increment is not None:
            properties['Ipv6Increment'] = Ipv6Increment
        if Ipv6StepPerInterface is not None:
            properties['Ipv6StepPerInterface'] = Ipv6StepPerInterface
        if Ipv6StepPerPort is not None:
            properties['Ipv6StepPerPort'] = Ipv6StepPerPort

        # call base class function, and it will send message to renix server to create a class.
        super(BfdWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RouterRole=None, TransmitInterval=None, ReceiveInterval=None, DetectMultiplier=None, EchoReceiveInterval=None, AuthenticationType=None, Password=None, KeyID=None, IsControlPlaneIndependentSession=None, Ipv4SessionNumber=None, Ipv4DestinationAddress=None, Ipv4Increment=None, Ipv4StepPerInterface=None, Ipv4StepPerPort=None, Ipv6SessionNumber=None, Ipv6DestinationAddress=None, Ipv6Increment=None, Ipv6StepPerInterface=None, Ipv6StepPerPort=None, **kwargs):
        properties = kwargs.copy()
        if RouterRole is not None:
            self._RouterRole = RouterRole
            properties['RouterRole'] = RouterRole
        if TransmitInterval is not None:
            self._TransmitInterval = TransmitInterval
            properties['TransmitInterval'] = TransmitInterval
        if ReceiveInterval is not None:
            self._ReceiveInterval = ReceiveInterval
            properties['ReceiveInterval'] = ReceiveInterval
        if DetectMultiplier is not None:
            self._DetectMultiplier = DetectMultiplier
            properties['DetectMultiplier'] = DetectMultiplier
        if EchoReceiveInterval is not None:
            self._EchoReceiveInterval = EchoReceiveInterval
            properties['EchoReceiveInterval'] = EchoReceiveInterval
        if AuthenticationType is not None:
            self._AuthenticationType = AuthenticationType
            properties['AuthenticationType'] = AuthenticationType
        if Password is not None:
            self._Password = Password
            properties['Password'] = Password
        if KeyID is not None:
            self._KeyID = KeyID
            properties['KeyID'] = KeyID
        if IsControlPlaneIndependentSession is not None:
            self._IsControlPlaneIndependentSession = IsControlPlaneIndependentSession
            properties['IsControlPlaneIndependentSession'] = IsControlPlaneIndependentSession
        if Ipv4SessionNumber is not None:
            self._Ipv4SessionNumber = Ipv4SessionNumber
            properties['Ipv4SessionNumber'] = Ipv4SessionNumber
        if Ipv4DestinationAddress is not None:
            self._Ipv4DestinationAddress = Ipv4DestinationAddress
            properties['Ipv4DestinationAddress'] = Ipv4DestinationAddress
        if Ipv4Increment is not None:
            self._Ipv4Increment = Ipv4Increment
            properties['Ipv4Increment'] = Ipv4Increment
        if Ipv4StepPerInterface is not None:
            self._Ipv4StepPerInterface = Ipv4StepPerInterface
            properties['Ipv4StepPerInterface'] = Ipv4StepPerInterface
        if Ipv4StepPerPort is not None:
            self._Ipv4StepPerPort = Ipv4StepPerPort
            properties['Ipv4StepPerPort'] = Ipv4StepPerPort
        if Ipv6SessionNumber is not None:
            self._Ipv6SessionNumber = Ipv6SessionNumber
            properties['Ipv6SessionNumber'] = Ipv6SessionNumber
        if Ipv6DestinationAddress is not None:
            self._Ipv6DestinationAddress = Ipv6DestinationAddress
            properties['Ipv6DestinationAddress'] = Ipv6DestinationAddress
        if Ipv6Increment is not None:
            self._Ipv6Increment = Ipv6Increment
            properties['Ipv6Increment'] = Ipv6Increment
        if Ipv6StepPerInterface is not None:
            self._Ipv6StepPerInterface = Ipv6StepPerInterface
            properties['Ipv6StepPerInterface'] = Ipv6StepPerInterface
        if Ipv6StepPerPort is not None:
            self._Ipv6StepPerPort = Ipv6StepPerPort
            properties['Ipv6StepPerPort'] = Ipv6StepPerPort

        super(BfdWizardConfig, self).edit(**properties)

    @property
    def RouterRole(self):
        """
        get the value of property _RouterRole
        """
        if self.force_auto_sync:
            self.get('RouterRole')
        return self._RouterRole

    @property
    def TransmitInterval(self):
        """
        get the value of property _TransmitInterval
        """
        if self.force_auto_sync:
            self.get('TransmitInterval')
        return self._TransmitInterval

    @property
    def ReceiveInterval(self):
        """
        get the value of property _ReceiveInterval
        """
        if self.force_auto_sync:
            self.get('ReceiveInterval')
        return self._ReceiveInterval

    @property
    def DetectMultiplier(self):
        """
        get the value of property _DetectMultiplier
        """
        if self.force_auto_sync:
            self.get('DetectMultiplier')
        return self._DetectMultiplier

    @property
    def EchoReceiveInterval(self):
        """
        get the value of property _EchoReceiveInterval
        """
        if self.force_auto_sync:
            self.get('EchoReceiveInterval')
        return self._EchoReceiveInterval

    @property
    def AuthenticationType(self):
        """
        get the value of property _AuthenticationType
        """
        if self.force_auto_sync:
            self.get('AuthenticationType')
        return self._AuthenticationType

    @property
    def Password(self):
        """
        get the value of property _Password
        """
        if self.force_auto_sync:
            self.get('Password')
        return self._Password

    @property
    def KeyID(self):
        """
        get the value of property _KeyID
        """
        if self.force_auto_sync:
            self.get('KeyID')
        return self._KeyID

    @property
    def IsControlPlaneIndependentSession(self):
        """
        get the value of property _IsControlPlaneIndependentSession
        """
        if self.force_auto_sync:
            self.get('IsControlPlaneIndependentSession')
        return self._IsControlPlaneIndependentSession

    @property
    def Ipv4SessionNumber(self):
        """
        get the value of property _Ipv4SessionNumber
        """
        if self.force_auto_sync:
            self.get('Ipv4SessionNumber')
        return self._Ipv4SessionNumber

    @property
    def Ipv4DestinationAddress(self):
        """
        get the value of property _Ipv4DestinationAddress
        """
        if self.force_auto_sync:
            self.get('Ipv4DestinationAddress')
        return self._Ipv4DestinationAddress

    @property
    def Ipv4Increment(self):
        """
        get the value of property _Ipv4Increment
        """
        if self.force_auto_sync:
            self.get('Ipv4Increment')
        return self._Ipv4Increment

    @property
    def Ipv4StepPerInterface(self):
        """
        get the value of property _Ipv4StepPerInterface
        """
        if self.force_auto_sync:
            self.get('Ipv4StepPerInterface')
        return self._Ipv4StepPerInterface

    @property
    def Ipv4StepPerPort(self):
        """
        get the value of property _Ipv4StepPerPort
        """
        if self.force_auto_sync:
            self.get('Ipv4StepPerPort')
        return self._Ipv4StepPerPort

    @property
    def Ipv6SessionNumber(self):
        """
        get the value of property _Ipv6SessionNumber
        """
        if self.force_auto_sync:
            self.get('Ipv6SessionNumber')
        return self._Ipv6SessionNumber

    @property
    def Ipv6DestinationAddress(self):
        """
        get the value of property _Ipv6DestinationAddress
        """
        if self.force_auto_sync:
            self.get('Ipv6DestinationAddress')
        return self._Ipv6DestinationAddress

    @property
    def Ipv6Increment(self):
        """
        get the value of property _Ipv6Increment
        """
        if self.force_auto_sync:
            self.get('Ipv6Increment')
        return self._Ipv6Increment

    @property
    def Ipv6StepPerInterface(self):
        """
        get the value of property _Ipv6StepPerInterface
        """
        if self.force_auto_sync:
            self.get('Ipv6StepPerInterface')
        return self._Ipv6StepPerInterface

    @property
    def Ipv6StepPerPort(self):
        """
        get the value of property _Ipv6StepPerPort
        """
        if self.force_auto_sync:
            self.get('Ipv6StepPerPort')
        return self._Ipv6StepPerPort

    @RouterRole.setter
    def RouterRole(self, value):
        self._RouterRole = value
        self.edit(RouterRole=value)

    @TransmitInterval.setter
    def TransmitInterval(self, value):
        self._TransmitInterval = value
        self.edit(TransmitInterval=value)

    @ReceiveInterval.setter
    def ReceiveInterval(self, value):
        self._ReceiveInterval = value
        self.edit(ReceiveInterval=value)

    @DetectMultiplier.setter
    def DetectMultiplier(self, value):
        self._DetectMultiplier = value
        self.edit(DetectMultiplier=value)

    @EchoReceiveInterval.setter
    def EchoReceiveInterval(self, value):
        self._EchoReceiveInterval = value
        self.edit(EchoReceiveInterval=value)

    @AuthenticationType.setter
    def AuthenticationType(self, value):
        self._AuthenticationType = value
        self.edit(AuthenticationType=value)

    @Password.setter
    def Password(self, value):
        self._Password = value
        self.edit(Password=value)

    @KeyID.setter
    def KeyID(self, value):
        self._KeyID = value
        self.edit(KeyID=value)

    @IsControlPlaneIndependentSession.setter
    def IsControlPlaneIndependentSession(self, value):
        self._IsControlPlaneIndependentSession = value
        self.edit(IsControlPlaneIndependentSession=value)

    @Ipv4SessionNumber.setter
    def Ipv4SessionNumber(self, value):
        self._Ipv4SessionNumber = value
        self.edit(Ipv4SessionNumber=value)

    @Ipv4DestinationAddress.setter
    def Ipv4DestinationAddress(self, value):
        self._Ipv4DestinationAddress = value
        self.edit(Ipv4DestinationAddress=value)

    @Ipv4Increment.setter
    def Ipv4Increment(self, value):
        self._Ipv4Increment = value
        self.edit(Ipv4Increment=value)

    @Ipv4StepPerInterface.setter
    def Ipv4StepPerInterface(self, value):
        self._Ipv4StepPerInterface = value
        self.edit(Ipv4StepPerInterface=value)

    @Ipv4StepPerPort.setter
    def Ipv4StepPerPort(self, value):
        self._Ipv4StepPerPort = value
        self.edit(Ipv4StepPerPort=value)

    @Ipv6SessionNumber.setter
    def Ipv6SessionNumber(self, value):
        self._Ipv6SessionNumber = value
        self.edit(Ipv6SessionNumber=value)

    @Ipv6DestinationAddress.setter
    def Ipv6DestinationAddress(self, value):
        self._Ipv6DestinationAddress = value
        self.edit(Ipv6DestinationAddress=value)

    @Ipv6Increment.setter
    def Ipv6Increment(self, value):
        self._Ipv6Increment = value
        self.edit(Ipv6Increment=value)

    @Ipv6StepPerInterface.setter
    def Ipv6StepPerInterface(self, value):
        self._Ipv6StepPerInterface = value
        self.edit(Ipv6StepPerInterface=value)

    @Ipv6StepPerPort.setter
    def Ipv6StepPerPort(self, value):
        self._Ipv6StepPerPort = value
        self.edit(Ipv6StepPerPort=value)

    def _set_routerrole_with_str(self, value):
        seperate = value.find(':')
        exec('self._RouterRole = BfdRouterRoleEnum.%s' % value[:seperate])

    def _set_transmitinterval_with_str(self, value):
        try:
            self._TransmitInterval = int(value)
        except ValueError:
            self._TransmitInterval = hex(int(value, 16))

    def _set_receiveinterval_with_str(self, value):
        try:
            self._ReceiveInterval = int(value)
        except ValueError:
            self._ReceiveInterval = hex(int(value, 16))

    def _set_detectmultiplier_with_str(self, value):
        try:
            self._DetectMultiplier = int(value)
        except ValueError:
            self._DetectMultiplier = hex(int(value, 16))

    def _set_echoreceiveinterval_with_str(self, value):
        try:
            self._EchoReceiveInterval = int(value)
        except ValueError:
            self._EchoReceiveInterval = hex(int(value, 16))

    def _set_authenticationtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._AuthenticationType = BfdAuthTypeEnum.%s' % value[:seperate])

    def _set_password_with_str(self, value):
        self._Password = value

    def _set_keyid_with_str(self, value):
        try:
            self._KeyID = int(value)
        except ValueError:
            self._KeyID = hex(int(value, 16))

    def _set_iscontrolplaneindependentsession_with_str(self, value):
        self._IsControlPlaneIndependentSession = (value == 'True')

    def _set_ipv4sessionnumber_with_str(self, value):
        try:
            self._Ipv4SessionNumber = int(value)
        except ValueError:
            self._Ipv4SessionNumber = hex(int(value, 16))

    def _set_ipv4destinationaddress_with_str(self, value):
        self._Ipv4DestinationAddress = value

    def _set_ipv4increment_with_str(self, value):
        self._Ipv4Increment = value

    def _set_ipv4stepperinterface_with_str(self, value):
        self._Ipv4StepPerInterface = value

    def _set_ipv4stepperport_with_str(self, value):
        self._Ipv4StepPerPort = value

    def _set_ipv6sessionnumber_with_str(self, value):
        try:
            self._Ipv6SessionNumber = int(value)
        except ValueError:
            self._Ipv6SessionNumber = hex(int(value, 16))

    def _set_ipv6destinationaddress_with_str(self, value):
        self._Ipv6DestinationAddress = value

    def _set_ipv6increment_with_str(self, value):
        self._Ipv6Increment = value

    def _set_ipv6stepperinterface_with_str(self, value):
        self._Ipv6StepPerInterface = value

    def _set_ipv6stepperport_with_str(self, value):
        self._Ipv6StepPerPort = value

