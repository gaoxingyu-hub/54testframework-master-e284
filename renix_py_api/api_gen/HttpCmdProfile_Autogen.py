"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class HttpCmdProfile(ROMObject):
    def __init__(self, AuthType=None, UserName=None, Password=None, **kwargs):
        self._AuthType = AuthType  # Auth Type
        self._UserName = UserName  # User Name
        self._Password = Password  # Password

        properties = kwargs.copy()
        if AuthType is not None:
            properties['AuthType'] = AuthType
        if UserName is not None:
            properties['UserName'] = UserName
        if Password is not None:
            properties['Password'] = Password

        # call base class function, and it will send message to renix server to create a class.
        super(HttpCmdProfile, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AuthType=None, UserName=None, Password=None, **kwargs):
        properties = kwargs.copy()
        if AuthType is not None:
            self._AuthType = AuthType
            properties['AuthType'] = AuthType
        if UserName is not None:
            self._UserName = UserName
            properties['UserName'] = UserName
        if Password is not None:
            self._Password = Password
            properties['Password'] = Password

        super(HttpCmdProfile, self).edit(**properties)

    @property
    def AuthType(self):
        """
        get the value of property _AuthType
        """
        if self.force_auto_sync:
            self.get('AuthType')
        return self._AuthType

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

    @AuthType.setter
    def AuthType(self, value):
        self._AuthType = value
        self.edit(AuthType=value)

    @UserName.setter
    def UserName(self, value):
        self._UserName = value
        self.edit(UserName=value)

    @Password.setter
    def Password(self, value):
        self._Password = value
        self.edit(Password=value)

    def _set_authtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._AuthType = EnumHttpAuthType.%s' % value[:seperate])

    def _set_username_with_str(self, value):
        self._UserName = value

    def _set_password_with_str(self, value):
        self._Password = value

