"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class StreamImixTemplate(ROMObject):
    def __init__(self, ImixName=None, ImixSeed=None, **kwargs):
        self._ImixName = ImixName  # iMIX Set
        self._ImixSeed = ImixSeed  # Seed

        properties = kwargs.copy()
        if ImixName is not None:
            properties['ImixName'] = ImixName
        if ImixSeed is not None:
            properties['ImixSeed'] = ImixSeed

        # call base class function, and it will send message to renix server to create a class.
        super(StreamImixTemplate, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ImixName=None, ImixSeed=None, **kwargs):
        properties = kwargs.copy()
        if ImixName is not None:
            self._ImixName = ImixName
            properties['ImixName'] = ImixName
        if ImixSeed is not None:
            self._ImixSeed = ImixSeed
            properties['ImixSeed'] = ImixSeed

        super(StreamImixTemplate, self).edit(**properties)

    @property
    def ImixName(self):
        """
        get the value of property _ImixName
        """
        if self.force_auto_sync:
            self.get('ImixName')
        return self._ImixName

    @property
    def ImixSeed(self):
        """
        get the value of property _ImixSeed
        """
        if self.force_auto_sync:
            self.get('ImixSeed')
        return self._ImixSeed

    @ImixName.setter
    def ImixName(self, value):
        self._ImixName = value
        self.edit(ImixName=value)

    @ImixSeed.setter
    def ImixSeed(self, value):
        self._ImixSeed = value
        self.edit(ImixSeed=value)

    def _set_imixname_with_str(self, value):
        self._ImixName = value

    def _set_imixseed_with_str(self, value):
        try:
            self._ImixSeed = int(value)
        except ValueError:
            self._ImixSeed = hex(int(value, 16))

