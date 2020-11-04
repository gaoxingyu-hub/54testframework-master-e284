"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class HistoryChartStopSavingCommand(ROMCommand):
    def __init__(self, ChartViewHandle=None, **kwargs):
        self._ChartViewHandle = ChartViewHandle  # Chart View
        self._FileName = ''  # File Name, not editable
        self._FullFileName = ''  # Full File Name, not editable

        properties = kwargs.copy()
        if ChartViewHandle is not None:
            properties['ChartViewHandle'] = ChartViewHandle

        # call base class function, and it will send message to renix server to create a class.
        super(HistoryChartStopSavingCommand, self).__init__(**properties)

    @property
    def ChartViewHandle(self):
        """
        get the value of property _ChartViewHandle
        """
        return self._ChartViewHandle

    @property
    def FileName(self):
        """
        get the value of property _FileName
        """
        return self._FileName

    @property
    def FullFileName(self):
        """
        get the value of property _FullFileName
        """
        return self._FullFileName

    @ChartViewHandle.setter
    def ChartViewHandle(self, value):
        self._ChartViewHandle = value

    def _set_chartviewhandle_with_str(self, value):
        self._ChartViewHandle = value

    def _set_filename_with_str(self, value):
        self._FileName = value

    def _set_fullfilename_with_str(self, value):
        self._FullFileName = value

