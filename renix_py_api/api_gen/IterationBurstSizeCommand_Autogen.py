"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .IterationStreamTemplateCommand_Autogen import IterationStreamTemplateCommand


@rom_manager.rom
class IterationBurstSizeCommand(IterationStreamTemplateCommand):
    def __init__(self, IterationMode=None, LoadUnits=None, FixedBurstSize=None, CustomBurstSizeList=None, StepBurstSizeStart=None, StepBurstSizeEnd=None, StepBurstSizeStep=None, InterFrameGapMode=None, InterFrameGap=None, **kwargs):
        self._IterationMode = IterationMode  # Burst Size Iteration Mode
        self._LoadUnits = LoadUnits  # Percent (%)
        self._FixedBurstSize = FixedBurstSize  # Fixed Burst Size
        self._CustomBurstSizeList = CustomBurstSizeList  # Custom Burst Size List
        self._StepBurstSizeStart = StepBurstSizeStart  # Burst Size Start
        self._StepBurstSizeEnd = StepBurstSizeEnd  # Burst Size End
        self._StepBurstSizeStep = StepBurstSizeStep  # Burst Size Step
        self._InterFrameGapMode = InterFrameGapMode  # Inter Frame Gap Mode
        self._InterFrameGap = InterFrameGap  # Inter Frame Gap

        properties = kwargs.copy()
        if IterationMode is not None:
            properties['IterationMode'] = IterationMode
        if LoadUnits is not None:
            properties['LoadUnits'] = LoadUnits
        if FixedBurstSize is not None:
            properties['FixedBurstSize'] = FixedBurstSize
        if CustomBurstSizeList is not None:
            properties['CustomBurstSizeList'] = CustomBurstSizeList
        if StepBurstSizeStart is not None:
            properties['StepBurstSizeStart'] = StepBurstSizeStart
        if StepBurstSizeEnd is not None:
            properties['StepBurstSizeEnd'] = StepBurstSizeEnd
        if StepBurstSizeStep is not None:
            properties['StepBurstSizeStep'] = StepBurstSizeStep
        if InterFrameGapMode is not None:
            properties['InterFrameGapMode'] = InterFrameGapMode
        if InterFrameGap is not None:
            properties['InterFrameGap'] = InterFrameGap

        # call base class function, and it will send message to renix server to create a class.
        super(IterationBurstSizeCommand, self).__init__(**properties)

    @property
    def IterationMode(self):
        """
        get the value of property _IterationMode
        """
        return self._IterationMode

    @property
    def LoadUnits(self):
        """
        get the value of property _LoadUnits
        """
        return self._LoadUnits

    @property
    def FixedBurstSize(self):
        """
        get the value of property _FixedBurstSize
        """
        return self._FixedBurstSize

    @property
    def CustomBurstSizeList(self):
        """
        get the value of property _CustomBurstSizeList
        """
        return self._CustomBurstSizeList

    @property
    def StepBurstSizeStart(self):
        """
        get the value of property _StepBurstSizeStart
        """
        return self._StepBurstSizeStart

    @property
    def StepBurstSizeEnd(self):
        """
        get the value of property _StepBurstSizeEnd
        """
        return self._StepBurstSizeEnd

    @property
    def StepBurstSizeStep(self):
        """
        get the value of property _StepBurstSizeStep
        """
        return self._StepBurstSizeStep

    @property
    def InterFrameGapMode(self):
        """
        get the value of property _InterFrameGapMode
        """
        return self._InterFrameGapMode

    @property
    def InterFrameGap(self):
        """
        get the value of property _InterFrameGap
        """
        return self._InterFrameGap

    @IterationMode.setter
    def IterationMode(self, value):
        self._IterationMode = value

    @LoadUnits.setter
    def LoadUnits(self, value):
        self._LoadUnits = value

    @FixedBurstSize.setter
    def FixedBurstSize(self, value):
        self._FixedBurstSize = value

    @CustomBurstSizeList.setter
    def CustomBurstSizeList(self, value):
        self._CustomBurstSizeList = value

    @StepBurstSizeStart.setter
    def StepBurstSizeStart(self, value):
        self._StepBurstSizeStart = value

    @StepBurstSizeEnd.setter
    def StepBurstSizeEnd(self, value):
        self._StepBurstSizeEnd = value

    @StepBurstSizeStep.setter
    def StepBurstSizeStep(self, value):
        self._StepBurstSizeStep = value

    @InterFrameGapMode.setter
    def InterFrameGapMode(self, value):
        self._InterFrameGapMode = value

    @InterFrameGap.setter
    def InterFrameGap(self, value):
        self._InterFrameGap = value

    def _set_iterationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._IterationMode = EnumIterationMode.%s' % value[:seperate])

    def _set_loadunits_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoadUnits = EnumLoadUnit.%s' % value[:seperate])

    def _set_fixedburstsize_with_str(self, value):
        try:
            self._FixedBurstSize = int(value)
        except ValueError:
            self._FixedBurstSize = hex(int(value, 16))

    def _set_customburstsizelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._CustomBurstSizeList = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._CustomBurstSizeList.append(int(str_value))
            except ValueError:
                self._CustomBurstSizeList.append(hex(int(str_value, 16)))

    def _set_stepburstsizestart_with_str(self, value):
        try:
            self._StepBurstSizeStart = int(value)
        except ValueError:
            self._StepBurstSizeStart = hex(int(value, 16))

    def _set_stepburstsizeend_with_str(self, value):
        try:
            self._StepBurstSizeEnd = int(value)
        except ValueError:
            self._StepBurstSizeEnd = hex(int(value, 16))

    def _set_stepburstsizestep_with_str(self, value):
        try:
            self._StepBurstSizeStep = int(value)
        except ValueError:
            self._StepBurstSizeStep = hex(int(value, 16))

    def _set_interframegapmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._InterFrameGapMode = EnumInterFrameGapMode.%s' % value[:seperate])

    def _set_interframegap_with_str(self, value):
        try:
            self._InterFrameGap = int(value)
        except ValueError:
            self._InterFrameGap = hex(int(value, 16))

