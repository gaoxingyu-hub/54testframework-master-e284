"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Y1564StartCommandTestCommand(ROMCommand):
    def __init__(self, CommandType=None, **kwargs):
        self._CommandType = CommandType  # Command Type

        properties = kwargs.copy()
        if CommandType is not None:
            properties['CommandType'] = CommandType

        # call base class function, and it will send message to renix server to create a class.
        super(Y1564StartCommandTestCommand, self).__init__(**properties)

    @property
    def CommandType(self):
        """
        get the value of property _CommandType
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, value):
        self._CommandType = value

    def _set_commandtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._CommandType = EnumConfigTestCommandType.%s' % value[:seperate])

