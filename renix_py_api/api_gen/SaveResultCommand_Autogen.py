"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SaveResultCommand(ROMCommand):
    def __init__(self, FileName=None, OverwriteExisting=None, **kwargs):
        self._FileName = FileName  # Save Result
        self._OverwriteExisting = OverwriteExisting  # Overwrite existing DB file
        self._ResultFile = ''  # Result File, not editable

        properties = kwargs.copy()
        if FileName is not None:
            properties['FileName'] = FileName
        if OverwriteExisting is not None:
            properties['OverwriteExisting'] = OverwriteExisting

        # call base class function, and it will send message to renix server to create a class.
        super(SaveResultCommand, self).__init__(**properties)

    @property
    def FileName(self):
        """
        get the value of property _FileName
        """
        return self._FileName

    @property
    def OverwriteExisting(self):
        """
        get the value of property _OverwriteExisting
        """
        return self._OverwriteExisting

    @property
    def ResultFile(self):
        """
        get the value of property _ResultFile
        """
        return self._ResultFile

    @FileName.setter
    def FileName(self, value):
        self._FileName = value

    @OverwriteExisting.setter
    def OverwriteExisting(self, value):
        self._OverwriteExisting = value

    def _set_filename_with_str(self, value):
        self._FileName = value

    def _set_overwriteexisting_with_str(self, value):
        self._OverwriteExisting = (value == 'True')

    def _set_resultfile_with_str(self, value):
        self._ResultFile = value

    def _set_output_property(self, value):
        self._set_resultfile_with_str(value)

