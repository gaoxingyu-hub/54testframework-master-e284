"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Ospfv3PortConfig(ROMObject):
    def __init__(self, TransmitRate=None, UpdateMsgTransmitRate=None, EnableLoop=None, **kwargs):
        self._TransmitRate = TransmitRate  # OSPFv3 Message Tx Rate (messages/second)
        self._UpdateMsgTransmitRate = UpdateMsgTransmitRate  # OSPFv3 Update Message Tx Rate (messages/second)
        self._EnableLoop = EnableLoop  # Enable Loop Back

        properties = kwargs.copy()
        if TransmitRate is not None:
            properties['TransmitRate'] = TransmitRate
        if UpdateMsgTransmitRate is not None:
            properties['UpdateMsgTransmitRate'] = UpdateMsgTransmitRate
        if EnableLoop is not None:
            properties['EnableLoop'] = EnableLoop

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv3PortConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TransmitRate=None, UpdateMsgTransmitRate=None, EnableLoop=None, **kwargs):
        properties = kwargs.copy()
        if TransmitRate is not None:
            self._TransmitRate = TransmitRate
            properties['TransmitRate'] = TransmitRate
        if UpdateMsgTransmitRate is not None:
            self._UpdateMsgTransmitRate = UpdateMsgTransmitRate
            properties['UpdateMsgTransmitRate'] = UpdateMsgTransmitRate
        if EnableLoop is not None:
            self._EnableLoop = EnableLoop
            properties['EnableLoop'] = EnableLoop

        super(Ospfv3PortConfig, self).edit(**properties)

    @property
    def TransmitRate(self):
        """
        get the value of property _TransmitRate
        """
        if self.force_auto_sync:
            self.get('TransmitRate')
        return self._TransmitRate

    @property
    def UpdateMsgTransmitRate(self):
        """
        get the value of property _UpdateMsgTransmitRate
        """
        if self.force_auto_sync:
            self.get('UpdateMsgTransmitRate')
        return self._UpdateMsgTransmitRate

    @property
    def EnableLoop(self):
        """
        get the value of property _EnableLoop
        """
        if self.force_auto_sync:
            self.get('EnableLoop')
        return self._EnableLoop

    @TransmitRate.setter
    def TransmitRate(self, value):
        self._TransmitRate = value
        self.edit(TransmitRate=value)

    @UpdateMsgTransmitRate.setter
    def UpdateMsgTransmitRate(self, value):
        self._UpdateMsgTransmitRate = value
        self.edit(UpdateMsgTransmitRate=value)

    @EnableLoop.setter
    def EnableLoop(self, value):
        self._EnableLoop = value
        self.edit(EnableLoop=value)

    def _set_transmitrate_with_str(self, value):
        try:
            self._TransmitRate = int(value)
        except ValueError:
            self._TransmitRate = hex(int(value, 16))

    def _set_updatemsgtransmitrate_with_str(self, value):
        try:
            self._UpdateMsgTransmitRate = int(value)
        except ValueError:
            self._UpdateMsgTransmitRate = hex(int(value, 16))

    def _set_enableloop_with_str(self, value):
        self._EnableLoop = (value == 'True')

