"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class DummyClass(ROMObject):
    def __init__(self, DummyProperty0=None, **kwargs):
        self._DummyProperty0 = DummyProperty0  # Dummy

        properties = kwargs.copy()
        if DummyProperty0 is not None:
            properties['DummyProperty0'] = DummyProperty0

        # call base class function, and it will send message to renix server to create a class.
        super(DummyClass, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, DummyProperty0=None, **kwargs):
        properties = kwargs.copy()
        if DummyProperty0 is not None:
            self._DummyProperty0 = DummyProperty0
            properties['DummyProperty0'] = DummyProperty0

        super(DummyClass, self).edit(**properties)

    @property
    def DummyProperty0(self):
        """
        get the value of property _DummyProperty0
        """
        if self.force_auto_sync:
            self.get('DummyProperty0')
        return self._DummyProperty0

    @DummyProperty0.setter
    def DummyProperty0(self, value):
        self._DummyProperty0 = value
        self.edit(DummyProperty0=value)

    def _set_dummyproperty0_with_str(self, value):
        seperate = value.find(':')
        exec('self._DummyProperty0 = EnumLogWhiteList.%s' % value[:seperate])

