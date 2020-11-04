"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ToggleObjectCommand(ROMCommand):
    def __init__(self, ObjectHandles=None, OnOff=None, Recursive=None, **kwargs):
        self._ObjectHandles = ObjectHandles  # Object Handles
        self._OnOff = OnOff  # Turn On
        self._Recursive = Recursive  # Recursive

        properties = kwargs.copy()
        if ObjectHandles is not None:
            properties['ObjectHandles'] = ObjectHandles
        if OnOff is not None:
            properties['OnOff'] = OnOff
        if Recursive is not None:
            properties['Recursive'] = Recursive

        # call base class function, and it will send message to renix server to create a class.
        super(ToggleObjectCommand, self).__init__(**properties)

    @property
    def ObjectHandles(self):
        """
        get the value of property _ObjectHandles
        """
        return self._ObjectHandles

    @property
    def OnOff(self):
        """
        get the value of property _OnOff
        """
        return self._OnOff

    @property
    def Recursive(self):
        """
        get the value of property _Recursive
        """
        return self._Recursive

    @ObjectHandles.setter
    def ObjectHandles(self, value):
        self._ObjectHandles = value

    @OnOff.setter
    def OnOff(self, value):
        self._OnOff = value

    @Recursive.setter
    def Recursive(self, value):
        self._Recursive = value

    def _set_objecthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ObjectHandles = tmp_value.split()

    def _set_onoff_with_str(self, value):
        self._OnOff = (value == 'True')

    def _set_recursive_with_str(self, value):
        self._Recursive = (value == 'True')

