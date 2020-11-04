"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class BfdSessionResult(Result):
    def __init__(self, **kwargs):
        self._SessionID = ''  # Session Name, not editable
        self._SessionState = 'Idle'  # Session State, not editable
        self._BfdSessionUpCount = 0  # BFD Session Up Count, not editable
        self._BfdSessionDownCount = 0  # BFD Session Down Count, not editable
        self._TXBfdPackets = 0  # Tx BFD Packets, not editable
        self._RXBfdPackets = 0  # Rx BFD Packets, not editable
        self._TimeoutsDetected = 0  # Timeouts Detected, not editable
        self._FlapsDetected = 0  # Flaps Detected, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(BfdSessionResult, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def SessionID(self):
        """
        get the value of property _SessionID
        """
        if self.force_auto_sync:
            self.get('SessionID')
        return self._SessionID

    @property
    def SessionState(self):
        """
        get the value of property _SessionState
        """
        if self.force_auto_sync:
            self.get('SessionState')
        return self._SessionState

    @property
    def BfdSessionUpCount(self):
        """
        get the value of property _BfdSessionUpCount
        """
        if self.force_auto_sync:
            self.get('BfdSessionUpCount')
        return self._BfdSessionUpCount

    @property
    def BfdSessionDownCount(self):
        """
        get the value of property _BfdSessionDownCount
        """
        if self.force_auto_sync:
            self.get('BfdSessionDownCount')
        return self._BfdSessionDownCount

    @property
    def TXBfdPackets(self):
        """
        get the value of property _TXBfdPackets
        """
        if self.force_auto_sync:
            self.get('TXBfdPackets')
        return self._TXBfdPackets

    @property
    def RXBfdPackets(self):
        """
        get the value of property _RXBfdPackets
        """
        if self.force_auto_sync:
            self.get('RXBfdPackets')
        return self._RXBfdPackets

    @property
    def TimeoutsDetected(self):
        """
        get the value of property _TimeoutsDetected
        """
        if self.force_auto_sync:
            self.get('TimeoutsDetected')
        return self._TimeoutsDetected

    @property
    def FlapsDetected(self):
        """
        get the value of property _FlapsDetected
        """
        if self.force_auto_sync:
            self.get('FlapsDetected')
        return self._FlapsDetected

    def _set_sessionid_with_str(self, value):
        self._SessionID = value

    def _set_sessionstate_with_str(self, value):
        self._SessionState = value

    def _set_bfdsessionupcount_with_str(self, value):
        try:
            self._BfdSessionUpCount = int(value)
        except ValueError:
            self._BfdSessionUpCount = hex(int(value, 16))

    def _set_bfdsessiondowncount_with_str(self, value):
        try:
            self._BfdSessionDownCount = int(value)
        except ValueError:
            self._BfdSessionDownCount = hex(int(value, 16))

    def _set_txbfdpackets_with_str(self, value):
        try:
            self._TXBfdPackets = int(value)
        except ValueError:
            self._TXBfdPackets = hex(int(value, 16))

    def _set_rxbfdpackets_with_str(self, value):
        try:
            self._RXBfdPackets = int(value)
        except ValueError:
            self._RXBfdPackets = hex(int(value, 16))

    def _set_timeoutsdetected_with_str(self, value):
        try:
            self._TimeoutsDetected = int(value)
        except ValueError:
            self._TimeoutsDetected = hex(int(value, 16))

    def _set_flapsdetected_with_str(self, value):
        try:
            self._FlapsDetected = int(value)
        except ValueError:
            self._FlapsDetected = hex(int(value, 16))

