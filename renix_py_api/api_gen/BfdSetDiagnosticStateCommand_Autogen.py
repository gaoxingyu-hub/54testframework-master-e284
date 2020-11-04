"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BfdCommand_Autogen import BfdCommand


@rom_manager.rom
class BfdSetDiagnosticStateCommand(BfdCommand):
    def __init__(self, BfdProtocolConfigs=None, DiagnosticState=None, **kwargs):
        self._BfdProtocolConfigs = BfdProtocolConfigs  # BFD Protocol Configs
        self._DiagnosticState = DiagnosticState  # BFD Diagnostic State

        properties = kwargs.copy()
        if BfdProtocolConfigs is not None:
            properties['BfdProtocolConfigs'] = BfdProtocolConfigs
        if DiagnosticState is not None:
            properties['DiagnosticState'] = DiagnosticState

        # call base class function, and it will send message to renix server to create a class.
        super(BfdSetDiagnosticStateCommand, self).__init__(**properties)

    @property
    def BfdProtocolConfigs(self):
        """
        get the value of property _BfdProtocolConfigs
        """
        return self._BfdProtocolConfigs

    @property
    def DiagnosticState(self):
        """
        get the value of property _DiagnosticState
        """
        return self._DiagnosticState

    @BfdProtocolConfigs.setter
    def BfdProtocolConfigs(self, value):
        self._BfdProtocolConfigs = value

    @DiagnosticState.setter
    def DiagnosticState(self, value):
        self._DiagnosticState = value

    def _set_bfdprotocolconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._BfdProtocolConfigs = tmp_value.split()

    def _set_diagnosticstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._DiagnosticState = BfdDiagnosticEnum.%s' % value[:seperate])

