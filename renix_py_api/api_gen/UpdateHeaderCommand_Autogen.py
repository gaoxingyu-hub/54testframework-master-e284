"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class UpdateHeaderCommand(ROMCommand):
    def __init__(self, Stream=None, Parameter=None, **kwargs):
        self._Stream = Stream  # Stream Handle
        self._Parameter = Parameter  # Parameter

        properties = kwargs.copy()
        if Stream is not None:
            properties['Stream'] = Stream
        if Parameter is not None:
            properties['Parameter'] = Parameter

        # call base class function, and it will send message to renix server to create a class.
        super(UpdateHeaderCommand, self).__init__(**properties)

    @property
    def Stream(self):
        """
        get the value of property _Stream
        """
        return self._Stream

    @property
    def Parameter(self):
        """
        get the value of property _Parameter
        """
        return self._Parameter

    @Stream.setter
    def Stream(self, value):
        self._Stream = value

    @Parameter.setter
    def Parameter(self, value):
        self._Parameter = value

    def _set_stream_with_str(self, value):
        self._Stream = value

    def _set_parameter_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Parameter = tmp_value.split()

