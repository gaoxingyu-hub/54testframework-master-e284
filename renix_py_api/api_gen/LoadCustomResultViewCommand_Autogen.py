"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class LoadCustomResultViewCommand(ROMCommand):
    def __init__(self, CustomResultViewFile=None, **kwargs):
        self._CustomResultViewFile = CustomResultViewFile  # Custom Result View File
        self._ResultViewHandle = ''  # Result View, not editable

        properties = kwargs.copy()
        if CustomResultViewFile is not None:
            properties['CustomResultViewFile'] = CustomResultViewFile

        # call base class function, and it will send message to renix server to create a class.
        super(LoadCustomResultViewCommand, self).__init__(**properties)

    @property
    def CustomResultViewFile(self):
        """
        get the value of property _CustomResultViewFile
        """
        return self._CustomResultViewFile

    @property
    def ResultViewHandle(self):
        """
        get the value of property _ResultViewHandle
        """
        return self._ResultViewHandle

    @CustomResultViewFile.setter
    def CustomResultViewFile(self, value):
        self._CustomResultViewFile = value

    def _set_customresultviewfile_with_str(self, value):
        self._CustomResultViewFile = value

    def _set_resultviewhandle_with_str(self, value):
        self._ResultViewHandle = value

    def _set_output_property(self, value):
        self._set_resultviewhandle_with_str(value)

