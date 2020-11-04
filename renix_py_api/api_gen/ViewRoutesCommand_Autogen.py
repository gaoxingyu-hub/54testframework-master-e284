"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ViewRoutesCommand(ROMCommand):
    def __init__(self, ObjectHandles=None, **kwargs):
        self._ObjectHandles = ObjectHandles  # Routes
        self._RouteData = None  # Route Data, not editable

        properties = kwargs.copy()
        if ObjectHandles is not None:
            properties['ObjectHandles'] = ObjectHandles

        # call base class function, and it will send message to renix server to create a class.
        super(ViewRoutesCommand, self).__init__(**properties)

    @property
    def ObjectHandles(self):
        """
        get the value of property _ObjectHandles
        """
        return self._ObjectHandles

    @property
    def RouteData(self):
        """
        get the value of property _RouteData
        """
        return self._RouteData

    @ObjectHandles.setter
    def ObjectHandles(self, value):
        self._ObjectHandles = value

    def _set_objecthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ObjectHandles = tmp_value.split()

    def _set_routedata_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._RouteData = tmp_value.split()

    def _set_output_property(self, value):
        self._set_routedata_with_str(value)

