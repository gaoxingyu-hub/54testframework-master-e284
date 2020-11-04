"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class HardwarePort(ROMObject):
    def __init__(self, **kwargs):
        self._PortIndex = 1  # Port Index, not editable
        self._ReserveState = EnumReserveState.AVAILABLE  # Reserve State, not editable
        self._OwnerId = ''  # Owner ID, not editable
        self._State = EnumPortState.PORT_DOWN  # Port State, not editable
        self._Location = '//0.0.0.0/1/1'  # Port Location, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(HardwarePort, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(HardwarePort, self).edit(**properties)

    @property
    def PortIndex(self):
        """
        get the value of property _PortIndex
        """
        if self.force_auto_sync:
            self.get('PortIndex')
        return self._PortIndex

    @property
    def ReserveState(self):
        """
        get the value of property _ReserveState
        """
        if self.force_auto_sync:
            self.get('ReserveState')
        return self._ReserveState

    @property
    def OwnerId(self):
        """
        get the value of property _OwnerId
        """
        if self.force_auto_sync:
            self.get('OwnerId')
        return self._OwnerId

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def Location(self):
        """
        get the value of property _Location
        """
        if self.force_auto_sync:
            self.get('Location')
        return self._Location

    def _set_portindex_with_str(self, value):
        try:
            self._PortIndex = int(value)
        except ValueError:
            self._PortIndex = hex(int(value, 16))

    def _set_reservestate_with_str(self, value):
        seperate = value.find(':')
        exec('self._ReserveState = EnumReserveState.%s' % value[:seperate])

    def _set_ownerid_with_str(self, value):
        self._OwnerId = value

    def _set_state_with_str(self, value):
        seperate = value.find(':')
        exec('self._State = EnumPortState.%s' % value[:seperate])

    def _set_location_with_str(self, value):
        self._Location = value

