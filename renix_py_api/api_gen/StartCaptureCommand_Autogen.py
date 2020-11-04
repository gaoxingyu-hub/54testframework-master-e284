"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class StartCaptureCommand(ROMCommand):
    def __init__(self, CaptureConfigs=None, **kwargs):
        self._CaptureConfigs = CaptureConfigs  # Capture Handle List

        properties = kwargs.copy()
        if CaptureConfigs is not None:
            properties['CaptureConfigs'] = CaptureConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(StartCaptureCommand, self).__init__(**properties)

    @property
    def CaptureConfigs(self):
        """
        get the value of property _CaptureConfigs
        """
        return self._CaptureConfigs

    @CaptureConfigs.setter
    def CaptureConfigs(self, value):
        self._CaptureConfigs = value

    def _set_captureconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._CaptureConfigs = tmp_value.split()

