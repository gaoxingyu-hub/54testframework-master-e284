"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class CloneROMCommand(ROMCommand):
    def __init__(self, ToClone=None, Count=None, **kwargs):
        self._ToClone = ToClone  # Objects to Clone
        self._Count = Count  # Clone Count
        self._ClonedObjects = None  # Cloned Objects, not editable

        properties = kwargs.copy()
        if ToClone is not None:
            properties['ToClone'] = ToClone
        if Count is not None:
            properties['Count'] = Count

        # call base class function, and it will send message to renix server to create a class.
        super(CloneROMCommand, self).__init__(**properties)

    @property
    def ToClone(self):
        """
        get the value of property _ToClone
        """
        return self._ToClone

    @property
    def Count(self):
        """
        get the value of property _Count
        """
        return self._Count

    @property
    def ClonedObjects(self):
        """
        get the value of property _ClonedObjects
        """
        return self._ClonedObjects

    @ToClone.setter
    def ToClone(self, value):
        self._ToClone = value

    @Count.setter
    def Count(self, value):
        self._Count = value

    def _set_toclone_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ToClone = tmp_value.split()

    def _set_count_with_str(self, value):
        try:
            self._Count = int(value)
        except ValueError:
            self._Count = hex(int(value, 16))

    def _set_clonedobjects_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ClonedObjects = tmp_value.split()

    def _set_output_property(self, value):
        self._set_clonedobjects_with_str(value)

