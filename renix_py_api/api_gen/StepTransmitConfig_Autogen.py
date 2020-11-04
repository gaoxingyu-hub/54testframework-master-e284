"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .PortTransmitConfig_Autogen import PortTransmitConfig


@rom_manager.rom
class StepTransmitConfig(PortTransmitConfig):
    def __init__(self, Frames=None, **kwargs):
        self._Frames = Frames  # Frames Count

        properties = kwargs.copy()
        if Frames is not None:
            properties['Frames'] = Frames

        # call base class function, and it will send message to renix server to create a class.
        super(StepTransmitConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Frames=None, **kwargs):
        properties = kwargs.copy()
        if Frames is not None:
            self._Frames = Frames
            properties['Frames'] = Frames

        super(StepTransmitConfig, self).edit(**properties)

    @property
    def Frames(self):
        """
        get the value of property _Frames
        """
        if self.force_auto_sync:
            self.get('Frames')
        return self._Frames

    @Frames.setter
    def Frames(self, value):
        self._Frames = value
        self.edit(Frames=value)

    def _set_frames_with_str(self, value):
        try:
            self._Frames = int(value)
        except ValueError:
            self._Frames = hex(int(value, 16))

