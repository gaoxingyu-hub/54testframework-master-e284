"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dot1xPortConfig(ROMObject):
    def __init__(self, AuthenticationRate=None, LogoutRate=None, OutstandingSessions=None, **kwargs):
        self._AuthenticationRate = AuthenticationRate  # Authentication Rate
        self._LogoutRate = LogoutRate  # Logout Rate
        self._OutstandingSessions = OutstandingSessions  # Outstanding Sessions

        properties = kwargs.copy()
        if AuthenticationRate is not None:
            properties['AuthenticationRate'] = AuthenticationRate
        if LogoutRate is not None:
            properties['LogoutRate'] = LogoutRate
        if OutstandingSessions is not None:
            properties['OutstandingSessions'] = OutstandingSessions

        # call base class function, and it will send message to renix server to create a class.
        super(Dot1xPortConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AuthenticationRate=None, LogoutRate=None, OutstandingSessions=None, **kwargs):
        properties = kwargs.copy()
        if AuthenticationRate is not None:
            self._AuthenticationRate = AuthenticationRate
            properties['AuthenticationRate'] = AuthenticationRate
        if LogoutRate is not None:
            self._LogoutRate = LogoutRate
            properties['LogoutRate'] = LogoutRate
        if OutstandingSessions is not None:
            self._OutstandingSessions = OutstandingSessions
            properties['OutstandingSessions'] = OutstandingSessions

        super(Dot1xPortConfig, self).edit(**properties)

    @property
    def AuthenticationRate(self):
        """
        get the value of property _AuthenticationRate
        """
        if self.force_auto_sync:
            self.get('AuthenticationRate')
        return self._AuthenticationRate

    @property
    def LogoutRate(self):
        """
        get the value of property _LogoutRate
        """
        if self.force_auto_sync:
            self.get('LogoutRate')
        return self._LogoutRate

    @property
    def OutstandingSessions(self):
        """
        get the value of property _OutstandingSessions
        """
        if self.force_auto_sync:
            self.get('OutstandingSessions')
        return self._OutstandingSessions

    @AuthenticationRate.setter
    def AuthenticationRate(self, value):
        self._AuthenticationRate = value
        self.edit(AuthenticationRate=value)

    @LogoutRate.setter
    def LogoutRate(self, value):
        self._LogoutRate = value
        self.edit(LogoutRate=value)

    @OutstandingSessions.setter
    def OutstandingSessions(self, value):
        self._OutstandingSessions = value
        self.edit(OutstandingSessions=value)

    def _set_authenticationrate_with_str(self, value):
        try:
            self._AuthenticationRate = int(value)
        except ValueError:
            self._AuthenticationRate = hex(int(value, 16))

    def _set_logoutrate_with_str(self, value):
        try:
            self._LogoutRate = int(value)
        except ValueError:
            self._LogoutRate = hex(int(value, 16))

    def _set_outstandingsessions_with_str(self, value):
        try:
            self._OutstandingSessions = int(value)
        except ValueError:
            self._OutstandingSessions = hex(int(value, 16))

