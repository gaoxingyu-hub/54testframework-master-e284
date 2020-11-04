"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Y1564PerformanceFrameSizeCommand(ROMCommand):
    def __init__(self, ServiceConfigHandles=None, **kwargs):
        self._ServiceConfigHandles = ServiceConfigHandles  # Service Config Handles

        properties = kwargs.copy()
        if ServiceConfigHandles is not None:
            properties['ServiceConfigHandles'] = ServiceConfigHandles

        # call base class function, and it will send message to renix server to create a class.
        super(Y1564PerformanceFrameSizeCommand, self).__init__(**properties)

    @property
    def ServiceConfigHandles(self):
        """
        get the value of property _ServiceConfigHandles
        """
        return self._ServiceConfigHandles

    @ServiceConfigHandles.setter
    def ServiceConfigHandles(self, value):
        self._ServiceConfigHandles = value

    def _set_serviceconfighandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ServiceConfigHandles = tmp_value.split()

