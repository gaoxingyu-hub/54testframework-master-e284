"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .CreateChartResultViewExCommand_Autogen import CreateChartResultViewExCommand


@rom_manager.rom
class UpdateChartResultViewExCommand(CreateChartResultViewExCommand):
    def __init__(self, DeletedChartResultSeriesHandles=None, **kwargs):
        self._DeletedChartResultSeriesHandles = DeletedChartResultSeriesHandles  # Deleted Chart Result Series

        properties = kwargs.copy()
        if DeletedChartResultSeriesHandles is not None:
            properties['DeletedChartResultSeriesHandles'] = DeletedChartResultSeriesHandles

        # call base class function, and it will send message to renix server to create a class.
        super(UpdateChartResultViewExCommand, self).__init__(**properties)

    @property
    def DeletedChartResultSeriesHandles(self):
        """
        get the value of property _DeletedChartResultSeriesHandles
        """
        return self._DeletedChartResultSeriesHandles

    @DeletedChartResultSeriesHandles.setter
    def DeletedChartResultSeriesHandles(self, value):
        self._DeletedChartResultSeriesHandles = value

    def _set_deletedchartresultserieshandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._DeletedChartResultSeriesHandles = tmp_value.split()

