"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BaseLoadProfileConfig_Autogen import BaseLoadProfileConfig


@rom_manager.rom
class StaticLoadProfileConfig(BaseLoadProfileConfig):
    def __init__(self, TrafficLoadMode=None, RandomMinLoad=None, RandomMaxLoad=None, TrafficLoadStart=None, TrafficLoadStep=None, TrafficLoadEnd=None, TrafficLoadCustom=None, **kwargs):
        self._TrafficLoadMode = TrafficLoadMode  # Rate mode
        self._RandomMinLoad = RandomMinLoad  # Min
        self._RandomMaxLoad = RandomMaxLoad  # Max
        self._TrafficLoadStart = TrafficLoadStart  # Start
        self._TrafficLoadStep = TrafficLoadStep  # Step
        self._TrafficLoadEnd = TrafficLoadEnd  # End
        self._TrafficLoadCustom = TrafficLoadCustom  # Custom Load List

        properties = kwargs.copy()
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
        super(StaticLoadProfileConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TrafficLoadMode=None, RandomMinLoad=None, RandomMaxLoad=None, TrafficLoadStart=None, TrafficLoadStep=None, TrafficLoadEnd=None, TrafficLoadCustom=None, **kwargs):
        properties = kwargs.copy()
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

        super(StaticLoadProfileConfig, self).edit(**properties)

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

    def _set_trafficloadmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficLoadMode = EnumAsymmetricLoadMode.%s' % value[:seperate])

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

