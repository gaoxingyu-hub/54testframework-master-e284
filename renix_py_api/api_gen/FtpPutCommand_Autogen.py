"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L47Command_Autogen import L47Command


@rom_manager.rom
class FtpPutCommand(L47Command):
    def __init__(self, DestAddress=None, DestPort=None, UserName=None, Password=None, FileName=None, **kwargs):
        self._DestAddress = DestAddress  # FTP Server Address
        self._DestPort = DestPort  # FTP Server Port
        self._UserName = UserName  # User Name
        self._Password = Password  # Password
        self._FileName = FileName  # File Name

        properties = kwargs.copy()
        if DestAddress is not None:
            properties['DestAddress'] = DestAddress
        if DestPort is not None:
            properties['DestPort'] = DestPort
        if UserName is not None:
            properties['UserName'] = UserName
        if Password is not None:
            properties['Password'] = Password
        if FileName is not None:
            properties['FileName'] = FileName

        # call base class function, and it will send message to renix server to create a class.
        super(FtpPutCommand, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, DestAddress=None, DestPort=None, UserName=None, Password=None, FileName=None, **kwargs):
        properties = kwargs.copy()
        if DestAddress is not None:
            self._DestAddress = DestAddress
            properties['DestAddress'] = DestAddress
        if DestPort is not None:
            self._DestPort = DestPort
            properties['DestPort'] = DestPort
        if UserName is not None:
            self._UserName = UserName
            properties['UserName'] = UserName
        if Password is not None:
            self._Password = Password
            properties['Password'] = Password
        if FileName is not None:
            self._FileName = FileName
            properties['FileName'] = FileName

        super(FtpPutCommand, self).edit(**properties)

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
    def FileName(self):
        """
        get the value of property _FileName
        """
        if self.force_auto_sync:
            self.get('FileName')
        return self._FileName

    @DestAddress.setter
    def DestAddress(self, value):
        self._DestAddress = value
        self.edit(DestAddress=value)

    @DestPort.setter
    def DestPort(self, value):
        self._DestPort = value
        self.edit(DestPort=value)

    @UserName.setter
    def UserName(self, value):
        self._UserName = value
        self.edit(UserName=value)

    @Password.setter
    def Password(self, value):
        self._Password = value
        self.edit(Password=value)

    @FileName.setter
    def FileName(self, value):
        self._FileName = value
        self.edit(FileName=value)

    def _set_destaddress_with_str(self, value):
        self._DestAddress = value

    def _set_destport_with_str(self, value):
        try:
            self._DestPort = int(value)
        except ValueError:
            self._DestPort = hex(int(value, 16))

    def _set_username_with_str(self, value):
        self._UserName = value

    def _set_password_with_str(self, value):
        self._Password = value

    def _set_filename_with_str(self, value):
        self._FileName = value

