"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class DownloadCaptureDataCommand(ROMCommand):
    def __init__(self, FileDir=None, FileName=None, CategoryByPort=None, CaptureConfigs=None, MaxDownloadDataCount=None, **kwargs):
        self._FileDir = FileDir  # Capture Data Directory
        self._FileName = FileName  # Capture Data File Name
        self._CategoryByPort = CategoryByPort  # Category By Port
        self._CaptureConfigs = CaptureConfigs  # Capture Configs
        self._MaxDownloadDataCount = MaxDownloadDataCount  # Max Download Data Count

        properties = kwargs.copy()
        if FileDir is not None:
            properties['FileDir'] = FileDir
        if FileName is not None:
            properties['FileName'] = FileName
        if CategoryByPort is not None:
            properties['CategoryByPort'] = CategoryByPort
        if CaptureConfigs is not None:
            properties['CaptureConfigs'] = CaptureConfigs
        if MaxDownloadDataCount is not None:
            properties['MaxDownloadDataCount'] = MaxDownloadDataCount

        # call base class function, and it will send message to renix server to create a class.
        super(DownloadCaptureDataCommand, self).__init__(**properties)

    @property
    def FileDir(self):
        """
        get the value of property _FileDir
        """
        return self._FileDir

    @property
    def FileName(self):
        """
        get the value of property _FileName
        """
        return self._FileName

    @property
    def CategoryByPort(self):
        """
        get the value of property _CategoryByPort
        """
        return self._CategoryByPort

    @property
    def CaptureConfigs(self):
        """
        get the value of property _CaptureConfigs
        """
        return self._CaptureConfigs

    @property
    def MaxDownloadDataCount(self):
        """
        get the value of property _MaxDownloadDataCount
        """
        return self._MaxDownloadDataCount

    @FileDir.setter
    def FileDir(self, value):
        self._FileDir = value

    @FileName.setter
    def FileName(self, value):
        self._FileName = value

    @CategoryByPort.setter
    def CategoryByPort(self, value):
        self._CategoryByPort = value

    @CaptureConfigs.setter
    def CaptureConfigs(self, value):
        self._CaptureConfigs = value

    @MaxDownloadDataCount.setter
    def MaxDownloadDataCount(self, value):
        self._MaxDownloadDataCount = value

    def _set_filedir_with_str(self, value):
        self._FileDir = value

    def _set_filename_with_str(self, value):
        self._FileName = value

    def _set_categorybyport_with_str(self, value):
        self._CategoryByPort = (value == 'True')

    def _set_captureconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._CaptureConfigs = tmp_value.split()

    def _set_maxdownloaddatacount_with_str(self, value):
        try:
            self._MaxDownloadDataCount = int(value)
        except ValueError:
            self._MaxDownloadDataCount = hex(int(value, 16))

