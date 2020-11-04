"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .IterationStreamTemplateCommand_Autogen import IterationStreamTemplateCommand


@rom_manager.rom
class IterationFrameSizeCommand(IterationStreamTemplateCommand):
    def __init__(self, FrameSizeType=None, FixedSize=None, RandomMinFrameSize=None, RandomMaxFrameSize=None, CustomFrameSizeList=None, FrameSizeStart=None, FrameSizeStep=None, FrameSizeEnd=None, GenerateError=None, **kwargs):
        self._FrameSizeType = FrameSizeType  # Frame Size Type
        self._FixedSize = FixedSize  # Fixed
        self._RandomMinFrameSize = RandomMinFrameSize  # Min Random Frame Size
        self._RandomMaxFrameSize = RandomMaxFrameSize  # Max Random Frame Size
        self._CustomFrameSizeList = CustomFrameSizeList  # Custom Frame Size List
        self._FrameSizeStart = FrameSizeStart  # Max Random Frame Size
        self._FrameSizeStep = FrameSizeStep  # Max Random Frame Size
        self._FrameSizeEnd = FrameSizeEnd  # Frame Size Step
        self._GenerateError = GenerateError  # Error Generation

        properties = kwargs.copy()
        if FrameSizeType is not None:
            properties['FrameSizeType'] = FrameSizeType
        if FixedSize is not None:
            properties['FixedSize'] = FixedSize
        if RandomMinFrameSize is not None:
            properties['RandomMinFrameSize'] = RandomMinFrameSize
        if RandomMaxFrameSize is not None:
            properties['RandomMaxFrameSize'] = RandomMaxFrameSize
        if CustomFrameSizeList is not None:
            properties['CustomFrameSizeList'] = CustomFrameSizeList
        if FrameSizeStart is not None:
            properties['FrameSizeStart'] = FrameSizeStart
        if FrameSizeStep is not None:
            properties['FrameSizeStep'] = FrameSizeStep
        if FrameSizeEnd is not None:
            properties['FrameSizeEnd'] = FrameSizeEnd
        if GenerateError is not None:
            properties['GenerateError'] = GenerateError

        # call base class function, and it will send message to renix server to create a class.
        super(IterationFrameSizeCommand, self).__init__(**properties)

    @property
    def FrameSizeType(self):
        """
        get the value of property _FrameSizeType
        """
        return self._FrameSizeType

    @property
    def FixedSize(self):
        """
        get the value of property _FixedSize
        """
        return self._FixedSize

    @property
    def RandomMinFrameSize(self):
        """
        get the value of property _RandomMinFrameSize
        """
        return self._RandomMinFrameSize

    @property
    def RandomMaxFrameSize(self):
        """
        get the value of property _RandomMaxFrameSize
        """
        return self._RandomMaxFrameSize

    @property
    def CustomFrameSizeList(self):
        """
        get the value of property _CustomFrameSizeList
        """
        return self._CustomFrameSizeList

    @property
    def FrameSizeStart(self):
        """
        get the value of property _FrameSizeStart
        """
        return self._FrameSizeStart

    @property
    def FrameSizeStep(self):
        """
        get the value of property _FrameSizeStep
        """
        return self._FrameSizeStep

    @property
    def FrameSizeEnd(self):
        """
        get the value of property _FrameSizeEnd
        """
        return self._FrameSizeEnd

    @property
    def GenerateError(self):
        """
        get the value of property _GenerateError
        """
        return self._GenerateError

    @FrameSizeType.setter
    def FrameSizeType(self, value):
        self._FrameSizeType = value

    @FixedSize.setter
    def FixedSize(self, value):
        self._FixedSize = value

    @RandomMinFrameSize.setter
    def RandomMinFrameSize(self, value):
        self._RandomMinFrameSize = value

    @RandomMaxFrameSize.setter
    def RandomMaxFrameSize(self, value):
        self._RandomMaxFrameSize = value

    @CustomFrameSizeList.setter
    def CustomFrameSizeList(self, value):
        self._CustomFrameSizeList = value

    @FrameSizeStart.setter
    def FrameSizeStart(self, value):
        self._FrameSizeStart = value

    @FrameSizeStep.setter
    def FrameSizeStep(self, value):
        self._FrameSizeStep = value

    @FrameSizeEnd.setter
    def FrameSizeEnd(self, value):
        self._FrameSizeEnd = value

    @GenerateError.setter
    def GenerateError(self, value):
        self._GenerateError = value

    def _set_framesizetype_with_str(self, value):
        seperate = value.find(':')
        exec('self._FrameSizeType = EnumFrameSizeType.%s' % value[:seperate])

    def _set_fixedsize_with_str(self, value):
        try:
            self._FixedSize = int(value)
        except ValueError:
            self._FixedSize = hex(int(value, 16))

    def _set_randomminframesize_with_str(self, value):
        try:
            self._RandomMinFrameSize = int(value)
        except ValueError:
            self._RandomMinFrameSize = hex(int(value, 16))

    def _set_randommaxframesize_with_str(self, value):
        try:
            self._RandomMaxFrameSize = int(value)
        except ValueError:
            self._RandomMaxFrameSize = hex(int(value, 16))

    def _set_customframesizelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._CustomFrameSizeList = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._CustomFrameSizeList.append(int(str_value))
            except ValueError:
                self._CustomFrameSizeList.append(hex(int(str_value, 16)))

    def _set_framesizestart_with_str(self, value):
        try:
            self._FrameSizeStart = int(value)
        except ValueError:
            self._FrameSizeStart = hex(int(value, 16))

    def _set_framesizestep_with_str(self, value):
        try:
            self._FrameSizeStep = int(value)
        except ValueError:
            self._FrameSizeStep = hex(int(value, 16))

    def _set_framesizeend_with_str(self, value):
        try:
            self._FrameSizeEnd = int(value)
        except ValueError:
            self._FrameSizeEnd = hex(int(value, 16))

    def _set_generateerror_with_str(self, value):
        seperate = value.find(':')
        exec('self._GenerateError = EnumErrorGen.%s' % value[:seperate])

