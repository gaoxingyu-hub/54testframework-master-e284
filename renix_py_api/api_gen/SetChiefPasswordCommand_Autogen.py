"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SetChiefPasswordCommand(ROMCommand):
    def __init__(self, Password=None, **kwargs):
        self._Password = Password  # Chief user password

        properties = kwargs.copy()
        if Password is not None:
            properties['Password'] = Password

        # call base class function, and it will send message to renix server to create a class.
        super(SetChiefPasswordCommand, self).__init__(**properties)

    @property
    def Password(self):
        """
        get the value of property _Password
        """
        return self._Password

    @Password.setter
    def Password(self, value):
        self._Password = value

    def _set_password_with_str(self, value):
        self._Password = value

