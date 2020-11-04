"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc2544Config_Autogen import Rfc2544Config


@rom_manager.rom
class Rfc2544BackToBackConfig(Rfc2544Config):
    def __init__(self, MinDurationTime=None, DurationTimeResolution=None, MinDurationBurst=None, DurationBurstResolution=None, AcceptableFrameLoss=None, TrafficLoadUnit=None, TrafficLoadMode=None, RandomMinLoad=None, RandomMaxLoad=None, TrafficLoadStart=None, TrafficLoadStep=None, TrafficLoadEnd=None, TrafficLoadCustom=None, **kwargs):
        self._MinDurationTime = MinDurationTime  # Min Duration (sec)
        self._DurationTimeResolution = DurationTimeResolution  # Duration Resolution
        self._MinDurationBurst = MinDurationBurst  # Min Duration (frames)
        self._DurationBurstResolution = DurationBurstResolution  # Duration Resolution (frames)
        self._AcceptableFrameLoss = AcceptableFrameLoss  # Acceptable Frame Loss(%)
        self._TrafficLoadUnit = TrafficLoadUnit  # Traffic Load Unit
        self._TrafficLoadMode = TrafficLoadMode  # Traffic Load Search Mode
        self._RandomMinLoad = RandomMinLoad  # Random Min Load
        self._RandomMaxLoad = RandomMaxLoad  # Random Max Load
        self._TrafficLoadStart = TrafficLoadStart  # Load Start
        self._TrafficLoadStep = TrafficLoadStep  # Load Step
        self._TrafficLoadEnd = TrafficLoadEnd  # Load End
        self._TrafficLoadCustom = TrafficLoadCustom  # Custom Load List

        properties = kwargs.copy()
        if MinDurationTime is not None:
            properties['MinDurationTime'] = MinDurationTime
        if DurationTimeResolution is not None:
            properties['DurationTimeResolution'] = DurationTimeResolution
        if MinDurationBurst is not None:
            properties['MinDurationBurst'] = MinDurationBurst
        if DurationBurstResolution is not None:
            properties['DurationBurstResolution'] = DurationBurstResolution
        if AcceptableFrameLoss is not None:
            properties['AcceptableFrameLoss'] = AcceptableFrameLoss
        if TrafficLoadUnit is not None:
            properties['TrafficLoadUnit'] = TrafficLoadUnit
        if TrafficLoadMode is not None:
            properties['TrafficLoadMode'] = TrafficLoadMode
        if RandomMinLoad is not None:
            properties['RandomMinLoad'] = RandomMinLoad
        if RandomMaxLoad is not None:
            properties['RandomMaxLoad'] = RandomMaxLoad
        if TrafficLoadStart is not None:
            properties['TrafficLoadStart'] = TrafficLoadStart
        if TrafficLoadStep is not None:
            properties['TrafficLoadStep'] = TrafficLoadStep
        if TrafficLoadEnd is not None:
            properties['TrafficLoadEnd'] = TrafficLoadEnd
        if TrafficLoadCustom is not None:
            properties['TrafficLoadCustom'] = TrafficLoadCustom

        # call base class function, and it will send message to renix server to create a class.
        super(Rfc2544BackToBackConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, MinDurationTime=None, DurationTimeResolution=None, MinDurationBurst=None, DurationBurstResolution=None, AcceptableFrameLoss=None, TrafficLoadUnit=None, TrafficLoadMode=None, RandomMinLoad=None, RandomMaxLoad=None, TrafficLoadStart=None, TrafficLoadStep=None, TrafficLoadEnd=None, TrafficLoadCustom=None, **kwargs):
        properties = kwargs.copy()
        if MinDurationTime is not None:
            self._MinDurationTime = MinDurationTime
            properties['MinDurationTime'] = MinDurationTime
        if DurationTimeResolution is not None:
            self._DurationTimeResolution = DurationTimeResolution
            properties['DurationTimeResolution'] = DurationTimeResolution
        if MinDurationBurst is not None:
            self._MinDurationBurst = MinDurationBurst
            properties['MinDurationBurst'] = MinDurationBurst
        if DurationBurstResolution is not None:
            self._DurationBurstResolution = DurationBurstResolution
            properties['DurationBurstResolution'] = DurationBurstResolution
        if AcceptableFrameLoss is not None:
            self._AcceptableFrameLoss = AcceptableFrameLoss
            properties['AcceptableFrameLoss'] = AcceptableFrameLoss
        if TrafficLoadUnit is not None:
            self._TrafficLoadUnit = TrafficLoadUnit
            properties['TrafficLoadUnit'] = TrafficLoadUnit
        if TrafficLoadMode is not None:
            self._TrafficLoadMode = TrafficLoadMode
            properties['TrafficLoadMode'] = TrafficLoadMode
        if RandomMinLoad is not None:
            self._RandomMinLoad = RandomMinLoad
            properties['RandomMinLoad'] = RandomMinLoad
        if RandomMaxLoad is not None:
            self._RandomMaxLoad = RandomMaxLoad
            properties['RandomMaxLoad'] = RandomMaxLoad
        if TrafficLoadStart is not None:
            self._TrafficLoadStart = TrafficLoadStart
            properties['TrafficLoadStart'] = TrafficLoadStart
        if TrafficLoadStep is not None:
            self._TrafficLoadStep = TrafficLoadStep
            properties['TrafficLoadStep'] = TrafficLoadStep
        if TrafficLoadEnd is not None:
            self._TrafficLoadEnd = TrafficLoadEnd
            properties['TrafficLoadEnd'] = TrafficLoadEnd
        if TrafficLoadCustom is not None:
            self._TrafficLoadCustom = TrafficLoadCustom
            properties['TrafficLoadCustom'] = TrafficLoadCustom

        super(Rfc2544BackToBackConfig, self).edit(**properties)

    @property
    def MinDurationTime(self):
        """
        get the value of property _MinDurationTime
        """
        if self.force_auto_sync:
            self.get('MinDurationTime')
        return self._MinDurationTime

    @property
    def DurationTimeResolution(self):
        """
        get the value of property _DurationTimeResolution
        """
        if self.force_auto_sync:
            self.get('DurationTimeResolution')
        return self._DurationTimeResolution

    @property
    def MinDurationBurst(self):
        """
        get the value of property _MinDurationBurst
        """
        if self.force_auto_sync:
            self.get('MinDurationBurst')
        return self._MinDurationBurst

    @property
    def DurationBurstResolution(self):
        """
        get the value of property _DurationBurstResolution
        """
        if self.force_auto_sync:
            self.get('DurationBurstResolution')
        return self._DurationBurstResolution

    @property
    def AcceptableFrameLoss(self):
        """
        get the value of property _AcceptableFrameLoss
        """
        if self.force_auto_sync:
            self.get('AcceptableFrameLoss')
        return self._AcceptableFrameLoss

    @property
    def TrafficLoadUnit(self):
        """
        get the value of property _TrafficLoadUnit
        """
        if self.force_auto_sync:
            self.get('TrafficLoadUnit')
        return self._TrafficLoadUnit

    @property
    def TrafficLoadMode(self):
        """
        get the value of property _TrafficLoadMode
        """
        if self.force_auto_sync:
            self.get('TrafficLoadMode')
        return self._TrafficLoadMode

    @property
    def RandomMinLoad(self):
        """
        get the value of property _RandomMinLoad
        """
        if self.force_auto_sync:
            self.get('RandomMinLoad')
        return self._RandomMinLoad

    @property
    def RandomMaxLoad(self):
        """
        get the value of property _RandomMaxLoad
        """
        if self.force_auto_sync:
            self.get('RandomMaxLoad')
        return self._RandomMaxLoad

    @property
    def TrafficLoadStart(self):
        """
        get the value of property _TrafficLoadStart
        """
        if self.force_auto_sync:
            self.get('TrafficLoadStart')
        return self._TrafficLoadStart

    @property
    def TrafficLoadStep(self):
        """
        get the value of property _TrafficLoadStep
        """
        if self.force_auto_sync:
            self.get('TrafficLoadStep')
        return self._TrafficLoadStep

    @property
    def TrafficLoadEnd(self):
        """
        get the value of property _TrafficLoadEnd
        """
        if self.force_auto_sync:
            self.get('TrafficLoadEnd')
        return self._TrafficLoadEnd

    @property
    def TrafficLoadCustom(self):
        """
        get the value of property _TrafficLoadCustom
        """
        if self.force_auto_sync:
            self.get('TrafficLoadCustom')
        return self._TrafficLoadCustom

    @MinDurationTime.setter
    def MinDurationTime(self, value):
        self._MinDurationTime = value
        self.edit(MinDurationTime=value)

    @DurationTimeResolution.setter
    def DurationTimeResolution(self, value):
        self._DurationTimeResolution = value
        self.edit(DurationTimeResolution=value)

    @MinDurationBurst.setter
    def MinDurationBurst(self, value):
        self._MinDurationBurst = value
        self.edit(MinDurationBurst=value)

    @DurationBurstResolution.setter
    def DurationBurstResolution(self, value):
        self._DurationBurstResolution = value
        self.edit(DurationBurstResolution=value)

    @AcceptableFrameLoss.setter
    def AcceptableFrameLoss(self, value):
        self._AcceptableFrameLoss = value
        self.edit(AcceptableFrameLoss=value)

    @TrafficLoadUnit.setter
    def TrafficLoadUnit(self, value):
        self._TrafficLoadUnit = value
        self.edit(TrafficLoadUnit=value)

    @TrafficLoadMode.setter
    def TrafficLoadMode(self, value):
        self._TrafficLoadMode = value
        self.edit(TrafficLoadMode=value)

    @RandomMinLoad.setter
    def RandomMinLoad(self, value):
        self._RandomMinLoad = value
        self.edit(RandomMinLoad=value)

    @RandomMaxLoad.setter
    def RandomMaxLoad(self, value):
        self._RandomMaxLoad = value
        self.edit(RandomMaxLoad=value)

    @TrafficLoadStart.setter
    def TrafficLoadStart(self, value):
        self._TrafficLoadStart = value
        self.edit(TrafficLoadStart=value)

    @TrafficLoadStep.setter
    def TrafficLoadStep(self, value):
        self._TrafficLoadStep = value
        self.edit(TrafficLoadStep=value)

    @TrafficLoadEnd.setter
    def TrafficLoadEnd(self, value):
        self._TrafficLoadEnd = value
        self.edit(TrafficLoadEnd=value)

    @TrafficLoadCustom.setter
    def TrafficLoadCustom(self, value):
        self._TrafficLoadCustom = value
        self.edit(TrafficLoadCustom=value)

    def _set_mindurationtime_with_str(self, value):
        self._MinDurationTime = float(value)

    def _set_durationtimeresolution_with_str(self, value):
        self._DurationTimeResolution = float(value)

    def _set_mindurationburst_with_str(self, value):
        try:
            self._MinDurationBurst = int(value)
        except ValueError:
            self._MinDurationBurst = hex(int(value, 16))

    def _set_durationburstresolution_with_str(self, value):
        try:
            self._DurationBurstResolution = int(value)
        except ValueError:
            self._DurationBurstResolution = hex(int(value, 16))

    def _set_acceptableframeloss_with_str(self, value):
        self._AcceptableFrameLoss = float(value)

    def _set_trafficloadunit_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficLoadUnit = EnumLoadUnit.%s' % value[:seperate])

    def _set_trafficloadmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficLoadMode = EnumLoadMode.%s' % value[:seperate])

    def _set_randomminload_with_str(self, value):
        self._RandomMinLoad = float(value)

    def _set_randommaxload_with_str(self, value):
        self._RandomMaxLoad = float(value)

    def _set_trafficloadstart_with_str(self, value):
        self._TrafficLoadStart = float(value)

    def _set_trafficloadstep_with_str(self, value):
        self._TrafficLoadStep = float(value)

    def _set_trafficloadend_with_str(self, value):
        self._TrafficLoadEnd = float(value)

    def _set_trafficloadcustom_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._TrafficLoadCustom = []
        values = tmp_value.split()
        for str_value in values:
            self._TrafficLoadCustom.append(float(str_value))

