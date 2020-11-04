"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .CreateChartResultViewCommand_Autogen import CreateChartResultViewCommand


@rom_manager.rom
class UpdateChartResultViewCommand(CreateChartResultViewCommand):
    def __init__(self, DeletedChartResultViewHandles=None, **kwargs):
        self._DeletedChartResultViewHandles = DeletedChartResultViewHandles  # Deleted Chart Result Views

        properties = kwargs.copy()
        if DeletedChartResultViewHandles is not None:
            properties['DeletedChartResultViewHandles'] = DeletedChartResultViewHandles

        # call base class function, and it will send message to renix server to create a class.
        super(UpdateChartResultViewCommand, self).__init__(**properties)

    @property
    def DeletedChartResultViewHandles(self):
        """
        get the value of property _DeletedChartResultViewHandles
        """
        return self._DeletedChartResultViewHandles

    @DeletedChartResultViewHandles.setter
    def DeletedChartResultViewHandles(self, value):
        self._DeletedChartResultViewHandles = value

    def _set_deletedchartresultviewhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._DeletedChartResultViewHandles = tmp_value.split()

