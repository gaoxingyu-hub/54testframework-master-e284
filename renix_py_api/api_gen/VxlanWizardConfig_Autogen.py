"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ProtocolWizardConfig_Autogen import ProtocolWizardConfig


@rom_manager.rom
class VxlanWizardConfig(ProtocolWizardConfig):
    def __init__(self, VtepCountPerVlan=None, AutoSelectUDPSourcePort=None, UDPSourcePortStart=None, UDPSourcePortStep=None, EnableUDPChecksum=None, SegmentsCountPerVtep=None, SegmentsCountPerBlock=None, VNI=None, VNIStep=None, UseSameSegmentsAcrossVteps=None, UseSameSegmentsAcrossPort=None, AddressMode=None, NumberofVMspersegment=None, EnableVlan=None, LearningMode=None, MulticastType=None, MulticastIPAddress=None, MulticastIPAddressStep=None, IGMPVersion=None, PIMMode=None, RPAddress=None, BiDirHelloOptionSet=None, EnableInterfaceCount=None, CountPerInterfaceBlcok=None, StepperSegmentBlock=None, **kwargs):
        self._VtepCountPerVlan = VtepCountPerVlan  # Number of VTEP devices per VLAN
        self._AutoSelectUDPSourcePort = AutoSelectUDPSourcePort  # Auto select UDP Source Port
        self._UDPSourcePortStart = UDPSourcePortStart  # UDP Source Port Start
        self._UDPSourcePortStep = UDPSourcePortStep  # UDP Source Port Step
        self._EnableUDPChecksum = EnableUDPChecksum  # Enable UDP Checksum
        self._SegmentsCountPerVtep = SegmentsCountPerVtep  # Segments per Vtep
        self._SegmentsCountPerBlock = SegmentsCountPerBlock  # Segments Count Per Block
        self._VNI = VNI  # VNI
        self._VNIStep = VNIStep  # VNI Step
        self._UseSameSegmentsAcrossVteps = UseSameSegmentsAcrossVteps  # Use Same Segments Across Vteps
        self._UseSameSegmentsAcrossPort = UseSameSegmentsAcrossPort  # Use Same Segments Across Port
        self._AddressMode = AddressMode  # Address Mode
        self._NumberofVMspersegment = NumberofVMspersegment  # Number of VMs per segment
        self._EnableVlan = EnableVlan  # Enable Vlan
        self._LearningMode = LearningMode  # Learning Mode
        self._MulticastType = MulticastType  # Multicast Type
        self._MulticastIPAddress = MulticastIPAddress  # Multicast IP Address
        self._MulticastIPAddressStep = MulticastIPAddressStep  # Multicast IP Address Step
        self._IGMPVersion = IGMPVersion  # IGMP Version
        self._PIMMode = PIMMode  # PIM Mode
        self._RPAddress = RPAddress  # RP Address
        self._BiDirHelloOptionSet = BiDirHelloOptionSet  # BiDir Hello Option Set
        self._EnableInterfaceCount = EnableInterfaceCount  # Enable Interface Count
        self._CountPerInterfaceBlcok = CountPerInterfaceBlcok  # Address Count
        self._StepperSegmentBlock = StepperSegmentBlock  # Step per Segment Block

        properties = kwargs.copy()
        if VtepCountPerVlan is not None:
            properties['VtepCountPerVlan'] = VtepCountPerVlan
        if AutoSelectUDPSourcePort is not None:
            properties['AutoSelectUDPSourcePort'] = AutoSelectUDPSourcePort
        if UDPSourcePortStart is not None:
            properties['UDPSourcePortStart'] = UDPSourcePortStart
        if UDPSourcePortStep is not None:
            properties['UDPSourcePortStep'] = UDPSourcePortStep
        if EnableUDPChecksum is not None:
            properties['EnableUDPChecksum'] = EnableUDPChecksum
        if SegmentsCountPerVtep is not None:
            properties['SegmentsCountPerVtep'] = SegmentsCountPerVtep
        if SegmentsCountPerBlock is not None:
            properties['SegmentsCountPerBlock'] = SegmentsCountPerBlock
        if VNI is not None:
            properties['VNI'] = VNI
        if VNIStep is not None:
            properties['VNIStep'] = VNIStep
        if UseSameSegmentsAcrossVteps is not None:
            properties['UseSameSegmentsAcrossVteps'] = UseSameSegmentsAcrossVteps
        if UseSameSegmentsAcrossPort is not None:
            properties['UseSameSegmentsAcrossPort'] = UseSameSegmentsAcrossPort
        if AddressMode is not None:
            properties['AddressMode'] = AddressMode
        if NumberofVMspersegment is not None:
            properties['NumberofVMspersegment'] = NumberofVMspersegment
        if EnableVlan is not None:
            properties['EnableVlan'] = EnableVlan
        if LearningMode is not None:
            properties['LearningMode'] = LearningMode
        if MulticastType is not None:
            properties['MulticastType'] = MulticastType
        if MulticastIPAddress is not None:
            properties['MulticastIPAddress'] = MulticastIPAddress
        if MulticastIPAddressStep is not None:
            properties['MulticastIPAddressStep'] = MulticastIPAddressStep
        if IGMPVersion is not None:
            properties['IGMPVersion'] = IGMPVersion
        if PIMMode is not None:
            properties['PIMMode'] = PIMMode
        if RPAddress is not None:
            properties['RPAddress'] = RPAddress
        if BiDirHelloOptionSet is not None:
            properties['BiDirHelloOptionSet'] = BiDirHelloOptionSet
        if EnableInterfaceCount is not None:
            properties['EnableInterfaceCount'] = EnableInterfaceCount
        if CountPerInterfaceBlcok is not None:
            properties['CountPerInterfaceBlcok'] = CountPerInterfaceBlcok
        if StepperSegmentBlock is not None:
            properties['StepperSegmentBlock'] = StepperSegmentBlock

        # call base class function, and it will send message to renix server to create a class.
        super(VxlanWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, VtepCountPerVlan=None, AutoSelectUDPSourcePort=None, UDPSourcePortStart=None, UDPSourcePortStep=None, EnableUDPChecksum=None, SegmentsCountPerVtep=None, SegmentsCountPerBlock=None, VNI=None, VNIStep=None, UseSameSegmentsAcrossVteps=None, UseSameSegmentsAcrossPort=None, AddressMode=None, NumberofVMspersegment=None, EnableVlan=None, LearningMode=None, MulticastType=None, MulticastIPAddress=None, MulticastIPAddressStep=None, IGMPVersion=None, PIMMode=None, RPAddress=None, BiDirHelloOptionSet=None, EnableInterfaceCount=None, CountPerInterfaceBlcok=None, StepperSegmentBlock=None, **kwargs):
        properties = kwargs.copy()
        if VtepCountPerVlan is not None:
            self._VtepCountPerVlan = VtepCountPerVlan
            properties['VtepCountPerVlan'] = VtepCountPerVlan
        if AutoSelectUDPSourcePort is not None:
            self._AutoSelectUDPSourcePort = AutoSelectUDPSourcePort
            properties['AutoSelectUDPSourcePort'] = AutoSelectUDPSourcePort
        if UDPSourcePortStart is not None:
            self._UDPSourcePortStart = UDPSourcePortStart
            properties['UDPSourcePortStart'] = UDPSourcePortStart
        if UDPSourcePortStep is not None:
            self._UDPSourcePortStep = UDPSourcePortStep
            properties['UDPSourcePortStep'] = UDPSourcePortStep
        if EnableUDPChecksum is not None:
            self._EnableUDPChecksum = EnableUDPChecksum
            properties['EnableUDPChecksum'] = EnableUDPChecksum
        if SegmentsCountPerVtep is not None:
            self._SegmentsCountPerVtep = SegmentsCountPerVtep
            properties['SegmentsCountPerVtep'] = SegmentsCountPerVtep
        if SegmentsCountPerBlock is not None:
            self._SegmentsCountPerBlock = SegmentsCountPerBlock
            properties['SegmentsCountPerBlock'] = SegmentsCountPerBlock
        if VNI is not None:
            self._VNI = VNI
            properties['VNI'] = VNI
        if VNIStep is not None:
            self._VNIStep = VNIStep
            properties['VNIStep'] = VNIStep
        if UseSameSegmentsAcrossVteps is not None:
            self._UseSameSegmentsAcrossVteps = UseSameSegmentsAcrossVteps
            properties['UseSameSegmentsAcrossVteps'] = UseSameSegmentsAcrossVteps
        if UseSameSegmentsAcrossPort is not None:
            self._UseSameSegmentsAcrossPort = UseSameSegmentsAcrossPort
            properties['UseSameSegmentsAcrossPort'] = UseSameSegmentsAcrossPort
        if AddressMode is not None:
            self._AddressMode = AddressMode
            properties['AddressMode'] = AddressMode
        if NumberofVMspersegment is not None:
            self._NumberofVMspersegment = NumberofVMspersegment
            properties['NumberofVMspersegment'] = NumberofVMspersegment
        if EnableVlan is not None:
            self._EnableVlan = EnableVlan
            properties['EnableVlan'] = EnableVlan
        if LearningMode is not None:
            self._LearningMode = LearningMode
            properties['LearningMode'] = LearningMode
        if MulticastType is not None:
            self._MulticastType = MulticastType
            properties['MulticastType'] = MulticastType
        if MulticastIPAddress is not None:
            self._MulticastIPAddress = MulticastIPAddress
            properties['MulticastIPAddress'] = MulticastIPAddress
        if MulticastIPAddressStep is not None:
            self._MulticastIPAddressStep = MulticastIPAddressStep
            properties['MulticastIPAddressStep'] = MulticastIPAddressStep
        if IGMPVersion is not None:
            self._IGMPVersion = IGMPVersion
            properties['IGMPVersion'] = IGMPVersion
        if PIMMode is not None:
            self._PIMMode = PIMMode
            properties['PIMMode'] = PIMMode
        if RPAddress is not None:
            self._RPAddress = RPAddress
            properties['RPAddress'] = RPAddress
        if BiDirHelloOptionSet is not None:
            self._BiDirHelloOptionSet = BiDirHelloOptionSet
            properties['BiDirHelloOptionSet'] = BiDirHelloOptionSet
        if EnableInterfaceCount is not None:
            self._EnableInterfaceCount = EnableInterfaceCount
            properties['EnableInterfaceCount'] = EnableInterfaceCount
        if CountPerInterfaceBlcok is not None:
            self._CountPerInterfaceBlcok = CountPerInterfaceBlcok
            properties['CountPerInterfaceBlcok'] = CountPerInterfaceBlcok
        if StepperSegmentBlock is not None:
            self._StepperSegmentBlock = StepperSegmentBlock
            properties['StepperSegmentBlock'] = StepperSegmentBlock

        super(VxlanWizardConfig, self).edit(**properties)

    @property
    def VtepCountPerVlan(self):
        """
        get the value of property _VtepCountPerVlan
        """
        if self.force_auto_sync:
            self.get('VtepCountPerVlan')
        return self._VtepCountPerVlan

    @property
    def AutoSelectUDPSourcePort(self):
        """
        get the value of property _AutoSelectUDPSourcePort
        """
        if self.force_auto_sync:
            self.get('AutoSelectUDPSourcePort')
        return self._AutoSelectUDPSourcePort

    @property
    def UDPSourcePortStart(self):
        """
        get the value of property _UDPSourcePortStart
        """
        if self.force_auto_sync:
            self.get('UDPSourcePortStart')
        return self._UDPSourcePortStart

    @property
    def UDPSourcePortStep(self):
        """
        get the value of property _UDPSourcePortStep
        """
        if self.force_auto_sync:
            self.get('UDPSourcePortStep')
        return self._UDPSourcePortStep

    @property
    def EnableUDPChecksum(self):
        """
        get the value of property _EnableUDPChecksum
        """
        if self.force_auto_sync:
            self.get('EnableUDPChecksum')
        return self._EnableUDPChecksum

    @property
    def SegmentsCountPerVtep(self):
        """
        get the value of property _SegmentsCountPerVtep
        """
        if self.force_auto_sync:
            self.get('SegmentsCountPerVtep')
        return self._SegmentsCountPerVtep

    @property
    def SegmentsCountPerBlock(self):
        """
        get the value of property _SegmentsCountPerBlock
        """
        if self.force_auto_sync:
            self.get('SegmentsCountPerBlock')
        return self._SegmentsCountPerBlock

    @property
    def VNI(self):
        """
        get the value of property _VNI
        """
        if self.force_auto_sync:
            self.get('VNI')
        return self._VNI

    @property
    def VNIStep(self):
        """
        get the value of property _VNIStep
        """
        if self.force_auto_sync:
            self.get('VNIStep')
        return self._VNIStep

    @property
    def UseSameSegmentsAcrossVteps(self):
        """
        get the value of property _UseSameSegmentsAcrossVteps
        """
        if self.force_auto_sync:
            self.get('UseSameSegmentsAcrossVteps')
        return self._UseSameSegmentsAcrossVteps

    @property
    def UseSameSegmentsAcrossPort(self):
        """
        get the value of property _UseSameSegmentsAcrossPort
        """
        if self.force_auto_sync:
            self.get('UseSameSegmentsAcrossPort')
        return self._UseSameSegmentsAcrossPort

    @property
    def AddressMode(self):
        """
        get the value of property _AddressMode
        """
        if self.force_auto_sync:
            self.get('AddressMode')
        return self._AddressMode

    @property
    def NumberofVMspersegment(self):
        """
        get the value of property _NumberofVMspersegment
        """
        if self.force_auto_sync:
            self.get('NumberofVMspersegment')
        return self._NumberofVMspersegment

    @property
    def EnableVlan(self):
        """
        get the value of property _EnableVlan
        """
        if self.force_auto_sync:
            self.get('EnableVlan')
        return self._EnableVlan

    @property
    def LearningMode(self):
        """
        get the value of property _LearningMode
        """
        if self.force_auto_sync:
            self.get('LearningMode')
        return self._LearningMode

    @property
    def MulticastType(self):
        """
        get the value of property _MulticastType
        """
        if self.force_auto_sync:
            self.get('MulticastType')
        return self._MulticastType

    @property
    def MulticastIPAddress(self):
        """
        get the value of property _MulticastIPAddress
        """
        if self.force_auto_sync:
            self.get('MulticastIPAddress')
        return self._MulticastIPAddress

    @property
    def MulticastIPAddressStep(self):
        """
        get the value of property _MulticastIPAddressStep
        """
        if self.force_auto_sync:
            self.get('MulticastIPAddressStep')
        return self._MulticastIPAddressStep

    @property
    def IGMPVersion(self):
        """
        get the value of property _IGMPVersion
        """
        if self.force_auto_sync:
            self.get('IGMPVersion')
        return self._IGMPVersion

    @property
    def PIMMode(self):
        """
        get the value of property _PIMMode
        """
        if self.force_auto_sync:
            self.get('PIMMode')
        return self._PIMMode

    @property
    def RPAddress(self):
        """
        get the value of property _RPAddress
        """
        if self.force_auto_sync:
            self.get('RPAddress')
        return self._RPAddress

    @property
    def BiDirHelloOptionSet(self):
        """
        get the value of property _BiDirHelloOptionSet
        """
        if self.force_auto_sync:
            self.get('BiDirHelloOptionSet')
        return self._BiDirHelloOptionSet

    @property
    def EnableInterfaceCount(self):
        """
        get the value of property _EnableInterfaceCount
        """
        if self.force_auto_sync:
            self.get('EnableInterfaceCount')
        return self._EnableInterfaceCount

    @property
    def CountPerInterfaceBlcok(self):
        """
        get the value of property _CountPerInterfaceBlcok
        """
        if self.force_auto_sync:
            self.get('CountPerInterfaceBlcok')
        return self._CountPerInterfaceBlcok

    @property
    def StepperSegmentBlock(self):
        """
        get the value of property _StepperSegmentBlock
        """
        if self.force_auto_sync:
            self.get('StepperSegmentBlock')
        return self._StepperSegmentBlock

    @VtepCountPerVlan.setter
    def VtepCountPerVlan(self, value):
        self._VtepCountPerVlan = value
        self.edit(VtepCountPerVlan=value)

    @AutoSelectUDPSourcePort.setter
    def AutoSelectUDPSourcePort(self, value):
        self._AutoSelectUDPSourcePort = value
        self.edit(AutoSelectUDPSourcePort=value)

    @UDPSourcePortStart.setter
    def UDPSourcePortStart(self, value):
        self._UDPSourcePortStart = value
        self.edit(UDPSourcePortStart=value)

    @UDPSourcePortStep.setter
    def UDPSourcePortStep(self, value):
        self._UDPSourcePortStep = value
        self.edit(UDPSourcePortStep=value)

    @EnableUDPChecksum.setter
    def EnableUDPChecksum(self, value):
        self._EnableUDPChecksum = value
        self.edit(EnableUDPChecksum=value)

    @SegmentsCountPerVtep.setter
    def SegmentsCountPerVtep(self, value):
        self._SegmentsCountPerVtep = value
        self.edit(SegmentsCountPerVtep=value)

    @SegmentsCountPerBlock.setter
    def SegmentsCountPerBlock(self, value):
        self._SegmentsCountPerBlock = value
        self.edit(SegmentsCountPerBlock=value)

    @VNI.setter
    def VNI(self, value):
        self._VNI = value
        self.edit(VNI=value)

    @VNIStep.setter
    def VNIStep(self, value):
        self._VNIStep = value
        self.edit(VNIStep=value)

    @UseSameSegmentsAcrossVteps.setter
    def UseSameSegmentsAcrossVteps(self, value):
        self._UseSameSegmentsAcrossVteps = value
        self.edit(UseSameSegmentsAcrossVteps=value)

    @UseSameSegmentsAcrossPort.setter
    def UseSameSegmentsAcrossPort(self, value):
        self._UseSameSegmentsAcrossPort = value
        self.edit(UseSameSegmentsAcrossPort=value)

    @AddressMode.setter
    def AddressMode(self, value):
        self._AddressMode = value
        self.edit(AddressMode=value)

    @NumberofVMspersegment.setter
    def NumberofVMspersegment(self, value):
        self._NumberofVMspersegment = value
        self.edit(NumberofVMspersegment=value)

    @EnableVlan.setter
    def EnableVlan(self, value):
        self._EnableVlan = value
        self.edit(EnableVlan=value)

    @LearningMode.setter
    def LearningMode(self, value):
        self._LearningMode = value
        self.edit(LearningMode=value)

    @MulticastType.setter
    def MulticastType(self, value):
        self._MulticastType = value
        self.edit(MulticastType=value)

    @MulticastIPAddress.setter
    def MulticastIPAddress(self, value):
        self._MulticastIPAddress = value
        self.edit(MulticastIPAddress=value)

    @MulticastIPAddressStep.setter
    def MulticastIPAddressStep(self, value):
        self._MulticastIPAddressStep = value
        self.edit(MulticastIPAddressStep=value)

    @IGMPVersion.setter
    def IGMPVersion(self, value):
        self._IGMPVersion = value
        self.edit(IGMPVersion=value)

    @PIMMode.setter
    def PIMMode(self, value):
        self._PIMMode = value
        self.edit(PIMMode=value)

    @RPAddress.setter
    def RPAddress(self, value):
        self._RPAddress = value
        self.edit(RPAddress=value)

    @BiDirHelloOptionSet.setter
    def BiDirHelloOptionSet(self, value):
        self._BiDirHelloOptionSet = value
        self.edit(BiDirHelloOptionSet=value)

    @EnableInterfaceCount.setter
    def EnableInterfaceCount(self, value):
        self._EnableInterfaceCount = value
        self.edit(EnableInterfaceCount=value)

    @CountPerInterfaceBlcok.setter
    def CountPerInterfaceBlcok(self, value):
        self._CountPerInterfaceBlcok = value
        self.edit(CountPerInterfaceBlcok=value)

    @StepperSegmentBlock.setter
    def StepperSegmentBlock(self, value):
        self._StepperSegmentBlock = value
        self.edit(StepperSegmentBlock=value)

    def _set_vtepcountpervlan_with_str(self, value):
        try:
            self._VtepCountPerVlan = int(value)
        except ValueError:
            self._VtepCountPerVlan = hex(int(value, 16))

    def _set_autoselectudpsourceport_with_str(self, value):
        self._AutoSelectUDPSourcePort = (value == 'True')

    def _set_udpsourceportstart_with_str(self, value):
        try:
            self._UDPSourcePortStart = int(value)
        except ValueError:
            self._UDPSourcePortStart = hex(int(value, 16))

    def _set_udpsourceportstep_with_str(self, value):
        try:
            self._UDPSourcePortStep = int(value)
        except ValueError:
            self._UDPSourcePortStep = hex(int(value, 16))

    def _set_enableudpchecksum_with_str(self, value):
        self._EnableUDPChecksum = (value == 'True')

    def _set_segmentscountpervtep_with_str(self, value):
        try:
            self._SegmentsCountPerVtep = int(value)
        except ValueError:
            self._SegmentsCountPerVtep = hex(int(value, 16))

    def _set_segmentscountperblock_with_str(self, value):
        try:
            self._SegmentsCountPerBlock = int(value)
        except ValueError:
            self._SegmentsCountPerBlock = hex(int(value, 16))

    def _set_vni_with_str(self, value):
        try:
            self._VNI = int(value)
        except ValueError:
            self._VNI = hex(int(value, 16))

    def _set_vnistep_with_str(self, value):
        try:
            self._VNIStep = int(value)
        except ValueError:
            self._VNIStep = hex(int(value, 16))

    def _set_usesamesegmentsacrossvteps_with_str(self, value):
        self._UseSameSegmentsAcrossVteps = (value == 'True')

    def _set_usesamesegmentsacrossport_with_str(self, value):
        self._UseSameSegmentsAcrossPort = (value == 'True')

    def _set_addressmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._AddressMode = EnumVxlanAddressMode.%s' % value[:seperate])

    def _set_numberofvmspersegment_with_str(self, value):
        try:
            self._NumberofVMspersegment = int(value)
        except ValueError:
            self._NumberofVMspersegment = hex(int(value, 16))

    def _set_enablevlan_with_str(self, value):
        self._EnableVlan = (value == 'True')

    def _set_learningmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._LearningMode = EnumCommunicationType.%s' % value[:seperate])

    def _set_multicasttype_with_str(self, value):
        seperate = value.find(':')
        exec('self._MulticastType = EnumMulticastType.%s' % value[:seperate])

    def _set_multicastipaddress_with_str(self, value):
        self._MulticastIPAddress = value

    def _set_multicastipaddressstep_with_str(self, value):
        self._MulticastIPAddressStep = value

    def _set_igmpversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._IGMPVersion = EnumIGMPVersion.%s' % value[:seperate])

    def _set_pimmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._PIMMode = EnumSessionMode.%s' % value[:seperate])

    def _set_rpaddress_with_str(self, value):
        self._RPAddress = value

    def _set_bidirhellooptionset_with_str(self, value):
        self._BiDirHelloOptionSet = (value == 'True')

    def _set_enableinterfacecount_with_str(self, value):
        self._EnableInterfaceCount = (value == 'True')

    def _set_countperinterfaceblcok_with_str(self, value):
        try:
            self._CountPerInterfaceBlcok = int(value)
        except ValueError:
            self._CountPerInterfaceBlcok = hex(int(value, 16))

    def _set_steppersegmentblock_with_str(self, value):
        self._StepperSegmentBlock = value

