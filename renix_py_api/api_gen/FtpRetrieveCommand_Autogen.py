"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L47Command_Autogen import L47Command


@rom_manager.rom
class FtpRetrieveCommand(L47Command):
    def __init__(self, FileName=None, **kwargs):
        self._FileName = FileName  # File Name

        properties = kwargs.copy()
        if FileName is not None:
            properties['FileName'] = FileName

        # call base class function, and it will send message to renix server to create a class.
        super(FtpRetrieveCommand, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, FileName=None, **kwargs):
        properties = kwargs.copy()
        if FileName is not None:
            self._FileName = FileName
            properties['FileName'] = FileName

        super(FtpRetrieveCommand, self).edit(**properties)

    @property
    def FileName(self):
        """
        get the value of property _FileName
        """
        if self.force_auto_sync:
            self.get('FileName')
        return self._FileName

    @FileName.setter
    def FileName(self, value):
        self._FileName = value
        self.edit(FileName=value)

    def _set_filename_with_str(self, value):
        self._FileName = value

