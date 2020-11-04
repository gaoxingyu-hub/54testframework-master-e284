"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SetDefaultImixTemplateCommand(ROMCommand):
    def __init__(self, ImixHandle=None, **kwargs):
        self._ImixHandle = ImixHandle  # iMIX Handle

        properties = kwargs.copy()
        if ImixHandle is not None:
            properties['ImixHandle'] = ImixHandle

        # call base class function, and it will send message to renix server to create a class.
        super(SetDefaultImixTemplateCommand, self).__init__(**properties)

    @property
    def ImixHandle(self):
        """
        get the value of property _ImixHandle
        """
        return self._ImixHandle

    @ImixHandle.setter
    def ImixHandle(self, value):
        self._ImixHandle = value

    def _set_imixhandle_with_str(self, value):
        self._ImixHandle = value

