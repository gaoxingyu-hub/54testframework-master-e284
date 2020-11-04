"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ResultCommand(ROMCommand):
    def __init__(self, ResultViewHandles=None, **kwargs):
        self._ResultViewHandles = ResultViewHandles  # Result View

        properties = kwargs.copy()
        if ResultViewHandles is not None:
            properties['ResultViewHandles'] = ResultViewHandles

        # call base class function, and it will send message to renix server to create a class.
        super(ResultCommand, self).__init__(**properties)

    @property
    def ResultViewHandles(self):
        """
        get the value of property _ResultViewHandles
        """
        return self._ResultViewHandles

    @ResultViewHandles.setter
    def ResultViewHandles(self, value):
        self._ResultViewHandles = value

    def _set_resultviewhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ResultViewHandles = tmp_value.split()

