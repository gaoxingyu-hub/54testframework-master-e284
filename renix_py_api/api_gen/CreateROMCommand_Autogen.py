"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class CreateROMCommand(ROMCommand):
    def __init__(self, UpperNodeList=None, ROMName=None, Count=None, **kwargs):
        self._UpperNodeList = UpperNodeList  # Upper Nodes
        self._ROMName = ROMName  # ROM Name
        self._Count = Count  # Create Count
        self._CreatedObjects = None  # Created Object Handles, not editable

        properties = kwargs.copy()
        if UpperNodeList is not None:
            properties['UpperNodeList'] = UpperNodeList
        if ROMName is not None:
            properties['ROMName'] = ROMName
        if Count is not None:
            properties['Count'] = Count

        # call base class function, and it will send message to renix server to create a class.
        super(CreateROMCommand, self).__init__(**properties)

    @property
    def UpperNodeList(self):
        """
        get the value of property _UpperNodeList
        """
        return self._UpperNodeList

    @property
    def ROMName(self):
        """
        get the value of property _ROMName
        """
        return self._ROMName

    @property
    def Count(self):
        """
        get the value of property _Count
        """
        return self._Count

    @property
    def CreatedObjects(self):
        """
        get the value of property _CreatedObjects
        """
        return self._CreatedObjects

    @UpperNodeList.setter
    def UpperNodeList(self, value):
        self._UpperNodeList = value

    @ROMName.setter
    def ROMName(self, value):
        self._ROMName = value

    @Count.setter
    def Count(self, value):
        self._Count = value

    def _set_uppernodelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._UpperNodeList = tmp_value.split()

    def _set_romname_with_str(self, value):
        self._ROMName = value

    def _set_count_with_str(self, value):
        try:
            self._Count = int(value)
        except ValueError:
            self._Count = hex(int(value, 16))

    def _set_createdobjects_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._CreatedObjects = tmp_value.split()

    def _set_output_property(self, value):
        self._set_createdobjects_with_str(value)

