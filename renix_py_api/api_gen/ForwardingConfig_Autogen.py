"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc2889Config_Autogen import Rfc2889Config


@rom_manager.rom
class ForwardingConfig(Rfc2889Config):
    def __init__(self, TrafficLoadSearchMode=None, LowestRate=None, UppermostRate=None, InitRate=None, RateStep=None, RateResolution=None, AcceptableFrameLoss=None, BurstSizeLoopMode=None, BurstSizeStart=None, BurstSizeStep=None, BurstSizeEnd=None, BurstSizeCustom=None, Backoff=None, IgnoreMinMaxLimit=None, **kwargs):
        self._TrafficLoadSearchMode = TrafficLoadSearchMode  # Traffic load search mode
        self._LowestRate = LowestRate  # Lowest Rate(%)
        self._UppermostRate = UppermostRate  # Uppermost Rate(%)
        self._InitRate = InitRate  # Init Rate(%)
        self._RateStep = RateStep  # Rate Step(%)
        self._RateResolution = RateResolution  # Rate Resolution(%)
        self._AcceptableFrameLoss = AcceptableFrameLoss  # Acceptable Frame Loss(%)
        self._BurstSizeLoopMode = BurstSizeLoopMode  # Burst Size loop mode
        self._BurstSizeStart = BurstSizeStart  # Start
        self._BurstSizeStep = BurstSizeStep  # Step
        self._BurstSizeEnd = BurstSizeEnd  # End
        self._BurstSizeCustom = BurstSizeCustom  # Custom
        self._Backoff = Backoff  # Load Start
        self._IgnoreMinMaxLimit = IgnoreMinMaxLimit  # Ignore Min and Max limit

        properties = kwargs.copy()
        if TrafficLoadSearchMode is not None:
            properties['TrafficLoadSearchMode'] = TrafficLoadSearchMode
        if LowestRate is not None:
            properties['LowestRate'] = LowestRate
        if UppermostRate is not None:
            properties['UppermostRate'] = UppermostRate
        if InitRate is not None:
            properties['InitRate'] = InitRate
        if RateStep is not None:
            properties['RateStep'] = RateStep
        if RateResolution is not None:
            properties['RateResolution'] = RateResolution
        if AcceptableFrameLoss is not None:
            properties['AcceptableFrameLoss'] = AcceptableFrameLoss
        if BurstSizeLoopMode is not None:
            properties['BurstSizeLoopMode'] = BurstSizeLoopMode
        if BurstSizeStart is not None:
            properties['BurstSizeStart'] = BurstSizeStart
        if BurstSizeStep is not None:
            properties['BurstSizeStep'] = BurstSizeStep
        if BurstSizeEnd is not None:
            properties['BurstSizeEnd'] = BurstSizeEnd
        if BurstSizeCustom is not None:
            properties['BurstSizeCustom'] = BurstSizeCustom
        if Backoff is not None:
            properties['Backoff'] = Backoff
        if IgnoreMinMaxLimit is not None:
            properties['IgnoreMinMaxLimit'] = IgnoreMinMaxLimit

        # call base class function, and it will send message to renix server to create a class.
        super(ForwardingConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TrafficLoadSearchMode=None, LowestRate=None, UppermostRate=None, InitRate=None, RateStep=None, RateResolution=None, AcceptableFrameLoss=None, BurstSizeLoopMode=None, BurstSizeStart=None, BurstSizeStep=None, BurstSizeEnd=None, BurstSizeCustom=None, Backoff=None, IgnoreMinMaxLimit=None, **kwargs):
        properties = kwargs.copy()
        if TrafficLoadSearchMode is not None:
            self._TrafficLoadSearchMode = TrafficLoadSearchMode
            properties['TrafficLoadSearchMode'] = TrafficLoadSearchMode
        if LowestRate is not None:
            self._LowestRate = LowestRate
            properties['LowestRate'] = LowestRate
        if UppermostRate is not None:
            self._UppermostRate = UppermostRate
            properties['UppermostRate'] = UppermostRate
        if InitRate is not None:
            self._InitRate = InitRate
            properties['InitRate'] = InitRate
        if RateStep is not None:
            self._RateStep = RateStep
            properties['RateStep'] = RateStep
        if RateResolution is not None:
            self._RateResolution = RateResolution
            properties['RateResolution'] = RateResolution
        if AcceptableFrameLoss is not None:
            self._AcceptableFrameLoss = AcceptableFrameLoss
            properties['AcceptableFrameLoss'] = AcceptableFrameLoss
        if BurstSizeLoopMode is not None:
            self._BurstSizeLoopMode = BurstSizeLoopMode
            properties['BurstSizeLoopMode'] = BurstSizeLoopMode
        if BurstSizeStart is not None:
            self._BurstSizeStart = BurstSizeStart
            properties['BurstSizeStart'] = BurstSizeStart
        if BurstSizeStep is not None:
            self._BurstSizeStep = BurstSizeStep
            properties['BurstSizeStep'] = BurstSizeStep
        if BurstSizeEnd is not None:
            self._BurstSizeEnd = BurstSizeEnd
            properties['BurstSizeEnd'] = BurstSizeEnd
        if BurstSizeCustom is not None:
            self._BurstSizeCustom = BurstSizeCustom
            properties['BurstSizeCustom'] = BurstSizeCustom
        if Backoff is not None:
            self._Backoff = Backoff
            properties['Backoff'] = Backoff
        if IgnoreMinMaxLimit is not None:
            self._IgnoreMinMaxLimit = IgnoreMinMaxLimit
            properties['IgnoreMinMaxLimit'] = IgnoreMinMaxLimit

        super(ForwardingConfig, self).edit(**properties)

    @property
    def TrafficLoadSearchMode(self):
        """
        get the value of property _TrafficLoadSearchMode
        """
        if self.force_auto_sync:
            self.get('TrafficLoadSearchMode')
        return self._TrafficLoadSearchMode

    @property
    def LowestRate(self):
        """
        get the value of property _LowestRate
        """
        if self.force_auto_sync:
            self.get('LowestRate')
        return self._LowestRate

    @property
    def UppermostRate(self):
        """
        get the value of property _UppermostRate
        """
        if self.force_auto_sync:
            self.get('UppermostRate')
        return self._UppermostRate

    @property
    def InitRate(self):
        """
        get the value of property _InitRate
        """
        if self.force_auto_sync:
            self.get('InitRate')
        return self._InitRate

    @property
    def RateStep(self):
        """
        get the value of property _RateStep
        """
        if self.force_auto_sync:
            self.get('RateStep')
        return self._RateStep

    @property
    def RateResolution(self):
        """
        get the value of property _RateResolution
        """
        if self.force_auto_sync:
            self.get('RateResolution')
        return self._RateResolution

    @property
    def AcceptableFrameLoss(self):
        """
        get the value of property _AcceptableFrameLoss
        """
        if self.force_auto_sync:
            self.get('AcceptableFrameLoss')
        return self._AcceptableFrameLoss

    @property
    def BurstSizeLoopMode(self):
        """
        get the value of property _BurstSizeLoopMode
        """
        if self.force_auto_sync:
            self.get('BurstSizeLoopMode')
        return self._BurstSizeLoopMode

    @property
    def BurstSizeStart(self):
        """
        get the value of property _BurstSizeStart
        """
        if self.force_auto_sync:
            self.get('BurstSizeStart')
        return self._BurstSizeStart

    @property
    def BurstSizeStep(self):
        """
        get the value of property _BurstSizeStep
        """
        if self.force_auto_sync:
            self.get('BurstSizeStep')
        return self._BurstSizeStep

    @property
    def BurstSizeEnd(self):
        """
        get the value of property _BurstSizeEnd
        """
        if self.force_auto_sync:
            self.get('BurstSizeEnd')
        return self._BurstSizeEnd

    @property
    def BurstSizeCustom(self):
        """
        get the value of property _BurstSizeCustom
        """
        if self.force_auto_sync:
            self.get('BurstSizeCustom')
        return self._BurstSizeCustom

    @property
    def Backoff(self):
        """
        get the value of property _Backoff
        """
        if self.force_auto_sync:
            self.get('Backoff')
        return self._Backoff

    @property
    def IgnoreMinMaxLimit(self):
        """
        get the value of property _IgnoreMinMaxLimit
        """
        if self.force_auto_sync:
            self.get('IgnoreMinMaxLimit')
        return self._IgnoreMinMaxLimit

    @TrafficLoadSearchMode.setter
    def TrafficLoadSearchMode(self, value):
        self._TrafficLoadSearchMode = value
        self.edit(TrafficLoadSearchMode=value)

    @LowestRate.setter
    def LowestRate(self, value):
        self._LowestRate = value
        self.edit(LowestRate=value)

    @UppermostRate.setter
    def UppermostRate(self, value):
        self._UppermostRate = value
        self.edit(UppermostRate=value)

    @InitRate.setter
    def InitRate(self, value):
        self._InitRate = value
        self.edit(InitRate=value)

    @RateStep.setter
    def RateStep(self, value):
        self._RateStep = value
        self.edit(RateStep=value)

    @RateResolution.setter
    def RateResolution(self, value):
        self._RateResolution = value
        self.edit(RateResolution=value)

    @AcceptableFrameLoss.setter
    def AcceptableFrameLoss(self, value):
        self._AcceptableFrameLoss = value
        self.edit(AcceptableFrameLoss=value)

    @BurstSizeLoopMode.setter
    def BurstSizeLoopMode(self, value):
        self._BurstSizeLoopMode = value
        self.edit(BurstSizeLoopMode=value)

    @BurstSizeStart.setter
    def BurstSizeStart(self, value):
        self._BurstSizeStart = value
        self.edit(BurstSizeStart=value)

    @BurstSizeStep.setter
    def BurstSizeStep(self, value):
        self._BurstSizeStep = value
        self.edit(BurstSizeStep=value)

    @BurstSizeEnd.setter
    def BurstSizeEnd(self, value):
        self._BurstSizeEnd = value
        self.edit(BurstSizeEnd=value)

    @BurstSizeCustom.setter
    def BurstSizeCustom(self, value):
        self._BurstSizeCustom = value
        self.edit(BurstSizeCustom=value)

    @Backoff.setter
    def Backoff(self, value):
        self._Backoff = value
        self.edit(Backoff=value)

    @IgnoreMinMaxLimit.setter
    def IgnoreMinMaxLimit(self, value):
        self._IgnoreMinMaxLimit = value
        self.edit(IgnoreMinMaxLimit=value)

    def _set_trafficloadsearchmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficLoadSearchMode = EnumSearchMode.%s' % value[:seperate])

    def _set_lowestrate_with_str(self, value):
        self._LowestRate = float(value)

    def _set_uppermostrate_with_str(self, value):
        self._UppermostRate = float(value)

    def _set_initrate_with_str(self, value):
        self._InitRate = float(value)

    def _set_ratestep_with_str(self, value):
        self._RateStep = float(value)

    def _set_rateresolution_with_str(self, value):
        self._RateResolution = float(value)

    def _set_acceptableframeloss_with_str(self, value):
        self._AcceptableFrameLoss = float(value)

    def _set_burstsizeloopmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._BurstSizeLoopMode = EnumIterationMode.%s' % value[:seperate])

    def _set_burstsizestart_with_str(self, value):
        try:
            self._BurstSizeStart = int(value)
        except ValueError:
            self._BurstSizeStart = hex(int(value, 16))

    def _set_burstsizestep_with_str(self, value):
        try:
            self._BurstSizeStep = int(value)
        except ValueError:
            self._BurstSizeStep = hex(int(value, 16))

    def _set_burstsizeend_with_str(self, value):
        try:
            self._BurstSizeEnd = int(value)
        except ValueError:
            self._BurstSizeEnd = hex(int(value, 16))

    def _set_burstsizecustom_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._BurstSizeCustom = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._BurstSizeCustom.append(int(str_value))
            except ValueError:
                self._BurstSizeCustom.append(hex(int(str_value, 16)))

    def _set_backoff_with_str(self, value):
        self._Backoff = float(value)

    def _set_ignoreminmaxlimit_with_str(self, value):
        self._IgnoreMinMaxLimit = (value == 'True')

