"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class RemoveMultipleChartResultSeriesCommand(ROMCommand):
    def __init__(self, ChartResultSeriesHandles=None, **kwargs):
        self._ChartResultSeriesHandles = ChartResultSeriesHandles  # 

        properties = kwargs.copy()
        if ChartResultSeriesHandles is not None:
            properties['ChartResultSeriesHandles'] = ChartResultSeriesHandles

        # call base class function, and it will send message to renix server to create a class.
        super(RemoveMultipleChartResultSeriesCommand, self).__init__(**properties)

    @property
    def ChartResultSeriesHandles(self):
        """
        get the value of property _ChartResultSeriesHandles
        """
        return self._ChartResultSeriesHandles

    @ChartResultSeriesHandles.setter
    def ChartResultSeriesHandles(self, value):
        self._ChartResultSeriesHandles = value

    def _set_chartresultserieshandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ChartResultSeriesHandles = tmp_value.split()

