"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class ChartSettings(ROMObject):
    def __init__(self, DefaultVisibleTimeDuration=None, MaxVisibleTimeDuration=None, **kwargs):
        self._DefaultVisibleTimeDuration = DefaultVisibleTimeDuration  # Default Visible Time Duration
        self._MaxVisibleTimeDuration = MaxVisibleTimeDuration  # Max Visible Time Duration

        properties = kwargs.copy()
        if DefaultVisibleTimeDuration is not None:
            properties['DefaultVisibleTimeDuration'] = DefaultVisibleTimeDuration
        if MaxVisibleTimeDuration is not None:
            properties['MaxVisibleTimeDuration'] = MaxVisibleTimeDuration

        # call base class function, and it will send message to renix server to create a class.
        super(ChartSettings, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, DefaultVisibleTimeDuration=None, MaxVisibleTimeDuration=None, **kwargs):
        properties = kwargs.copy()
        if DefaultVisibleTimeDuration is not None:
            self._DefaultVisibleTimeDuration = DefaultVisibleTimeDuration
            properties['DefaultVisibleTimeDuration'] = DefaultVisibleTimeDuration
        if MaxVisibleTimeDuration is not None:
            self._MaxVisibleTimeDuration = MaxVisibleTimeDuration
            properties['MaxVisibleTimeDuration'] = MaxVisibleTimeDuration

        super(ChartSettings, self).edit(**properties)

    @property
    def DefaultVisibleTimeDuration(self):
        """
        get the value of property _DefaultVisibleTimeDuration
        """
        if self.force_auto_sync:
            self.get('DefaultVisibleTimeDuration')
        return self._DefaultVisibleTimeDuration

    @property
    def MaxVisibleTimeDuration(self):
        """
        get the value of property _MaxVisibleTimeDuration
        """
        if self.force_auto_sync:
            self.get('MaxVisibleTimeDuration')
        return self._MaxVisibleTimeDuration

    @DefaultVisibleTimeDuration.setter
    def DefaultVisibleTimeDuration(self, value):
        self._DefaultVisibleTimeDuration = value
        self.edit(DefaultVisibleTimeDuration=value)

    @MaxVisibleTimeDuration.setter
    def MaxVisibleTimeDuration(self, value):
        self._MaxVisibleTimeDuration = value
        self.edit(MaxVisibleTimeDuration=value)

    def _set_defaultvisibletimeduration_with_str(self, value):
        self._DefaultVisibleTimeDuration = float(value)

    def _set_maxvisibletimeduration_with_str(self, value):
        self._MaxVisibleTimeDuration = float(value)

