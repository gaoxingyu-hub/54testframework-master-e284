"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc3918Config_Autogen import Rfc3918Config


@rom_manager.rom
class MulticastGroupCapacityConfig(Rfc3918Config):
    def __init__(self, McGroupCountSearchMode=None, MinMcGroupCount=None, MaxMcGroupCount=None, InitMcGroupCount=None, McGroupCountStep=None, McGroupCountResolution=None, McGroupCountBackoff=None, TrafficLoadUnit=None, TrafficLoadMode=None, TrafficLoad=None, RandomMinLoad=None, RandomMaxLoad=None, TrafficLoadStart=None, TrafficLoadStep=None, TrafficLoadEnd=None, TrafficLoadCustom=None, **kwargs):
        self._McGroupCountSearchMode = McGroupCountSearchMode  # Multicast Group Count search mode
        self._MinMcGroupCount = MinMcGroupCount  # Minimum Multicast Group Count
        self._MaxMcGroupCount = MaxMcGroupCount  # Maximum Multicast Group Count
        self._InitMcGroupCount = InitMcGroupCount  # Init Multicast Group Count
        self._McGroupCountStep = McGroupCountStep  # Multicast Group Count Step
        self._McGroupCountResolution = McGroupCountResolution  # Multicast Group Count Resolution
        self._McGroupCountBackoff = McGroupCountBackoff  # Back Off
        self._TrafficLoadUnit = TrafficLoadUnit  # Traffic load units
        self._TrafficLoadMode = TrafficLoadMode  # Traffic load search mode
        self._TrafficLoad = TrafficLoad  # Traffic Load
        self._RandomMinLoad = RandomMinLoad  # Min
        self._RandomMaxLoad = RandomMaxLoad  # Max
        self._TrafficLoadStart = TrafficLoadStart  # Start
        self._TrafficLoadStep = TrafficLoadStep  # Step
        self._TrafficLoadEnd = TrafficLoadEnd  # End
        self._TrafficLoadCustom = TrafficLoadCustom  # Custom

        properties = kwargs.copy()
        if McGroupCountSearchMode is not None:
            properties['McGroupCountSearchMode'] = McGroupCountSearchMode
        if MinMcGroupCount is not None:
            properties['MinMcGroupCount'] = MinMcGroupCount
        if MaxMcGroupCount is not None:
            properties['MaxMcGroupCount'] = MaxMcGroupCount
        if InitMcGroupCount is not None:
            properties['InitMcGroupCount'] = InitMcGroupCount
        if McGroupCountStep is not None:
            properties['McGroupCountStep'] = McGroupCountStep
        if McGroupCountResolution is not None:
            properties['McGroupCountResolution'] = McGroupCountResolution
        if McGroupCountBackoff is not None:
            properties['McGroupCountBackoff'] = McGroupCountBackoff
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

        # call base class function, and it will send message to renix server to create a class.
        super(MulticastGroupCapacityConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, McGroupCountSearchMode=None, MinMcGroupCount=None, MaxMcGroupCount=None, InitMcGroupCount=None, McGroupCountStep=None, McGroupCountResolution=None, McGroupCountBackoff=None, TrafficLoadUnit=None, TrafficLoadMode=None, TrafficLoad=None, RandomMinLoad=None, RandomMaxLoad=None, TrafficLoadStart=None, TrafficLoadStep=None, TrafficLoadEnd=None, TrafficLoadCustom=None, **kwargs):
        properties = kwargs.copy()
        if McGroupCountSearchMode is not None:
            self._McGroupCountSearchMode = McGroupCountSearchMode
            properties['McGroupCountSearchMode'] = McGroupCountSearchMode
        if MinMcGroupCount is not None:
            self._MinMcGroupCount = MinMcGroupCount
            properties['MinMcGroupCount'] = MinMcGroupCount
        if MaxMcGroupCount is not None:
            self._MaxMcGroupCount = MaxMcGroupCount
            properties['MaxMcGroupCount'] = MaxMcGroupCount
        if InitMcGroupCount is not None:
            self._InitMcGroupCount = InitMcGroupCount
            properties['InitMcGroupCount'] = InitMcGroupCount
        if McGroupCountStep is not None:
            self._McGroupCountStep = McGroupCountStep
            properties['McGroupCountStep'] = McGroupCountStep
        if McGroupCountResolution is not None:
            self._McGroupCountResolution = McGroupCountResolution
            properties['McGroupCountResolution'] = McGroupCountResolution
        if McGroupCountBackoff is not None:
            self._McGroupCountBackoff = McGroupCountBackoff
            properties['McGroupCountBackoff'] = McGroupCountBackoff
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

        super(MulticastGroupCapacityConfig, self).edit(**properties)

    @property
    def McGroupCountSearchMode(self):
        """
        get the value of property _McGroupCountSearchMode
        """
        if self.force_auto_sync:
            self.get('McGroupCountSearchMode')
        return self._McGroupCountSearchMode

    @property
    def MinMcGroupCount(self):
        """
        get the value of property _MinMcGroupCount
        """
        if self.force_auto_sync:
            self.get('MinMcGroupCount')
        return self._MinMcGroupCount

    @property
    def MaxMcGroupCount(self):
        """
        get the value of property _MaxMcGroupCount
        """
        if self.force_auto_sync:
            self.get('MaxMcGroupCount')
        return self._MaxMcGroupCount

    @property
    def InitMcGroupCount(self):
        """
        get the value of property _InitMcGroupCount
        """
        if self.force_auto_sync:
            self.get('InitMcGroupCount')
        return self._InitMcGroupCount

    @property
    def McGroupCountStep(self):
        """
        get the value of property _McGroupCountStep
        """
        if self.force_auto_sync:
            self.get('McGroupCountStep')
        return self._McGroupCountStep

    @property
    def McGroupCountResolution(self):
        """
        get the value of property _McGroupCountResolution
        """
        if self.force_auto_sync:
            self.get('McGroupCountResolution')
        return self._McGroupCountResolution

    @property
    def McGroupCountBackoff(self):
        """
        get the value of property _McGroupCountBackoff
        """
        if self.force_auto_sync:
            self.get('McGroupCountBackoff')
        return self._McGroupCountBackoff

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

    @McGroupCountSearchMode.setter
    def McGroupCountSearchMode(self, value):
        self._McGroupCountSearchMode = value
        self.edit(McGroupCountSearchMode=value)

    @MinMcGroupCount.setter
    def MinMcGroupCount(self, value):
        self._MinMcGroupCount = value
        self.edit(MinMcGroupCount=value)

    @MaxMcGroupCount.setter
    def MaxMcGroupCount(self, value):
        self._MaxMcGroupCount = value
        self.edit(MaxMcGroupCount=value)

    @InitMcGroupCount.setter
    def InitMcGroupCount(self, value):
        self._InitMcGroupCount = value
        self.edit(InitMcGroupCount=value)

    @McGroupCountStep.setter
    def McGroupCountStep(self, value):
        self._McGroupCountStep = value
        self.edit(McGroupCountStep=value)

    @McGroupCountResolution.setter
    def McGroupCountResolution(self, value):
        self._McGroupCountResolution = value
        self.edit(McGroupCountResolution=value)

    @McGroupCountBackoff.setter
    def McGroupCountBackoff(self, value):
        self._McGroupCountBackoff = value
        self.edit(McGroupCountBackoff=value)

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

    def _set_mcgroupcountsearchmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._McGroupCountSearchMode = EnumSearchMode.%s' % value[:seperate])

    def _set_minmcgroupcount_with_str(self, value):
        try:
            self._MinMcGroupCount = int(value)
        except ValueError:
            self._MinMcGroupCount = hex(int(value, 16))

    def _set_maxmcgroupcount_with_str(self, value):
        try:
            self._MaxMcGroupCount = int(value)
        except ValueError:
            self._MaxMcGroupCount = hex(int(value, 16))

    def _set_initmcgroupcount_with_str(self, value):
        try:
            self._InitMcGroupCount = int(value)
        except ValueError:
            self._InitMcGroupCount = hex(int(value, 16))

    def _set_mcgroupcountstep_with_str(self, value):
        try:
            self._McGroupCountStep = int(value)
        except ValueError:
            self._McGroupCountStep = hex(int(value, 16))

    def _set_mcgroupcountresolution_with_str(self, value):
        try:
            self._McGroupCountResolution = int(value)
        except ValueError:
            self._McGroupCountResolution = hex(int(value, 16))

    def _set_mcgroupcountbackoff_with_str(self, value):
        self._McGroupCountBackoff = float(value)

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

