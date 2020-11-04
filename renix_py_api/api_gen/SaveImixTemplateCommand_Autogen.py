"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SaveImixTemplateCommand(ROMCommand):
    def __init__(self, ImixHandle=None, FilePath=None, FileName=None, **kwargs):
        self._ImixHandle = ImixHandle  # iMIX Handle
        self._FilePath = FilePath  # Import iMIX Template File Path
        self._FileName = FileName  # Import iMIX Template File Name
        self._ImixFilePath = ''  # Saved iMIX Template File, not editable

        properties = kwargs.copy()
        if ImixHandle is not None:
            properties['ImixHandle'] = ImixHandle
        if FilePath is not None:
            properties['FilePath'] = FilePath
        if FileName is not None:
            properties['FileName'] = FileName

        # call base class function, and it will send message to renix server to create a class.
        super(SaveImixTemplateCommand, self).__init__(**properties)

    @property
    def ImixHandle(self):
        """
        get the value of property _ImixHandle
        """
        return self._ImixHandle

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
    def ImixFilePath(self):
        """
        get the value of property _ImixFilePath
        """
        return self._ImixFilePath

    @ImixHandle.setter
    def ImixHandle(self, value):
        self._ImixHandle = value

    @FilePath.setter
    def FilePath(self, value):
        self._FilePath = value

    @FileName.setter
    def FileName(self, value):
        self._FileName = value

    def _set_imixhandle_with_str(self, value):
        self._ImixHandle = value

    def _set_filepath_with_str(self, value):
        self._FilePath = value

    def _set_filename_with_str(self, value):
        self._FileName = value

    def _set_imixfilepath_with_str(self, value):
        self._ImixFilePath = value

    def _set_output_property(self, value):
        self._set_imixfilepath_with_str(value)

