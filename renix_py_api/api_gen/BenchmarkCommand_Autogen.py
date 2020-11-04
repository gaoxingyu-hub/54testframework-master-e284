"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class BenchmarkCommand(ROMCommand):
    def __init__(self, StreamTemplateHandles=None, StreamTemplateExceptionHandles=None, **kwargs):
        self._StreamTemplateHandles = StreamTemplateHandles  # StreamTemplate Handles
        self._StreamTemplateExceptionHandles = StreamTemplateExceptionHandles  # StreamTemplate Exception Handles

        properties = kwargs.copy()
        if StreamTemplateHandles is not None:
            properties['StreamTemplateHandles'] = StreamTemplateHandles
        if StreamTemplateExceptionHandles is not None:
            properties['StreamTemplateExceptionHandles'] = StreamTemplateExceptionHandles

        # call base class function, and it will send message to renix server to create a class.
        super(BenchmarkCommand, self).__init__(**properties)

    @property
    def StreamTemplateHandles(self):
        """
        get the value of property _StreamTemplateHandles
        """
        return self._StreamTemplateHandles

    @property
    def StreamTemplateExceptionHandles(self):
        """
        get the value of property _StreamTemplateExceptionHandles
        """
        return self._StreamTemplateExceptionHandles

    @StreamTemplateHandles.setter
    def StreamTemplateHandles(self, value):
        self._StreamTemplateHandles = value

    @StreamTemplateExceptionHandles.setter
    def StreamTemplateExceptionHandles(self, value):
        self._StreamTemplateExceptionHandles = value

    def _set_streamtemplatehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamTemplateHandles = tmp_value.split()

    def _set_streamtemplateexceptionhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamTemplateExceptionHandles = tmp_value.split()

