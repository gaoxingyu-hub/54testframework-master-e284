"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .TransportFilesCommand_Autogen import TransportFilesCommand


@rom_manager.rom
class DownloadFilesCommand(TransportFilesCommand):
    def __init__(self, LocalPath=None, **kwargs):
        self._LocalPath = LocalPath  # Local Path

        properties = kwargs.copy()
        if LocalPath is not None:
            properties['LocalPath'] = LocalPath

        # call base class function, and it will send message to renix server to create a class.
        super(DownloadFilesCommand, self).__init__(**properties)

    @property
    def LocalPath(self):
        """
        get the value of property _LocalPath
        """
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, value):
        self._LocalPath = value

    def _set_localpath_with_str(self, value):
        self._LocalPath = value

