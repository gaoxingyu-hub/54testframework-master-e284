"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class StartSmartScripterCommand(ROMCommand):
    def __init__(self, Mode=None, **kwargs):
        self._Mode = Mode  # Smart Scripter Mode

        properties = kwargs.copy()
        if Mode is not None:
            properties['Mode'] = Mode

        # call base class function, and it will send message to renix server to create a class.
        super(StartSmartScripterCommand, self).__init__(**properties)

    @property
    def Mode(self):
        """
        get the value of property _Mode
        """
        return self._Mode

    @Mode.setter
    def Mode(self, value):
        self._Mode = value

    def _set_mode_with_str(self, value):
        seperate = value.find(':')
        exec('self._Mode = EnumSmartScripterMode.%s' % value[:seperate])

