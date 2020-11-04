"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .HttpCommand_Autogen import HttpCommand


@rom_manager.rom
class HttpHeaderCommand(HttpCommand):
    def __init__(self, NameValueArgs=None, **kwargs):
        self._NameValueArgs = NameValueArgs  # NameValueArgs

        properties = kwargs.copy()
        if NameValueArgs is not None:
            properties['NameValueArgs'] = NameValueArgs

        # call base class function, and it will send message to renix server to create a class.
        super(HttpHeaderCommand, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, NameValueArgs=None, **kwargs):
        properties = kwargs.copy()
        if NameValueArgs is not None:
            self._NameValueArgs = NameValueArgs
            properties['NameValueArgs'] = NameValueArgs

        super(HttpHeaderCommand, self).edit(**properties)

    @property
    def NameValueArgs(self):
        """
        get the value of property _NameValueArgs
        """
        if self.force_auto_sync:
            self.get('NameValueArgs')
        return self._NameValueArgs

    @NameValueArgs.setter
    def NameValueArgs(self, value):
        self._NameValueArgs = value
        self.edit(NameValueArgs=value)

    def _set_namevalueargs_with_str(self, value):
        self._NameValueArgs = value

