"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .TrafficTestCommand_Autogen import TrafficTestCommand


@rom_manager.rom
class StartTrafficCommand(TrafficTestCommand):
    def __init__(self, ConfigList=None, **kwargs):
        self._ConfigList = ConfigList  # Stream Handles

        properties = kwargs.copy()
        if ConfigList is not None:
            properties['ConfigList'] = ConfigList

        # call base class function, and it will send message to renix server to create a class.
        super(StartTrafficCommand, self).__init__(**properties)

    @property
    def ConfigList(self):
        """
        get the value of property _ConfigList
        """
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, value):
        self._ConfigList = value

    def _set_configlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ConfigList = tmp_value.split()

