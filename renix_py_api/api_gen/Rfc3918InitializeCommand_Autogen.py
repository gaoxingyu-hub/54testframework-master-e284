"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Rfc3918InitializeCommand(ROMCommand):
    def __init__(self, MulticastMsgTxRate=None, **kwargs):
        self._MulticastMsgTxRate = MulticastMsgTxRate  # Multicast Message Tx Rate

        properties = kwargs.copy()
        if MulticastMsgTxRate is not None:
            properties['MulticastMsgTxRate'] = MulticastMsgTxRate

        # call base class function, and it will send message to renix server to create a class.
        super(Rfc3918InitializeCommand, self).__init__(**properties)

    @property
    def MulticastMsgTxRate(self):
        """
        get the value of property _MulticastMsgTxRate
        """
        return self._MulticastMsgTxRate

    @MulticastMsgTxRate.setter
    def MulticastMsgTxRate(self, value):
        self._MulticastMsgTxRate = value

    def _set_multicastmsgtxrate_with_str(self, value):
        try:
            self._MulticastMsgTxRate = int(value)
        except ValueError:
            self._MulticastMsgTxRate = hex(int(value, 16))

