"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BenchmarkIterationThroughputLoadSizeCommand_Autogen import BenchmarkIterationThroughputLoadSizeCommand


@rom_manager.rom
class BenchmarkIterationWeightedThroughputCommand(BenchmarkIterationThroughputLoadSizeCommand):
    def __init__(self, UcStreamTemplateList=None, **kwargs):
        self._UcStreamTemplateList = UcStreamTemplateList  # Stream Template List

        properties = kwargs.copy()
        if UcStreamTemplateList is not None:
            properties['UcStreamTemplateList'] = UcStreamTemplateList

        # call base class function, and it will send message to renix server to create a class.
        super(BenchmarkIterationWeightedThroughputCommand, self).__init__(**properties)

    @property
    def UcStreamTemplateList(self):
        """
        get the value of property _UcStreamTemplateList
        """
        return self._UcStreamTemplateList

    @UcStreamTemplateList.setter
    def UcStreamTemplateList(self, value):
        self._UcStreamTemplateList = value

    def _set_ucstreamtemplatelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._UcStreamTemplateList = tmp_value.split()

