"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SetLogLevelCommand(ROMCommand):
    def __init__(self, ChassisHandles=None, LoggerLevel=None, **kwargs):
        self._ChassisHandles = ChassisHandles  # Chassis handle
        self._LoggerLevel = LoggerLevel  # Logger level

        properties = kwargs.copy()
        if ChassisHandles is not None:
            properties['ChassisHandles'] = ChassisHandles
        if LoggerLevel is not None:
            properties['LoggerLevel'] = LoggerLevel

        # call base class function, and it will send message to renix server to create a class.
        super(SetLogLevelCommand, self).__init__(**properties)

    @property
    def ChassisHandles(self):
        """
        get the value of property _ChassisHandles
        """
        return self._ChassisHandles

    @property
    def LoggerLevel(self):
        """
        get the value of property _LoggerLevel
        """
        return self._LoggerLevel

    @ChassisHandles.setter
    def ChassisHandles(self, value):
        self._ChassisHandles = value

    @LoggerLevel.setter
    def LoggerLevel(self, value):
        self._LoggerLevel = value

    def _set_chassishandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ChassisHandles = tmp_value.split()

    def _set_loggerlevel_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoggerLevel = EnumLoggerLevel.%s' % value[:seperate])

