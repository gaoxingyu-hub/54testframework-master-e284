"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class GetDiagnosticInfoCommand(ROMCommand):
    def __init__(self, SaveDir=None, LogType=None, **kwargs):
        self._SaveDir = SaveDir  # Save Directory
        self._LogType = LogType  # Log Type
        self._LoggerFolder = ''  # Saved Logger Folder, not editable

        properties = kwargs.copy()
        if SaveDir is not None:
            properties['SaveDir'] = SaveDir
        if LogType is not None:
            properties['LogType'] = LogType

        # call base class function, and it will send message to renix server to create a class.
        super(GetDiagnosticInfoCommand, self).__init__(**properties)

    @property
    def SaveDir(self):
        """
        get the value of property _SaveDir
        """
        return self._SaveDir

    @property
    def LogType(self):
        """
        get the value of property _LogType
        """
        return self._LogType

    @property
    def LoggerFolder(self):
        """
        get the value of property _LoggerFolder
        """
        return self._LoggerFolder

    @SaveDir.setter
    def SaveDir(self, value):
        self._SaveDir = value

    @LogType.setter
    def LogType(self, value):
        self._LogType = value

    def _set_savedir_with_str(self, value):
        self._SaveDir = value

    def _set_logtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._LogType = LogType.%s' % value[:seperate])

    def _set_loggerfolder_with_str(self, value):
        self._LoggerFolder = value

    def _set_output_property(self, value):
        self._set_loggerfolder_with_str(value)

