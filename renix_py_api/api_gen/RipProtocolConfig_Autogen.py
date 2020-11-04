"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class RipProtocolConfig(L23ProtocolConfig):
    def __init__(self, Version=None, UpdateType=None, DutIpv4Address=None, DutIpv6Address=None, AuthMethod=None, Password=None, Md5KeyId=None, UpdateInterval=None, UpdateJitter=None, MaxRoutePerUpdate=None, SplitHorizon=None, EnableViewRoutes=None, EnableIpAddrValidation=None, **kwargs):
        self._ProtocolState = EnumProtocolState.DISABLE  # Protocol State, not editable
        self._Version = Version  # RIP Version
        self._UpdateType = UpdateType  # Update Type
        self._DutIpv4Address = DutIpv4Address  # DUT IPv4 Address
        self._DutIpv6Address = DutIpv6Address  # DUT IPv6 Address
        self._AuthMethod = AuthMethod  # Authentication
        self._Password = Password  # Password
        self._Md5KeyId = Md5KeyId  # MD5 Key ID
        self._UpdateInterval = UpdateInterval  # Update Interval (sec)
        self._UpdateJitter = UpdateJitter  # Update Jitter
        self._MaxRoutePerUpdate = MaxRoutePerUpdate  # Max Route Per Update
        self._SplitHorizon = SplitHorizon  # Enable Split Horizon
        self._EnableViewRoutes = EnableViewRoutes  # Enable View Routes
        self._EnableIpAddrValidation = EnableIpAddrValidation  # Validate Interface IP Address
        self._Ipv4RouteCount = 0  # IPv4 Route Count, not editable
        self._Ipv6RouteCount = 0  # IPv6 Route Count, not editable

        properties = kwargs.copy()
        if Version is not None:
            properties['Version'] = Version
        if UpdateType is not None:
            properties['UpdateType'] = UpdateType
        if DutIpv4Address is not None:
            properties['DutIpv4Address'] = DutIpv4Address
        if DutIpv6Address is not None:
            properties['DutIpv6Address'] = DutIpv6Address
        if AuthMethod is not None:
            properties['AuthMethod'] = AuthMethod
        if Password is not None:
            properties['Password'] = Password
        if Md5KeyId is not None:
            properties['Md5KeyId'] = Md5KeyId
        if UpdateInterval is not None:
            properties['UpdateInterval'] = UpdateInterval
        if UpdateJitter is not None:
            properties['UpdateJitter'] = UpdateJitter
        if MaxRoutePerUpdate is not None:
            properties['MaxRoutePerUpdate'] = MaxRoutePerUpdate
        if SplitHorizon is not None:
            properties['SplitHorizon'] = SplitHorizon
        if EnableViewRoutes is not None:
            properties['EnableViewRoutes'] = EnableViewRoutes
        if EnableIpAddrValidation is not None:
            properties['EnableIpAddrValidation'] = EnableIpAddrValidation

        # call base class function, and it will send message to renix server to create a class.
        super(RipProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Version=None, UpdateType=None, DutIpv4Address=None, DutIpv6Address=None, AuthMethod=None, Password=None, Md5KeyId=None, UpdateInterval=None, UpdateJitter=None, MaxRoutePerUpdate=None, SplitHorizon=None, EnableViewRoutes=None, EnableIpAddrValidation=None, **kwargs):
        properties = kwargs.copy()
        if Version is not None:
            self._Version = Version
            properties['Version'] = Version
        if UpdateType is not None:
            self._UpdateType = UpdateType
            properties['UpdateType'] = UpdateType
        if DutIpv4Address is not None:
            self._DutIpv4Address = DutIpv4Address
            properties['DutIpv4Address'] = DutIpv4Address
        if DutIpv6Address is not None:
            self._DutIpv6Address = DutIpv6Address
            properties['DutIpv6Address'] = DutIpv6Address
        if AuthMethod is not None:
            self._AuthMethod = AuthMethod
            properties['AuthMethod'] = AuthMethod
        if Password is not None:
            self._Password = Password
            properties['Password'] = Password
        if Md5KeyId is not None:
            self._Md5KeyId = Md5KeyId
            properties['Md5KeyId'] = Md5KeyId
        if UpdateInterval is not None:
            self._UpdateInterval = UpdateInterval
            properties['UpdateInterval'] = UpdateInterval
        if UpdateJitter is not None:
            self._UpdateJitter = UpdateJitter
            properties['UpdateJitter'] = UpdateJitter
        if MaxRoutePerUpdate is not None:
            self._MaxRoutePerUpdate = MaxRoutePerUpdate
            properties['MaxRoutePerUpdate'] = MaxRoutePerUpdate
        if SplitHorizon is not None:
            self._SplitHorizon = SplitHorizon
            properties['SplitHorizon'] = SplitHorizon
        if EnableViewRoutes is not None:
            self._EnableViewRoutes = EnableViewRoutes
            properties['EnableViewRoutes'] = EnableViewRoutes
        if EnableIpAddrValidation is not None:
            self._EnableIpAddrValidation = EnableIpAddrValidation
            properties['EnableIpAddrValidation'] = EnableIpAddrValidation

        super(RipProtocolConfig, self).edit(**properties)

    @property
    def ProtocolState(self):
        """
        get the value of property _ProtocolState
        """
        if self.force_auto_sync:
            self.get('ProtocolState')
        return self._ProtocolState

    @property
    def Version(self):
        """
        get the value of property _Version
        """
        if self.force_auto_sync:
            self.get('Version')
        return self._Version

    @property
    def UpdateType(self):
        """
        get the value of property _UpdateType
        """
        if self.force_auto_sync:
            self.get('UpdateType')
        return self._UpdateType

    @property
    def DutIpv4Address(self):
        """
        get the value of property _DutIpv4Address
        """
        if self.force_auto_sync:
            self.get('DutIpv4Address')
        return self._DutIpv4Address

    @property
    def DutIpv6Address(self):
        """
        get the value of property _DutIpv6Address
        """
        if self.force_auto_sync:
            self.get('DutIpv6Address')
        return self._DutIpv6Address

    @property
    def AuthMethod(self):
        """
        get the value of property _AuthMethod
        """
        if self.force_auto_sync:
            self.get('AuthMethod')
        return self._AuthMethod

    @property
    def Password(self):
        """
        get the value of property _Password
        """
        if self.force_auto_sync:
            self.get('Password')
        return self._Password

    @property
    def Md5KeyId(self):
        """
        get the value of property _Md5KeyId
        """
        if self.force_auto_sync:
            self.get('Md5KeyId')
        return self._Md5KeyId

    @property
    def UpdateInterval(self):
        """
        get the value of property _UpdateInterval
        """
        if self.force_auto_sync:
            self.get('UpdateInterval')
        return self._UpdateInterval

    @property
    def UpdateJitter(self):
        """
        get the value of property _UpdateJitter
        """
        if self.force_auto_sync:
            self.get('UpdateJitter')
        return self._UpdateJitter

    @property
    def MaxRoutePerUpdate(self):
        """
        get the value of property _MaxRoutePerUpdate
        """
        if self.force_auto_sync:
            self.get('MaxRoutePerUpdate')
        return self._MaxRoutePerUpdate

    @property
    def SplitHorizon(self):
        """
        get the value of property _SplitHorizon
        """
        if self.force_auto_sync:
            self.get('SplitHorizon')
        return self._SplitHorizon

    @property
    def EnableViewRoutes(self):
        """
        get the value of property _EnableViewRoutes
        """
        if self.force_auto_sync:
            self.get('EnableViewRoutes')
        return self._EnableViewRoutes

    @property
    def EnableIpAddrValidation(self):
        """
        get the value of property _EnableIpAddrValidation
        """
        if self.force_auto_sync:
            self.get('EnableIpAddrValidation')
        return self._EnableIpAddrValidation

    @property
    def Ipv4RouteCount(self):
        """
        get the value of property _Ipv4RouteCount
        """
        if self.force_auto_sync:
            self.get('Ipv4RouteCount')
        return self._Ipv4RouteCount

    @property
    def Ipv6RouteCount(self):
        """
        get the value of property _Ipv6RouteCount
        """
        if self.force_auto_sync:
            self.get('Ipv6RouteCount')
        return self._Ipv6RouteCount

    @Version.setter
    def Version(self, value):
        self._Version = value
        self.edit(Version=value)

    @UpdateType.setter
    def UpdateType(self, value):
        self._UpdateType = value
        self.edit(UpdateType=value)

    @DutIpv4Address.setter
    def DutIpv4Address(self, value):
        self._DutIpv4Address = value
        self.edit(DutIpv4Address=value)

    @DutIpv6Address.setter
    def DutIpv6Address(self, value):
        self._DutIpv6Address = value
        self.edit(DutIpv6Address=value)

    @AuthMethod.setter
    def AuthMethod(self, value):
        self._AuthMethod = value
        self.edit(AuthMethod=value)

    @Password.setter
    def Password(self, value):
        self._Password = value
        self.edit(Password=value)

    @Md5KeyId.setter
    def Md5KeyId(self, value):
        self._Md5KeyId = value
        self.edit(Md5KeyId=value)

    @UpdateInterval.setter
    def UpdateInterval(self, value):
        self._UpdateInterval = value
        self.edit(UpdateInterval=value)

    @UpdateJitter.setter
    def UpdateJitter(self, value):
        self._UpdateJitter = value
        self.edit(UpdateJitter=value)

    @MaxRoutePerUpdate.setter
    def MaxRoutePerUpdate(self, value):
        self._MaxRoutePerUpdate = value
        self.edit(MaxRoutePerUpdate=value)

    @SplitHorizon.setter
    def SplitHorizon(self, value):
        self._SplitHorizon = value
        self.edit(SplitHorizon=value)

    @EnableViewRoutes.setter
    def EnableViewRoutes(self, value):
        self._EnableViewRoutes = value
        self.edit(EnableViewRoutes=value)

    @EnableIpAddrValidation.setter
    def EnableIpAddrValidation(self, value):
        self._EnableIpAddrValidation = value
        self.edit(EnableIpAddrValidation=value)

    def _set_protocolstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._ProtocolState = EnumProtocolState.%s' % value[:seperate])

    def _set_version_with_str(self, value):
        seperate = value.find(':')
        exec('self._Version = EnumRipVersion.%s' % value[:seperate])

    def _set_updatetype_with_str(self, value):
        seperate = value.find(':')
        exec('self._UpdateType = EnumUpdateType.%s' % value[:seperate])

    def _set_dutipv4address_with_str(self, value):
        self._DutIpv4Address = value

    def _set_dutipv6address_with_str(self, value):
        self._DutIpv6Address = value

    def _set_authmethod_with_str(self, value):
        seperate = value.find(':')
        exec('self._AuthMethod = EnumRipAuthMethod.%s' % value[:seperate])

    def _set_password_with_str(self, value):
        self._Password = value

    def _set_md5keyid_with_str(self, value):
        try:
            self._Md5KeyId = int(value)
        except ValueError:
            self._Md5KeyId = hex(int(value, 16))

    def _set_updateinterval_with_str(self, value):
        try:
            self._UpdateInterval = int(value)
        except ValueError:
            self._UpdateInterval = hex(int(value, 16))

    def _set_updatejitter_with_str(self, value):
        try:
            self._UpdateJitter = int(value)
        except ValueError:
            self._UpdateJitter = hex(int(value, 16))

    def _set_maxrouteperupdate_with_str(self, value):
        try:
            self._MaxRoutePerUpdate = int(value)
        except ValueError:
            self._MaxRoutePerUpdate = hex(int(value, 16))

    def _set_splithorizon_with_str(self, value):
        self._SplitHorizon = (value == 'True')

    def _set_enableviewroutes_with_str(self, value):
        self._EnableViewRoutes = (value == 'True')

    def _set_enableipaddrvalidation_with_str(self, value):
        self._EnableIpAddrValidation = (value == 'True')

    def _set_ipv4routecount_with_str(self, value):
        try:
            self._Ipv4RouteCount = int(value)
        except ValueError:
            self._Ipv4RouteCount = hex(int(value, 16))

    def _set_ipv6routecount_with_str(self, value):
        try:
            self._Ipv6RouteCount = int(value)
        except ValueError:
            self._Ipv6RouteCount = hex(int(value, 16))

