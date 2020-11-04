"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class ChartView(ROMObject):
    def __init__(self, ViewName=None, **kwargs):
        self._ViewName = ViewName  # Result View Name

        properties = kwargs.copy()
        if ViewName is not None:
            properties['ViewName'] = ViewName

        # call base class function, and it will send message to renix server to create a class.
        super(ChartView, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ViewName=None, **kwargs):
        properties = kwargs.copy()
        if ViewName is not None:
            self._ViewName = ViewName
            properties['ViewName'] = ViewName

        super(ChartView, self).edit(**properties)

    @property
    def ViewName(self):
        """
        get the value of property _ViewName
        """
        if self.force_auto_sync:
            self.get('ViewName')
        return self._ViewName

    @ViewName.setter
    def ViewName(self, value):
        self._ViewName = value
        self.edit(ViewName=value)

    def _set_viewname_with_str(self, value):
        self._ViewName = value

