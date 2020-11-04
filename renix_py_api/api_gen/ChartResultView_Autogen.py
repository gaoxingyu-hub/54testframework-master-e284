"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ResultView_Autogen import ResultView


@rom_manager.rom
class ChartResultView(ResultView):
    def __init__(self, ObjectName=None, **kwargs):
        self._ObjectName = ObjectName  # Object Name

        properties = kwargs.copy()
        if ObjectName is not None:
            properties['ObjectName'] = ObjectName

        # call base class function, and it will send message to renix server to create a class.
        super(ChartResultView, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ObjectName=None, **kwargs):
        properties = kwargs.copy()
        if ObjectName is not None:
            self._ObjectName = ObjectName
            properties['ObjectName'] = ObjectName

        super(ChartResultView, self).edit(**properties)

    @property
    def ObjectName(self):
        """
        get the value of property _ObjectName
        """
        if self.force_auto_sync:
            self.get('ObjectName')
        return self._ObjectName

    @ObjectName.setter
    def ObjectName(self, value):
        self._ObjectName = value
        self.edit(ObjectName=value)

    def _set_objectname_with_str(self, value):
        self._ObjectName = value

