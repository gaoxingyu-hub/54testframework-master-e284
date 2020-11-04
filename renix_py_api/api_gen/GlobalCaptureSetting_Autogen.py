"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class GlobalCaptureSetting(ROMObject):
    def __init__(self, CreateOptionForEvent=None, CreateOptionForFilter=None, **kwargs):
        self._CreateOptionForEvent = CreateOptionForEvent  # Create Capture Option for Capture Event
        self._CreateOptionForFilter = CreateOptionForFilter  # Create Capture Option for Capture Filter

        properties = kwargs.copy()
        if CreateOptionForEvent is not None:
            properties['CreateOptionForEvent'] = CreateOptionForEvent
        if CreateOptionForFilter is not None:
            properties['CreateOptionForFilter'] = CreateOptionForFilter

        # call base class function, and it will send message to renix server to create a class.
        super(GlobalCaptureSetting, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, CreateOptionForEvent=None, CreateOptionForFilter=None, **kwargs):
        properties = kwargs.copy()
        if CreateOptionForEvent is not None:
            self._CreateOptionForEvent = CreateOptionForEvent
            properties['CreateOptionForEvent'] = CreateOptionForEvent
        if CreateOptionForFilter is not None:
            self._CreateOptionForFilter = CreateOptionForFilter
            properties['CreateOptionForFilter'] = CreateOptionForFilter

        super(GlobalCaptureSetting, self).edit(**properties)

    @property
    def CreateOptionForEvent(self):
        """
        get the value of property _CreateOptionForEvent
        """
        if self.force_auto_sync:
            self.get('CreateOptionForEvent')
        return self._CreateOptionForEvent

    @property
    def CreateOptionForFilter(self):
        """
        get the value of property _CreateOptionForFilter
        """
        if self.force_auto_sync:
            self.get('CreateOptionForFilter')
        return self._CreateOptionForFilter

    @CreateOptionForEvent.setter
    def CreateOptionForEvent(self, value):
        self._CreateOptionForEvent = value
        self.edit(CreateOptionForEvent=value)

    @CreateOptionForFilter.setter
    def CreateOptionForFilter(self, value):
        self._CreateOptionForFilter = value
        self.edit(CreateOptionForFilter=value)

    def _set_createoptionforevent_with_str(self, value):
        self._CreateOptionForEvent = (value == 'True')

    def _set_createoptionforfilter_with_str(self, value):
        self._CreateOptionForFilter = (value == 'True')

