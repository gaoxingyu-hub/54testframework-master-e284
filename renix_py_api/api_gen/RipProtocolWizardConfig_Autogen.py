"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ProtocolWizardConfig_Autogen import ProtocolWizardConfig


@rom_manager.rom
class RipProtocolWizardConfig(ProtocolWizardConfig):
    def __init__(self, Version=None, UpdateType=None, AuthMethod=None, Password=None, Md5KeyId=None, UpdateInterval=None, UpdateJitter=None, MaxRoutePerUpdate=None, SplitHorizon=None, **kwargs):
        self._Version = Version  # RIP Version
        self._UpdateType = UpdateType  # Update Type
        self._AuthMethod = AuthMethod  # Authentication
        self._Password = Password  # Password
        self._Md5KeyId = Md5KeyId  # MD5 Key ID
        self._UpdateInterval = UpdateInterval  # Update Interval (sec)
        self._UpdateJitter = UpdateJitter  # Update Jitter
        self._MaxRoutePerUpdate = MaxRoutePerUpdate  # Max Route Per Update
        self._SplitHorizon = SplitHorizon  # Enable Split Horizon

        properties = kwargs.copy()
        if Version is not None:
            properties['Version'] = Version
        if UpdateType is not None:
            properties['UpdateType'] = UpdateType
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

        # call base class function, and it will send message to renix server to create a class.
        super(RipProtocolWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Version=None, UpdateType=None, AuthMethod=None, Password=None, Md5KeyId=None, UpdateInterval=None, UpdateJitter=None, MaxRoutePerUpdate=None, SplitHorizon=None, **kwargs):
        properties = kwargs.copy()
        if Version is not None:
            self._Version = Version
            properties['Version'] = Version
        if UpdateType is not None:
            self._UpdateType = UpdateType
            properties['UpdateType'] = UpdateType
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

        super(RipProtocolWizardConfig, self).edit(**properties)

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

    @Version.setter
    def Version(self, value):
        self._Version = value
        self.edit(Version=value)

    @UpdateType.setter
    def UpdateType(self, value):
        self._UpdateType = value
        self.edit(UpdateType=value)

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

    def _set_version_with_str(self, value):
        seperate = value.find(':')
        exec('self._Version = EnumRipVersion.%s' % value[:seperate])

    def _set_updatetype_with_str(self, value):
        seperate = value.find(':')
        exec('self._UpdateType = EnumUpdateType.%s' % value[:seperate])

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

