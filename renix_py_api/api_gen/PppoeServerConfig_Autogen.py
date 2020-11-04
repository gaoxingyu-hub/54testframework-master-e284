"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .PppoeProtocolConfig_Autogen import PppoeProtocolConfig


@rom_manager.rom
class PppoeServerConfig(PppoeProtocolConfig):
    def __init__(self, AcName=None, ChapReplyTimeout=None, ChapMaxChalAttempts=None, PapPeerReqTimeout=None, Ipv4Start=None, Ipv4Step=None, Ipv4Count=None, Ipv6InterfaceId=None, Ipv6InterfaceIdStep=None, Ipv6PrefixStart=None, Ipv6PrefixStep=None, Ipv6Count=None, EnableForceConnectMode=None, UnconnectedSessionThreshold=None, MAndOFlag=None, **kwargs):
        self._AcName = AcName  # AC-Name
        self._ChapReplyTimeout = ChapReplyTimeout  # CHAP Reply Timeout (sec)
        self._ChapMaxChalAttempts = ChapMaxChalAttempts  # CHAP Max Challenge Attempts
        self._PapPeerReqTimeout = PapPeerReqTimeout  # PAP Peer Request Timeout (sec)
        self._Ipv4Start = Ipv4Start  # IPv4 Address Start
        self._Ipv4Step = Ipv4Step  # IPv4 Address Step
        self._Ipv4Count = Ipv4Count  # IPv4 Address Count
        self._Ipv6InterfaceId = Ipv6InterfaceId  # IPv6 Interface ID
        self._Ipv6InterfaceIdStep = Ipv6InterfaceIdStep  # IPv6 Interface ID Step
        self._Ipv6PrefixStart = Ipv6PrefixStart  # IPv6 Prefix Start
        self._Ipv6PrefixStep = Ipv6PrefixStep  # IPv6 Prefix Step
        self._Ipv6Count = Ipv6Count  # IPv6 Address Count
        self._EnableForceConnectMode = EnableForceConnectMode  # Enable Force Connect Mode
        self._UnconnectedSessionThreshold = UnconnectedSessionThreshold  # Unconnected Session Threshold
        self._MAndOFlag = MAndOFlag  # M and O Flag

        properties = kwargs.copy()
        if AcName is not None:
            properties['AcName'] = AcName
        if ChapReplyTimeout is not None:
            properties['ChapReplyTimeout'] = ChapReplyTimeout
        if ChapMaxChalAttempts is not None:
            properties['ChapMaxChalAttempts'] = ChapMaxChalAttempts
        if PapPeerReqTimeout is not None:
            properties['PapPeerReqTimeout'] = PapPeerReqTimeout
        if Ipv4Start is not None:
            properties['Ipv4Start'] = Ipv4Start
        if Ipv4Step is not None:
            properties['Ipv4Step'] = Ipv4Step
        if Ipv4Count is not None:
            properties['Ipv4Count'] = Ipv4Count
        if Ipv6InterfaceId is not None:
            properties['Ipv6InterfaceId'] = Ipv6InterfaceId
        if Ipv6InterfaceIdStep is not None:
            properties['Ipv6InterfaceIdStep'] = Ipv6InterfaceIdStep
        if Ipv6PrefixStart is not None:
            properties['Ipv6PrefixStart'] = Ipv6PrefixStart
        if Ipv6PrefixStep is not None:
            properties['Ipv6PrefixStep'] = Ipv6PrefixStep
        if Ipv6Count is not None:
            properties['Ipv6Count'] = Ipv6Count
        if EnableForceConnectMode is not None:
            properties['EnableForceConnectMode'] = EnableForceConnectMode
        if UnconnectedSessionThreshold is not None:
            properties['UnconnectedSessionThreshold'] = UnconnectedSessionThreshold
        if MAndOFlag is not None:
            properties['MAndOFlag'] = MAndOFlag

        # call base class function, and it will send message to renix server to create a class.
        super(PppoeServerConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AcName=None, ChapReplyTimeout=None, ChapMaxChalAttempts=None, PapPeerReqTimeout=None, Ipv4Start=None, Ipv4Step=None, Ipv4Count=None, Ipv6InterfaceId=None, Ipv6InterfaceIdStep=None, Ipv6PrefixStart=None, Ipv6PrefixStep=None, Ipv6Count=None, EnableForceConnectMode=None, UnconnectedSessionThreshold=None, MAndOFlag=None, **kwargs):
        properties = kwargs.copy()
        if AcName is not None:
            self._AcName = AcName
            properties['AcName'] = AcName
        if ChapReplyTimeout is not None:
            self._ChapReplyTimeout = ChapReplyTimeout
            properties['ChapReplyTimeout'] = ChapReplyTimeout
        if ChapMaxChalAttempts is not None:
            self._ChapMaxChalAttempts = ChapMaxChalAttempts
            properties['ChapMaxChalAttempts'] = ChapMaxChalAttempts
        if PapPeerReqTimeout is not None:
            self._PapPeerReqTimeout = PapPeerReqTimeout
            properties['PapPeerReqTimeout'] = PapPeerReqTimeout
        if Ipv4Start is not None:
            self._Ipv4Start = Ipv4Start
            properties['Ipv4Start'] = Ipv4Start
        if Ipv4Step is not None:
            self._Ipv4Step = Ipv4Step
            properties['Ipv4Step'] = Ipv4Step
        if Ipv4Count is not None:
            self._Ipv4Count = Ipv4Count
            properties['Ipv4Count'] = Ipv4Count
        if Ipv6InterfaceId is not None:
            self._Ipv6InterfaceId = Ipv6InterfaceId
            properties['Ipv6InterfaceId'] = Ipv6InterfaceId
        if Ipv6InterfaceIdStep is not None:
            self._Ipv6InterfaceIdStep = Ipv6InterfaceIdStep
            properties['Ipv6InterfaceIdStep'] = Ipv6InterfaceIdStep
        if Ipv6PrefixStart is not None:
            self._Ipv6PrefixStart = Ipv6PrefixStart
            properties['Ipv6PrefixStart'] = Ipv6PrefixStart
        if Ipv6PrefixStep is not None:
            self._Ipv6PrefixStep = Ipv6PrefixStep
            properties['Ipv6PrefixStep'] = Ipv6PrefixStep
        if Ipv6Count is not None:
            self._Ipv6Count = Ipv6Count
            properties['Ipv6Count'] = Ipv6Count
        if EnableForceConnectMode is not None:
            self._EnableForceConnectMode = EnableForceConnectMode
            properties['EnableForceConnectMode'] = EnableForceConnectMode
        if UnconnectedSessionThreshold is not None:
            self._UnconnectedSessionThreshold = UnconnectedSessionThreshold
            properties['UnconnectedSessionThreshold'] = UnconnectedSessionThreshold
        if MAndOFlag is not None:
            self._MAndOFlag = MAndOFlag
            properties['MAndOFlag'] = MAndOFlag

        super(PppoeServerConfig, self).edit(**properties)

    @property
    def AcName(self):
        """
        get the value of property _AcName
        """
        if self.force_auto_sync:
            self.get('AcName')
        return self._AcName

    @property
    def ChapReplyTimeout(self):
        """
        get the value of property _ChapReplyTimeout
        """
        if self.force_auto_sync:
            self.get('ChapReplyTimeout')
        return self._ChapReplyTimeout

    @property
    def ChapMaxChalAttempts(self):
        """
        get the value of property _ChapMaxChalAttempts
        """
        if self.force_auto_sync:
            self.get('ChapMaxChalAttempts')
        return self._ChapMaxChalAttempts

    @property
    def PapPeerReqTimeout(self):
        """
        get the value of property _PapPeerReqTimeout
        """
        if self.force_auto_sync:
            self.get('PapPeerReqTimeout')
        return self._PapPeerReqTimeout

    @property
    def Ipv4Start(self):
        """
        get the value of property _Ipv4Start
        """
        if self.force_auto_sync:
            self.get('Ipv4Start')
        return self._Ipv4Start

    @property
    def Ipv4Step(self):
        """
        get the value of property _Ipv4Step
        """
        if self.force_auto_sync:
            self.get('Ipv4Step')
        return self._Ipv4Step

    @property
    def Ipv4Count(self):
        """
        get the value of property _Ipv4Count
        """
        if self.force_auto_sync:
            self.get('Ipv4Count')
        return self._Ipv4Count

    @property
    def Ipv6InterfaceId(self):
        """
        get the value of property _Ipv6InterfaceId
        """
        if self.force_auto_sync:
            self.get('Ipv6InterfaceId')
        return self._Ipv6InterfaceId

    @property
    def Ipv6InterfaceIdStep(self):
        """
        get the value of property _Ipv6InterfaceIdStep
        """
        if self.force_auto_sync:
            self.get('Ipv6InterfaceIdStep')
        return self._Ipv6InterfaceIdStep

    @property
    def Ipv6PrefixStart(self):
        """
        get the value of property _Ipv6PrefixStart
        """
        if self.force_auto_sync:
            self.get('Ipv6PrefixStart')
        return self._Ipv6PrefixStart

    @property
    def Ipv6PrefixStep(self):
        """
        get the value of property _Ipv6PrefixStep
        """
        if self.force_auto_sync:
            self.get('Ipv6PrefixStep')
        return self._Ipv6PrefixStep

    @property
    def Ipv6Count(self):
        """
        get the value of property _Ipv6Count
        """
        if self.force_auto_sync:
            self.get('Ipv6Count')
        return self._Ipv6Count

    @property
    def EnableForceConnectMode(self):
        """
        get the value of property _EnableForceConnectMode
        """
        if self.force_auto_sync:
            self.get('EnableForceConnectMode')
        return self._EnableForceConnectMode

    @property
    def UnconnectedSessionThreshold(self):
        """
        get the value of property _UnconnectedSessionThreshold
        """
        if self.force_auto_sync:
            self.get('UnconnectedSessionThreshold')
        return self._UnconnectedSessionThreshold

    @property
    def MAndOFlag(self):
        """
        get the value of property _MAndOFlag
        """
        if self.force_auto_sync:
            self.get('MAndOFlag')
        return self._MAndOFlag

    @AcName.setter
    def AcName(self, value):
        self._AcName = value
        self.edit(AcName=value)

    @ChapReplyTimeout.setter
    def ChapReplyTimeout(self, value):
        self._ChapReplyTimeout = value
        self.edit(ChapReplyTimeout=value)

    @ChapMaxChalAttempts.setter
    def ChapMaxChalAttempts(self, value):
        self._ChapMaxChalAttempts = value
        self.edit(ChapMaxChalAttempts=value)

    @PapPeerReqTimeout.setter
    def PapPeerReqTimeout(self, value):
        self._PapPeerReqTimeout = value
        self.edit(PapPeerReqTimeout=value)

    @Ipv4Start.setter
    def Ipv4Start(self, value):
        self._Ipv4Start = value
        self.edit(Ipv4Start=value)

    @Ipv4Step.setter
    def Ipv4Step(self, value):
        self._Ipv4Step = value
        self.edit(Ipv4Step=value)

    @Ipv4Count.setter
    def Ipv4Count(self, value):
        self._Ipv4Count = value
        self.edit(Ipv4Count=value)

    @Ipv6InterfaceId.setter
    def Ipv6InterfaceId(self, value):
        self._Ipv6InterfaceId = value
        self.edit(Ipv6InterfaceId=value)

    @Ipv6InterfaceIdStep.setter
    def Ipv6InterfaceIdStep(self, value):
        self._Ipv6InterfaceIdStep = value
        self.edit(Ipv6InterfaceIdStep=value)

    @Ipv6PrefixStart.setter
    def Ipv6PrefixStart(self, value):
        self._Ipv6PrefixStart = value
        self.edit(Ipv6PrefixStart=value)

    @Ipv6PrefixStep.setter
    def Ipv6PrefixStep(self, value):
        self._Ipv6PrefixStep = value
        self.edit(Ipv6PrefixStep=value)

    @Ipv6Count.setter
    def Ipv6Count(self, value):
        self._Ipv6Count = value
        self.edit(Ipv6Count=value)

    @EnableForceConnectMode.setter
    def EnableForceConnectMode(self, value):
        self._EnableForceConnectMode = value
        self.edit(EnableForceConnectMode=value)

    @UnconnectedSessionThreshold.setter
    def UnconnectedSessionThreshold(self, value):
        self._UnconnectedSessionThreshold = value
        self.edit(UnconnectedSessionThreshold=value)

    @MAndOFlag.setter
    def MAndOFlag(self, value):
        self._MAndOFlag = value
        self.edit(MAndOFlag=value)

    def _set_acname_with_str(self, value):
        self._AcName = value

    def _set_chapreplytimeout_with_str(self, value):
        try:
            self._ChapReplyTimeout = int(value)
        except ValueError:
            self._ChapReplyTimeout = hex(int(value, 16))

    def _set_chapmaxchalattempts_with_str(self, value):
        try:
            self._ChapMaxChalAttempts = int(value)
        except ValueError:
            self._ChapMaxChalAttempts = hex(int(value, 16))

    def _set_pappeerreqtimeout_with_str(self, value):
        try:
            self._PapPeerReqTimeout = int(value)
        except ValueError:
            self._PapPeerReqTimeout = hex(int(value, 16))

    def _set_ipv4start_with_str(self, value):
        self._Ipv4Start = value

    def _set_ipv4step_with_str(self, value):
        self._Ipv4Step = value

    def _set_ipv4count_with_str(self, value):
        try:
            self._Ipv4Count = int(value)
        except ValueError:
            self._Ipv4Count = hex(int(value, 16))

    def _set_ipv6interfaceid_with_str(self, value):
        self._Ipv6InterfaceId = value

    def _set_ipv6interfaceidstep_with_str(self, value):
        self._Ipv6InterfaceIdStep = value

    def _set_ipv6prefixstart_with_str(self, value):
        self._Ipv6PrefixStart = value

    def _set_ipv6prefixstep_with_str(self, value):
        self._Ipv6PrefixStep = value

    def _set_ipv6count_with_str(self, value):
        try:
            self._Ipv6Count = int(value)
        except ValueError:
            self._Ipv6Count = hex(int(value, 16))

    def _set_enableforceconnectmode_with_str(self, value):
        self._EnableForceConnectMode = (value == 'True')

    def _set_unconnectedsessionthreshold_with_str(self, value):
        try:
            self._UnconnectedSessionThreshold = int(value)
        except ValueError:
            self._UnconnectedSessionThreshold = hex(int(value, 16))

    def _set_mandoflag_with_str(self, value):
        seperate = value.find(':')
        exec('self._MAndOFlag = EnumPppoeMOFlag.%s' % value[:seperate])

