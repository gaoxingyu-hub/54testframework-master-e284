"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .TrafficTestCommand_Autogen import TrafficTestCommand


@rom_manager.rom
class ParallelLoadCommand(TrafficTestCommand):
    def __init__(self, ProfileAllocation=None, LoadUnit=None, **kwargs):
        self._ProfileAllocation = ProfileAllocation  # Profile Allocation
        self._LoadUnit = LoadUnit  # Traffic load units

        properties = kwargs.copy()
        if ProfileAllocation is not None:
            properties['ProfileAllocation'] = ProfileAllocation
        if LoadUnit is not None:
            properties['LoadUnit'] = LoadUnit

        # call base class function, and it will send message to renix server to create a class.
        super(ParallelLoadCommand, self).__init__(**properties)

    @property
    def ProfileAllocation(self):
        """
        get the value of property _ProfileAllocation
        """
        return self._ProfileAllocation

    @property
    def LoadUnit(self):
        """
        get the value of property _LoadUnit
        """
        return self._LoadUnit

    @ProfileAllocation.setter
    def ProfileAllocation(self, value):
        self._ProfileAllocation = value

    @LoadUnit.setter
    def LoadUnit(self, value):
        self._LoadUnit = value

    def _set_profileallocation_with_str(self, value):
        seperate = value.find(':')
        exec('self._ProfileAllocation = EnumProfileAllocation.%s' % value[:seperate])

    def _set_loadunit_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoadUnit = EnumLoadUnit.%s' % value[:seperate])

