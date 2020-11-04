"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class DeleteCustomResultColumnCommand(ROMCommand):
    def __init__(self, CustomResultColumnHandle=None, **kwargs):
        self._CustomResultColumnHandle = CustomResultColumnHandle  # Custom Result Column

        properties = kwargs.copy()
        if CustomResultColumnHandle is not None:
            properties['CustomResultColumnHandle'] = CustomResultColumnHandle

        # call base class function, and it will send message to renix server to create a class.
        super(DeleteCustomResultColumnCommand, self).__init__(**properties)

    @property
    def CustomResultColumnHandle(self):
        """
        get the value of property _CustomResultColumnHandle
        """
        return self._CustomResultColumnHandle

    @CustomResultColumnHandle.setter
    def CustomResultColumnHandle(self, value):
        self._CustomResultColumnHandle = value

    def _set_customresultcolumnhandle_with_str(self, value):
        self._CustomResultColumnHandle = value

