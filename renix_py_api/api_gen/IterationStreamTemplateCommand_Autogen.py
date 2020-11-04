"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .IterationCommand_Autogen import IterationCommand


@rom_manager.rom
class IterationStreamTemplateCommand(IterationCommand):
    def __init__(self, StreamTemplateList=None, **kwargs):
        self._StreamTemplateList = StreamTemplateList  # Stream Template List

        properties = kwargs.copy()
        if StreamTemplateList is not None:
            properties['StreamTemplateList'] = StreamTemplateList

        # call base class function, and it will send message to renix server to create a class.
        super(IterationStreamTemplateCommand, self).__init__(**properties)

    @property
    def StreamTemplateList(self):
        """
        get the value of property _StreamTemplateList
        """
        return self._StreamTemplateList

    @StreamTemplateList.setter
    def StreamTemplateList(self, value):
        self._StreamTemplateList = value

    def _set_streamtemplatelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamTemplateList = tmp_value.split()

