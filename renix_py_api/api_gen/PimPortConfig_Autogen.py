"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class PimPortConfig(ROMObject):
    def __init__(self, MsgTransRate=None, TriggerHelloDelay=None, DisableHelloExpireTimer=None, DisableRecvHelloInNeighborState=None, DisableNonHelloRecv=None, **kwargs):
        self._MsgTransRate = MsgTransRate  # PIM Message Transmit Rate (messages/sec)
        self._TriggerHelloDelay = TriggerHelloDelay  # Trigger Hello Delay (sec)
        self._DisableHelloExpireTimer = DisableHelloExpireTimer  # Disable Hello Expire Timer
        self._DisableRecvHelloInNeighborState = DisableRecvHelloInNeighborState  # Disable Receive Hello In Neighbor State
        self._DisableNonHelloRecv = DisableNonHelloRecv  # Disable Non Hello Receive

        properties = kwargs.copy()
        if MsgTransRate is not None:
            properties['MsgTransRate'] = MsgTransRate
        if TriggerHelloDelay is not None:
            properties['TriggerHelloDelay'] = TriggerHelloDelay
        if DisableHelloExpireTimer is not None:
            properties['DisableHelloExpireTimer'] = DisableHelloExpireTimer
        if DisableRecvHelloInNeighborState is not None:
            properties['DisableRecvHelloInNeighborState'] = DisableRecvHelloInNeighborState
        if DisableNonHelloRecv is not None:
            properties['DisableNonHelloRecv'] = DisableNonHelloRecv

        # call base class function, and it will send message to renix server to create a class.
        super(PimPortConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, MsgTransRate=None, TriggerHelloDelay=None, DisableHelloExpireTimer=None, DisableRecvHelloInNeighborState=None, DisableNonHelloRecv=None, **kwargs):
        properties = kwargs.copy()
        if MsgTransRate is not None:
            self._MsgTransRate = MsgTransRate
            properties['MsgTransRate'] = MsgTransRate
        if TriggerHelloDelay is not None:
            self._TriggerHelloDelay = TriggerHelloDelay
            properties['TriggerHelloDelay'] = TriggerHelloDelay
        if DisableHelloExpireTimer is not None:
            self._DisableHelloExpireTimer = DisableHelloExpireTimer
            properties['DisableHelloExpireTimer'] = DisableHelloExpireTimer
        if DisableRecvHelloInNeighborState is not None:
            self._DisableRecvHelloInNeighborState = DisableRecvHelloInNeighborState
            properties['DisableRecvHelloInNeighborState'] = DisableRecvHelloInNeighborState
        if DisableNonHelloRecv is not None:
            self._DisableNonHelloRecv = DisableNonHelloRecv
            properties['DisableNonHelloRecv'] = DisableNonHelloRecv

        super(PimPortConfig, self).edit(**properties)

    @property
    def MsgTransRate(self):
        """
        get the value of property _MsgTransRate
        """
        if self.force_auto_sync:
            self.get('MsgTransRate')
        return self._MsgTransRate

    @property
    def TriggerHelloDelay(self):
        """
        get the value of property _TriggerHelloDelay
        """
        if self.force_auto_sync:
            self.get('TriggerHelloDelay')
        return self._TriggerHelloDelay

    @property
    def DisableHelloExpireTimer(self):
        """
        get the value of property _DisableHelloExpireTimer
        """
        if self.force_auto_sync:
            self.get('DisableHelloExpireTimer')
        return self._DisableHelloExpireTimer

    @property
    def DisableRecvHelloInNeighborState(self):
        """
        get the value of property _DisableRecvHelloInNeighborState
        """
        if self.force_auto_sync:
            self.get('DisableRecvHelloInNeighborState')
        return self._DisableRecvHelloInNeighborState

    @property
    def DisableNonHelloRecv(self):
        """
        get the value of property _DisableNonHelloRecv
        """
        if self.force_auto_sync:
            self.get('DisableNonHelloRecv')
        return self._DisableNonHelloRecv

    @MsgTransRate.setter
    def MsgTransRate(self, value):
        self._MsgTransRate = value
        self.edit(MsgTransRate=value)

    @TriggerHelloDelay.setter
    def TriggerHelloDelay(self, value):
        self._TriggerHelloDelay = value
        self.edit(TriggerHelloDelay=value)

    @DisableHelloExpireTimer.setter
    def DisableHelloExpireTimer(self, value):
        self._DisableHelloExpireTimer = value
        self.edit(DisableHelloExpireTimer=value)

    @DisableRecvHelloInNeighborState.setter
    def DisableRecvHelloInNeighborState(self, value):
        self._DisableRecvHelloInNeighborState = value
        self.edit(DisableRecvHelloInNeighborState=value)

    @DisableNonHelloRecv.setter
    def DisableNonHelloRecv(self, value):
        self._DisableNonHelloRecv = value
        self.edit(DisableNonHelloRecv=value)

    def _set_msgtransrate_with_str(self, value):
        try:
            self._MsgTransRate = int(value)
        except ValueError:
            self._MsgTransRate = hex(int(value, 16))

    def _set_triggerhellodelay_with_str(self, value):
        try:
            self._TriggerHelloDelay = int(value)
        except ValueError:
            self._TriggerHelloDelay = hex(int(value, 16))

    def _set_disablehelloexpiretimer_with_str(self, value):
        self._DisableHelloExpireTimer = (value == 'True')

    def _set_disablerecvhelloinneighborstate_with_str(self, value):
        self._DisableRecvHelloInNeighborState = (value == 'True')

    def _set_disablenonhellorecv_with_str(self, value):
        self._DisableNonHelloRecv = (value == 'True')

