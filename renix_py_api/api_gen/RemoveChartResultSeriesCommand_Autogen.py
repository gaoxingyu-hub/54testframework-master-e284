"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class RemoveChartResultSeriesCommand(ROMCommand):
    def __init__(self, ChartResultSeriesHandle=None, **kwargs):
        self._ChartResultSeriesHandle = ChartResultSeriesHandle  # 

        properties = kwargs.copy()
        if ChartResultSeriesHandle is not None:
            properties['ChartResultSeriesHandle'] = ChartResultSeriesHandle

        # call base class function, and it will send message to renix server to create a class.
        super(RemoveChartResultSeriesCommand, self).__init__(**properties)

    @property
    def ChartResultSeriesHandle(self):
        """
        get the value of property _ChartResultSeriesHandle
        """
        return self._ChartResultSeriesHandle

    @ChartResultSeriesHandle.setter
    def ChartResultSeriesHandle(self, value):
        self._ChartResultSeriesHandle = value

    def _set_chartresultserieshandle_with_str(self, value):
        self._ChartResultSeriesHandle = value

