"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc2889Config_Autogen import Rfc2889Config


@rom_manager.rom
class BroadcastFrameLatencyConfig(Rfc2889Config):
    def __init__(self, DiagramMode=None, **kwargs):
        self._DiagramMode = DiagramMode  # Diagram Mode

        properties = kwargs.copy()
        if DiagramMode is not None:
            properties['DiagramMode'] = DiagramMode

        # call base class function, and it will send message to renix server to create a class.
        super(BroadcastFrameLatencyConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, DiagramMode=None, **kwargs):
        properties = kwargs.copy()
        if DiagramMode is not None:
            self._DiagramMode = DiagramMode
            properties['DiagramMode'] = DiagramMode

        super(BroadcastFrameLatencyConfig, self).edit(**properties)

    @property
    def DiagramMode(self):
        """
        get the value of property _DiagramMode
        """
        if self.force_auto_sync:
            self.get('DiagramMode')
        return self._DiagramMode

    @DiagramMode.setter
    def DiagramMode(self, value):
        self._DiagramMode = value
        self.edit(DiagramMode=value)

    def _set_diagrammode_with_str(self, value):
        seperate = value.find(':')
        exec('self._DiagramMode = EnumDiagramMode.%s' % value[:seperate])

