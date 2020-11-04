"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L47Command_Autogen import L47Command


@rom_manager.rom
class HttpCommand(L47Command):
    def __init__(self, DestAddress=None, DestPort=None, Page=None, ConnectionType=None, AbortType=None, BaseAuthentication=None, UserName=None, Password=None, **kwargs):
        self._DestAddress = DestAddress  # HTTP Server Address or Name
        self._DestPort = DestPort  # HTTP Server Port
        self._Page = Page  # Page
        self._ConnectionType = ConnectionType  # Connection Type
        self._AbortType = AbortType  # AbortType
        self._BaseAuthentication = BaseAuthentication  # Enable Base Authentication
        self._UserName = UserName  # User Name
        self._Password = Password  # Password

        properties = kwargs.copy()
        if DestAddress is not None:
            properties['DestAddress'] = DestAddress
        if DestPort is not None:
            properties['DestPort'] = DestPort
        if Page is not None:
            properties['Page'] = Page
        if ConnectionType is not None:
            properties['ConnectionType'] = ConnectionType
        if AbortType is not None:
            properties['AbortType'] = AbortType
        if BaseAuthentication is not None:
            properties['BaseAuthentication'] = BaseAuthentication
        if UserName is not None:
            properties['UserName'] = UserName
        if Password is not None:
            properties['Password'] = Password

        # call base class function, and it will send message to renix server to create a class.
        super(HttpCommand, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, DestAddress=None, DestPort=None, Page=None, ConnectionType=None, AbortType=None, BaseAuthentication=None, UserName=None, Password=None, **kwargs):
        properties = kwargs.copy()
        if DestAddress is not None:
            self._DestAddress = DestAddress
            properties['DestAddress'] = DestAddress
        if DestPort is not None:
            self._DestPort = DestPort
            properties['DestPort'] = DestPort
        if Page is not None:
            self._Page = Page
            properties['Page'] = Page
        if ConnectionType is not None:
            self._ConnectionType = ConnectionType
            properties['ConnectionType'] = ConnectionType
        if AbortType is not None:
            self._AbortType = AbortType
            properties['AbortType'] = AbortType
        if BaseAuthentication is not None:
            self._BaseAuthentication = BaseAuthentication
            properties['BaseAuthentication'] = BaseAuthentication
        if UserName is not None:
            self._UserName = UserName
            properties['UserName'] = UserName
        if Password is not None:
            self._Password = Password
            properties['Password'] = Password

        super(HttpCommand, self).edit(**properties)

    @property
    def DestAddress(self):
        """
        get the value of property _DestAddress
        """
        if self.force_auto_sync:
            self.get('DestAddress')
        return self._DestAddress

    @property
    def DestPort(self):
        """
        get the value of property _DestPort
        """
        if self.force_auto_sync:
            self.get('DestPort')
        return self._DestPort

    @property
    def Page(self):
        """
        get the value of property _Page
        """
        if self.force_auto_sync:
            self.get('Page')
        return self._Page

    @property
    def ConnectionType(self):
        """
        get the value of property _ConnectionType
        """
        if self.force_auto_sync:
            self.get('ConnectionType')
        return self._ConnectionType

    @property
    def AbortType(self):
        """
        get the value of property _AbortType
        """
        if self.force_auto_sync:
            self.get('AbortType')
        return self._AbortType

    @property
    def BaseAuthentication(self):
        """
        get the value of property _BaseAuthentication
        """
        if self.force_auto_sync:
            self.get('BaseAuthentication')
        return self._BaseAuthentication

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

    @DestAddress.setter
    def DestAddress(self, value):
        self._DestAddress = value
        self.edit(DestAddress=value)

    @DestPort.setter
    def DestPort(self, value):
        self._DestPort = value
        self.edit(DestPort=value)

    @Page.setter
    def Page(self, value):
        self._Page = value
        self.edit(Page=value)

    @ConnectionType.setter
    def ConnectionType(self, value):
        self._ConnectionType = value
        self.edit(ConnectionType=value)

    @AbortType.setter
    def AbortType(self, value):
        self._AbortType = value
        self.edit(AbortType=value)

    @BaseAuthentication.setter
    def BaseAuthentication(self, value):
        self._BaseAuthentication = value
        self.edit(BaseAuthentication=value)

    @UserName.setter
    def UserName(self, value):
        self._UserName = value
        self.edit(UserName=value)

    @Password.setter
    def Password(self, value):
        self._Password = value
        self.edit(Password=value)

    def _set_destaddress_with_str(self, value):
        self._DestAddress = value

    def _set_destport_with_str(self, value):
        try:
            self._DestPort = int(value)
        except ValueError:
            self._DestPort = hex(int(value, 16))

    def _set_page_with_str(self, value):
        self._Page = value

    def _set_connectiontype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ConnectionType = EnumConnectionType.%s' % value[:seperate])

    def _set_aborttype_with_str(self, value):
        seperate = value.find(':')
        exec('self._AbortType = EnumCmdAbortType.%s' % value[:seperate])

    def _set_baseauthentication_with_str(self, value):
        self._BaseAuthentication = (value == 'True')

    def _set_username_with_str(self, value):
        self._UserName = value

    def _set_password_with_str(self, value):
        self._Password = value

