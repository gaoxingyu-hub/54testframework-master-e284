"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ExportResultCommand(ROMCommand):
    def __init__(self, ViewName=None, FileName=None, WriteMode=None, Format=None, **kwargs):
        self._ViewName = ViewName  # View Name
        self._FileName = FileName  # File Name
        self._WriteMode = WriteMode  # Write Mode
        self._Format = Format  # Output Format

        properties = kwargs.copy()
        if ViewName is not None:
            properties['ViewName'] = ViewName
        if FileName is not None:
            properties['FileName'] = FileName
        if WriteMode is not None:
            properties['WriteMode'] = WriteMode
        if Format is not None:
            properties['Format'] = Format

        # call base class function, and it will send message to renix server to create a class.
        super(ExportResultCommand, self).__init__(**properties)

    @property
    def ViewName(self):
        """
        get the value of property _ViewName
        """
        return self._ViewName

    @property
    def FileName(self):
        """
        get the value of property _FileName
        """
        return self._FileName

    @property
    def WriteMode(self):
        """
        get the value of property _WriteMode
        """
        return self._WriteMode

    @property
    def Format(self):
        """
        get the value of property _Format
        """
        return self._Format

    @ViewName.setter
    def ViewName(self, value):
        self._ViewName = value

    @FileName.setter
    def FileName(self, value):
        self._FileName = value

    @WriteMode.setter
    def WriteMode(self, value):
        self._WriteMode = value

    @Format.setter
    def Format(self, value):
        self._Format = value

    def _set_viewname_with_str(self, value):
        self._ViewName = value

    def _set_filename_with_str(self, value):
        self._FileName = value

    def _set_writemode_with_str(self, value):
        seperate = value.find(':')
        exec('self._WriteMode = EnumWriteMode.%s' % value[:seperate])

    def _set_format_with_str(self, value):
        seperate = value.find(':')
        exec('self._Format = EnumOutputFormat.%s' % value[:seperate])

