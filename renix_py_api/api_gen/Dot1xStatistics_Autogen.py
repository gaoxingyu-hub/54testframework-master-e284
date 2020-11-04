"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Dot1xStatistics(Result):
    def __init__(self, **kwargs):
        self._Dot1xBlockHandle = ''  # 802.1x Block Name, not editable
        self._SessionIndex = 0  # Session Index, not editable
        self._State = ''  # Session State, not editable
        self._ReqIdentity = 0  # Rx Request Identity, not editable
        self._RespIdentity = 0  # Tx Response Identity, not editable
        self._ReqChallenge = 0  # Rx Request Challenge, not editable
        self._RespChallenge = 0  # Tx Response Challenge, not editable
        self._TLSEstablish = 0  # TLS Established, not editable
        self._ReceiveOK = 0  # Receive Success, not editable
        self._ReceiveFail = 0  # Rx Failure, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Dot1xStatistics, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def Dot1xBlockHandle(self):
        """
        get the value of property _Dot1xBlockHandle
        """
        if self.force_auto_sync:
            self.get('Dot1xBlockHandle')
        return self._Dot1xBlockHandle

    @property
    def SessionIndex(self):
        """
        get the value of property _SessionIndex
        """
        if self.force_auto_sync:
            self.get('SessionIndex')
        return self._SessionIndex

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def ReqIdentity(self):
        """
        get the value of property _ReqIdentity
        """
        if self.force_auto_sync:
            self.get('ReqIdentity')
        return self._ReqIdentity

    @property
    def RespIdentity(self):
        """
        get the value of property _RespIdentity
        """
        if self.force_auto_sync:
            self.get('RespIdentity')
        return self._RespIdentity

    @property
    def ReqChallenge(self):
        """
        get the value of property _ReqChallenge
        """
        if self.force_auto_sync:
            self.get('ReqChallenge')
        return self._ReqChallenge

    @property
    def RespChallenge(self):
        """
        get the value of property _RespChallenge
        """
        if self.force_auto_sync:
            self.get('RespChallenge')
        return self._RespChallenge

    @property
    def TLSEstablish(self):
        """
        get the value of property _TLSEstablish
        """
        if self.force_auto_sync:
            self.get('TLSEstablish')
        return self._TLSEstablish

    @property
    def ReceiveOK(self):
        """
        get the value of property _ReceiveOK
        """
        if self.force_auto_sync:
            self.get('ReceiveOK')
        return self._ReceiveOK

    @property
    def ReceiveFail(self):
        """
        get the value of property _ReceiveFail
        """
        if self.force_auto_sync:
            self.get('ReceiveFail')
        return self._ReceiveFail

    def _set_dot1xblockhandle_with_str(self, value):
        self._Dot1xBlockHandle = value

    def _set_sessionindex_with_str(self, value):
        try:
            self._SessionIndex = int(value)
        except ValueError:
            self._SessionIndex = hex(int(value, 16))

    def _set_state_with_str(self, value):
        self._State = value

    def _set_reqidentity_with_str(self, value):
        try:
            self._ReqIdentity = int(value)
        except ValueError:
            self._ReqIdentity = hex(int(value, 16))

    def _set_respidentity_with_str(self, value):
        try:
            self._RespIdentity = int(value)
        except ValueError:
            self._RespIdentity = hex(int(value, 16))

    def _set_reqchallenge_with_str(self, value):
        try:
            self._ReqChallenge = int(value)
        except ValueError:
            self._ReqChallenge = hex(int(value, 16))

    def _set_respchallenge_with_str(self, value):
        try:
            self._RespChallenge = int(value)
        except ValueError:
            self._RespChallenge = hex(int(value, 16))

    def _set_tlsestablish_with_str(self, value):
        try:
            self._TLSEstablish = int(value)
        except ValueError:
            self._TLSEstablish = hex(int(value, 16))

    def _set_receiveok_with_str(self, value):
        try:
            self._ReceiveOK = int(value)
        except ValueError:
            self._ReceiveOK = hex(int(value, 16))

    def _set_receivefail_with_str(self, value):
        try:
            self._ReceiveFail = int(value)
        except ValueError:
            self._ReceiveFail = hex(int(value, 16))

