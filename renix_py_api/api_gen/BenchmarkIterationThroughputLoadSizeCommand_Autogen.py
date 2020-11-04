"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .TrafficTestCommand_Autogen import TrafficTestCommand


@rom_manager.rom
class BenchmarkIterationThroughputLoadSizeCommand(TrafficTestCommand):
    def __init__(self, LoadUnit=None, SearchMode=None, StreamTemplateList=None, LoadMode=None, IgnoreMinMaxLimit=None, LowerBoundLimit=None, UpperBoundLimit=None, ValueStep=None, InitValue=None, Resolution=None, Backoff=None, AcceptableFrameLoss=None, CurrentLoad=None, EnableSmartScriptLoopBreak=None, EnableMaxLatencyThreshold=None, EnableOutOfSeqThreshold=None, MaxLatencyThreshold=None, OutOfSeqThreshold=None, **kwargs):
        self._LoadUnit = LoadUnit  # %
        self._SearchMode = SearchMode  # Search Type
        self._StreamTemplateList = StreamTemplateList  # Stream Template List
        self._LoadMode = LoadMode  # Load Type
        self._IgnoreMinMaxLimit = IgnoreMinMaxLimit  # Ignore Min and Max limit
        self._LowerBoundLimit = LowerBoundLimit  # Start Value
        self._UpperBoundLimit = UpperBoundLimit  # Stop Value
        self._ValueStep = ValueStep  # Step Value
        self._InitValue = InitValue  # Initial Value
        self._Resolution = Resolution  # Resolution
        self._Backoff = Backoff  # Load Start
        self._AcceptableFrameLoss = AcceptableFrameLoss  # Load Step
        self._CurrentLoad = CurrentLoad  # Load End
        self._EnableSmartScriptLoopBreak = EnableSmartScriptLoopBreak  # Enable Break SmartScript Loop
        self._EnableMaxLatencyThreshold = EnableMaxLatencyThreshold  # Enable Maximum Latency Threshold (us)
        self._EnableOutOfSeqThreshold = EnableOutOfSeqThreshold  # Enable Maximum Latency Threshold (us)
        self._MaxLatencyThreshold = MaxLatencyThreshold  # Maximum Latency Threshold
        self._OutOfSeqThreshold = OutOfSeqThreshold  # Out of Sequence Threshold

        properties = kwargs.copy()
        if LoadUnit is not None:
            properties['LoadUnit'] = LoadUnit
        if SearchMode is not None:
            properties['SearchMode'] = SearchMode
        if StreamTemplateList is not None:
            properties['StreamTemplateList'] = StreamTemplateList
        if LoadMode is not None:
            properties['LoadMode'] = LoadMode
        if IgnoreMinMaxLimit is not None:
            properties['IgnoreMinMaxLimit'] = IgnoreMinMaxLimit
        if LowerBoundLimit is not None:
            properties['LowerBoundLimit'] = LowerBoundLimit
        if UpperBoundLimit is not None:
            properties['UpperBoundLimit'] = UpperBoundLimit
        if ValueStep is not None:
            properties['ValueStep'] = ValueStep
        if InitValue is not None:
            properties['InitValue'] = InitValue
        if Resolution is not None:
            properties['Resolution'] = Resolution
        if Backoff is not None:
            properties['Backoff'] = Backoff
        if AcceptableFrameLoss is not None:
            properties['AcceptableFrameLoss'] = AcceptableFrameLoss
        if CurrentLoad is not None:
            properties['CurrentLoad'] = CurrentLoad
        if EnableSmartScriptLoopBreak is not None:
            properties['EnableSmartScriptLoopBreak'] = EnableSmartScriptLoopBreak
        if EnableMaxLatencyThreshold is not None:
            properties['EnableMaxLatencyThreshold'] = EnableMaxLatencyThreshold
        if EnableOutOfSeqThreshold is not None:
            properties['EnableOutOfSeqThreshold'] = EnableOutOfSeqThreshold
        if MaxLatencyThreshold is not None:
            properties['MaxLatencyThreshold'] = MaxLatencyThreshold
        if OutOfSeqThreshold is not None:
            properties['OutOfSeqThreshold'] = OutOfSeqThreshold

        # call base class function, and it will send message to renix server to create a class.
        super(BenchmarkIterationThroughputLoadSizeCommand, self).__init__(**properties)

    @property
    def LoadUnit(self):
        """
        get the value of property _LoadUnit
        """
        return self._LoadUnit

    @property
    def SearchMode(self):
        """
        get the value of property _SearchMode
        """
        return self._SearchMode

    @property
    def StreamTemplateList(self):
        """
        get the value of property _StreamTemplateList
        """
        return self._StreamTemplateList

    @property
    def LoadMode(self):
        """
        get the value of property _LoadMode
        """
        return self._LoadMode

    @property
    def IgnoreMinMaxLimit(self):
        """
        get the value of property _IgnoreMinMaxLimit
        """
        return self._IgnoreMinMaxLimit

    @property
    def LowerBoundLimit(self):
        """
        get the value of property _LowerBoundLimit
        """
        return self._LowerBoundLimit

    @property
    def UpperBoundLimit(self):
        """
        get the value of property _UpperBoundLimit
        """
        return self._UpperBoundLimit

    @property
    def ValueStep(self):
        """
        get the value of property _ValueStep
        """
        return self._ValueStep

    @property
    def InitValue(self):
        """
        get the value of property _InitValue
        """
        return self._InitValue

    @property
    def Resolution(self):
        """
        get the value of property _Resolution
        """
        return self._Resolution

    @property
    def Backoff(self):
        """
        get the value of property _Backoff
        """
        return self._Backoff

    @property
    def AcceptableFrameLoss(self):
        """
        get the value of property _AcceptableFrameLoss
        """
        return self._AcceptableFrameLoss

    @property
    def CurrentLoad(self):
        """
        get the value of property _CurrentLoad
        """
        return self._CurrentLoad

    @property
    def EnableSmartScriptLoopBreak(self):
        """
        get the value of property _EnableSmartScriptLoopBreak
        """
        return self._EnableSmartScriptLoopBreak

    @property
    def EnableMaxLatencyThreshold(self):
        """
        get the value of property _EnableMaxLatencyThreshold
        """
        return self._EnableMaxLatencyThreshold

    @property
    def EnableOutOfSeqThreshold(self):
        """
        get the value of property _EnableOutOfSeqThreshold
        """
        return self._EnableOutOfSeqThreshold

    @property
    def MaxLatencyThreshold(self):
        """
        get the value of property _MaxLatencyThreshold
        """
        return self._MaxLatencyThreshold

    @property
    def OutOfSeqThreshold(self):
        """
        get the value of property _OutOfSeqThreshold
        """
        return self._OutOfSeqThreshold

    @LoadUnit.setter
    def LoadUnit(self, value):
        self._LoadUnit = value

    @SearchMode.setter
    def SearchMode(self, value):
        self._SearchMode = value

    @StreamTemplateList.setter
    def StreamTemplateList(self, value):
        self._StreamTemplateList = value

    @LoadMode.setter
    def LoadMode(self, value):
        self._LoadMode = value

    @IgnoreMinMaxLimit.setter
    def IgnoreMinMaxLimit(self, value):
        self._IgnoreMinMaxLimit = value

    @LowerBoundLimit.setter
    def LowerBoundLimit(self, value):
        self._LowerBoundLimit = value

    @UpperBoundLimit.setter
    def UpperBoundLimit(self, value):
        self._UpperBoundLimit = value

    @ValueStep.setter
    def ValueStep(self, value):
        self._ValueStep = value

    @InitValue.setter
    def InitValue(self, value):
        self._InitValue = value

    @Resolution.setter
    def Resolution(self, value):
        self._Resolution = value

    @Backoff.setter
    def Backoff(self, value):
        self._Backoff = value

    @AcceptableFrameLoss.setter
    def AcceptableFrameLoss(self, value):
        self._AcceptableFrameLoss = value

    @CurrentLoad.setter
    def CurrentLoad(self, value):
        self._CurrentLoad = value

    @EnableSmartScriptLoopBreak.setter
    def EnableSmartScriptLoopBreak(self, value):
        self._EnableSmartScriptLoopBreak = value

    @EnableMaxLatencyThreshold.setter
    def EnableMaxLatencyThreshold(self, value):
        self._EnableMaxLatencyThreshold = value

    @EnableOutOfSeqThreshold.setter
    def EnableOutOfSeqThreshold(self, value):
        self._EnableOutOfSeqThreshold = value

    @MaxLatencyThreshold.setter
    def MaxLatencyThreshold(self, value):
        self._MaxLatencyThreshold = value

    @OutOfSeqThreshold.setter
    def OutOfSeqThreshold(self, value):
        self._OutOfSeqThreshold = value

    def _set_loadunit_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoadUnit = EnumLoadUnit.%s' % value[:seperate])

    def _set_searchmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._SearchMode = EnumSearchMode.%s' % value[:seperate])

    def _set_streamtemplatelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamTemplateList = tmp_value.split()

    def _set_loadmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoadMode = EnumLoadMode.%s' % value[:seperate])

    def _set_ignoreminmaxlimit_with_str(self, value):
        self._IgnoreMinMaxLimit = (value == 'True')

    def _set_lowerboundlimit_with_str(self, value):
        self._LowerBoundLimit = float(value)

    def _set_upperboundlimit_with_str(self, value):
        self._UpperBoundLimit = float(value)

    def _set_valuestep_with_str(self, value):
        self._ValueStep = float(value)

    def _set_initvalue_with_str(self, value):
        self._InitValue = float(value)

    def _set_resolution_with_str(self, value):
        self._Resolution = float(value)

    def _set_backoff_with_str(self, value):
        self._Backoff = float(value)

    def _set_acceptableframeloss_with_str(self, value):
        self._AcceptableFrameLoss = float(value)

    def _set_currentload_with_str(self, value):
        self._CurrentLoad = float(value)

    def _set_enablesmartscriptloopbreak_with_str(self, value):
        self._EnableSmartScriptLoopBreak = (value == 'True')

    def _set_enablemaxlatencythreshold_with_str(self, value):
        self._EnableMaxLatencyThreshold = (value == 'True')

    def _set_enableoutofseqthreshold_with_str(self, value):
        self._EnableOutOfSeqThreshold = (value == 'True')

    def _set_maxlatencythreshold_with_str(self, value):
        self._MaxLatencyThreshold = float(value)

    def _set_outofseqthreshold_with_str(self, value):
        self._OutOfSeqThreshold = float(value)

