"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .FilesCommand_Autogen import FilesCommand


@rom_manager.rom
class ListFilesCommand(FilesCommand):
    def __init__(self, RemotePath=None, **kwargs):
        self._Results = None  # Results, not editable
        self._RemotePath = RemotePath  # Remote Path

        properties = kwargs.copy()
        if RemotePath is not None:
            properties['RemotePath'] = RemotePath

        # call base class function, and it will send message to renix server to create a class.
        super(ListFilesCommand, self).__init__(**properties)

    @property
    def Results(self):
        """
        get the value of property _Results
        """
        return self._Results

    @property
    def RemotePath(self):
        """
        get the value of property _RemotePath
        """
        return self._RemotePath

    @RemotePath.setter
    def RemotePath(self, value):
        self._RemotePath = value

    def _set_results_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Results = tmp_value.split()

    def _set_remotepath_with_str(self, value):
        self._RemotePath = value

