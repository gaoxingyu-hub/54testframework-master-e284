"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class RemoveSmartScripterCommand(ROMCommand):
    def __init__(self, ObjectHandle=None, **kwargs):
        self._ObjectHandle = ObjectHandle  # Object Handles

        properties = kwargs.copy()
        if ObjectHandle is not None:
            properties['ObjectHandle'] = ObjectHandle

        # call base class function, and it will send message to renix server to create a class.
        super(RemoveSmartScripterCommand, self).__init__(**properties)

    @property
    def ObjectHandle(self):
        """
        get the value of property _ObjectHandle
        """
        return self._ObjectHandle

    @ObjectHandle.setter
    def ObjectHandle(self, value):
        self._ObjectHandle = value

    def _set_objecthandle_with_str(self, value):
        self._ObjectHandle = value

