"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class TrillWaitForRBridgeStateCommand(ROMCommand):
    def __init__(self, TrillProtocolConfigs=None, RBridgeState=None, **kwargs):
        self._TrillProtocolConfigs = TrillProtocolConfigs  # TRILL Protocol Configs
        self._RBridgeState = RBridgeState  # RBridge State

        properties = kwargs.copy()
        if TrillProtocolConfigs is not None:
            properties['TrillProtocolConfigs'] = TrillProtocolConfigs
        if RBridgeState is not None:
            properties['RBridgeState'] = RBridgeState

        # call base class function, and it will send message to renix server to create a class.
        super(TrillWaitForRBridgeStateCommand, self).__init__(**properties)

    @property
    def TrillProtocolConfigs(self):
        """
        get the value of property _TrillProtocolConfigs
        """
        return self._TrillProtocolConfigs

    @property
    def RBridgeState(self):
        """
        get the value of property _RBridgeState
        """
        return self._RBridgeState

    @TrillProtocolConfigs.setter
    def TrillProtocolConfigs(self, value):
        self._TrillProtocolConfigs = value

    @RBridgeState.setter
    def RBridgeState(self, value):
        self._RBridgeState = value

    def _set_trillprotocolconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._TrillProtocolConfigs = tmp_value.split()

    def _set_rbridgestate_with_str(self, value):
        seperate = value.find(':')
        exec('self._RBridgeState = TrillRBridgeStateEnum.%s' % value[:seperate])

