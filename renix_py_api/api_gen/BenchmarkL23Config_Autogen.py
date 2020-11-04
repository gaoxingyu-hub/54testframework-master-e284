"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BenchmarkConfig_Autogen import BenchmarkConfig


@rom_manager.rom
class BenchmarkL23Config(BenchmarkConfig):
    def __init__(self, EnableUserBreak=None, DelayAfterTransmit=None, TrafficStartDelay=None, LatencyType=None, StreamTemplateHandles=None, EnableAddressLearning=None, EnableArpLearning=None, AddressLearningMode=None, AddressLearningRetryCount=None, DelayBeforeAddressLearning=None, AddressLearningRate=None, ArpPacketRate=None, ArpRetryCount=None, FrameSizeType=None, FrameSizeFix=None, FrameSizeMin=None, FrameSizeMax=None, FrameSizeStart=None, FrameSizeStep=None, FrameSizeEnd=None, FrameSizeCustom=None, FrameSizeImix=None, ResultPath=None, Bidirection=None, TrafficMeshMode=None, EndpointMapping=None, **kwargs):
        self._EnableUserBreak = EnableUserBreak  # Enable User Break
        self._DelayAfterTransmit = DelayAfterTransmit  # Delay After Transmit (sec)
        self._TrafficStartDelay = TrafficStartDelay  # Traffic start delay (sec)
        self._LatencyType = LatencyType  # Latency type
        self._StreamTemplateHandles = StreamTemplateHandles  # Config Handle
        self._EnableAddressLearning = EnableAddressLearning  # Enable Address Learning
        self._EnableArpLearning = EnableArpLearning  # Enable Arp Learning
        self._AddressLearningMode = AddressLearningMode  # Address Learning Mode
        self._AddressLearningRetryCount = AddressLearningRetryCount  # Address Learning Retry Count
        self._DelayBeforeAddressLearning = DelayBeforeAddressLearning  # Delay Before Address Learning
        self._AddressLearningRate = AddressLearningRate  # Address Learning Rate
        self._ArpPacketRate = ArpPacketRate  # Arp Packet Rate
        self._ArpRetryCount = ArpRetryCount  # Arp Retry Count
        self._FrameSizeType = FrameSizeType  # Frame size loop mode
        self._FrameSizeFix = FrameSizeFix  # Size
        self._FrameSizeMin = FrameSizeMin  # Min
        self._FrameSizeMax = FrameSizeMax  # Max
        self._FrameSizeStart = FrameSizeStart  # Start
        self._FrameSizeStep = FrameSizeStep  # Step
        self._FrameSizeEnd = FrameSizeEnd  # End
        self._FrameSizeCustom = FrameSizeCustom  # Frame Size Custom List
        self._FrameSizeImix = FrameSizeImix  # Frame Size iMIX List
        self._ResultPath = ResultPath  # Result Path
        self._Bidirection = Bidirection  # Bidirection
        self._TrafficMeshMode = TrafficMeshMode  # Traffic Mode
        self._EndpointMapping = EndpointMapping  # Traffic Mode

        properties = kwargs.copy()
        if EnableUserBreak is not None:
            properties['EnableUserBreak'] = EnableUserBreak
        if DelayAfterTransmit is not None:
            properties['DelayAfterTransmit'] = DelayAfterTransmit
        if TrafficStartDelay is not None:
            properties['TrafficStartDelay'] = TrafficStartDelay
        if LatencyType is not None:
            properties['LatencyType'] = LatencyType
        if StreamTemplateHandles is not None:
            properties['StreamTemplateHandles'] = StreamTemplateHandles
        if EnableAddressLearning is not None:
            properties['EnableAddressLearning'] = EnableAddressLearning
        if EnableArpLearning is not None:
            properties['EnableArpLearning'] = EnableArpLearning
        if AddressLearningMode is not None:
            properties['AddressLearningMode'] = AddressLearningMode
        if AddressLearningRetryCount is not None:
            properties['AddressLearningRetryCount'] = AddressLearningRetryCount
        if DelayBeforeAddressLearning is not None:
            properties['DelayBeforeAddressLearning'] = DelayBeforeAddressLearning
        if AddressLearningRate is not None:
            properties['AddressLearningRate'] = AddressLearningRate
        if ArpPacketRate is not None:
            properties['ArpPacketRate'] = ArpPacketRate
        if ArpRetryCount is not None:
            properties['ArpRetryCount'] = ArpRetryCount
        if FrameSizeType is not None:
            properties['FrameSizeType'] = FrameSizeType
        if FrameSizeFix is not None:
            properties['FrameSizeFix'] = FrameSizeFix
        if FrameSizeMin is not None:
            properties['FrameSizeMin'] = FrameSizeMin
        if FrameSizeMax is not None:
            properties['FrameSizeMax'] = FrameSizeMax
        if FrameSizeStart is not None:
            properties['FrameSizeStart'] = FrameSizeStart
        if FrameSizeStep is not None:
            properties['FrameSizeStep'] = FrameSizeStep
        if FrameSizeEnd is not None:
            properties['FrameSizeEnd'] = FrameSizeEnd
        if FrameSizeCustom is not None:
            properties['FrameSizeCustom'] = FrameSizeCustom
        if FrameSizeImix is not None:
            properties['FrameSizeImix'] = FrameSizeImix
        if ResultPath is not None:
            properties['ResultPath'] = ResultPath
        if Bidirection is not None:
            properties['Bidirection'] = Bidirection
        if TrafficMeshMode is not None:
            properties['TrafficMeshMode'] = TrafficMeshMode
        if EndpointMapping is not None:
            properties['EndpointMapping'] = EndpointMapping

        # call base class function, and it will send message to renix server to create a class.
        super(BenchmarkL23Config, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EnableUserBreak=None, DelayAfterTransmit=None, TrafficStartDelay=None, LatencyType=None, StreamTemplateHandles=None, EnableAddressLearning=None, EnableArpLearning=None, AddressLearningMode=None, AddressLearningRetryCount=None, DelayBeforeAddressLearning=None, AddressLearningRate=None, ArpPacketRate=None, ArpRetryCount=None, FrameSizeType=None, FrameSizeFix=None, FrameSizeMin=None, FrameSizeMax=None, FrameSizeStart=None, FrameSizeStep=None, FrameSizeEnd=None, FrameSizeCustom=None, FrameSizeImix=None, ResultPath=None, Bidirection=None, TrafficMeshMode=None, EndpointMapping=None, **kwargs):
        properties = kwargs.copy()
        if EnableUserBreak is not None:
            self._EnableUserBreak = EnableUserBreak
            properties['EnableUserBreak'] = EnableUserBreak
        if DelayAfterTransmit is not None:
            self._DelayAfterTransmit = DelayAfterTransmit
            properties['DelayAfterTransmit'] = DelayAfterTransmit
        if TrafficStartDelay is not None:
            self._TrafficStartDelay = TrafficStartDelay
            properties['TrafficStartDelay'] = TrafficStartDelay
        if LatencyType is not None:
            self._LatencyType = LatencyType
            properties['LatencyType'] = LatencyType
        if StreamTemplateHandles is not None:
            self._StreamTemplateHandles = StreamTemplateHandles
            properties['StreamTemplateHandles'] = StreamTemplateHandles
        if EnableAddressLearning is not None:
            self._EnableAddressLearning = EnableAddressLearning
            properties['EnableAddressLearning'] = EnableAddressLearning
        if EnableArpLearning is not None:
            self._EnableArpLearning = EnableArpLearning
            properties['EnableArpLearning'] = EnableArpLearning
        if AddressLearningMode is not None:
            self._AddressLearningMode = AddressLearningMode
            properties['AddressLearningMode'] = AddressLearningMode
        if AddressLearningRetryCount is not None:
            self._AddressLearningRetryCount = AddressLearningRetryCount
            properties['AddressLearningRetryCount'] = AddressLearningRetryCount
        if DelayBeforeAddressLearning is not None:
            self._DelayBeforeAddressLearning = DelayBeforeAddressLearning
            properties['DelayBeforeAddressLearning'] = DelayBeforeAddressLearning
        if AddressLearningRate is not None:
            self._AddressLearningRate = AddressLearningRate
            properties['AddressLearningRate'] = AddressLearningRate
        if ArpPacketRate is not None:
            self._ArpPacketRate = ArpPacketRate
            properties['ArpPacketRate'] = ArpPacketRate
        if ArpRetryCount is not None:
            self._ArpRetryCount = ArpRetryCount
            properties['ArpRetryCount'] = ArpRetryCount
        if FrameSizeType is not None:
            self._FrameSizeType = FrameSizeType
            properties['FrameSizeType'] = FrameSizeType
        if FrameSizeFix is not None:
            self._FrameSizeFix = FrameSizeFix
            properties['FrameSizeFix'] = FrameSizeFix
        if FrameSizeMin is not None:
            self._FrameSizeMin = FrameSizeMin
            properties['FrameSizeMin'] = FrameSizeMin
        if FrameSizeMax is not None:
            self._FrameSizeMax = FrameSizeMax
            properties['FrameSizeMax'] = FrameSizeMax
        if FrameSizeStart is not None:
            self._FrameSizeStart = FrameSizeStart
            properties['FrameSizeStart'] = FrameSizeStart
        if FrameSizeStep is not None:
            self._FrameSizeStep = FrameSizeStep
            properties['FrameSizeStep'] = FrameSizeStep
        if FrameSizeEnd is not None:
            self._FrameSizeEnd = FrameSizeEnd
            properties['FrameSizeEnd'] = FrameSizeEnd
        if FrameSizeCustom is not None:
            self._FrameSizeCustom = FrameSizeCustom
            properties['FrameSizeCustom'] = FrameSizeCustom
        if FrameSizeImix is not None:
            self._FrameSizeImix = FrameSizeImix
            properties['FrameSizeImix'] = FrameSizeImix
        if ResultPath is not None:
            self._ResultPath = ResultPath
            properties['ResultPath'] = ResultPath
        if Bidirection is not None:
            self._Bidirection = Bidirection
            properties['Bidirection'] = Bidirection
        if TrafficMeshMode is not None:
            self._TrafficMeshMode = TrafficMeshMode
            properties['TrafficMeshMode'] = TrafficMeshMode
        if EndpointMapping is not None:
            self._EndpointMapping = EndpointMapping
            properties['EndpointMapping'] = EndpointMapping

        super(BenchmarkL23Config, self).edit(**properties)

    @property
    def EnableUserBreak(self):
        """
        get the value of property _EnableUserBreak
        """
        if self.force_auto_sync:
            self.get('EnableUserBreak')
        return self._EnableUserBreak

    @property
    def DelayAfterTransmit(self):
        """
        get the value of property _DelayAfterTransmit
        """
        if self.force_auto_sync:
            self.get('DelayAfterTransmit')
        return self._DelayAfterTransmit

    @property
    def TrafficStartDelay(self):
        """
        get the value of property _TrafficStartDelay
        """
        if self.force_auto_sync:
            self.get('TrafficStartDelay')
        return self._TrafficStartDelay

    @property
    def LatencyType(self):
        """
        get the value of property _LatencyType
        """
        if self.force_auto_sync:
            self.get('LatencyType')
        return self._LatencyType

    @property
    def StreamTemplateHandles(self):
        """
        get the value of property _StreamTemplateHandles
        """
        if self.force_auto_sync:
            self.get('StreamTemplateHandles')
        return self._StreamTemplateHandles

    @property
    def EnableAddressLearning(self):
        """
        get the value of property _EnableAddressLearning
        """
        if self.force_auto_sync:
            self.get('EnableAddressLearning')
        return self._EnableAddressLearning

    @property
    def EnableArpLearning(self):
        """
        get the value of property _EnableArpLearning
        """
        if self.force_auto_sync:
            self.get('EnableArpLearning')
        return self._EnableArpLearning

    @property
    def AddressLearningMode(self):
        """
        get the value of property _AddressLearningMode
        """
        if self.force_auto_sync:
            self.get('AddressLearningMode')
        return self._AddressLearningMode

    @property
    def AddressLearningRetryCount(self):
        """
        get the value of property _AddressLearningRetryCount
        """
        if self.force_auto_sync:
            self.get('AddressLearningRetryCount')
        return self._AddressLearningRetryCount

    @property
    def DelayBeforeAddressLearning(self):
        """
        get the value of property _DelayBeforeAddressLearning
        """
        if self.force_auto_sync:
            self.get('DelayBeforeAddressLearning')
        return self._DelayBeforeAddressLearning

    @property
    def AddressLearningRate(self):
        """
        get the value of property _AddressLearningRate
        """
        if self.force_auto_sync:
            self.get('AddressLearningRate')
        return self._AddressLearningRate

    @property
    def ArpPacketRate(self):
        """
        get the value of property _ArpPacketRate
        """
        if self.force_auto_sync:
            self.get('ArpPacketRate')
        return self._ArpPacketRate

    @property
    def ArpRetryCount(self):
        """
        get the value of property _ArpRetryCount
        """
        if self.force_auto_sync:
            self.get('ArpRetryCount')
        return self._ArpRetryCount

    @property
    def FrameSizeType(self):
        """
        get the value of property _FrameSizeType
        """
        if self.force_auto_sync:
            self.get('FrameSizeType')
        return self._FrameSizeType

    @property
    def FrameSizeFix(self):
        """
        get the value of property _FrameSizeFix
        """
        if self.force_auto_sync:
            self.get('FrameSizeFix')
        return self._FrameSizeFix

    @property
    def FrameSizeMin(self):
        """
        get the value of property _FrameSizeMin
        """
        if self.force_auto_sync:
            self.get('FrameSizeMin')
        return self._FrameSizeMin

    @property
    def FrameSizeMax(self):
        """
        get the value of property _FrameSizeMax
        """
        if self.force_auto_sync:
            self.get('FrameSizeMax')
        return self._FrameSizeMax

    @property
    def FrameSizeStart(self):
        """
        get the value of property _FrameSizeStart
        """
        if self.force_auto_sync:
            self.get('FrameSizeStart')
        return self._FrameSizeStart

    @property
    def FrameSizeStep(self):
        """
        get the value of property _FrameSizeStep
        """
        if self.force_auto_sync:
            self.get('FrameSizeStep')
        return self._FrameSizeStep

    @property
    def FrameSizeEnd(self):
        """
        get the value of property _FrameSizeEnd
        """
        if self.force_auto_sync:
            self.get('FrameSizeEnd')
        return self._FrameSizeEnd

    @property
    def FrameSizeCustom(self):
        """
        get the value of property _FrameSizeCustom
        """
        if self.force_auto_sync:
            self.get('FrameSizeCustom')
        return self._FrameSizeCustom

    @property
    def FrameSizeImix(self):
        """
        get the value of property _FrameSizeImix
        """
        if self.force_auto_sync:
            self.get('FrameSizeImix')
        return self._FrameSizeImix

    @property
    def ResultPath(self):
        """
        get the value of property _ResultPath
        """
        if self.force_auto_sync:
            self.get('ResultPath')
        return self._ResultPath

    @property
    def Bidirection(self):
        """
        get the value of property _Bidirection
        """
        if self.force_auto_sync:
            self.get('Bidirection')
        return self._Bidirection

    @property
    def TrafficMeshMode(self):
        """
        get the value of property _TrafficMeshMode
        """
        if self.force_auto_sync:
            self.get('TrafficMeshMode')
        return self._TrafficMeshMode

    @property
    def EndpointMapping(self):
        """
        get the value of property _EndpointMapping
        """
        if self.force_auto_sync:
            self.get('EndpointMapping')
        return self._EndpointMapping

    @EnableUserBreak.setter
    def EnableUserBreak(self, value):
        self._EnableUserBreak = value
        self.edit(EnableUserBreak=value)

    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        self._DelayAfterTransmit = value
        self.edit(DelayAfterTransmit=value)

    @TrafficStartDelay.setter
    def TrafficStartDelay(self, value):
        self._TrafficStartDelay = value
        self.edit(TrafficStartDelay=value)

    @LatencyType.setter
    def LatencyType(self, value):
        self._LatencyType = value
        self.edit(LatencyType=value)

    @StreamTemplateHandles.setter
    def StreamTemplateHandles(self, value):
        self._StreamTemplateHandles = value
        self.edit(StreamTemplateHandles=value)

    @EnableAddressLearning.setter
    def EnableAddressLearning(self, value):
        self._EnableAddressLearning = value
        self.edit(EnableAddressLearning=value)

    @EnableArpLearning.setter
    def EnableArpLearning(self, value):
        self._EnableArpLearning = value
        self.edit(EnableArpLearning=value)

    @AddressLearningMode.setter
    def AddressLearningMode(self, value):
        self._AddressLearningMode = value
        self.edit(AddressLearningMode=value)

    @AddressLearningRetryCount.setter
    def AddressLearningRetryCount(self, value):
        self._AddressLearningRetryCount = value
        self.edit(AddressLearningRetryCount=value)

    @DelayBeforeAddressLearning.setter
    def DelayBeforeAddressLearning(self, value):
        self._DelayBeforeAddressLearning = value
        self.edit(DelayBeforeAddressLearning=value)

    @AddressLearningRate.setter
    def AddressLearningRate(self, value):
        self._AddressLearningRate = value
        self.edit(AddressLearningRate=value)

    @ArpPacketRate.setter
    def ArpPacketRate(self, value):
        self._ArpPacketRate = value
        self.edit(ArpPacketRate=value)

    @ArpRetryCount.setter
    def ArpRetryCount(self, value):
        self._ArpRetryCount = value
        self.edit(ArpRetryCount=value)

    @FrameSizeType.setter
    def FrameSizeType(self, value):
        self._FrameSizeType = value
        self.edit(FrameSizeType=value)

    @FrameSizeFix.setter
    def FrameSizeFix(self, value):
        self._FrameSizeFix = value
        self.edit(FrameSizeFix=value)

    @FrameSizeMin.setter
    def FrameSizeMin(self, value):
        self._FrameSizeMin = value
        self.edit(FrameSizeMin=value)

    @FrameSizeMax.setter
    def FrameSizeMax(self, value):
        self._FrameSizeMax = value
        self.edit(FrameSizeMax=value)

    @FrameSizeStart.setter
    def FrameSizeStart(self, value):
        self._FrameSizeStart = value
        self.edit(FrameSizeStart=value)

    @FrameSizeStep.setter
    def FrameSizeStep(self, value):
        self._FrameSizeStep = value
        self.edit(FrameSizeStep=value)

    @FrameSizeEnd.setter
    def FrameSizeEnd(self, value):
        self._FrameSizeEnd = value
        self.edit(FrameSizeEnd=value)

    @FrameSizeCustom.setter
    def FrameSizeCustom(self, value):
        self._FrameSizeCustom = value
        self.edit(FrameSizeCustom=value)

    @FrameSizeImix.setter
    def FrameSizeImix(self, value):
        self._FrameSizeImix = value
        self.edit(FrameSizeImix=value)

    @ResultPath.setter
    def ResultPath(self, value):
        self._ResultPath = value
        self.edit(ResultPath=value)

    @Bidirection.setter
    def Bidirection(self, value):
        self._Bidirection = value
        self.edit(Bidirection=value)

    @TrafficMeshMode.setter
    def TrafficMeshMode(self, value):
        self._TrafficMeshMode = value
        self.edit(TrafficMeshMode=value)

    @EndpointMapping.setter
    def EndpointMapping(self, value):
        self._EndpointMapping = value
        self.edit(EndpointMapping=value)

    def _set_enableuserbreak_with_str(self, value):
        self._EnableUserBreak = (value == 'True')

    def _set_delayaftertransmit_with_str(self, value):
        try:
            self._DelayAfterTransmit = int(value)
        except ValueError:
            self._DelayAfterTransmit = hex(int(value, 16))

    def _set_trafficstartdelay_with_str(self, value):
        self._TrafficStartDelay = float(value)

    def _set_latencytype_with_str(self, value):
        seperate = value.find(':')
        exec('self._LatencyType = EnumLatencyType.%s' % value[:seperate])

    def _set_streamtemplatehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamTemplateHandles = tmp_value.split()

    def _set_enableaddresslearning_with_str(self, value):
        self._EnableAddressLearning = (value == 'True')

    def _set_enablearplearning_with_str(self, value):
        self._EnableArpLearning = (value == 'True')

    def _set_addresslearningmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._AddressLearningMode = EnumAddressLearningMode.%s' % value[:seperate])

    def _set_addresslearningretrycount_with_str(self, value):
        try:
            self._AddressLearningRetryCount = int(value)
        except ValueError:
            self._AddressLearningRetryCount = hex(int(value, 16))

    def _set_delaybeforeaddresslearning_with_str(self, value):
        try:
            self._DelayBeforeAddressLearning = int(value)
        except ValueError:
            self._DelayBeforeAddressLearning = hex(int(value, 16))

    def _set_addresslearningrate_with_str(self, value):
        try:
            self._AddressLearningRate = int(value)
        except ValueError:
            self._AddressLearningRate = hex(int(value, 16))

    def _set_arppacketrate_with_str(self, value):
        try:
            self._ArpPacketRate = int(value)
        except ValueError:
            self._ArpPacketRate = hex(int(value, 16))

    def _set_arpretrycount_with_str(self, value):
        try:
            self._ArpRetryCount = int(value)
        except ValueError:
            self._ArpRetryCount = hex(int(value, 16))

    def _set_framesizetype_with_str(self, value):
        seperate = value.find(':')
        exec('self._FrameSizeType = EnumFrameSizeType.%s' % value[:seperate])

    def _set_framesizefix_with_str(self, value):
        try:
            self._FrameSizeFix = int(value)
        except ValueError:
            self._FrameSizeFix = hex(int(value, 16))

    def _set_framesizemin_with_str(self, value):
        try:
            self._FrameSizeMin = int(value)
        except ValueError:
            self._FrameSizeMin = hex(int(value, 16))

    def _set_framesizemax_with_str(self, value):
        try:
            self._FrameSizeMax = int(value)
        except ValueError:
            self._FrameSizeMax = hex(int(value, 16))

    def _set_framesizestart_with_str(self, value):
        try:
            self._FrameSizeStart = int(value)
        except ValueError:
            self._FrameSizeStart = hex(int(value, 16))

    def _set_framesizestep_with_str(self, value):
        try:
            self._FrameSizeStep = int(value)
        except ValueError:
            self._FrameSizeStep = hex(int(value, 16))

    def _set_framesizeend_with_str(self, value):
        try:
            self._FrameSizeEnd = int(value)
        except ValueError:
            self._FrameSizeEnd = hex(int(value, 16))

    def _set_framesizecustom_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._FrameSizeCustom = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._FrameSizeCustom.append(int(str_value))
            except ValueError:
                self._FrameSizeCustom.append(hex(int(str_value, 16)))

    def _set_framesizeimix_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._FrameSizeImix = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._FrameSizeImix.append(int(str_value))
            except ValueError:
                self._FrameSizeImix.append(hex(int(str_value, 16)))

    def _set_resultpath_with_str(self, value):
        self._ResultPath = value

    def _set_bidirection_with_str(self, value):
        self._Bidirection = (value == 'True')

    def _set_trafficmeshmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficMeshMode = EnumTrafficMesh.%s' % value[:seperate])

    def _set_endpointmapping_with_str(self, value):
        seperate = value.find(':')
        exec('self._EndpointMapping = EnumEndpointMapping.%s' % value[:seperate])

