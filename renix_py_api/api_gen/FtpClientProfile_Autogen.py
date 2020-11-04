"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L47ClientProfile_Autogen import L47ClientProfile


@rom_manager.rom
class FtpClientProfile(L47ClientProfile):
    def __init__(self, UserName=None, Password=None, LoginMode=None, VlanPriority=None, Tos=None, TrafficClass=None, **kwargs):
        self._UserName = UserName  # User Name
        self._Password = Password  # Password
        self._LoginMode = LoginMode  # Login Mode
        self._VlanPriority = VlanPriority  # VLAN Priority
        self._Tos = Tos  # ToS/DSCP
        self._TrafficClass = TrafficClass  # Traffic Class

        properties = kwargs.copy()
        if UserName is not None:
            properties['UserName'] = UserName
        if Password is not None:
            properties['Password'] = Password
        if LoginMode is not None:
            properties['LoginMode'] = LoginMode
        if VlanPriority is not None:
            properties['VlanPriority'] = VlanPriority
        if Tos is not None:
            properties['Tos'] = Tos
        if TrafficClass is not None:
            properties['TrafficClass'] = TrafficClass

        # call base class function, and it will send message to renix server to create a class.
        super(FtpClientProfile, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, UserName=None, Password=None, LoginMode=None, VlanPriority=None, Tos=None, TrafficClass=None, **kwargs):
        properties = kwargs.copy()
        if UserName is not None:
            self._UserName = UserName
            properties['UserName'] = UserName
        if Password is not None:
            self._Password = Password
            properties['Password'] = Password
        if LoginMode is not None:
            self._LoginMode = LoginMode
            properties['LoginMode'] = LoginMode
        if VlanPriority is not None:
            self._VlanPriority = VlanPriority
            properties['VlanPriority'] = VlanPriority
        if Tos is not None:
            self._Tos = Tos
            properties['Tos'] = Tos
        if TrafficClass is not None:
            self._TrafficClass = TrafficClass
            properties['TrafficClass'] = TrafficClass

        super(FtpClientProfile, self).edit(**properties)

    @property
    def UserName(self):
        """
        get the value of property _UserName
        """
        if self.force_auto_sync:
            self.get('UserName')
        return self._UserName

    @property
    def Password(self):
        """
        get the value of property _Password
        """
        if self.force_auto_sync:
            self.get('Password')
        return self._Password

    @property
    def LoginMode(self):
        """
        get the value of property _LoginMode
        """
        if self.force_auto_sync:
            self.get('LoginMode')
        return self._LoginMode

    @property
    def VlanPriority(self):
        """
        get the value of property _VlanPriority
        """
        if self.force_auto_sync:
            self.get('VlanPriority')
        return self._VlanPriority

    @property
    def Tos(self):
        """
        get the value of property _Tos
        """
        if self.force_auto_sync:
            self.get('Tos')
        return self._Tos

    @property
    def TrafficClass(self):
        """
        get the value of property _TrafficClass
        """
        if self.force_auto_sync:
            self.get('TrafficClass')
        return self._TrafficClass

    @UserName.setter
    def UserName(self, value):
        self._UserName = value
        self.edit(UserName=value)

    @Password.setter
    def Password(self, value):
        self._Password = value
        self.edit(Password=value)

    @LoginMode.setter
    def LoginMode(self, value):
        self._LoginMode = value
        self.edit(LoginMode=value)

    @VlanPriority.setter
    def VlanPriority(self, value):
        self._VlanPriority = value
        self.edit(VlanPriority=value)

    @Tos.setter
    def Tos(self, value):
        self._Tos = value
        self.edit(Tos=value)

    @TrafficClass.setter
    def TrafficClass(self, value):
        self._TrafficClass = value
        self.edit(TrafficClass=value)

    def _set_username_with_str(self, value):
        self._UserName = value

    def _set_password_with_str(self, value):
        self._Password = value

    def _set_loginmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoginMode = EnumLoginMode.%s' % value[:seperate])

    def _set_vlanpriority_with_str(self, value):
        try:
            self._VlanPriority = int(value)
        except ValueError:
            self._VlanPriority = hex(int(value, 16))

    def _set_tos_with_str(self, value):
        try:
            self._Tos = int(value)
        except ValueError:
            self._Tos = hex(int(value, 16))

    def _set_trafficclass_with_str(self, value):
        try:
            self._TrafficClass = int(value)
        except ValueError:
            self._TrafficClass = hex(int(value, 16))

