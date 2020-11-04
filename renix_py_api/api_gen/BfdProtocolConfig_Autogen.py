"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class BfdProtocolConfig(L23ProtocolConfig):
    def __init__(self, RouterRole=None, TimeIntervalUnit=None, DesiredMinTXInterval=None, RequiredMinRXInterval=None, RequiredMinEchoRXInterval=None, DetectMultiple=None, AuthenticationType=None, Password=None, KeyID=None, **kwargs):
        self._RouterRole = RouterRole  # Router Role
        self._ProtocolState = BfdProtocolStateEnum.DISABLED  # Protocol State, not editable
        self._BFDSessionUpCount = 0  # BFD Session Up Count, not editable
        self._BFDSessionDownCount = 0  # BFD Session Down Count, not editable
        self._TimeIntervalUnit = TimeIntervalUnit  # Time Interval Unit
        self._DesiredMinTXInterval = DesiredMinTXInterval  # Transmit Interval
        self._RequiredMinRXInterval = RequiredMinRXInterval  # Receive Interval
        self._RequiredMinEchoRXInterval = RequiredMinEchoRXInterval  # Echo Receive Interval
        self._DetectMultiple = DetectMultiple  # Detect Multiplier
        self._AuthenticationType = AuthenticationType  # Authentication Type
        self._Password = Password  # Password
        self._KeyID = KeyID  # Key ID
        self._ProtocolDependentSession = BfdProtocolDependentSessionEnum.INDEPENDENT  # Protocol Dependent Session State, not editable
        self._Ipv4ControlPlaneIndependentSessionCount = 0  # IPv4 Static Session Count, not editable
        self._Ipv6ControlPlaneIndependentSessionCount = 0  # IPv6 Static Session Count, not editable

        properties = kwargs.copy()
        if RouterRole is not None:
            properties['RouterRole'] = RouterRole
        if TimeIntervalUnit is not None:
            properties['TimeIntervalUnit'] = TimeIntervalUnit
        if DesiredMinTXInterval is not None:
            properties['DesiredMinTXInterval'] = DesiredMinTXInterval
        if RequiredMinRXInterval is not None:
            properties['RequiredMinRXInterval'] = RequiredMinRXInterval
        if RequiredMinEchoRXInterval is not None:
            properties['RequiredMinEchoRXInterval'] = RequiredMinEchoRXInterval
        if DetectMultiple is not None:
            properties['DetectMultiple'] = DetectMultiple
        if AuthenticationType is not None:
            properties['AuthenticationType'] = AuthenticationType
        if Password is not None:
            properties['Password'] = Password
        if KeyID is not None:
            properties['KeyID'] = KeyID

        # call base class function, and it will send message to renix server to create a class.
        super(BfdProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RouterRole=None, TimeIntervalUnit=None, DesiredMinTXInterval=None, RequiredMinRXInterval=None, RequiredMinEchoRXInterval=None, DetectMultiple=None, AuthenticationType=None, Password=None, KeyID=None, **kwargs):
        properties = kwargs.copy()
        if RouterRole is not None:
            self._RouterRole = RouterRole
            properties['RouterRole'] = RouterRole
        if TimeIntervalUnit is not None:
            self._TimeIntervalUnit = TimeIntervalUnit
            properties['TimeIntervalUnit'] = TimeIntervalUnit
        if DesiredMinTXInterval is not None:
            self._DesiredMinTXInterval = DesiredMinTXInterval
            properties['DesiredMinTXInterval'] = DesiredMinTXInterval
        if RequiredMinRXInterval is not None:
            self._RequiredMinRXInterval = RequiredMinRXInterval
            properties['RequiredMinRXInterval'] = RequiredMinRXInterval
        if RequiredMinEchoRXInterval is not None:
            self._RequiredMinEchoRXInterval = RequiredMinEchoRXInterval
            properties['RequiredMinEchoRXInterval'] = RequiredMinEchoRXInterval
        if DetectMultiple is not None:
            self._DetectMultiple = DetectMultiple
            properties['DetectMultiple'] = DetectMultiple
        if AuthenticationType is not None:
            self._AuthenticationType = AuthenticationType
            properties['AuthenticationType'] = AuthenticationType
        if Password is not None:
            self._Password = Password
            properties['Password'] = Password
        if KeyID is not None:
            self._KeyID = KeyID
            properties['KeyID'] = KeyID

        super(BfdProtocolConfig, self).edit(**properties)

    @property
    def RouterRole(self):
        """
        get the value of property _RouterRole
        """
        if self.force_auto_sync:
            self.get('RouterRole')
        return self._RouterRole

    @property
    def ProtocolState(self):
        """
        get the value of property _ProtocolState
        """
        if self.force_auto_sync:
            self.get('ProtocolState')
        return self._ProtocolState

    @property
    def BFDSessionUpCount(self):
        """
        get the value of property _BFDSessionUpCount
        """
        if self.force_auto_sync:
            self.get('BFDSessionUpCount')
        return self._BFDSessionUpCount

    @property
    def BFDSessionDownCount(self):
        """
        get the value of property _BFDSessionDownCount
        """
        if self.force_auto_sync:
            self.get('BFDSessionDownCount')
        return self._BFDSessionDownCount

    @property
    def TimeIntervalUnit(self):
        """
        get the value of property _TimeIntervalUnit
        """
        if self.force_auto_sync:
            self.get('TimeIntervalUnit')
        return self._TimeIntervalUnit

    @property
    def DesiredMinTXInterval(self):
        """
        get the value of property _DesiredMinTXInterval
        """
        if self.force_auto_sync:
            self.get('DesiredMinTXInterval')
        return self._DesiredMinTXInterval

    @property
    def RequiredMinRXInterval(self):
        """
        get the value of property _RequiredMinRXInterval
        """
        if self.force_auto_sync:
            self.get('RequiredMinRXInterval')
        return self._RequiredMinRXInterval

    @property
    def RequiredMinEchoRXInterval(self):
        """
        get the value of property _RequiredMinEchoRXInterval
        """
        if self.force_auto_sync:
            self.get('RequiredMinEchoRXInterval')
        return self._RequiredMinEchoRXInterval

    @property
    def DetectMultiple(self):
        """
        get the value of property _DetectMultiple
        """
        if self.force_auto_sync:
            self.get('DetectMultiple')
        return self._DetectMultiple

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
    def ProtocolDependentSession(self):
        """
        get the value of property _ProtocolDependentSession
        """
        if self.force_auto_sync:
            self.get('ProtocolDependentSession')
        return self._ProtocolDependentSession

    @property
    def Ipv4ControlPlaneIndependentSessionCount(self):
        """
        get the value of property _Ipv4ControlPlaneIndependentSessionCount
        """
        if self.force_auto_sync:
            self.get('Ipv4ControlPlaneIndependentSessionCount')
        return self._Ipv4ControlPlaneIndependentSessionCount

    @property
    def Ipv6ControlPlaneIndependentSessionCount(self):
        """
        get the value of property _Ipv6ControlPlaneIndependentSessionCount
        """
        if self.force_auto_sync:
            self.get('Ipv6ControlPlaneIndependentSessionCount')
        return self._Ipv6ControlPlaneIndependentSessionCount

    @RouterRole.setter
    def RouterRole(self, value):
        self._RouterRole = value
        self.edit(RouterRole=value)

    @TimeIntervalUnit.setter
    def TimeIntervalUnit(self, value):
        self._TimeIntervalUnit = value
        self.edit(TimeIntervalUnit=value)

    @DesiredMinTXInterval.setter
    def DesiredMinTXInterval(self, value):
        self._DesiredMinTXInterval = value
        self.edit(DesiredMinTXInterval=value)

    @RequiredMinRXInterval.setter
    def RequiredMinRXInterval(self, value):
        self._RequiredMinRXInterval = value
        self.edit(RequiredMinRXInterval=value)

    @RequiredMinEchoRXInterval.setter
    def RequiredMinEchoRXInterval(self, value):
        self._RequiredMinEchoRXInterval = value
        self.edit(RequiredMinEchoRXInterval=value)

    @DetectMultiple.setter
    def DetectMultiple(self, value):
        self._DetectMultiple = value
        self.edit(DetectMultiple=value)

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

    def _set_routerrole_with_str(self, value):
        seperate = value.find(':')
        exec('self._RouterRole = BfdRouterRoleEnum.%s' % value[:seperate])

    def _set_protocolstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._ProtocolState = BfdProtocolStateEnum.%s' % value[:seperate])

    def _set_bfdsessionupcount_with_str(self, value):
        try:
            self._BFDSessionUpCount = int(value)
        except ValueError:
            self._BFDSessionUpCount = hex(int(value, 16))

    def _set_bfdsessiondowncount_with_str(self, value):
        try:
            self._BFDSessionDownCount = int(value)
        except ValueError:
            self._BFDSessionDownCount = hex(int(value, 16))

    def _set_timeintervalunit_with_str(self, value):
        seperate = value.find(':')
        exec('self._TimeIntervalUnit = BfdTimeIntervalUnitEnum.%s' % value[:seperate])

    def _set_desiredmintxinterval_with_str(self, value):
        try:
            self._DesiredMinTXInterval = int(value)
        except ValueError:
            self._DesiredMinTXInterval = hex(int(value, 16))

    def _set_requiredminrxinterval_with_str(self, value):
        try:
            self._RequiredMinRXInterval = int(value)
        except ValueError:
            self._RequiredMinRXInterval = hex(int(value, 16))

    def _set_requiredminechorxinterval_with_str(self, value):
        try:
            self._RequiredMinEchoRXInterval = int(value)
        except ValueError:
            self._RequiredMinEchoRXInterval = hex(int(value, 16))

    def _set_detectmultiple_with_str(self, value):
        try:
            self._DetectMultiple = int(value)
        except ValueError:
            self._DetectMultiple = hex(int(value, 16))

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

    def _set_protocoldependentsession_with_str(self, value):
        seperate = value.find(':')
        exec('self._ProtocolDependentSession = BfdProtocolDependentSessionEnum.%s' % value[:seperate])

    def _set_ipv4controlplaneindependentsessioncount_with_str(self, value):
        try:
            self._Ipv4ControlPlaneIndependentSessionCount = int(value)
        except ValueError:
            self._Ipv4ControlPlaneIndependentSessionCount = hex(int(value, 16))

    def _set_ipv6controlplaneindependentsessioncount_with_str(self, value):
        try:
            self._Ipv6ControlPlaneIndependentSessionCount = int(value)
        except ValueError:
            self._Ipv6ControlPlaneIndependentSessionCount = hex(int(value, 16))

