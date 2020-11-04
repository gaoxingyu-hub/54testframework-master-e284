"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class GroupCommand(ROMCommand):
    def __init__(self, CommandHandles=None, **kwargs):
        self._CommandHandles = CommandHandles  # Command Handles

        properties = kwargs.copy()
        if CommandHandles is not None:
            properties['CommandHandles'] = CommandHandles

        # call base class function, and it will send message to renix server to create a class.
        super(GroupCommand, self).__init__(**properties)

    @property
    def CommandHandles(self):
        """
        get the value of property _CommandHandles
        """
        return self._CommandHandles

    @CommandHandles.setter
    def CommandHandles(self, value):
        self._CommandHandles = value

    def _set_commandhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._CommandHandles = tmp_value.split()

