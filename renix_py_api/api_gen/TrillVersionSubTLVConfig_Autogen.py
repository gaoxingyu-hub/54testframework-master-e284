"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillVersionSubTLVConfig(ROMObject):
    def __init__(self, MaxVersion=None, **kwargs):
        self._MaxVersion = MaxVersion  # Max-Version

        properties = kwargs.copy()
        if MaxVersion is not None:
            properties['MaxVersion'] = MaxVersion

        # call base class function, and it will send message to renix server to create a class.
        super(TrillVersionSubTLVConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, MaxVersion=None, **kwargs):
        properties = kwargs.copy()
        if MaxVersion is not None:
            self._MaxVersion = MaxVersion
            properties['MaxVersion'] = MaxVersion

        super(TrillVersionSubTLVConfig, self).edit(**properties)

    @property
    def MaxVersion(self):
        """
        get the value of property _MaxVersion
        """
        if self.force_auto_sync:
            self.get('MaxVersion')
        return self._MaxVersion

    @MaxVersion.setter
    def MaxVersion(self, value):
        self._MaxVersion = value
        self.edit(MaxVersion=value)

    def _set_maxversion_with_str(self, value):
        try:
            self._MaxVersion = int(value)
        except ValueError:
            self._MaxVersion = hex(int(value, 16))

