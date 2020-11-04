"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc2544Config_Autogen import Rfc2544Config


@rom_manager.rom
class AsymmetricTestConfig(Rfc2544Config):
    def __init__(self, BackOffMode=None, TrafficDirection=None, ProfileAllocation=None, LatencyDistribution=None, BreakLoadLoop=None, PassLoadIteration=None, TrafficLoadUnit=None, **kwargs):
        self._BackOffMode = BackOffMode  # Back-Off Mode
        self._TrafficDirection = TrafficDirection  # Direction
        self._ProfileAllocation = ProfileAllocation  # Profile Allocation
        self._LatencyDistribution = LatencyDistribution  # Latency Distribution (ns)
        self._BreakLoadLoop = BreakLoadLoop  # Break Load Loop
        self._PassLoadIteration = PassLoadIteration  # Pass iterations
        self._TrafficLoadUnit = TrafficLoadUnit  # Traffic load units

        properties = kwargs.copy()
        if BackOffMode is not None:
            properties['BackOffMode'] = BackOffMode
        if TrafficDirection is not None:
            properties['TrafficDirection'] = TrafficDirection
        if ProfileAllocation is not None:
            properties['ProfileAllocation'] = ProfileAllocation
        if LatencyDistribution is not None:
            properties['LatencyDistribution'] = LatencyDistribution
        if BreakLoadLoop is not None:
            properties['BreakLoadLoop'] = BreakLoadLoop
        if PassLoadIteration is not None:
            properties['PassLoadIteration'] = PassLoadIteration
        if TrafficLoadUnit is not None:
            properties['TrafficLoadUnit'] = TrafficLoadUnit

        # call base class function, and it will send message to renix server to create a class.
        super(AsymmetricTestConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, BackOffMode=None, TrafficDirection=None, ProfileAllocation=None, LatencyDistribution=None, BreakLoadLoop=None, PassLoadIteration=None, TrafficLoadUnit=None, **kwargs):
        properties = kwargs.copy()
        if BackOffMode is not None:
            self._BackOffMode = BackOffMode
            properties['BackOffMode'] = BackOffMode
        if TrafficDirection is not None:
            self._TrafficDirection = TrafficDirection
            properties['TrafficDirection'] = TrafficDirection
        if ProfileAllocation is not None:
            self._ProfileAllocation = ProfileAllocation
            properties['ProfileAllocation'] = ProfileAllocation
        if LatencyDistribution is not None:
            self._LatencyDistribution = LatencyDistribution
            properties['LatencyDistribution'] = LatencyDistribution
        if BreakLoadLoop is not None:
            self._BreakLoadLoop = BreakLoadLoop
            properties['BreakLoadLoop'] = BreakLoadLoop
        if PassLoadIteration is not None:
            self._PassLoadIteration = PassLoadIteration
            properties['PassLoadIteration'] = PassLoadIteration
        if TrafficLoadUnit is not None:
            self._TrafficLoadUnit = TrafficLoadUnit
            properties['TrafficLoadUnit'] = TrafficLoadUnit

        super(AsymmetricTestConfig, self).edit(**properties)

    @property
    def BackOffMode(self):
        """
        get the value of property _BackOffMode
        """
        if self.force_auto_sync:
            self.get('BackOffMode')
        return self._BackOffMode

    @property
    def TrafficDirection(self):
        """
        get the value of property _TrafficDirection
        """
        if self.force_auto_sync:
            self.get('TrafficDirection')
        return self._TrafficDirection

    @property
    def ProfileAllocation(self):
        """
        get the value of property _ProfileAllocation
        """
        if self.force_auto_sync:
            self.get('ProfileAllocation')
        return self._ProfileAllocation

    @property
    def LatencyDistribution(self):
        """
        get the value of property _LatencyDistribution
        """
        if self.force_auto_sync:
            self.get('LatencyDistribution')
        return self._LatencyDistribution

    @property
    def BreakLoadLoop(self):
        """
        get the value of property _BreakLoadLoop
        """
        if self.force_auto_sync:
            self.get('BreakLoadLoop')
        return self._BreakLoadLoop

    @property
    def PassLoadIteration(self):
        """
        get the value of property _PassLoadIteration
        """
        if self.force_auto_sync:
            self.get('PassLoadIteration')
        return self._PassLoadIteration

    @property
    def TrafficLoadUnit(self):
        """
        get the value of property _TrafficLoadUnit
        """
        if self.force_auto_sync:
            self.get('TrafficLoadUnit')
        return self._TrafficLoadUnit

    @BackOffMode.setter
    def BackOffMode(self, value):
        self._BackOffMode = value
        self.edit(BackOffMode=value)

    @TrafficDirection.setter
    def TrafficDirection(self, value):
        self._TrafficDirection = value
        self.edit(TrafficDirection=value)

    @ProfileAllocation.setter
    def ProfileAllocation(self, value):
        self._ProfileAllocation = value
        self.edit(ProfileAllocation=value)

    @LatencyDistribution.setter
    def LatencyDistribution(self, value):
        self._LatencyDistribution = value
        self.edit(LatencyDistribution=value)

    @BreakLoadLoop.setter
    def BreakLoadLoop(self, value):
        self._BreakLoadLoop = value
        self.edit(BreakLoadLoop=value)

    @PassLoadIteration.setter
    def PassLoadIteration(self, value):
        self._PassLoadIteration = value
        self.edit(PassLoadIteration=value)

    @TrafficLoadUnit.setter
    def TrafficLoadUnit(self, value):
        self._TrafficLoadUnit = value
        self.edit(TrafficLoadUnit=value)

    def _set_backoffmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._BackOffMode = EnumBackOffMode.%s' % value[:seperate])

    def _set_trafficdirection_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficDirection = EnumTrafficDirection.%s' % value[:seperate])

    def _set_profileallocation_with_str(self, value):
        seperate = value.find(':')
        exec('self._ProfileAllocation = EnumProfileAllocation.%s' % value[:seperate])

    def _set_latencydistribution_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._LatencyDistribution = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._LatencyDistribution.append(int(str_value))
            except ValueError:
                self._LatencyDistribution.append(hex(int(str_value, 16)))

    def _set_breakloadloop_with_str(self, value):
        self._BreakLoadLoop = (value == 'True')

    def _set_passloaditeration_with_str(self, value):
        try:
            self._PassLoadIteration = int(value)
        except ValueError:
            self._PassLoadIteration = hex(int(value, 16))

    def _set_trafficloadunit_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficLoadUnit = EnumLoadUnit.%s' % value[:seperate])

