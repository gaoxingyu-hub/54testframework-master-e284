"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class StreamGlobalConfig(ROMObject):
    def __init__(self, PortSendMode=None, **kwargs):
        self._PortSendMode = PortSendMode  # Port Send Mode
        self._ElapsedTime = ''  # Elapsed Time, not editable

        properties = kwargs.copy()
        if PortSendMode is not None:
            properties['PortSendMode'] = PortSendMode

        # call base class function, and it will send message to renix server to create a class.
        super(StreamGlobalConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PortSendMode=None, **kwargs):
        properties = kwargs.copy()
        if PortSendMode is not None:
            self._PortSendMode = PortSendMode
            properties['PortSendMode'] = PortSendMode

        super(StreamGlobalConfig, self).edit(**properties)

    @property
    def PortSendMode(self):
        """
        get the value of property _PortSendMode
        """
        if self.force_auto_sync:
            self.get('PortSendMode')
        return self._PortSendMode

    @property
    def ElapsedTime(self):
        """
        get the value of property _ElapsedTime
        """
        if self.force_auto_sync:
            self.get('ElapsedTime')
        return self._ElapsedTime

    @PortSendMode.setter
    def PortSendMode(self, value):
        self._PortSendMode = value
        self.edit(PortSendMode=value)

    def _set_portsendmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._PortSendMode = EnumSendMode.%s' % value[:seperate])

    def _set_elapsedtime_with_str(self, value):
        self._ElapsedTime = value

