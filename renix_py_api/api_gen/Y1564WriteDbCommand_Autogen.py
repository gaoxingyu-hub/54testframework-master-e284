"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BenchmarkWriteDbCommand_Autogen import BenchmarkWriteDbCommand


@rom_manager.rom
class Y1564WriteDbCommand(BenchmarkWriteDbCommand):
    def __init__(self, LoadUnit=None, **kwargs):
        self._LoadUnit = LoadUnit  # Load Unit

        properties = kwargs.copy()
        if LoadUnit is not None:
            properties['LoadUnit'] = LoadUnit

        # call base class function, and it will send message to renix server to create a class.
        super(Y1564WriteDbCommand, self).__init__(**properties)

    @property
    def LoadUnit(self):
        """
        get the value of property _LoadUnit
        """
        return self._LoadUnit

    @LoadUnit.setter
    def LoadUnit(self, value):
        self._LoadUnit = value

    def _set_loadunit_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoadUnit = EnumLoadUnit.%s' % value[:seperate])

