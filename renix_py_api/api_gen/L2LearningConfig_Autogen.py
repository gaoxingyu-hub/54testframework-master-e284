"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class L2LearningConfig(ROMObject):
    def __init__(self, Rate=None, RepeatCount=None, DelayTime=None, RxLearningEncapsulation=None, **kwargs):
        self._Rate = Rate  # Rate (fps)
        self._RepeatCount = RepeatCount  # Repeat Count
        self._DelayTime = DelayTime  # Delay Before Learning (sec)
        self._RxLearningEncapsulation = RxLearningEncapsulation  # Rx Learning Encapsulation

        properties = kwargs.copy()
        if Rate is not None:
            properties['Rate'] = Rate
        if RepeatCount is not None:
            properties['RepeatCount'] = RepeatCount
        if DelayTime is not None:
            properties['DelayTime'] = DelayTime
        if RxLearningEncapsulation is not None:
            properties['RxLearningEncapsulation'] = RxLearningEncapsulation

        # call base class function, and it will send message to renix server to create a class.
        super(L2LearningConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Rate=None, RepeatCount=None, DelayTime=None, RxLearningEncapsulation=None, **kwargs):
        properties = kwargs.copy()
        if Rate is not None:
            self._Rate = Rate
            properties['Rate'] = Rate
        if RepeatCount is not None:
            self._RepeatCount = RepeatCount
            properties['RepeatCount'] = RepeatCount
        if DelayTime is not None:
            self._DelayTime = DelayTime
            properties['DelayTime'] = DelayTime
        if RxLearningEncapsulation is not None:
            self._RxLearningEncapsulation = RxLearningEncapsulation
            properties['RxLearningEncapsulation'] = RxLearningEncapsulation

        super(L2LearningConfig, self).edit(**properties)

    @property
    def Rate(self):
        """
        get the value of property _Rate
        """
        if self.force_auto_sync:
            self.get('Rate')
        return self._Rate

    @property
    def RepeatCount(self):
        """
        get the value of property _RepeatCount
        """
        if self.force_auto_sync:
            self.get('RepeatCount')
        return self._RepeatCount

    @property
    def DelayTime(self):
        """
        get the value of property _DelayTime
        """
        if self.force_auto_sync:
            self.get('DelayTime')
        return self._DelayTime

    @property
    def RxLearningEncapsulation(self):
        """
        get the value of property _RxLearningEncapsulation
        """
        if self.force_auto_sync:
            self.get('RxLearningEncapsulation')
        return self._RxLearningEncapsulation

    @Rate.setter
    def Rate(self, value):
        self._Rate = value
        self.edit(Rate=value)

    @RepeatCount.setter
    def RepeatCount(self, value):
        self._RepeatCount = value
        self.edit(RepeatCount=value)

    @DelayTime.setter
    def DelayTime(self, value):
        self._DelayTime = value
        self.edit(DelayTime=value)

    @RxLearningEncapsulation.setter
    def RxLearningEncapsulation(self, value):
        self._RxLearningEncapsulation = value
        self.edit(RxLearningEncapsulation=value)

    def _set_rate_with_str(self, value):
        try:
            self._Rate = int(value)
        except ValueError:
            self._Rate = hex(int(value, 16))

    def _set_repeatcount_with_str(self, value):
        try:
            self._RepeatCount = int(value)
        except ValueError:
            self._RepeatCount = hex(int(value, 16))

    def _set_delaytime_with_str(self, value):
        try:
            self._DelayTime = int(value)
        except ValueError:
            self._DelayTime = hex(int(value, 16))

    def _set_rxlearningencapsulation_with_str(self, value):
        seperate = value.find(':')
        exec('self._RxLearningEncapsulation = EnumRxLearningEncap.%s' % value[:seperate])

