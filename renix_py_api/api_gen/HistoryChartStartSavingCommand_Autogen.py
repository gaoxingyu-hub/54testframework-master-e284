"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .SamplingCommand_Autogen import SamplingCommand


@rom_manager.rom
class HistoryChartStartSavingCommand(SamplingCommand):
    def __init__(self, ChartViewHandle=None, ChartResultViewHandles=None, **kwargs):
        self._ChartViewHandle = ChartViewHandle  # Chart View
        self._ChartResultViewHandles = ChartResultViewHandles  # Chart Result Views
        self._SaveResult = False  # Save Result, not editable

        properties = kwargs.copy()
        if ChartViewHandle is not None:
            properties['ChartViewHandle'] = ChartViewHandle
        if ChartResultViewHandles is not None:
            properties['ChartResultViewHandles'] = ChartResultViewHandles

        # call base class function, and it will send message to renix server to create a class.
        super(HistoryChartStartSavingCommand, self).__init__(**properties)

    @property
    def ChartViewHandle(self):
        """
        get the value of property _ChartViewHandle
        """
        return self._ChartViewHandle

    @property
    def ChartResultViewHandles(self):
        """
        get the value of property _ChartResultViewHandles
        """
        return self._ChartResultViewHandles

    @property
    def SaveResult(self):
        """
        get the value of property _SaveResult
        """
        return self._SaveResult

    @ChartViewHandle.setter
    def ChartViewHandle(self, value):
        self._ChartViewHandle = value

    @ChartResultViewHandles.setter
    def ChartResultViewHandles(self, value):
        self._ChartResultViewHandles = value

    def _set_chartviewhandle_with_str(self, value):
        self._ChartViewHandle = value

    def _set_chartresultviewhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ChartResultViewHandles = tmp_value.split()

    def _set_saveresult_with_str(self, value):
        self._SaveResult = (value == 'True')

    def _set_output_property(self, value):
        self._set_saveresult_with_str(value)

