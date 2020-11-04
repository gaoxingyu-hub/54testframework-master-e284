"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ListHistoryChartCommand(ROMCommand):
    def __init__(self, **kwargs):
        self._FileNames = None  # File Names, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(ListHistoryChartCommand, self).__init__(**properties)

    @property
    def FileNames(self):
        """
        get the value of property _FileNames
        """
        return self._FileNames

    def _set_filenames_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._FileNames = tmp_value.split()

    def _set_output_property(self, value):
        self._set_filenames_with_str(value)

