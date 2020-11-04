"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ChartSettingsCommand(ROMCommand):
    def __init__(self, DefaultVisibleTimeDuration=None, MaxVisibleTimeDuration=None, **kwargs):
        self._DefaultVisibleTimeDuration = DefaultVisibleTimeDuration  # Default Visible Time Duration
        self._MaxVisibleTimeDuration = MaxVisibleTimeDuration  # Max Visible Time Duration

        properties = kwargs.copy()
        if DefaultVisibleTimeDuration is not None:
            properties['DefaultVisibleTimeDuration'] = DefaultVisibleTimeDuration
        if MaxVisibleTimeDuration is not None:
            properties['MaxVisibleTimeDuration'] = MaxVisibleTimeDuration

        # call base class function, and it will send message to renix server to create a class.
        super(ChartSettingsCommand, self).__init__(**properties)

    @property
    def DefaultVisibleTimeDuration(self):
        """
        get the value of property _DefaultVisibleTimeDuration
        """
        return self._DefaultVisibleTimeDuration

    @property
    def MaxVisibleTimeDuration(self):
        """
        get the value of property _MaxVisibleTimeDuration
        """
        return self._MaxVisibleTimeDuration

    @DefaultVisibleTimeDuration.setter
    def DefaultVisibleTimeDuration(self, value):
        self._DefaultVisibleTimeDuration = value

    @MaxVisibleTimeDuration.setter
    def MaxVisibleTimeDuration(self, value):
        self._MaxVisibleTimeDuration = value

    def _set_defaultvisibletimeduration_with_str(self, value):
        self._DefaultVisibleTimeDuration = float(value)

    def _set_maxvisibletimeduration_with_str(self, value):
        self._MaxVisibleTimeDuration = float(value)

