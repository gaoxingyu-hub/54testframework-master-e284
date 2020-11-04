"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BenchmarkL23Config_Autogen import BenchmarkL23Config


@rom_manager.rom
class Y1564TestConfig(BenchmarkL23Config):
    def __init__(self, TrialNum=None, DurationMode=None, MaxDurationTime=None, MaxDurationBurst=None, AddressLearnFrequency=None, InitialRate=None, Step=None, LoadUnit1564=None, TestAlgorithm=None, EnableCbsEbsTest=None, **kwargs):
        self._TrialNum = TrialNum  # Trial Times
        self._DurationMode = DurationMode  # Trial Duration Mode
        self._MaxDurationTime = MaxDurationTime  # Trial Duration (seconds)
        self._MaxDurationBurst = MaxDurationBurst  # Trial Duration (frames)
        self._AddressLearnFrequency = AddressLearnFrequency  # Address Learn Frequency
        self._InitialRate = InitialRate  # Initial Rate (% of CIR)
        self._Step = Step  # Step (%)
        self._LoadUnit1564 = LoadUnit1564  # Load Unit
        self._TestAlgorithm = TestAlgorithm  # Test Algorithm
        self._EnableCbsEbsTest = EnableCbsEbsTest  # Enable CBS/EBS Test
        self._EnablePassEvaluation = False  # Enable Pass/Fail Evaluation, not editable

        properties = kwargs.copy()
        if TrialNum is not None:
            properties['TrialNum'] = TrialNum
        if DurationMode is not None:
            properties['DurationMode'] = DurationMode
        if MaxDurationTime is not None:
            properties['MaxDurationTime'] = MaxDurationTime
        if MaxDurationBurst is not None:
            properties['MaxDurationBurst'] = MaxDurationBurst
        if AddressLearnFrequency is not None:
            properties['AddressLearnFrequency'] = AddressLearnFrequency
        if InitialRate is not None:
            properties['InitialRate'] = InitialRate
        if Step is not None:
            properties['Step'] = Step
        if LoadUnit1564 is not None:
            properties['LoadUnit1564'] = LoadUnit1564
        if TestAlgorithm is not None:
            properties['TestAlgorithm'] = TestAlgorithm
        if EnableCbsEbsTest is not None:
            properties['EnableCbsEbsTest'] = EnableCbsEbsTest

        # call base class function, and it will send message to renix server to create a class.
        super(Y1564TestConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TrialNum=None, DurationMode=None, MaxDurationTime=None, MaxDurationBurst=None, AddressLearnFrequency=None, InitialRate=None, Step=None, LoadUnit1564=None, TestAlgorithm=None, EnableCbsEbsTest=None, **kwargs):
        properties = kwargs.copy()
        if TrialNum is not None:
            self._TrialNum = TrialNum
            properties['TrialNum'] = TrialNum
        if DurationMode is not None:
            self._DurationMode = DurationMode
            properties['DurationMode'] = DurationMode
        if MaxDurationTime is not None:
            self._MaxDurationTime = MaxDurationTime
            properties['MaxDurationTime'] = MaxDurationTime
        if MaxDurationBurst is not None:
            self._MaxDurationBurst = MaxDurationBurst
            properties['MaxDurationBurst'] = MaxDurationBurst
        if AddressLearnFrequency is not None:
            self._AddressLearnFrequency = AddressLearnFrequency
            properties['AddressLearnFrequency'] = AddressLearnFrequency
        if InitialRate is not None:
            self._InitialRate = InitialRate
            properties['InitialRate'] = InitialRate
        if Step is not None:
            self._Step = Step
            properties['Step'] = Step
        if LoadUnit1564 is not None:
            self._LoadUnit1564 = LoadUnit1564
            properties['LoadUnit1564'] = LoadUnit1564
        if TestAlgorithm is not None:
            self._TestAlgorithm = TestAlgorithm
            properties['TestAlgorithm'] = TestAlgorithm
        if EnableCbsEbsTest is not None:
            self._EnableCbsEbsTest = EnableCbsEbsTest
            properties['EnableCbsEbsTest'] = EnableCbsEbsTest

        super(Y1564TestConfig, self).edit(**properties)

    @property
    def TrialNum(self):
        """
        get the value of property _TrialNum
        """
        if self.force_auto_sync:
            self.get('TrialNum')
        return self._TrialNum

    @property
    def DurationMode(self):
        """
        get the value of property _DurationMode
        """
        if self.force_auto_sync:
            self.get('DurationMode')
        return self._DurationMode

    @property
    def MaxDurationTime(self):
        """
        get the value of property _MaxDurationTime
        """
        if self.force_auto_sync:
            self.get('MaxDurationTime')
        return self._MaxDurationTime

    @property
    def MaxDurationBurst(self):
        """
        get the value of property _MaxDurationBurst
        """
        if self.force_auto_sync:
            self.get('MaxDurationBurst')
        return self._MaxDurationBurst

    @property
    def AddressLearnFrequency(self):
        """
        get the value of property _AddressLearnFrequency
        """
        if self.force_auto_sync:
            self.get('AddressLearnFrequency')
        return self._AddressLearnFrequency

    @property
    def InitialRate(self):
        """
        get the value of property _InitialRate
        """
        if self.force_auto_sync:
            self.get('InitialRate')
        return self._InitialRate

    @property
    def Step(self):
        """
        get the value of property _Step
        """
        if self.force_auto_sync:
            self.get('Step')
        return self._Step

    @property
    def LoadUnit1564(self):
        """
        get the value of property _LoadUnit1564
        """
        if self.force_auto_sync:
            self.get('LoadUnit1564')
        return self._LoadUnit1564

    @property
    def TestAlgorithm(self):
        """
        get the value of property _TestAlgorithm
        """
        if self.force_auto_sync:
            self.get('TestAlgorithm')
        return self._TestAlgorithm

    @property
    def EnableCbsEbsTest(self):
        """
        get the value of property _EnableCbsEbsTest
        """
        if self.force_auto_sync:
            self.get('EnableCbsEbsTest')
        return self._EnableCbsEbsTest

    @property
    def EnablePassEvaluation(self):
        """
        get the value of property _EnablePassEvaluation
        """
        if self.force_auto_sync:
            self.get('EnablePassEvaluation')
        return self._EnablePassEvaluation

    @TrialNum.setter
    def TrialNum(self, value):
        self._TrialNum = value
        self.edit(TrialNum=value)

    @DurationMode.setter
    def DurationMode(self, value):
        self._DurationMode = value
        self.edit(DurationMode=value)

    @MaxDurationTime.setter
    def MaxDurationTime(self, value):
        self._MaxDurationTime = value
        self.edit(MaxDurationTime=value)

    @MaxDurationBurst.setter
    def MaxDurationBurst(self, value):
        self._MaxDurationBurst = value
        self.edit(MaxDurationBurst=value)

    @AddressLearnFrequency.setter
    def AddressLearnFrequency(self, value):
        self._AddressLearnFrequency = value
        self.edit(AddressLearnFrequency=value)

    @InitialRate.setter
    def InitialRate(self, value):
        self._InitialRate = value
        self.edit(InitialRate=value)

    @Step.setter
    def Step(self, value):
        self._Step = value
        self.edit(Step=value)

    @LoadUnit1564.setter
    def LoadUnit1564(self, value):
        self._LoadUnit1564 = value
        self.edit(LoadUnit1564=value)

    @TestAlgorithm.setter
    def TestAlgorithm(self, value):
        self._TestAlgorithm = value
        self.edit(TestAlgorithm=value)

    @EnableCbsEbsTest.setter
    def EnableCbsEbsTest(self, value):
        self._EnableCbsEbsTest = value
        self.edit(EnableCbsEbsTest=value)

    def _set_trialnum_with_str(self, value):
        try:
            self._TrialNum = int(value)
        except ValueError:
            self._TrialNum = hex(int(value, 16))

    def _set_durationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._DurationMode = EnumDurationMode.%s' % value[:seperate])

    def _set_maxdurationtime_with_str(self, value):
        try:
            self._MaxDurationTime = int(value)
        except ValueError:
            self._MaxDurationTime = hex(int(value, 16))

    def _set_maxdurationburst_with_str(self, value):
        try:
            self._MaxDurationBurst = int(value)
        except ValueError:
            self._MaxDurationBurst = hex(int(value, 16))

    def _set_addresslearnfrequency_with_str(self, value):
        seperate = value.find(':')
        exec('self._AddressLearnFrequency = EnumY1564AdddressLearningFrequency.%s' % value[:seperate])

    def _set_initialrate_with_str(self, value):
        try:
            self._InitialRate = int(value)
        except ValueError:
            self._InitialRate = hex(int(value, 16))

    def _set_step_with_str(self, value):
        try:
            self._Step = int(value)
        except ValueError:
            self._Step = hex(int(value, 16))

    def _set_loadunit1564_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoadUnit1564 = EnumY1564LoadUnit.%s' % value[:seperate])

    def _set_testalgorithm_with_str(self, value):
        seperate = value.find(':')
        exec('self._TestAlgorithm = EnumTestAlgorithm.%s' % value[:seperate])

    def _set_enablecbsebstest_with_str(self, value):
        self._EnableCbsEbsTest = (value == 'True')

    def _set_enablepassevaluation_with_str(self, value):
        self._EnablePassEvaluation = (value == 'True')

