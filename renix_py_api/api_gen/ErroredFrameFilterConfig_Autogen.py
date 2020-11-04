"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc2889Config_Autogen import Rfc2889Config


@rom_manager.rom
class ErroredFrameFilterConfig(Rfc2889Config):
    def __init__(self, TrafficLoadMode=None, TrafficLoadUnit=None, RandomMinLoad=None, RandomMaxLoad=None, TrafficLoadStart=None, TrafficLoadStep=None, TrafficLoadEnd=None, TrafficLoadCustom=None, CrcChecked=None, CrcErroredFrameSize=None, UnderSizedChecked=None, UnderSizedFrameSize=None, OverSizedChecked=None, OverSizedFrameSize=None, MaxLegalFrameSize=None, BurstSize=None, **kwargs):
        self._TrafficLoadMode = TrafficLoadMode  # Traffic Load loop mode
        self._TrafficLoadUnit = TrafficLoadUnit  # Traffic Load Unit
        self._RandomMinLoad = RandomMinLoad  # Min
        self._RandomMaxLoad = RandomMaxLoad  # Max
        self._TrafficLoadStart = TrafficLoadStart  # Start
        self._TrafficLoadStep = TrafficLoadStep  # Step
        self._TrafficLoadEnd = TrafficLoadEnd  # End
        self._TrafficLoadCustom = TrafficLoadCustom  # Custom
        self._CrcChecked = CrcChecked  # Enable Crc Errored Frame
        self._CrcErroredFrameSize = CrcErroredFrameSize  # Crc Errored Frame Size
        self._UnderSizedChecked = UnderSizedChecked  # Enable Under Sized Frame
        self._UnderSizedFrameSize = UnderSizedFrameSize  # Under Sized Frame Size
        self._OverSizedChecked = OverSizedChecked  # Enable Over Sized Frame
        self._OverSizedFrameSize = OverSizedFrameSize  # Over Sized Frame Size
        self._MaxLegalFrameSize = MaxLegalFrameSize  # Max Legal Frame Size
        self._BurstSize = BurstSize  # Burst Size

        properties = kwargs.copy()
        if TrafficLoadMode is not None:
            properties['TrafficLoadMode'] = TrafficLoadMode
        if TrafficLoadUnit is not None:
            properties['TrafficLoadUnit'] = TrafficLoadUnit
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
        if MaxLegalFrameSize is not None:
            properties['MaxLegalFrameSize'] = MaxLegalFrameSize
        if BurstSize is not None:
            properties['BurstSize'] = BurstSize

        # call base class function, and it will send message to renix server to create a class.
        super(ErroredFrameFilterConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TrafficLoadMode=None, TrafficLoadUnit=None, RandomMinLoad=None, RandomMaxLoad=None, TrafficLoadStart=None, TrafficLoadStep=None, TrafficLoadEnd=None, TrafficLoadCustom=None, CrcChecked=None, CrcErroredFrameSize=None, UnderSizedChecked=None, UnderSizedFrameSize=None, OverSizedChecked=None, OverSizedFrameSize=None, MaxLegalFrameSize=None, BurstSize=None, **kwargs):
        properties = kwargs.copy()
        if TrafficLoadMode is not None:
            self._TrafficLoadMode = TrafficLoadMode
            properties['TrafficLoadMode'] = TrafficLoadMode
        if TrafficLoadUnit is not None:
            self._TrafficLoadUnit = TrafficLoadUnit
            properties['TrafficLoadUnit'] = TrafficLoadUnit
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
        if CrcChecked is not None:
            self._CrcChecked = CrcChecked
            properties['CrcChecked'] = CrcChecked
        if CrcErroredFrameSize is not None:
            self._CrcErroredFrameSize = CrcErroredFrameSize
            properties['CrcErroredFrameSize'] = CrcErroredFrameSize
        if UnderSizedChecked is not None:
            self._UnderSizedChecked = UnderSizedChecked
            properties['UnderSizedChecked'] = UnderSizedChecked
        if UnderSizedFrameSize is not None:
            self._UnderSizedFrameSize = UnderSizedFrameSize
            properties['UnderSizedFrameSize'] = UnderSizedFrameSize
        if OverSizedChecked is not None:
            self._OverSizedChecked = OverSizedChecked
            properties['OverSizedChecked'] = OverSizedChecked
        if OverSizedFrameSize is not None:
            self._OverSizedFrameSize = OverSizedFrameSize
            properties['OverSizedFrameSize'] = OverSizedFrameSize
        if MaxLegalFrameSize is not None:
            self._MaxLegalFrameSize = MaxLegalFrameSize
            properties['MaxLegalFrameSize'] = MaxLegalFrameSize
        if BurstSize is not None:
            self._BurstSize = BurstSize
            properties['BurstSize'] = BurstSize

        super(ErroredFrameFilterConfig, self).edit(**properties)

    @property
    def TrafficLoadMode(self):
        """
        get the value of property _TrafficLoadMode
        """
        if self.force_auto_sync:
            self.get('TrafficLoadMode')
        return self._TrafficLoadMode

    @property
    def TrafficLoadUnit(self):
        """
        get the value of property _TrafficLoadUnit
        """
        if self.force_auto_sync:
            self.get('TrafficLoadUnit')
        return self._TrafficLoadUnit

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

    @property
    def CrcChecked(self):
        """
        get the value of property _CrcChecked
        """
        if self.force_auto_sync:
            self.get('CrcChecked')
        return self._CrcChecked

    @property
    def CrcErroredFrameSize(self):
        """
        get the value of property _CrcErroredFrameSize
        """
        if self.force_auto_sync:
            self.get('CrcErroredFrameSize')
        return self._CrcErroredFrameSize

    @property
    def UnderSizedChecked(self):
        """
        get the value of property _UnderSizedChecked
        """
        if self.force_auto_sync:
            self.get('UnderSizedChecked')
        return self._UnderSizedChecked

    @property
    def UnderSizedFrameSize(self):
        """
        get the value of property _UnderSizedFrameSize
        """
        if self.force_auto_sync:
            self.get('UnderSizedFrameSize')
        return self._UnderSizedFrameSize

    @property
    def OverSizedChecked(self):
        """
        get the value of property _OverSizedChecked
        """
        if self.force_auto_sync:
            self.get('OverSizedChecked')
        return self._OverSizedChecked

    @property
    def OverSizedFrameSize(self):
        """
        get the value of property _OverSizedFrameSize
        """
        if self.force_auto_sync:
            self.get('OverSizedFrameSize')
        return self._OverSizedFrameSize

    @property
    def MaxLegalFrameSize(self):
        """
        get the value of property _MaxLegalFrameSize
        """
        if self.force_auto_sync:
            self.get('MaxLegalFrameSize')
        return self._MaxLegalFrameSize

    @property
    def BurstSize(self):
        """
        get the value of property _BurstSize
        """
        if self.force_auto_sync:
            self.get('BurstSize')
        return self._BurstSize

    @TrafficLoadMode.setter
    def TrafficLoadMode(self, value):
        self._TrafficLoadMode = value
        self.edit(TrafficLoadMode=value)

    @TrafficLoadUnit.setter
    def TrafficLoadUnit(self, value):
        self._TrafficLoadUnit = value
        self.edit(TrafficLoadUnit=value)

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

    @CrcChecked.setter
    def CrcChecked(self, value):
        self._CrcChecked = value
        self.edit(CrcChecked=value)

    @CrcErroredFrameSize.setter
    def CrcErroredFrameSize(self, value):
        self._CrcErroredFrameSize = value
        self.edit(CrcErroredFrameSize=value)

    @UnderSizedChecked.setter
    def UnderSizedChecked(self, value):
        self._UnderSizedChecked = value
        self.edit(UnderSizedChecked=value)

    @UnderSizedFrameSize.setter
    def UnderSizedFrameSize(self, value):
        self._UnderSizedFrameSize = value
        self.edit(UnderSizedFrameSize=value)

    @OverSizedChecked.setter
    def OverSizedChecked(self, value):
        self._OverSizedChecked = value
        self.edit(OverSizedChecked=value)

    @OverSizedFrameSize.setter
    def OverSizedFrameSize(self, value):
        self._OverSizedFrameSize = value
        self.edit(OverSizedFrameSize=value)

    @MaxLegalFrameSize.setter
    def MaxLegalFrameSize(self, value):
        self._MaxLegalFrameSize = value
        self.edit(MaxLegalFrameSize=value)

    @BurstSize.setter
    def BurstSize(self, value):
        self._BurstSize = value
        self.edit(BurstSize=value)

    def _set_trafficloadmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficLoadMode = EnumLoadMode.%s' % value[:seperate])

    def _set_trafficloadunit_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficLoadUnit = EnumLoadUnit.%s' % value[:seperate])

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

    def _set_maxlegalframesize_with_str(self, value):
        try:
            self._MaxLegalFrameSize = int(value)
        except ValueError:
            self._MaxLegalFrameSize = hex(int(value, 16))

    def _set_burstsize_with_str(self, value):
        try:
            self._BurstSize = int(value)
        except ValueError:
            self._BurstSize = hex(int(value, 16))

