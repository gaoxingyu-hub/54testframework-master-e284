"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class OpenImixTemplateCommand(ROMCommand):
    def __init__(self, FilePath=None, FileName=None, FullFileName=None, **kwargs):
        self._FilePath = FilePath  # Import iMIX Template File Path
        self._FileName = FileName  # Import iMIX Template File Name
        self._FullFileName = FullFileName  # Import iMIX Template File Name

        properties = kwargs.copy()
        if FilePath is not None:
            properties['FilePath'] = FilePath
        if FileName is not None:
            properties['FileName'] = FileName
        if FullFileName is not None:
            properties['FullFileName'] = FullFileName

        # call base class function, and it will send message to renix server to create a class.
        super(OpenImixTemplateCommand, self).__init__(**properties)

    @property
    def FilePath(self):
        """
        get the value of property _FilePath
        """
        return self._FilePath

    @property
    def FileName(self):
        """
        get the value of property _FileName
        """
        return self._FileName

    @property
    def FullFileName(self):
        """
        get the value of property _FullFileName
        """
        return self._FullFileName

    @FilePath.setter
    def FilePath(self, value):
        self._FilePath = value

    @FileName.setter
    def FileName(self, value):
        self._FileName = value

    @FullFileName.setter
    def FullFileName(self, value):
        self._FullFileName = value

    def _set_filepath_with_str(self, value):
        self._FilePath = value

    def _set_filename_with_str(self, value):
        self._FileName = value

    def _set_fullfilename_with_str(self, value):
        self._FullFileName = value

