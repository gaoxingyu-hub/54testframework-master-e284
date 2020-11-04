"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .TrafficTestCommand_Autogen import TrafficTestCommand


@rom_manager.rom
class Y1564SmartScripterCommand(TrafficTestCommand):
    def __init__(self, StreamTemplateHandles=None, **kwargs):
        self._StreamTemplateHandles = StreamTemplateHandles  # Stream Template Handle List

        properties = kwargs.copy()
        if StreamTemplateHandles is not None:
            properties['StreamTemplateHandles'] = StreamTemplateHandles

        # call base class function, and it will send message to renix server to create a class.
        super(Y1564SmartScripterCommand, self).__init__(**properties)

    @property
    def StreamTemplateHandles(self):
        """
        get the value of property _StreamTemplateHandles
        """
        return self._StreamTemplateHandles

    @StreamTemplateHandles.setter
    def StreamTemplateHandles(self, value):
        self._StreamTemplateHandles = value

    def _set_streamtemplatehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamTemplateHandles = tmp_value.split()

