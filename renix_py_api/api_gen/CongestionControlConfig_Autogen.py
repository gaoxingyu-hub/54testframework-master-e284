"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc2889Config_Autogen import Rfc2889Config


@rom_manager.rom
class CongestionControlConfig(Rfc2889Config):
    def __init__(self, TrafficLoadMode=None, TrafficLoadUnit=None, RandomMinLoad=None, RandomMaxLoad=None, TrafficLoadStart=None, TrafficLoadStep=None, TrafficLoadEnd=None, TrafficLoadCustom=None, BurstSizeLoopMode=None, BurstSizeStart=None, BurstSizeStep=None, BurstSizeEnd=None, BurstSizeCustom=None, DiagramMode=None, **kwargs):
        self._TrafficLoadMode = TrafficLoadMode  # Traffic Load loop mode
        self._TrafficLoadUnit = TrafficLoadUnit  # Traffic Load Unit
        self._RandomMinLoad = RandomMinLoad  # Min
        self._RandomMaxLoad = RandomMaxLoad  # Max
        self._TrafficLoadStart = TrafficLoadStart  # Start
        self._TrafficLoadStep = TrafficLoadStep  # Step
        self._TrafficLoadEnd = TrafficLoadEnd  # End
        self._TrafficLoadCustom = TrafficLoadCustom  # Custom
        self._BurstSizeLoopMode = BurstSizeLoopMode  # Burst Size loop mode
        self._BurstSizeStart = BurstSizeStart  # Start
        self._BurstSizeStep = BurstSizeStep  # Step
        self._BurstSizeEnd = BurstSizeEnd  # End
        self._BurstSizeCustom = BurstSizeCustom  # Custom
        self._DiagramMode = DiagramMode  # Diagram Mode

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
        if DiagramMode is not None:
            properties['DiagramMode'] = DiagramMode

        # call base class function, and it will send message to renix server to create a class.
        super(CongestionControlConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TrafficLoadMode=None, TrafficLoadUnit=None, RandomMinLoad=None, RandomMaxLoad=None, TrafficLoadStart=None, TrafficLoadStep=None, TrafficLoadEnd=None, TrafficLoadCustom=None, BurstSizeLoopMode=None, BurstSizeStart=None, BurstSizeStep=None, BurstSizeEnd=None, BurstSizeCustom=None, DiagramMode=None, **kwargs):
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
        if DiagramMode is not None:
            self._DiagramMode = DiagramMode
            properties['DiagramMode'] = DiagramMode

        super(CongestionControlConfig, self).edit(**properties)

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
    def DiagramMode(self):
        """
        get the value of property _DiagramMode
        """
        if self.force_auto_sync:
            self.get('DiagramMode')
        return self._DiagramMode

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

    @DiagramMode.setter
    def DiagramMode(self, value):
        self._DiagramMode = value
        self.edit(DiagramMode=value)

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

    def _set_diagrammode_with_str(self, value):
        seperate = value.find(':')
        exec('self._DiagramMode = EnumDiagramMode.%s' % value[:seperate])

