"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class BenchmarkConfig(ROMObject):
    def __init__(self, LoadUnit=None, **kwargs):
        self._LoadUnit = LoadUnit  # Load Unit

        properties = kwargs.copy()
        if LoadUnit is not None:
            properties['LoadUnit'] = LoadUnit

        # call base class function, and it will send message to renix server to create a class.
        super(BenchmarkConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, LoadUnit=None, **kwargs):
        properties = kwargs.copy()
        if LoadUnit is not None:
            self._LoadUnit = LoadUnit
            properties['LoadUnit'] = LoadUnit

        super(BenchmarkConfig, self).edit(**properties)

    @property
    def LoadUnit(self):
        """
        get the value of property _LoadUnit
        """
        if self.force_auto_sync:
            self.get('LoadUnit')
        return self._LoadUnit

    @LoadUnit.setter
    def LoadUnit(self, value):
        self._LoadUnit = value
        self.edit(LoadUnit=value)

    def _set_loadunit_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoadUnit = EnumLoadUnit.%s' % value[:seperate])

