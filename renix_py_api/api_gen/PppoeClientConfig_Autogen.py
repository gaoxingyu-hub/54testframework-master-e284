"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .PppoeProtocolConfig_Autogen import PppoeProtocolConfig


@rom_manager.rom
class PppoeClientConfig(PppoeProtocolConfig):
    def __init__(self, PadiTimeout=None, PadiMaxAttempts=None, PadrTimeout=None, PadrMaxAttempts=None, EnableRelayAgent=None, RelayAgentDestMac=None, RelayAgentDestMacStep=None, UseRelayAgentPadi=None, UseRelayAgentPadr=None, RelaySessionId=None, ChapChalReqTimeout=None, ChapAckTimeout=None, ChapMaxReplyAttempts=None, PapReqTimeout=None, PapReqMaxAttempts=None, EnableAutoRetry=None, AutoRetryCount=None, LcpDelay=None, EnableAutoFillIpv6=None, **kwargs):
        self._PadiTimeout = PadiTimeout  # PADI Timeout (sec)
        self._PadiMaxAttempts = PadiMaxAttempts  # PADI Max Attempts
        self._PadrTimeout = PadrTimeout  # PADR Timeout (sec)
        self._PadrMaxAttempts = PadrMaxAttempts  # PADR Max Attempts
        self._EnableRelayAgent = EnableRelayAgent  # Enable Relay Agent
        self._RelayAgentDestMac = RelayAgentDestMac  # Relay Agent Destination MAC Address
        self._RelayAgentDestMacStep = RelayAgentDestMacStep  # Relay Agent Destination MAC Address Step
        self._UseRelayAgentPadi = UseRelayAgentPadi  # Use Relay Agent in PADI
        self._UseRelayAgentPadr = UseRelayAgentPadr  # Use Relay Agent in PADR
        self._RelaySessionId = RelaySessionId  # Relay Session ID
        self._ChapChalReqTimeout = ChapChalReqTimeout  # CHAP Challenge Req Timeout (sec)
        self._ChapAckTimeout = ChapAckTimeout  # CHAP Ack Timeout (sec)
        self._ChapMaxReplyAttempts = ChapMaxReplyAttempts  # CHAP Max Reply Attempts
        self._PapReqTimeout = PapReqTimeout  # PAP Req Timeout (sec)
        self._PapReqMaxAttempts = PapReqMaxAttempts  # PAP Req Max Attempts
        self._EnableAutoRetry = EnableAutoRetry  # Enable Auto Retry
        self._AutoRetryCount = AutoRetryCount  # Auto Retry Count
        self._LcpDelay = LcpDelay  # LCP Delay (ms)
        self._EnableAutoFillIpv6 = EnableAutoFillIpv6  # Enable Auto Fill IPv6

        properties = kwargs.copy()
        if PadiTimeout is not None:
            properties['PadiTimeout'] = PadiTimeout
        if PadiMaxAttempts is not None:
            properties['PadiMaxAttempts'] = PadiMaxAttempts
        if PadrTimeout is not None:
            properties['PadrTimeout'] = PadrTimeout
        if PadrMaxAttempts is not None:
            properties['PadrMaxAttempts'] = PadrMaxAttempts
        if EnableRelayAgent is not None:
            properties['EnableRelayAgent'] = EnableRelayAgent
        if RelayAgentDestMac is not None:
            properties['RelayAgentDestMac'] = RelayAgentDestMac
        if RelayAgentDestMacStep is not None:
            properties['RelayAgentDestMacStep'] = RelayAgentDestMacStep
        if UseRelayAgentPadi is not None:
            properties['UseRelayAgentPadi'] = UseRelayAgentPadi
        if UseRelayAgentPadr is not None:
            properties['UseRelayAgentPadr'] = UseRelayAgentPadr
        if RelaySessionId is not None:
            properties['RelaySessionId'] = RelaySessionId
        if ChapChalReqTimeout is not None:
            properties['ChapChalReqTimeout'] = ChapChalReqTimeout
        if ChapAckTimeout is not None:
            properties['ChapAckTimeout'] = ChapAckTimeout
        if ChapMaxReplyAttempts is not None:
            properties['ChapMaxReplyAttempts'] = ChapMaxReplyAttempts
        if PapReqTimeout is not None:
            properties['PapReqTimeout'] = PapReqTimeout
        if PapReqMaxAttempts is not None:
            properties['PapReqMaxAttempts'] = PapReqMaxAttempts
        if EnableAutoRetry is not None:
            properties['EnableAutoRetry'] = EnableAutoRetry
        if AutoRetryCount is not None:
            properties['AutoRetryCount'] = AutoRetryCount
        if LcpDelay is not None:
            properties['LcpDelay'] = LcpDelay
        if EnableAutoFillIpv6 is not None:
            properties['EnableAutoFillIpv6'] = EnableAutoFillIpv6

        # call base class function, and it will send message to renix server to create a class.
        super(PppoeClientConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PadiTimeout=None, PadiMaxAttempts=None, PadrTimeout=None, PadrMaxAttempts=None, EnableRelayAgent=None, RelayAgentDestMac=None, RelayAgentDestMacStep=None, UseRelayAgentPadi=None, UseRelayAgentPadr=None, RelaySessionId=None, ChapChalReqTimeout=None, ChapAckTimeout=None, ChapMaxReplyAttempts=None, PapReqTimeout=None, PapReqMaxAttempts=None, EnableAutoRetry=None, AutoRetryCount=None, LcpDelay=None, EnableAutoFillIpv6=None, **kwargs):
        properties = kwargs.copy()
        if PadiTimeout is not None:
            self._PadiTimeout = PadiTimeout
            properties['PadiTimeout'] = PadiTimeout
        if PadiMaxAttempts is not None:
            self._PadiMaxAttempts = PadiMaxAttempts
            properties['PadiMaxAttempts'] = PadiMaxAttempts
        if PadrTimeout is not None:
            self._PadrTimeout = PadrTimeout
            properties['PadrTimeout'] = PadrTimeout
        if PadrMaxAttempts is not None:
            self._PadrMaxAttempts = PadrMaxAttempts
            properties['PadrMaxAttempts'] = PadrMaxAttempts
        if EnableRelayAgent is not None:
            self._EnableRelayAgent = EnableRelayAgent
            properties['EnableRelayAgent'] = EnableRelayAgent
        if RelayAgentDestMac is not None:
            self._RelayAgentDestMac = RelayAgentDestMac
            properties['RelayAgentDestMac'] = RelayAgentDestMac
        if RelayAgentDestMacStep is not None:
            self._RelayAgentDestMacStep = RelayAgentDestMacStep
            properties['RelayAgentDestMacStep'] = RelayAgentDestMacStep
        if UseRelayAgentPadi is not None:
            self._UseRelayAgentPadi = UseRelayAgentPadi
            properties['UseRelayAgentPadi'] = UseRelayAgentPadi
        if UseRelayAgentPadr is not None:
            self._UseRelayAgentPadr = UseRelayAgentPadr
            properties['UseRelayAgentPadr'] = UseRelayAgentPadr
        if RelaySessionId is not None:
            self._RelaySessionId = RelaySessionId
            properties['RelaySessionId'] = RelaySessionId
        if ChapChalReqTimeout is not None:
            self._ChapChalReqTimeout = ChapChalReqTimeout
            properties['ChapChalReqTimeout'] = ChapChalReqTimeout
        if ChapAckTimeout is not None:
            self._ChapAckTimeout = ChapAckTimeout
            properties['ChapAckTimeout'] = ChapAckTimeout
        if ChapMaxReplyAttempts is not None:
            self._ChapMaxReplyAttempts = ChapMaxReplyAttempts
            properties['ChapMaxReplyAttempts'] = ChapMaxReplyAttempts
        if PapReqTimeout is not None:
            self._PapReqTimeout = PapReqTimeout
            properties['PapReqTimeout'] = PapReqTimeout
        if PapReqMaxAttempts is not None:
            self._PapReqMaxAttempts = PapReqMaxAttempts
            properties['PapReqMaxAttempts'] = PapReqMaxAttempts
        if EnableAutoRetry is not None:
            self._EnableAutoRetry = EnableAutoRetry
            properties['EnableAutoRetry'] = EnableAutoRetry
        if AutoRetryCount is not None:
            self._AutoRetryCount = AutoRetryCount
            properties['AutoRetryCount'] = AutoRetryCount
        if LcpDelay is not None:
            self._LcpDelay = LcpDelay
            properties['LcpDelay'] = LcpDelay
        if EnableAutoFillIpv6 is not None:
            self._EnableAutoFillIpv6 = EnableAutoFillIpv6
            properties['EnableAutoFillIpv6'] = EnableAutoFillIpv6

        super(PppoeClientConfig, self).edit(**properties)

    @property
    def PadiTimeout(self):
        """
        get the value of property _PadiTimeout
        """
        if self.force_auto_sync:
            self.get('PadiTimeout')
        return self._PadiTimeout

    @property
    def PadiMaxAttempts(self):
        """
        get the value of property _PadiMaxAttempts
        """
        if self.force_auto_sync:
            self.get('PadiMaxAttempts')
        return self._PadiMaxAttempts

    @property
    def PadrTimeout(self):
        """
        get the value of property _PadrTimeout
        """
        if self.force_auto_sync:
            self.get('PadrTimeout')
        return self._PadrTimeout

    @property
    def PadrMaxAttempts(self):
        """
        get the value of property _PadrMaxAttempts
        """
        if self.force_auto_sync:
            self.get('PadrMaxAttempts')
        return self._PadrMaxAttempts

    @property
    def EnableRelayAgent(self):
        """
        get the value of property _EnableRelayAgent
        """
        if self.force_auto_sync:
            self.get('EnableRelayAgent')
        return self._EnableRelayAgent

    @property
    def RelayAgentDestMac(self):
        """
        get the value of property _RelayAgentDestMac
        """
        if self.force_auto_sync:
            self.get('RelayAgentDestMac')
        return self._RelayAgentDestMac

    @property
    def RelayAgentDestMacStep(self):
        """
        get the value of property _RelayAgentDestMacStep
        """
        if self.force_auto_sync:
            self.get('RelayAgentDestMacStep')
        return self._RelayAgentDestMacStep

    @property
    def UseRelayAgentPadi(self):
        """
        get the value of property _UseRelayAgentPadi
        """
        if self.force_auto_sync:
            self.get('UseRelayAgentPadi')
        return self._UseRelayAgentPadi

    @property
    def UseRelayAgentPadr(self):
        """
        get the value of property _UseRelayAgentPadr
        """
        if self.force_auto_sync:
            self.get('UseRelayAgentPadr')
        return self._UseRelayAgentPadr

    @property
    def RelaySessionId(self):
        """
        get the value of property _RelaySessionId
        """
        if self.force_auto_sync:
            self.get('RelaySessionId')
        return self._RelaySessionId

    @property
    def ChapChalReqTimeout(self):
        """
        get the value of property _ChapChalReqTimeout
        """
        if self.force_auto_sync:
            self.get('ChapChalReqTimeout')
        return self._ChapChalReqTimeout

    @property
    def ChapAckTimeout(self):
        """
        get the value of property _ChapAckTimeout
        """
        if self.force_auto_sync:
            self.get('ChapAckTimeout')
        return self._ChapAckTimeout

    @property
    def ChapMaxReplyAttempts(self):
        """
        get the value of property _ChapMaxReplyAttempts
        """
        if self.force_auto_sync:
            self.get('ChapMaxReplyAttempts')
        return self._ChapMaxReplyAttempts

    @property
    def PapReqTimeout(self):
        """
        get the value of property _PapReqTimeout
        """
        if self.force_auto_sync:
            self.get('PapReqTimeout')
        return self._PapReqTimeout

    @property
    def PapReqMaxAttempts(self):
        """
        get the value of property _PapReqMaxAttempts
        """
        if self.force_auto_sync:
            self.get('PapReqMaxAttempts')
        return self._PapReqMaxAttempts

    @property
    def EnableAutoRetry(self):
        """
        get the value of property _EnableAutoRetry
        """
        if self.force_auto_sync:
            self.get('EnableAutoRetry')
        return self._EnableAutoRetry

    @property
    def AutoRetryCount(self):
        """
        get the value of property _AutoRetryCount
        """
        if self.force_auto_sync:
            self.get('AutoRetryCount')
        return self._AutoRetryCount

    @property
    def LcpDelay(self):
        """
        get the value of property _LcpDelay
        """
        if self.force_auto_sync:
            self.get('LcpDelay')
        return self._LcpDelay

    @property
    def EnableAutoFillIpv6(self):
        """
        get the value of property _EnableAutoFillIpv6
        """
        if self.force_auto_sync:
            self.get('EnableAutoFillIpv6')
        return self._EnableAutoFillIpv6

    @PadiTimeout.setter
    def PadiTimeout(self, value):
        self._PadiTimeout = value
        self.edit(PadiTimeout=value)

    @PadiMaxAttempts.setter
    def PadiMaxAttempts(self, value):
        self._PadiMaxAttempts = value
        self.edit(PadiMaxAttempts=value)

    @PadrTimeout.setter
    def PadrTimeout(self, value):
        self._PadrTimeout = value
        self.edit(PadrTimeout=value)

    @PadrMaxAttempts.setter
    def PadrMaxAttempts(self, value):
        self._PadrMaxAttempts = value
        self.edit(PadrMaxAttempts=value)

    @EnableRelayAgent.setter
    def EnableRelayAgent(self, value):
        self._EnableRelayAgent = value
        self.edit(EnableRelayAgent=value)

    @RelayAgentDestMac.setter
    def RelayAgentDestMac(self, value):
        self._RelayAgentDestMac = value
        self.edit(RelayAgentDestMac=value)

    @RelayAgentDestMacStep.setter
    def RelayAgentDestMacStep(self, value):
        self._RelayAgentDestMacStep = value
        self.edit(RelayAgentDestMacStep=value)

    @UseRelayAgentPadi.setter
    def UseRelayAgentPadi(self, value):
        self._UseRelayAgentPadi = value
        self.edit(UseRelayAgentPadi=value)

    @UseRelayAgentPadr.setter
    def UseRelayAgentPadr(self, value):
        self._UseRelayAgentPadr = value
        self.edit(UseRelayAgentPadr=value)

    @RelaySessionId.setter
    def RelaySessionId(self, value):
        self._RelaySessionId = value
        self.edit(RelaySessionId=value)

    @ChapChalReqTimeout.setter
    def ChapChalReqTimeout(self, value):
        self._ChapChalReqTimeout = value
        self.edit(ChapChalReqTimeout=value)

    @ChapAckTimeout.setter
    def ChapAckTimeout(self, value):
        self._ChapAckTimeout = value
        self.edit(ChapAckTimeout=value)

    @ChapMaxReplyAttempts.setter
    def ChapMaxReplyAttempts(self, value):
        self._ChapMaxReplyAttempts = value
        self.edit(ChapMaxReplyAttempts=value)

    @PapReqTimeout.setter
    def PapReqTimeout(self, value):
        self._PapReqTimeout = value
        self.edit(PapReqTimeout=value)

    @PapReqMaxAttempts.setter
    def PapReqMaxAttempts(self, value):
        self._PapReqMaxAttempts = value
        self.edit(PapReqMaxAttempts=value)

    @EnableAutoRetry.setter
    def EnableAutoRetry(self, value):
        self._EnableAutoRetry = value
        self.edit(EnableAutoRetry=value)

    @AutoRetryCount.setter
    def AutoRetryCount(self, value):
        self._AutoRetryCount = value
        self.edit(AutoRetryCount=value)

    @LcpDelay.setter
    def LcpDelay(self, value):
        self._LcpDelay = value
        self.edit(LcpDelay=value)

    @EnableAutoFillIpv6.setter
    def EnableAutoFillIpv6(self, value):
        self._EnableAutoFillIpv6 = value
        self.edit(EnableAutoFillIpv6=value)

    def _set_paditimeout_with_str(self, value):
        try:
            self._PadiTimeout = int(value)
        except ValueError:
            self._PadiTimeout = hex(int(value, 16))

    def _set_padimaxattempts_with_str(self, value):
        try:
            self._PadiMaxAttempts = int(value)
        except ValueError:
            self._PadiMaxAttempts = hex(int(value, 16))

    def _set_padrtimeout_with_str(self, value):
        try:
            self._PadrTimeout = int(value)
        except ValueError:
            self._PadrTimeout = hex(int(value, 16))

    def _set_padrmaxattempts_with_str(self, value):
        try:
            self._PadrMaxAttempts = int(value)
        except ValueError:
            self._PadrMaxAttempts = hex(int(value, 16))

    def _set_enablerelayagent_with_str(self, value):
        self._EnableRelayAgent = (value == 'True')

    def _set_relayagentdestmac_with_str(self, value):
        self._RelayAgentDestMac = value

    def _set_relayagentdestmacstep_with_str(self, value):
        self._RelayAgentDestMacStep = value

    def _set_userelayagentpadi_with_str(self, value):
        self._UseRelayAgentPadi = (value == 'True')

    def _set_userelayagentpadr_with_str(self, value):
        self._UseRelayAgentPadr = (value == 'True')

    def _set_relaysessionid_with_str(self, value):
        self._RelaySessionId = value

    def _set_chapchalreqtimeout_with_str(self, value):
        try:
            self._ChapChalReqTimeout = int(value)
        except ValueError:
            self._ChapChalReqTimeout = hex(int(value, 16))

    def _set_chapacktimeout_with_str(self, value):
        try:
            self._ChapAckTimeout = int(value)
        except ValueError:
            self._ChapAckTimeout = hex(int(value, 16))

    def _set_chapmaxreplyattempts_with_str(self, value):
        try:
            self._ChapMaxReplyAttempts = int(value)
        except ValueError:
            self._ChapMaxReplyAttempts = hex(int(value, 16))

    def _set_papreqtimeout_with_str(self, value):
        try:
            self._PapReqTimeout = int(value)
        except ValueError:
            self._PapReqTimeout = hex(int(value, 16))

    def _set_papreqmaxattempts_with_str(self, value):
        try:
            self._PapReqMaxAttempts = int(value)
        except ValueError:
            self._PapReqMaxAttempts = hex(int(value, 16))

    def _set_enableautoretry_with_str(self, value):
        self._EnableAutoRetry = (value == 'True')

    def _set_autoretrycount_with_str(self, value):
        try:
            self._AutoRetryCount = int(value)
        except ValueError:
            self._AutoRetryCount = hex(int(value, 16))

    def _set_lcpdelay_with_str(self, value):
        try:
            self._LcpDelay = int(value)
        except ValueError:
            self._LcpDelay = hex(int(value, 16))

    def _set_enableautofillipv6_with_str(self, value):
        self._EnableAutoFillIpv6 = (value == 'True')

