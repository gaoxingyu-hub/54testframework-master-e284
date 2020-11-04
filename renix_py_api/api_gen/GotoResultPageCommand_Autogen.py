"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class GotoResultPageCommand(ROMCommand):
    def __init__(self, ResultViewHandle=None, PageNumber=None, **kwargs):
        self._ResultViewHandle = ResultViewHandle  # Result View
        self._PageNumber = PageNumber  # Page Number

        properties = kwargs.copy()
        if ResultViewHandle is not None:
            properties['ResultViewHandle'] = ResultViewHandle
        if PageNumber is not None:
            properties['PageNumber'] = PageNumber

        # call base class function, and it will send message to renix server to create a class.
        super(GotoResultPageCommand, self).__init__(**properties)

    @property
    def ResultViewHandle(self):
        """
        get the value of property _ResultViewHandle
        """
        return self._ResultViewHandle

    @property
    def PageNumber(self):
        """
        get the value of property _PageNumber
        """
        return self._PageNumber

    @ResultViewHandle.setter
    def ResultViewHandle(self, value):
        self._ResultViewHandle = value

    @PageNumber.setter
    def PageNumber(self, value):
        self._PageNumber = value

    def _set_resultviewhandle_with_str(self, value):
        self._ResultViewHandle = value

    def _set_pagenumber_with_str(self, value):
        try:
            self._PageNumber = int(value)
        except ValueError:
            self._PageNumber = hex(int(value, 16))

