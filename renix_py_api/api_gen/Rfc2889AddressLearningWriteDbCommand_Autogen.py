"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc2889WriteDbCommand_Autogen import Rfc2889WriteDbCommand


@rom_manager.rom
class Rfc2889AddressLearningWriteDbCommand(Rfc2889WriteDbCommand):
    def __init__(self, StreamTemplateList=None, MonitorPortHandles=None, **kwargs):
        self._StreamTemplateList = StreamTemplateList  # Stream Template List
        self._MonitorPortHandles = MonitorPortHandles  # Monitor Port

        properties = kwargs.copy()
        if StreamTemplateList is not None:
            properties['StreamTemplateList'] = StreamTemplateList
        if MonitorPortHandles is not None:
            properties['MonitorPortHandles'] = MonitorPortHandles

        # call base class function, and it will send message to renix server to create a class.
        super(Rfc2889AddressLearningWriteDbCommand, self).__init__(**properties)

    @property
    def StreamTemplateList(self):
        """
        get the value of property _StreamTemplateList
        """
        return self._StreamTemplateList

    @property
    def MonitorPortHandles(self):
        """
        get the value of property _MonitorPortHandles
        """
        return self._MonitorPortHandles

    @StreamTemplateList.setter
    def StreamTemplateList(self, value):
        self._StreamTemplateList = value

    @MonitorPortHandles.setter
    def MonitorPortHandles(self, value):
        self._MonitorPortHandles = value

    def _set_streamtemplatelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamTemplateList = tmp_value.split()

    def _set_monitorporthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MonitorPortHandles = tmp_value.split()

