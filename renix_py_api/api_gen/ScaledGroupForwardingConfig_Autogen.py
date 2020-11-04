"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc3918Config_Autogen import Rfc3918Config


@rom_manager.rom
class ScaledGroupForwardingConfig(Rfc3918Config):
    def __init__(self, TrafficLoadUnit=None, TrafficLoadMode=None, TrafficLoad=None, RandomMinLoad=None, RandomMaxLoad=None, TrafficLoadStart=None, TrafficLoadStep=None, TrafficLoadEnd=None, TrafficLoadCustom=None, McGroupCountMode=None, McGroupCount=None, RandomMinMcGroupCount=None, RandomMaxMcGroupCount=None, McGroupCountStart=None, McGroupCountStep=None, McGroupCountEnd=None, McGroupCountCustom=None, **kwargs):
        self._TrafficLoadUnit = TrafficLoadUnit  # Traffic load units
        self._TrafficLoadMode = TrafficLoadMode  # Traffic load search mode
        self._TrafficLoad = TrafficLoad  # Traffic Load
        self._RandomMinLoad = RandomMinLoad  # Min
        self._RandomMaxLoad = RandomMaxLoad  # Max
        self._TrafficLoadStart = TrafficLoadStart  # Start
        self._TrafficLoadStep = TrafficLoadStep  # Step
        self._TrafficLoadEnd = TrafficLoadEnd  # End
        self._TrafficLoadCustom = TrafficLoadCustom  # Custom
        self._McGroupCountMode = McGroupCountMode  # Multicast Group Mode
        self._McGroupCount = McGroupCount  # Multicast Group Count
        self._RandomMinMcGroupCount = RandomMinMcGroupCount  # Min
        self._RandomMaxMcGroupCount = RandomMaxMcGroupCount  # Max
        self._McGroupCountStart = McGroupCountStart  # Start
        self._McGroupCountStep = McGroupCountStep  # Step
        self._McGroupCountEnd = McGroupCountEnd  # End
        self._McGroupCountCustom = McGroupCountCustom  # Custom

        properties = kwargs.copy()
        if TrafficLoadUnit is not None:
            properties['TrafficLoadUnit'] = TrafficLoadUnit
        if TrafficLoadMode is not None:
            properties['TrafficLoadMode'] = TrafficLoadMode
        if TrafficLoad is not None:
            properties['TrafficLoad'] = TrafficLoad
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
        if McGroupCountMode is not None:
            properties['McGroupCountMode'] = McGroupCountMode
        if McGroupCount is not None:
            properties['McGroupCount'] = McGroupCount
        if RandomMinMcGroupCount is not None:
            properties['RandomMinMcGroupCount'] = RandomMinMcGroupCount
        if RandomMaxMcGroupCount is not None:
            properties['RandomMaxMcGroupCount'] = RandomMaxMcGroupCount
        if McGroupCountStart is not None:
            properties['McGroupCountStart'] = McGroupCountStart
        if McGroupCountStep is not None:
            properties['McGroupCountStep'] = McGroupCountStep
        if McGroupCountEnd is not None:
            properties['McGroupCountEnd'] = McGroupCountEnd
        if McGroupCountCustom is not None:
            properties['McGroupCountCustom'] = McGroupCountCustom

        # call base class function, and it will send message to renix server to create a class.
        super(ScaledGroupForwardingConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TrafficLoadUnit=None, TrafficLoadMode=None, TrafficLoad=None, RandomMinLoad=None, RandomMaxLoad=None, TrafficLoadStart=None, TrafficLoadStep=None, TrafficLoadEnd=None, TrafficLoadCustom=None, McGroupCountMode=None, McGroupCount=None, RandomMinMcGroupCount=None, RandomMaxMcGroupCount=None, McGroupCountStart=None, McGroupCountStep=None, McGroupCountEnd=None, McGroupCountCustom=None, **kwargs):
        properties = kwargs.copy()
        if TrafficLoadUnit is not None:
            self._TrafficLoadUnit = TrafficLoadUnit
            properties['TrafficLoadUnit'] = TrafficLoadUnit
        if TrafficLoadMode is not None:
            self._TrafficLoadMode = TrafficLoadMode
            properties['TrafficLoadMode'] = TrafficLoadMode
        if TrafficLoad is not None:
            self._TrafficLoad = TrafficLoad
            properties['TrafficLoad'] = TrafficLoad
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
        if McGroupCountMode is not None:
            self._McGroupCountMode = McGroupCountMode
            properties['McGroupCountMode'] = McGroupCountMode
        if McGroupCount is not None:
            self._McGroupCount = McGroupCount
            properties['McGroupCount'] = McGroupCount
        if RandomMinMcGroupCount is not None:
            self._RandomMinMcGroupCount = RandomMinMcGroupCount
            properties['RandomMinMcGroupCount'] = RandomMinMcGroupCount
        if RandomMaxMcGroupCount is not None:
            self._RandomMaxMcGroupCount = RandomMaxMcGroupCount
            properties['RandomMaxMcGroupCount'] = RandomMaxMcGroupCount
        if McGroupCountStart is not None:
            self._McGroupCountStart = McGroupCountStart
            properties['McGroupCountStart'] = McGroupCountStart
        if McGroupCountStep is not None:
            self._McGroupCountStep = McGroupCountStep
            properties['McGroupCountStep'] = McGroupCountStep
        if McGroupCountEnd is not None:
            self._McGroupCountEnd = McGroupCountEnd
            properties['McGroupCountEnd'] = McGroupCountEnd
        if McGroupCountCustom is not None:
            self._McGroupCountCustom = McGroupCountCustom
            properties['McGroupCountCustom'] = McGroupCountCustom

        super(ScaledGroupForwardingConfig, self).edit(**properties)

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
    def TrafficLoad(self):
        """
        get the value of property _TrafficLoad
        """
        if self.force_auto_sync:
            self.get('TrafficLoad')
        return self._TrafficLoad

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
    def McGroupCountMode(self):
        """
        get the value of property _McGroupCountMode
        """
        if self.force_auto_sync:
            self.get('McGroupCountMode')
        return self._McGroupCountMode

    @property
    def McGroupCount(self):
        """
        get the value of property _McGroupCount
        """
        if self.force_auto_sync:
            self.get('McGroupCount')
        return self._McGroupCount

    @property
    def RandomMinMcGroupCount(self):
        """
        get the value of property _RandomMinMcGroupCount
        """
        if self.force_auto_sync:
            self.get('RandomMinMcGroupCount')
        return self._RandomMinMcGroupCount

    @property
    def RandomMaxMcGroupCount(self):
        """
        get the value of property _RandomMaxMcGroupCount
        """
        if self.force_auto_sync:
            self.get('RandomMaxMcGroupCount')
        return self._RandomMaxMcGroupCount

    @property
    def McGroupCountStart(self):
        """
        get the value of property _McGroupCountStart
        """
        if self.force_auto_sync:
            self.get('McGroupCountStart')
        return self._McGroupCountStart

    @property
    def McGroupCountStep(self):
        """
        get the value of property _McGroupCountStep
        """
        if self.force_auto_sync:
            self.get('McGroupCountStep')
        return self._McGroupCountStep

    @property
    def McGroupCountEnd(self):
        """
        get the value of property _McGroupCountEnd
        """
        if self.force_auto_sync:
            self.get('McGroupCountEnd')
        return self._McGroupCountEnd

    @property
    def McGroupCountCustom(self):
        """
        get the value of property _McGroupCountCustom
        """
        if self.force_auto_sync:
            self.get('McGroupCountCustom')
        return self._McGroupCountCustom

    @TrafficLoadUnit.setter
    def TrafficLoadUnit(self, value):
        self._TrafficLoadUnit = value
        self.edit(TrafficLoadUnit=value)

    @TrafficLoadMode.setter
    def TrafficLoadMode(self, value):
        self._TrafficLoadMode = value
        self.edit(TrafficLoadMode=value)

    @TrafficLoad.setter
    def TrafficLoad(self, value):
        self._TrafficLoad = value
        self.edit(TrafficLoad=value)

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

    @McGroupCountMode.setter
    def McGroupCountMode(self, value):
        self._McGroupCountMode = value
        self.edit(McGroupCountMode=value)

    @McGroupCount.setter
    def McGroupCount(self, value):
        self._McGroupCount = value
        self.edit(McGroupCount=value)

    @RandomMinMcGroupCount.setter
    def RandomMinMcGroupCount(self, value):
        self._RandomMinMcGroupCount = value
        self.edit(RandomMinMcGroupCount=value)

    @RandomMaxMcGroupCount.setter
    def RandomMaxMcGroupCount(self, value):
        self._RandomMaxMcGroupCount = value
        self.edit(RandomMaxMcGroupCount=value)

    @McGroupCountStart.setter
    def McGroupCountStart(self, value):
        self._McGroupCountStart = value
        self.edit(McGroupCountStart=value)

    @McGroupCountStep.setter
    def McGroupCountStep(self, value):
        self._McGroupCountStep = value
        self.edit(McGroupCountStep=value)

    @McGroupCountEnd.setter
    def McGroupCountEnd(self, value):
        self._McGroupCountEnd = value
        self.edit(McGroupCountEnd=value)

    @McGroupCountCustom.setter
    def McGroupCountCustom(self, value):
        self._McGroupCountCustom = value
        self.edit(McGroupCountCustom=value)

    def _set_trafficloadunit_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficLoadUnit = EnumLoadUnit.%s' % value[:seperate])

    def _set_trafficloadmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficLoadMode = EnumLoadMode.%s' % value[:seperate])

    def _set_trafficload_with_str(self, value):
        self._TrafficLoad = float(value)

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

    def _set_mcgroupcountmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._McGroupCountMode = EnumMulticastGroupCountMode.%s' % value[:seperate])

    def _set_mcgroupcount_with_str(self, value):
        try:
            self._McGroupCount = int(value)
        except ValueError:
            self._McGroupCount = hex(int(value, 16))

    def _set_randomminmcgroupcount_with_str(self, value):
        try:
            self._RandomMinMcGroupCount = int(value)
        except ValueError:
            self._RandomMinMcGroupCount = hex(int(value, 16))

    def _set_randommaxmcgroupcount_with_str(self, value):
        try:
            self._RandomMaxMcGroupCount = int(value)
        except ValueError:
            self._RandomMaxMcGroupCount = hex(int(value, 16))

    def _set_mcgroupcountstart_with_str(self, value):
        try:
            self._McGroupCountStart = int(value)
        except ValueError:
            self._McGroupCountStart = hex(int(value, 16))

    def _set_mcgroupcountstep_with_str(self, value):
        try:
            self._McGroupCountStep = int(value)
        except ValueError:
            self._McGroupCountStep = hex(int(value, 16))

    def _set_mcgroupcountend_with_str(self, value):
        try:
            self._McGroupCountEnd = int(value)
        except ValueError:
            self._McGroupCountEnd = hex(int(value, 16))

    def _set_mcgroupcountcustom_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._McGroupCountCustom = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._McGroupCountCustom.append(int(str_value))
            except ValueError:
                self._McGroupCountCustom.append(hex(int(str_value, 16)))

