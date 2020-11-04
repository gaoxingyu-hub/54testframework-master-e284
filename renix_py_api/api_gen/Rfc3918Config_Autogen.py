"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BenchmarkL23Config_Autogen import BenchmarkL23Config


@rom_manager.rom
class Rfc3918Config(BenchmarkL23Config):
    def __init__(self, TrialNum=None, DurationMode=None, DurationTime=None, DurationBurst=None, DeviceConfigurationMode=None, MonitorPortHandles=None, AddressLearningFrequency=None, JoinGroupDelay=None, LeaveGroupDelay=None, McMessageTxRate=None, McGroupDistMode=None, McClientVersion=None, McBaseIPAddress=None, McBaseIPStep=None, McGroupIncrement=None, McIPPrefixLength=None, McBaseIPv6Address=None, McBaseIPv6Step=None, McIPv6PrefixLength=None, TransportLayerHeaderType=None, UseRandomPorts=None, SourcePortBase=None, SourcePortCount=None, SourcePortStep=None, DestPortBase=None, DestPortCount=None, DestPortStep=None, Ipv4Tos=None, Ipv6FlowLabel=None, IpTtl=None, VlanPriority=None, TrafficVerificationAbortOnFail=None, TrafficVerificationFreqMode=None, TrafficVerificationDurationMode=None, TrafficVerfictionTxFrameCount=None, TrafficVerfictionTxSeconds=None, TrafficVerificationTxFrameRate=None, TopLayerType=None, **kwargs):
        self._TrialNum = TrialNum  # Trial Times
        self._DurationMode = DurationMode  # Duration Mode
        self._DurationTime = DurationTime  # Trial Duration
        self._DurationBurst = DurationBurst  # Max Duration (frames)
        self._DeviceConfigurationMode = DeviceConfigurationMode  # Device Configuration Mode
        self._MonitorPortHandles = MonitorPortHandles  # Monitor Port
        self._AddressLearningFrequency = AddressLearningFrequency  # Address Learn Frequency
        self._JoinGroupDelay = JoinGroupDelay  # Join Group Delay(seconds)
        self._LeaveGroupDelay = LeaveGroupDelay  # Leave Group Delay(seconds)
        self._McMessageTxRate = McMessageTxRate  # Multicast Message Tx Rate
        self._McGroupDistMode = McGroupDistMode  # Multicast Group Distribution Mode
        self._McClientVersion = McClientVersion  # Multicast Client Version
        self._McBaseIPAddress = McBaseIPAddress  # Base IP Address
        self._McBaseIPStep = McBaseIPStep  # Base IP Step
        self._McGroupIncrement = McGroupIncrement  # Group Increment
        self._McIPPrefixLength = McIPPrefixLength  # Prefix Length
        self._McBaseIPv6Address = McBaseIPv6Address  # Base IPv6 Address
        self._McBaseIPv6Step = McBaseIPv6Step  # Base IPv6 Step
        self._McIPv6PrefixLength = McIPv6PrefixLength  # Prefix Length
        self._TransportLayerHeaderType = TransportLayerHeaderType  # Transport Layer Header Type
        self._UseRandomPorts = UseRandomPorts  # Use Random Ports
        self._SourcePortBase = SourcePortBase  # Base Source Port
        self._SourcePortCount = SourcePortCount  # Source Port Count
        self._SourcePortStep = SourcePortStep  # Source Port Step
        self._DestPortBase = DestPortBase  # Base Dest Port
        self._DestPortCount = DestPortCount  # Dest Port Count
        self._DestPortStep = DestPortStep  # Dest Port Step
        self._Ipv4Tos = Ipv4Tos  # Ipv4 ToS
        self._Ipv6FlowLabel = Ipv6FlowLabel  # Ipv6 Flow Label
        self._IpTtl = IpTtl  # IP TTL
        self._VlanPriority = VlanPriority  # Vlan Priority
        self._TrafficVerificationAbortOnFail = TrafficVerificationAbortOnFail  # Abort when traffic verification failed
        self._TrafficVerificationFreqMode = TrafficVerificationFreqMode  # Traffic Verify Frequency
        self._TrafficVerificationDurationMode = TrafficVerificationDurationMode  # Duration Mode
        self._TrafficVerfictionTxFrameCount = TrafficVerfictionTxFrameCount  # Verification Tx Frame Count
        self._TrafficVerfictionTxSeconds = TrafficVerfictionTxSeconds  # Verification Tx Seconds
        self._TrafficVerificationTxFrameRate = TrafficVerificationTxFrameRate  # Verification Tx Frame Rate
        self._TopLayerType = TopLayerType  # Traffic Top Layer Type

        properties = kwargs.copy()
        if TrialNum is not None:
            properties['TrialNum'] = TrialNum
        if DurationMode is not None:
            properties['DurationMode'] = DurationMode
        if DurationTime is not None:
            properties['DurationTime'] = DurationTime
        if DurationBurst is not None:
            properties['DurationBurst'] = DurationBurst
        if DeviceConfigurationMode is not None:
            properties['DeviceConfigurationMode'] = DeviceConfigurationMode
        if MonitorPortHandles is not None:
            properties['MonitorPortHandles'] = MonitorPortHandles
        if AddressLearningFrequency is not None:
            properties['AddressLearningFrequency'] = AddressLearningFrequency
        if JoinGroupDelay is not None:
            properties['JoinGroupDelay'] = JoinGroupDelay
        if LeaveGroupDelay is not None:
            properties['LeaveGroupDelay'] = LeaveGroupDelay
        if McMessageTxRate is not None:
            properties['McMessageTxRate'] = McMessageTxRate
        if McGroupDistMode is not None:
            properties['McGroupDistMode'] = McGroupDistMode
        if McClientVersion is not None:
            properties['McClientVersion'] = McClientVersion
        if McBaseIPAddress is not None:
            properties['McBaseIPAddress'] = McBaseIPAddress
        if McBaseIPStep is not None:
            properties['McBaseIPStep'] = McBaseIPStep
        if McGroupIncrement is not None:
            properties['McGroupIncrement'] = McGroupIncrement
        if McIPPrefixLength is not None:
            properties['McIPPrefixLength'] = McIPPrefixLength
        if McBaseIPv6Address is not None:
            properties['McBaseIPv6Address'] = McBaseIPv6Address
        if McBaseIPv6Step is not None:
            properties['McBaseIPv6Step'] = McBaseIPv6Step
        if McIPv6PrefixLength is not None:
            properties['McIPv6PrefixLength'] = McIPv6PrefixLength
        if TransportLayerHeaderType is not None:
            properties['TransportLayerHeaderType'] = TransportLayerHeaderType
        if UseRandomPorts is not None:
            properties['UseRandomPorts'] = UseRandomPorts
        if SourcePortBase is not None:
            properties['SourcePortBase'] = SourcePortBase
        if SourcePortCount is not None:
            properties['SourcePortCount'] = SourcePortCount
        if SourcePortStep is not None:
            properties['SourcePortStep'] = SourcePortStep
        if DestPortBase is not None:
            properties['DestPortBase'] = DestPortBase
        if DestPortCount is not None:
            properties['DestPortCount'] = DestPortCount
        if DestPortStep is not None:
            properties['DestPortStep'] = DestPortStep
        if Ipv4Tos is not None:
            properties['Ipv4Tos'] = Ipv4Tos
        if Ipv6FlowLabel is not None:
            properties['Ipv6FlowLabel'] = Ipv6FlowLabel
        if IpTtl is not None:
            properties['IpTtl'] = IpTtl
        if VlanPriority is not None:
            properties['VlanPriority'] = VlanPriority
        if TrafficVerificationAbortOnFail is not None:
            properties['TrafficVerificationAbortOnFail'] = TrafficVerificationAbortOnFail
        if TrafficVerificationFreqMode is not None:
            properties['TrafficVerificationFreqMode'] = TrafficVerificationFreqMode
        if TrafficVerificationDurationMode is not None:
            properties['TrafficVerificationDurationMode'] = TrafficVerificationDurationMode
        if TrafficVerfictionTxFrameCount is not None:
            properties['TrafficVerfictionTxFrameCount'] = TrafficVerfictionTxFrameCount
        if TrafficVerfictionTxSeconds is not None:
            properties['TrafficVerfictionTxSeconds'] = TrafficVerfictionTxSeconds
        if TrafficVerificationTxFrameRate is not None:
            properties['TrafficVerificationTxFrameRate'] = TrafficVerificationTxFrameRate
        if TopLayerType is not None:
            properties['TopLayerType'] = TopLayerType

        # call base class function, and it will send message to renix server to create a class.
        super(Rfc3918Config, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TrialNum=None, DurationMode=None, DurationTime=None, DurationBurst=None, DeviceConfigurationMode=None, MonitorPortHandles=None, AddressLearningFrequency=None, JoinGroupDelay=None, LeaveGroupDelay=None, McMessageTxRate=None, McGroupDistMode=None, McClientVersion=None, McBaseIPAddress=None, McBaseIPStep=None, McGroupIncrement=None, McIPPrefixLength=None, McBaseIPv6Address=None, McBaseIPv6Step=None, McIPv6PrefixLength=None, TransportLayerHeaderType=None, UseRandomPorts=None, SourcePortBase=None, SourcePortCount=None, SourcePortStep=None, DestPortBase=None, DestPortCount=None, DestPortStep=None, Ipv4Tos=None, Ipv6FlowLabel=None, IpTtl=None, VlanPriority=None, TrafficVerificationAbortOnFail=None, TrafficVerificationFreqMode=None, TrafficVerificationDurationMode=None, TrafficVerfictionTxFrameCount=None, TrafficVerfictionTxSeconds=None, TrafficVerificationTxFrameRate=None, TopLayerType=None, **kwargs):
        properties = kwargs.copy()
        if TrialNum is not None:
            self._TrialNum = TrialNum
            properties['TrialNum'] = TrialNum
        if DurationMode is not None:
            self._DurationMode = DurationMode
            properties['DurationMode'] = DurationMode
        if DurationTime is not None:
            self._DurationTime = DurationTime
            properties['DurationTime'] = DurationTime
        if DurationBurst is not None:
            self._DurationBurst = DurationBurst
            properties['DurationBurst'] = DurationBurst
        if DeviceConfigurationMode is not None:
            self._DeviceConfigurationMode = DeviceConfigurationMode
            properties['DeviceConfigurationMode'] = DeviceConfigurationMode
        if MonitorPortHandles is not None:
            self._MonitorPortHandles = MonitorPortHandles
            properties['MonitorPortHandles'] = MonitorPortHandles
        if AddressLearningFrequency is not None:
            self._AddressLearningFrequency = AddressLearningFrequency
            properties['AddressLearningFrequency'] = AddressLearningFrequency
        if JoinGroupDelay is not None:
            self._JoinGroupDelay = JoinGroupDelay
            properties['JoinGroupDelay'] = JoinGroupDelay
        if LeaveGroupDelay is not None:
            self._LeaveGroupDelay = LeaveGroupDelay
            properties['LeaveGroupDelay'] = LeaveGroupDelay
        if McMessageTxRate is not None:
            self._McMessageTxRate = McMessageTxRate
            properties['McMessageTxRate'] = McMessageTxRate
        if McGroupDistMode is not None:
            self._McGroupDistMode = McGroupDistMode
            properties['McGroupDistMode'] = McGroupDistMode
        if McClientVersion is not None:
            self._McClientVersion = McClientVersion
            properties['McClientVersion'] = McClientVersion
        if McBaseIPAddress is not None:
            self._McBaseIPAddress = McBaseIPAddress
            properties['McBaseIPAddress'] = McBaseIPAddress
        if McBaseIPStep is not None:
            self._McBaseIPStep = McBaseIPStep
            properties['McBaseIPStep'] = McBaseIPStep
        if McGroupIncrement is not None:
            self._McGroupIncrement = McGroupIncrement
            properties['McGroupIncrement'] = McGroupIncrement
        if McIPPrefixLength is not None:
            self._McIPPrefixLength = McIPPrefixLength
            properties['McIPPrefixLength'] = McIPPrefixLength
        if McBaseIPv6Address is not None:
            self._McBaseIPv6Address = McBaseIPv6Address
            properties['McBaseIPv6Address'] = McBaseIPv6Address
        if McBaseIPv6Step is not None:
            self._McBaseIPv6Step = McBaseIPv6Step
            properties['McBaseIPv6Step'] = McBaseIPv6Step
        if McIPv6PrefixLength is not None:
            self._McIPv6PrefixLength = McIPv6PrefixLength
            properties['McIPv6PrefixLength'] = McIPv6PrefixLength
        if TransportLayerHeaderType is not None:
            self._TransportLayerHeaderType = TransportLayerHeaderType
            properties['TransportLayerHeaderType'] = TransportLayerHeaderType
        if UseRandomPorts is not None:
            self._UseRandomPorts = UseRandomPorts
            properties['UseRandomPorts'] = UseRandomPorts
        if SourcePortBase is not None:
            self._SourcePortBase = SourcePortBase
            properties['SourcePortBase'] = SourcePortBase
        if SourcePortCount is not None:
            self._SourcePortCount = SourcePortCount
            properties['SourcePortCount'] = SourcePortCount
        if SourcePortStep is not None:
            self._SourcePortStep = SourcePortStep
            properties['SourcePortStep'] = SourcePortStep
        if DestPortBase is not None:
            self._DestPortBase = DestPortBase
            properties['DestPortBase'] = DestPortBase
        if DestPortCount is not None:
            self._DestPortCount = DestPortCount
            properties['DestPortCount'] = DestPortCount
        if DestPortStep is not None:
            self._DestPortStep = DestPortStep
            properties['DestPortStep'] = DestPortStep
        if Ipv4Tos is not None:
            self._Ipv4Tos = Ipv4Tos
            properties['Ipv4Tos'] = Ipv4Tos
        if Ipv6FlowLabel is not None:
            self._Ipv6FlowLabel = Ipv6FlowLabel
            properties['Ipv6FlowLabel'] = Ipv6FlowLabel
        if IpTtl is not None:
            self._IpTtl = IpTtl
            properties['IpTtl'] = IpTtl
        if VlanPriority is not None:
            self._VlanPriority = VlanPriority
            properties['VlanPriority'] = VlanPriority
        if TrafficVerificationAbortOnFail is not None:
            self._TrafficVerificationAbortOnFail = TrafficVerificationAbortOnFail
            properties['TrafficVerificationAbortOnFail'] = TrafficVerificationAbortOnFail
        if TrafficVerificationFreqMode is not None:
            self._TrafficVerificationFreqMode = TrafficVerificationFreqMode
            properties['TrafficVerificationFreqMode'] = TrafficVerificationFreqMode
        if TrafficVerificationDurationMode is not None:
            self._TrafficVerificationDurationMode = TrafficVerificationDurationMode
            properties['TrafficVerificationDurationMode'] = TrafficVerificationDurationMode
        if TrafficVerfictionTxFrameCount is not None:
            self._TrafficVerfictionTxFrameCount = TrafficVerfictionTxFrameCount
            properties['TrafficVerfictionTxFrameCount'] = TrafficVerfictionTxFrameCount
        if TrafficVerfictionTxSeconds is not None:
            self._TrafficVerfictionTxSeconds = TrafficVerfictionTxSeconds
            properties['TrafficVerfictionTxSeconds'] = TrafficVerfictionTxSeconds
        if TrafficVerificationTxFrameRate is not None:
            self._TrafficVerificationTxFrameRate = TrafficVerificationTxFrameRate
            properties['TrafficVerificationTxFrameRate'] = TrafficVerificationTxFrameRate
        if TopLayerType is not None:
            self._TopLayerType = TopLayerType
            properties['TopLayerType'] = TopLayerType

        super(Rfc3918Config, self).edit(**properties)

    @property
    def TrialNum(self):
        """
        get the value of property _TrialNum
        """
        if self.force_auto_sync:
            self.get('TrialNum')
        return self._TrialNum

    @property
    def DurationMode(self):
        """
        get the value of property _DurationMode
        """
        if self.force_auto_sync:
            self.get('DurationMode')
        return self._DurationMode

    @property
    def DurationTime(self):
        """
        get the value of property _DurationTime
        """
        if self.force_auto_sync:
            self.get('DurationTime')
        return self._DurationTime

    @property
    def DurationBurst(self):
        """
        get the value of property _DurationBurst
        """
        if self.force_auto_sync:
            self.get('DurationBurst')
        return self._DurationBurst

    @property
    def DeviceConfigurationMode(self):
        """
        get the value of property _DeviceConfigurationMode
        """
        if self.force_auto_sync:
            self.get('DeviceConfigurationMode')
        return self._DeviceConfigurationMode

    @property
    def MonitorPortHandles(self):
        """
        get the value of property _MonitorPortHandles
        """
        if self.force_auto_sync:
            self.get('MonitorPortHandles')
        return self._MonitorPortHandles

    @property
    def AddressLearningFrequency(self):
        """
        get the value of property _AddressLearningFrequency
        """
        if self.force_auto_sync:
            self.get('AddressLearningFrequency')
        return self._AddressLearningFrequency

    @property
    def JoinGroupDelay(self):
        """
        get the value of property _JoinGroupDelay
        """
        if self.force_auto_sync:
            self.get('JoinGroupDelay')
        return self._JoinGroupDelay

    @property
    def LeaveGroupDelay(self):
        """
        get the value of property _LeaveGroupDelay
        """
        if self.force_auto_sync:
            self.get('LeaveGroupDelay')
        return self._LeaveGroupDelay

    @property
    def McMessageTxRate(self):
        """
        get the value of property _McMessageTxRate
        """
        if self.force_auto_sync:
            self.get('McMessageTxRate')
        return self._McMessageTxRate

    @property
    def McGroupDistMode(self):
        """
        get the value of property _McGroupDistMode
        """
        if self.force_auto_sync:
            self.get('McGroupDistMode')
        return self._McGroupDistMode

    @property
    def McClientVersion(self):
        """
        get the value of property _McClientVersion
        """
        if self.force_auto_sync:
            self.get('McClientVersion')
        return self._McClientVersion

    @property
    def McBaseIPAddress(self):
        """
        get the value of property _McBaseIPAddress
        """
        if self.force_auto_sync:
            self.get('McBaseIPAddress')
        return self._McBaseIPAddress

    @property
    def McBaseIPStep(self):
        """
        get the value of property _McBaseIPStep
        """
        if self.force_auto_sync:
            self.get('McBaseIPStep')
        return self._McBaseIPStep

    @property
    def McGroupIncrement(self):
        """
        get the value of property _McGroupIncrement
        """
        if self.force_auto_sync:
            self.get('McGroupIncrement')
        return self._McGroupIncrement

    @property
    def McIPPrefixLength(self):
        """
        get the value of property _McIPPrefixLength
        """
        if self.force_auto_sync:
            self.get('McIPPrefixLength')
        return self._McIPPrefixLength

    @property
    def McBaseIPv6Address(self):
        """
        get the value of property _McBaseIPv6Address
        """
        if self.force_auto_sync:
            self.get('McBaseIPv6Address')
        return self._McBaseIPv6Address

    @property
    def McBaseIPv6Step(self):
        """
        get the value of property _McBaseIPv6Step
        """
        if self.force_auto_sync:
            self.get('McBaseIPv6Step')
        return self._McBaseIPv6Step

    @property
    def McIPv6PrefixLength(self):
        """
        get the value of property _McIPv6PrefixLength
        """
        if self.force_auto_sync:
            self.get('McIPv6PrefixLength')
        return self._McIPv6PrefixLength

    @property
    def TransportLayerHeaderType(self):
        """
        get the value of property _TransportLayerHeaderType
        """
        if self.force_auto_sync:
            self.get('TransportLayerHeaderType')
        return self._TransportLayerHeaderType

    @property
    def UseRandomPorts(self):
        """
        get the value of property _UseRandomPorts
        """
        if self.force_auto_sync:
            self.get('UseRandomPorts')
        return self._UseRandomPorts

    @property
    def SourcePortBase(self):
        """
        get the value of property _SourcePortBase
        """
        if self.force_auto_sync:
            self.get('SourcePortBase')
        return self._SourcePortBase

    @property
    def SourcePortCount(self):
        """
        get the value of property _SourcePortCount
        """
        if self.force_auto_sync:
            self.get('SourcePortCount')
        return self._SourcePortCount

    @property
    def SourcePortStep(self):
        """
        get the value of property _SourcePortStep
        """
        if self.force_auto_sync:
            self.get('SourcePortStep')
        return self._SourcePortStep

    @property
    def DestPortBase(self):
        """
        get the value of property _DestPortBase
        """
        if self.force_auto_sync:
            self.get('DestPortBase')
        return self._DestPortBase

    @property
    def DestPortCount(self):
        """
        get the value of property _DestPortCount
        """
        if self.force_auto_sync:
            self.get('DestPortCount')
        return self._DestPortCount

    @property
    def DestPortStep(self):
        """
        get the value of property _DestPortStep
        """
        if self.force_auto_sync:
            self.get('DestPortStep')
        return self._DestPortStep

    @property
    def Ipv4Tos(self):
        """
        get the value of property _Ipv4Tos
        """
        if self.force_auto_sync:
            self.get('Ipv4Tos')
        return self._Ipv4Tos

    @property
    def Ipv6FlowLabel(self):
        """
        get the value of property _Ipv6FlowLabel
        """
        if self.force_auto_sync:
            self.get('Ipv6FlowLabel')
        return self._Ipv6FlowLabel

    @property
    def IpTtl(self):
        """
        get the value of property _IpTtl
        """
        if self.force_auto_sync:
            self.get('IpTtl')
        return self._IpTtl

    @property
    def VlanPriority(self):
        """
        get the value of property _VlanPriority
        """
        if self.force_auto_sync:
            self.get('VlanPriority')
        return self._VlanPriority

    @property
    def TrafficVerificationAbortOnFail(self):
        """
        get the value of property _TrafficVerificationAbortOnFail
        """
        if self.force_auto_sync:
            self.get('TrafficVerificationAbortOnFail')
        return self._TrafficVerificationAbortOnFail

    @property
    def TrafficVerificationFreqMode(self):
        """
        get the value of property _TrafficVerificationFreqMode
        """
        if self.force_auto_sync:
            self.get('TrafficVerificationFreqMode')
        return self._TrafficVerificationFreqMode

    @property
    def TrafficVerificationDurationMode(self):
        """
        get the value of property _TrafficVerificationDurationMode
        """
        if self.force_auto_sync:
            self.get('TrafficVerificationDurationMode')
        return self._TrafficVerificationDurationMode

    @property
    def TrafficVerfictionTxFrameCount(self):
        """
        get the value of property _TrafficVerfictionTxFrameCount
        """
        if self.force_auto_sync:
            self.get('TrafficVerfictionTxFrameCount')
        return self._TrafficVerfictionTxFrameCount

    @property
    def TrafficVerfictionTxSeconds(self):
        """
        get the value of property _TrafficVerfictionTxSeconds
        """
        if self.force_auto_sync:
            self.get('TrafficVerfictionTxSeconds')
        return self._TrafficVerfictionTxSeconds

    @property
    def TrafficVerificationTxFrameRate(self):
        """
        get the value of property _TrafficVerificationTxFrameRate
        """
        if self.force_auto_sync:
            self.get('TrafficVerificationTxFrameRate')
        return self._TrafficVerificationTxFrameRate

    @property
    def TopLayerType(self):
        """
        get the value of property _TopLayerType
        """
        if self.force_auto_sync:
            self.get('TopLayerType')
        return self._TopLayerType

    @TrialNum.setter
    def TrialNum(self, value):
        self._TrialNum = value
        self.edit(TrialNum=value)

    @DurationMode.setter
    def DurationMode(self, value):
        self._DurationMode = value
        self.edit(DurationMode=value)

    @DurationTime.setter
    def DurationTime(self, value):
        self._DurationTime = value
        self.edit(DurationTime=value)

    @DurationBurst.setter
    def DurationBurst(self, value):
        self._DurationBurst = value
        self.edit(DurationBurst=value)

    @DeviceConfigurationMode.setter
    def DeviceConfigurationMode(self, value):
        self._DeviceConfigurationMode = value
        self.edit(DeviceConfigurationMode=value)

    @MonitorPortHandles.setter
    def MonitorPortHandles(self, value):
        self._MonitorPortHandles = value
        self.edit(MonitorPortHandles=value)

    @AddressLearningFrequency.setter
    def AddressLearningFrequency(self, value):
        self._AddressLearningFrequency = value
        self.edit(AddressLearningFrequency=value)

    @JoinGroupDelay.setter
    def JoinGroupDelay(self, value):
        self._JoinGroupDelay = value
        self.edit(JoinGroupDelay=value)

    @LeaveGroupDelay.setter
    def LeaveGroupDelay(self, value):
        self._LeaveGroupDelay = value
        self.edit(LeaveGroupDelay=value)

    @McMessageTxRate.setter
    def McMessageTxRate(self, value):
        self._McMessageTxRate = value
        self.edit(McMessageTxRate=value)

    @McGroupDistMode.setter
    def McGroupDistMode(self, value):
        self._McGroupDistMode = value
        self.edit(McGroupDistMode=value)

    @McClientVersion.setter
    def McClientVersion(self, value):
        self._McClientVersion = value
        self.edit(McClientVersion=value)

    @McBaseIPAddress.setter
    def McBaseIPAddress(self, value):
        self._McBaseIPAddress = value
        self.edit(McBaseIPAddress=value)

    @McBaseIPStep.setter
    def McBaseIPStep(self, value):
        self._McBaseIPStep = value
        self.edit(McBaseIPStep=value)

    @McGroupIncrement.setter
    def McGroupIncrement(self, value):
        self._McGroupIncrement = value
        self.edit(McGroupIncrement=value)

    @McIPPrefixLength.setter
    def McIPPrefixLength(self, value):
        self._McIPPrefixLength = value
        self.edit(McIPPrefixLength=value)

    @McBaseIPv6Address.setter
    def McBaseIPv6Address(self, value):
        self._McBaseIPv6Address = value
        self.edit(McBaseIPv6Address=value)

    @McBaseIPv6Step.setter
    def McBaseIPv6Step(self, value):
        self._McBaseIPv6Step = value
        self.edit(McBaseIPv6Step=value)

    @McIPv6PrefixLength.setter
    def McIPv6PrefixLength(self, value):
        self._McIPv6PrefixLength = value
        self.edit(McIPv6PrefixLength=value)

    @TransportLayerHeaderType.setter
    def TransportLayerHeaderType(self, value):
        self._TransportLayerHeaderType = value
        self.edit(TransportLayerHeaderType=value)

    @UseRandomPorts.setter
    def UseRandomPorts(self, value):
        self._UseRandomPorts = value
        self.edit(UseRandomPorts=value)

    @SourcePortBase.setter
    def SourcePortBase(self, value):
        self._SourcePortBase = value
        self.edit(SourcePortBase=value)

    @SourcePortCount.setter
    def SourcePortCount(self, value):
        self._SourcePortCount = value
        self.edit(SourcePortCount=value)

    @SourcePortStep.setter
    def SourcePortStep(self, value):
        self._SourcePortStep = value
        self.edit(SourcePortStep=value)

    @DestPortBase.setter
    def DestPortBase(self, value):
        self._DestPortBase = value
        self.edit(DestPortBase=value)

    @DestPortCount.setter
    def DestPortCount(self, value):
        self._DestPortCount = value
        self.edit(DestPortCount=value)

    @DestPortStep.setter
    def DestPortStep(self, value):
        self._DestPortStep = value
        self.edit(DestPortStep=value)

    @Ipv4Tos.setter
    def Ipv4Tos(self, value):
        self._Ipv4Tos = value
        self.edit(Ipv4Tos=value)

    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        self._Ipv6FlowLabel = value
        self.edit(Ipv6FlowLabel=value)

    @IpTtl.setter
    def IpTtl(self, value):
        self._IpTtl = value
        self.edit(IpTtl=value)

    @VlanPriority.setter
    def VlanPriority(self, value):
        self._VlanPriority = value
        self.edit(VlanPriority=value)

    @TrafficVerificationAbortOnFail.setter
    def TrafficVerificationAbortOnFail(self, value):
        self._TrafficVerificationAbortOnFail = value
        self.edit(TrafficVerificationAbortOnFail=value)

    @TrafficVerificationFreqMode.setter
    def TrafficVerificationFreqMode(self, value):
        self._TrafficVerificationFreqMode = value
        self.edit(TrafficVerificationFreqMode=value)

    @TrafficVerificationDurationMode.setter
    def TrafficVerificationDurationMode(self, value):
        self._TrafficVerificationDurationMode = value
        self.edit(TrafficVerificationDurationMode=value)

    @TrafficVerfictionTxFrameCount.setter
    def TrafficVerfictionTxFrameCount(self, value):
        self._TrafficVerfictionTxFrameCount = value
        self.edit(TrafficVerfictionTxFrameCount=value)

    @TrafficVerfictionTxSeconds.setter
    def TrafficVerfictionTxSeconds(self, value):
        self._TrafficVerfictionTxSeconds = value
        self.edit(TrafficVerfictionTxSeconds=value)

    @TrafficVerificationTxFrameRate.setter
    def TrafficVerificationTxFrameRate(self, value):
        self._TrafficVerificationTxFrameRate = value
        self.edit(TrafficVerificationTxFrameRate=value)

    @TopLayerType.setter
    def TopLayerType(self, value):
        self._TopLayerType = value
        self.edit(TopLayerType=value)

    def _set_trialnum_with_str(self, value):
        try:
            self._TrialNum = int(value)
        except ValueError:
            self._TrialNum = hex(int(value, 16))

    def _set_durationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._DurationMode = EnumDurationMode.%s' % value[:seperate])

    def _set_durationtime_with_str(self, value):
        try:
            self._DurationTime = int(value)
        except ValueError:
            self._DurationTime = hex(int(value, 16))

    def _set_durationburst_with_str(self, value):
        try:
            self._DurationBurst = int(value)
        except ValueError:
            self._DurationBurst = hex(int(value, 16))

    def _set_deviceconfigurationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._DeviceConfigurationMode = EnumDeviceConfigurationMode.%s' % value[:seperate])

    def _set_monitorporthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MonitorPortHandles = tmp_value.split()

    def _set_addresslearningfrequency_with_str(self, value):
        seperate = value.find(':')
        exec('self._AddressLearningFrequency = Enum3918AdddressLearningFrequency.%s' % value[:seperate])

    def _set_joingroupdelay_with_str(self, value):
        try:
            self._JoinGroupDelay = int(value)
        except ValueError:
            self._JoinGroupDelay = hex(int(value, 16))

    def _set_leavegroupdelay_with_str(self, value):
        try:
            self._LeaveGroupDelay = int(value)
        except ValueError:
            self._LeaveGroupDelay = hex(int(value, 16))

    def _set_mcmessagetxrate_with_str(self, value):
        try:
            self._McMessageTxRate = int(value)
        except ValueError:
            self._McMessageTxRate = hex(int(value, 16))

    def _set_mcgroupdistmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._McGroupDistMode = EnumMulticastGroupDist.%s' % value[:seperate])

    def _set_mcclientversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._McClientVersion = EnumMulticastClientVersion.%s' % value[:seperate])

    def _set_mcbaseipaddress_with_str(self, value):
        self._McBaseIPAddress = value

    def _set_mcbaseipstep_with_str(self, value):
        self._McBaseIPStep = value

    def _set_mcgroupincrement_with_str(self, value):
        try:
            self._McGroupIncrement = int(value)
        except ValueError:
            self._McGroupIncrement = hex(int(value, 16))

    def _set_mcipprefixlength_with_str(self, value):
        try:
            self._McIPPrefixLength = int(value)
        except ValueError:
            self._McIPPrefixLength = hex(int(value, 16))

    def _set_mcbaseipv6address_with_str(self, value):
        self._McBaseIPv6Address = value

    def _set_mcbaseipv6step_with_str(self, value):
        self._McBaseIPv6Step = value

    def _set_mcipv6prefixlength_with_str(self, value):
        try:
            self._McIPv6PrefixLength = int(value)
        except ValueError:
            self._McIPv6PrefixLength = hex(int(value, 16))

    def _set_transportlayerheadertype_with_str(self, value):
        seperate = value.find(':')
        exec('self._TransportLayerHeaderType = EnumTransportLayerHeaderType.%s' % value[:seperate])

    def _set_userandomports_with_str(self, value):
        self._UseRandomPorts = (value == 'True')

    def _set_sourceportbase_with_str(self, value):
        try:
            self._SourcePortBase = int(value)
        except ValueError:
            self._SourcePortBase = hex(int(value, 16))

    def _set_sourceportcount_with_str(self, value):
        try:
            self._SourcePortCount = int(value)
        except ValueError:
            self._SourcePortCount = hex(int(value, 16))

    def _set_sourceportstep_with_str(self, value):
        try:
            self._SourcePortStep = int(value)
        except ValueError:
            self._SourcePortStep = hex(int(value, 16))

    def _set_destportbase_with_str(self, value):
        try:
            self._DestPortBase = int(value)
        except ValueError:
            self._DestPortBase = hex(int(value, 16))

    def _set_destportcount_with_str(self, value):
        try:
            self._DestPortCount = int(value)
        except ValueError:
            self._DestPortCount = hex(int(value, 16))

    def _set_destportstep_with_str(self, value):
        try:
            self._DestPortStep = int(value)
        except ValueError:
            self._DestPortStep = hex(int(value, 16))

    def _set_ipv4tos_with_str(self, value):
        try:
            self._Ipv4Tos = int(value)
        except ValueError:
            self._Ipv4Tos = hex(int(value, 16))

    def _set_ipv6flowlabel_with_str(self, value):
        try:
            self._Ipv6FlowLabel = int(value)
        except ValueError:
            self._Ipv6FlowLabel = hex(int(value, 16))

    def _set_ipttl_with_str(self, value):
        try:
            self._IpTtl = int(value)
        except ValueError:
            self._IpTtl = hex(int(value, 16))

    def _set_vlanpriority_with_str(self, value):
        try:
            self._VlanPriority = int(value)
        except ValueError:
            self._VlanPriority = hex(int(value, 16))

    def _set_trafficverificationabortonfail_with_str(self, value):
        self._TrafficVerificationAbortOnFail = (value == 'True')

    def _set_trafficverificationfreqmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficVerificationFreqMode = EnumTrafficVerificationFrequency.%s' % value[:seperate])

    def _set_trafficverificationdurationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficVerificationDurationMode = EnumDurationMode.%s' % value[:seperate])

    def _set_trafficverfictiontxframecount_with_str(self, value):
        try:
            self._TrafficVerfictionTxFrameCount = int(value)
        except ValueError:
            self._TrafficVerfictionTxFrameCount = hex(int(value, 16))

    def _set_trafficverfictiontxseconds_with_str(self, value):
        try:
            self._TrafficVerfictionTxSeconds = int(value)
        except ValueError:
            self._TrafficVerfictionTxSeconds = hex(int(value, 16))

    def _set_trafficverificationtxframerate_with_str(self, value):
        try:
            self._TrafficVerificationTxFrameRate = int(value)
        except ValueError:
            self._TrafficVerificationTxFrameRate = hex(int(value, 16))

    def _set_toplayertype_with_str(self, value):
        seperate = value.find(':')
        exec('self._TopLayerType = EnumTrafficType.%s' % value[:seperate])

