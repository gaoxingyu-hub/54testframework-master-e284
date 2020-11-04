"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc3918Command_Autogen import Rfc3918Command


@rom_manager.rom
class MixedClassThroughputCommand(Rfc3918Command):
    def __init__(self, UcStreamTemplateHandles=None, McStreamTemplateHandles=None, **kwargs):
        self._UcStreamTemplateHandles = UcStreamTemplateHandles  # Unicast Stream Config Handle
        self._McStreamTemplateHandles = McStreamTemplateHandles  # Multicast Stream Config Handle

        properties = kwargs.copy()
        if UcStreamTemplateHandles is not None:
            properties['UcStreamTemplateHandles'] = UcStreamTemplateHandles
        if McStreamTemplateHandles is not None:
            properties['McStreamTemplateHandles'] = McStreamTemplateHandles

        # call base class function, and it will send message to renix server to create a class.
        super(MixedClassThroughputCommand, self).__init__(**properties)

    @property
    def UcStreamTemplateHandles(self):
        """
        get the value of property _UcStreamTemplateHandles
        """
        return self._UcStreamTemplateHandles

    @property
    def McStreamTemplateHandles(self):
        """
        get the value of property _McStreamTemplateHandles
        """
        return self._McStreamTemplateHandles

    @UcStreamTemplateHandles.setter
    def UcStreamTemplateHandles(self, value):
        self._UcStreamTemplateHandles = value

    @McStreamTemplateHandles.setter
    def McStreamTemplateHandles(self, value):
        self._McStreamTemplateHandles = value

    def _set_ucstreamtemplatehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._UcStreamTemplateHandles = tmp_value.split()

    def _set_mcstreamtemplatehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._McStreamTemplateHandles = tmp_value.split()

