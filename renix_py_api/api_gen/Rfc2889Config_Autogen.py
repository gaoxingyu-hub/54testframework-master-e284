"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BenchmarkL23Config_Autogen import BenchmarkL23Config


@rom_manager.rom
class Rfc2889Config(BenchmarkL23Config):
    def __init__(self, EtherType=None, TrialNum=None, DurationMode=None, MaxDurationTime=None, MaxDurationBurst=None, AddressLearningFrequency=None, **kwargs):
        self._EtherType = EtherType  # Ether Type
        self._TrialNum = TrialNum  # Trial Times
        self._DurationMode = DurationMode  # Trial Duration Mode
        self._MaxDurationTime = MaxDurationTime  # Trial Duration (seconds)
        self._MaxDurationBurst = MaxDurationBurst  # Trial Duration (frames)
        self._AddressLearningFrequency = AddressLearningFrequency  # Address Learn Frequency

        properties = kwargs.copy()
        if EtherType is not None:
            properties['EtherType'] = EtherType
        if TrialNum is not None:
            properties['TrialNum'] = TrialNum
        if DurationMode is not None:
            properties['DurationMode'] = DurationMode
        if MaxDurationTime is not None:
            properties['MaxDurationTime'] = MaxDurationTime
        if MaxDurationBurst is not None:
            properties['MaxDurationBurst'] = MaxDurationBurst
        if AddressLearningFrequency is not None:
            properties['AddressLearningFrequency'] = AddressLearningFrequency

        # call base class function, and it will send message to renix server to create a class.
        super(Rfc2889Config, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EtherType=None, TrialNum=None, DurationMode=None, MaxDurationTime=None, MaxDurationBurst=None, AddressLearningFrequency=None, **kwargs):
        properties = kwargs.copy()
        if EtherType is not None:
            self._EtherType = EtherType
            properties['EtherType'] = EtherType
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
        if AddressLearningFrequency is not None:
            self._AddressLearningFrequency = AddressLearningFrequency
            properties['AddressLearningFrequency'] = AddressLearningFrequency

        super(Rfc2889Config, self).edit(**properties)

    @property
    def EtherType(self):
        """
        get the value of property _EtherType
        """
        if self.force_auto_sync:
            self.get('EtherType')
        return self._EtherType

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
    def AddressLearningFrequency(self):
        """
        get the value of property _AddressLearningFrequency
        """
        if self.force_auto_sync:
            self.get('AddressLearningFrequency')
        return self._AddressLearningFrequency

    @EtherType.setter
    def EtherType(self, value):
        self._EtherType = value
        self.edit(EtherType=value)

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

    @AddressLearningFrequency.setter
    def AddressLearningFrequency(self, value):
        self._AddressLearningFrequency = value
        self.edit(AddressLearningFrequency=value)

    def _set_ethertype_with_str(self, value):
        seperate = value.find(':')
        exec('self._EtherType = EnumEtherType.%s' % value[:seperate])

    def _set_trialnum_with_str(self, value):
        try:
            self._TrialNum = int(value)
        except ValueError:
            self._TrialNum = hex(int(value, 16))

    def _set_durationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._DurationMode = EnumTrialDurationMode.%s' % value[:seperate])

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

    def _set_addresslearningfrequency_with_str(self, value):
        seperate = value.find(':')
        exec('self._AddressLearningFrequency = EnumAdddressLearningFrequency.%s' % value[:seperate])

