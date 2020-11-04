"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class GetCaptureDataByIndexCommand(ROMCommand):
    def __init__(self, CaptureConfig=None, Index=None, **kwargs):
        self._CaptureConfig = CaptureConfig  # Capture Handle
        self._Index = Index  # Frame Index
        self._Timestamp = 0.0  # Frame Timestamp, not editable
        self._Length = 0  # Frame Length, not editable
        self._Data = ''  # Frame Data, not editable

        properties = kwargs.copy()
        if CaptureConfig is not None:
            properties['CaptureConfig'] = CaptureConfig
        if Index is not None:
            properties['Index'] = Index

        # call base class function, and it will send message to renix server to create a class.
        super(GetCaptureDataByIndexCommand, self).__init__(**properties)

    @property
    def CaptureConfig(self):
        """
        get the value of property _CaptureConfig
        """
        return self._CaptureConfig

    @property
    def Index(self):
        """
        get the value of property _Index
        """
        return self._Index

    @property
    def Timestamp(self):
        """
        get the value of property _Timestamp
        """
        return self._Timestamp

    @property
    def Length(self):
        """
        get the value of property _Length
        """
        return self._Length

    @property
    def Data(self):
        """
        get the value of property _Data
        """
        return self._Data

    @CaptureConfig.setter
    def CaptureConfig(self, value):
        self._CaptureConfig = value

    @Index.setter
    def Index(self, value):
        self._Index = value

    def _set_captureconfig_with_str(self, value):
        self._CaptureConfig = value

    def _set_index_with_str(self, value):
        try:
            self._Index = int(value)
        except ValueError:
            self._Index = hex(int(value, 16))

    def _set_timestamp_with_str(self, value):
        self._Timestamp = float(value)

    def _set_length_with_str(self, value):
        try:
            self._Length = int(value)
        except ValueError:
            self._Length = hex(int(value, 16))

    def _set_data_with_str(self, value):
        self._Data = value

