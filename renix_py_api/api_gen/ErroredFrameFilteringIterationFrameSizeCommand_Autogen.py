"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BenchmarkIterationFrameSizeCommand_Autogen import BenchmarkIterationFrameSizeCommand


@rom_manager.rom
class ErroredFrameFilteringIterationFrameSizeCommand(BenchmarkIterationFrameSizeCommand):
    def __init__(self, CrcChecked=None, CrcErroredFrameSize=None, UnderSizedChecked=None, UnderSizedFrameSize=None, OverSizedChecked=None, OverSizedFrameSize=None, **kwargs):
        self._CrcChecked = CrcChecked  # Enable Crc Errored Frame
        self._CrcErroredFrameSize = CrcErroredFrameSize  # Crc Errored Frame Size
        self._UnderSizedChecked = UnderSizedChecked  # Enable Under Sized Frame
        self._UnderSizedFrameSize = UnderSizedFrameSize  # Under Sized Frame Size
        self._OverSizedChecked = OverSizedChecked  # Enable Over Sized Frame
        self._OverSizedFrameSize = OverSizedFrameSize  # Over Sized Frame Size

        properties = kwargs.copy()
        if CrcChecked is not None:
            properties['CrcChecked'] = CrcChecked
        if CrcErroredFrameSize is not None:
            properties['CrcErroredFrameSize'] = CrcErroredFrameSize
        if UnderSizedChecked is not None:
            properties['UnderSizedChecked'] = UnderSizedChecked
        if UnderSizedFrameSize is not None:
            properties['UnderSizedFrameSize'] = UnderSizedFrameSize
        if OverSizedChecked is not None:
            properties['OverSizedChecked'] = OverSizedChecked
        if OverSizedFrameSize is not None:
            properties['OverSizedFrameSize'] = OverSizedFrameSize

        # call base class function, and it will send message to renix server to create a class.
        super(ErroredFrameFilteringIterationFrameSizeCommand, self).__init__(**properties)

    @property
    def CrcChecked(self):
        """
        get the value of property _CrcChecked
        """
        return self._CrcChecked

    @property
    def CrcErroredFrameSize(self):
        """
        get the value of property _CrcErroredFrameSize
        """
        return self._CrcErroredFrameSize

    @property
    def UnderSizedChecked(self):
        """
        get the value of property _UnderSizedChecked
        """
        return self._UnderSizedChecked

    @property
    def UnderSizedFrameSize(self):
        """
        get the value of property _UnderSizedFrameSize
        """
        return self._UnderSizedFrameSize

    @property
    def OverSizedChecked(self):
        """
        get the value of property _OverSizedChecked
        """
        return self._OverSizedChecked

    @property
    def OverSizedFrameSize(self):
        """
        get the value of property _OverSizedFrameSize
        """
        return self._OverSizedFrameSize

    @CrcChecked.setter
    def CrcChecked(self, value):
        self._CrcChecked = value

    @CrcErroredFrameSize.setter
    def CrcErroredFrameSize(self, value):
        self._CrcErroredFrameSize = value

    @UnderSizedChecked.setter
    def UnderSizedChecked(self, value):
        self._UnderSizedChecked = value

    @UnderSizedFrameSize.setter
    def UnderSizedFrameSize(self, value):
        self._UnderSizedFrameSize = value

    @OverSizedChecked.setter
    def OverSizedChecked(self, value):
        self._OverSizedChecked = value

    @OverSizedFrameSize.setter
    def OverSizedFrameSize(self, value):
        self._OverSizedFrameSize = value

    def _set_crcchecked_with_str(self, value):
        self._CrcChecked = (value == 'True')

    def _set_crcerroredframesize_with_str(self, value):
        try:
            self._CrcErroredFrameSize = int(value)
        except ValueError:
            self._CrcErroredFrameSize = hex(int(value, 16))

    def _set_undersizedchecked_with_str(self, value):
        self._UnderSizedChecked = (value == 'True')

    def _set_undersizedframesize_with_str(self, value):
        try:
            self._UnderSizedFrameSize = int(value)
        except ValueError:
            self._UnderSizedFrameSize = hex(int(value, 16))

    def _set_oversizedchecked_with_str(self, value):
        self._OverSizedChecked = (value == 'True')

    def _set_oversizedframesize_with_str(self, value):
        try:
            self._OverSizedFrameSize = int(value)
        except ValueError:
            self._OverSizedFrameSize = hex(int(value, 16))

