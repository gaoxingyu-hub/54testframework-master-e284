"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .FilesCommand_Autogen import FilesCommand


@rom_manager.rom
class RefreshFilesCommand(FilesCommand):
    def __init__(self, Results=None, **kwargs):
        self._Results = Results  # List Results

        properties = kwargs.copy()
        if Results is not None:
            properties['Results'] = Results

        # call base class function, and it will send message to renix server to create a class.
        super(RefreshFilesCommand, self).__init__(**properties)

    @property
    def Results(self):
        """
        get the value of property _Results
        """
        return self._Results

    @Results.setter
    def Results(self, value):
        self._Results = value

    def _set_results_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Results = tmp_value.split()

