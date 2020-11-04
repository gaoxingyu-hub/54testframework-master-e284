"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class PingConfig(ROMObject):
    def __init__(self, PingStatus=None, **kwargs):
        self._State = EnumPingConfigState.IDLE  # State, not editable
        self._PingStatus = PingStatus  # Ping Status
        self._InterfaceHandle = ''  # Ping Interface, not editable

        properties = kwargs.copy()
        if PingStatus is not None:
            properties['PingStatus'] = PingStatus

        # call base class function, and it will send message to renix server to create a class.
        super(PingConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PingStatus=None, **kwargs):
        properties = kwargs.copy()
        if PingStatus is not None:
            self._PingStatus = PingStatus
            properties['PingStatus'] = PingStatus

        super(PingConfig, self).edit(**properties)

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def PingStatus(self):
        """
        get the value of property _PingStatus
        """
        if self.force_auto_sync:
            self.get('PingStatus')
        return self._PingStatus

    @property
    def InterfaceHandle(self):
        """
        get the value of property _InterfaceHandle
        """
        if self.force_auto_sync:
            self.get('InterfaceHandle')
        return self._InterfaceHandle

    @PingStatus.setter
    def PingStatus(self, value):
        self._PingStatus = value
        self.edit(PingStatus=value)

    def _set_state_with_str(self, value):
        seperate = value.find(':')
        exec('self._State = EnumPingConfigState.%s' % value[:seperate])

    def _set_pingstatus_with_str(self, value):
        self._PingStatus = value

    def _set_interfacehandle_with_str(self, value):
        self._InterfaceHandle = value

