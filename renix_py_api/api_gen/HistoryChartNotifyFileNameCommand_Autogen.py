"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class HistoryChartNotifyFileNameCommand(ROMCommand):
    def __init__(self, TargetFileName=None, SourceFileName=None, **kwargs):
        self._TargetFileName = TargetFileName  # Target File Name
        self._SourceFileName = SourceFileName  # Source File Name
        self._ChartViewFile = ''  # Chart View File, not editable

        properties = kwargs.copy()
        if TargetFileName is not None:
            properties['TargetFileName'] = TargetFileName
        if SourceFileName is not None:
            properties['SourceFileName'] = SourceFileName

        # call base class function, and it will send message to renix server to create a class.
        super(HistoryChartNotifyFileNameCommand, self).__init__(**properties)

    @property
    def TargetFileName(self):
        """
        get the value of property _TargetFileName
        """
        return self._TargetFileName

    @property
    def SourceFileName(self):
        """
        get the value of property _SourceFileName
        """
        return self._SourceFileName

    @property
    def ChartViewFile(self):
        """
        get the value of property _ChartViewFile
        """
        return self._ChartViewFile

    @TargetFileName.setter
    def TargetFileName(self, value):
        self._TargetFileName = value

    @SourceFileName.setter
    def SourceFileName(self, value):
        self._SourceFileName = value

    def _set_targetfilename_with_str(self, value):
        self._TargetFileName = value

    def _set_sourcefilename_with_str(self, value):
        self._SourceFileName = value

    def _set_chartviewfile_with_str(self, value):
        self._ChartViewFile = value

    def _set_output_property(self, value):
        self._set_chartviewfile_with_str(value)

