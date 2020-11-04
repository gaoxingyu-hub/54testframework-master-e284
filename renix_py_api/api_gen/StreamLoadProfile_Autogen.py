"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .LoadProfile_Autogen import LoadProfile


@rom_manager.rom
class StreamLoadProfile(LoadProfile):
    def __init__(self, Unit=None, **kwargs):
        self._Unit = Unit  # Unit

        properties = kwargs.copy()
        if Unit is not None:
            properties['Unit'] = Unit

        # call base class function, and it will send message to renix server to create a class.
        super(StreamLoadProfile, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Unit=None, **kwargs):
        properties = kwargs.copy()
        if Unit is not None:
            self._Unit = Unit
            properties['Unit'] = Unit

        super(StreamLoadProfile, self).edit(**properties)

    @property
    def Unit(self):
        """
        get the value of property _Unit
        """
        if self.force_auto_sync:
            self.get('Unit')
        return self._Unit

    @Unit.setter
    def Unit(self, value):
        self._Unit = value
        self.edit(Unit=value)

    def _set_unit_with_str(self, value):
        seperate = value.find(':')
        exec('self._Unit = EnumRateUnit.%s' % value[:seperate])

