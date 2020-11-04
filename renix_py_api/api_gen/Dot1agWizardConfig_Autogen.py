"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .WizardConfigBase_Autogen import WizardConfigBase


@rom_manager.rom
class Dot1agWizardConfig(WizardConfigBase):
    def __init__(self, MaIdFormat=None, MaIdNumber=None, MaName=None, MaStep=None, MdIdLevelSet=None, MdIdFormat=None, MdIdStart=None, MdName=None, MepNumberPerMa=None, MepIdStart=None, MepIdStep=None, MacAddressStart=None, MacAddressStep=None, C_VidStart=None, C_VidStep=None, S_VidStart=None, S_VidStep=None, S_VlanPriority=None, C_VlanPriority=None, VlanType=None, C_Vlan_Tpid=None, S_Vlan_Tpid=None, CCPriority=None, LBPriority=None, LTPriority=None, **kwargs):
        self._MaIdFormat = MaIdFormat  # MA ID Format
        self._MaIdNumber = MaIdNumber  # ID Number
        self._MaName = MaName  # MA Name
        self._MaStep = MaStep  # MD Step
        self._MdIdLevelSet = MdIdLevelSet  # MD Levels
        self._MdIdFormat = MdIdFormat  # MD ID Format
        self._MdIdStart = MdIdStart  # ID Number
        self._MdName = MdName  # MD Name
        self._MepNumberPerMa = MepNumberPerMa  # Number of MEP per MA
        self._MepIdStart = MepIdStart  # MEP ID Start
        self._MepIdStep = MepIdStep  # MEP ID Step
        self._MacAddressStart = MacAddressStart  # Start MAC
        self._MacAddressStep = MacAddressStep  # MAC Step
        self._C_VidStart = C_VidStart  # C-VID Start
        self._C_VidStep = C_VidStep  # C-VID Step
        self._S_VidStart = S_VidStart  # S-VID Start
        self._S_VidStep = S_VidStep  # S-VID Step
        self._S_VlanPriority = S_VlanPriority  # S-VLAN Priority
        self._C_VlanPriority = C_VlanPriority  # C-VLAN Priority
        self._VlanType = VlanType  # VLAN Type
        self._C_Vlan_Tpid = C_Vlan_Tpid  # C-VLAN  TPID
        self._S_Vlan_Tpid = S_Vlan_Tpid  # S-VLAN  TPID
        self._CCPriority = CCPriority  # CC Priority
        self._LBPriority = LBPriority  # LB Priority
        self._LTPriority = LTPriority  # LT Priority

        properties = kwargs.copy()
        if MaIdFormat is not None:
            properties['MaIdFormat'] = MaIdFormat
        if MaIdNumber is not None:
            properties['MaIdNumber'] = MaIdNumber
        if MaName is not None:
            properties['MaName'] = MaName
        if MaStep is not None:
            properties['MaStep'] = MaStep
        if MdIdLevelSet is not None:
            properties['MdIdLevelSet'] = MdIdLevelSet
        if MdIdFormat is not None:
            properties['MdIdFormat'] = MdIdFormat
        if MdIdStart is not None:
            properties['MdIdStart'] = MdIdStart
        if MdName is not None:
            properties['MdName'] = MdName
        if MepNumberPerMa is not None:
            properties['MepNumberPerMa'] = MepNumberPerMa
        if MepIdStart is not None:
            properties['MepIdStart'] = MepIdStart
        if MepIdStep is not None:
            properties['MepIdStep'] = MepIdStep
        if MacAddressStart is not None:
            properties['MacAddressStart'] = MacAddressStart
        if MacAddressStep is not None:
            properties['MacAddressStep'] = MacAddressStep
        if C_VidStart is not None:
            properties['C_VidStart'] = C_VidStart
        if C_VidStep is not None:
            properties['C_VidStep'] = C_VidStep
        if S_VidStart is not None:
            properties['S_VidStart'] = S_VidStart
        if S_VidStep is not None:
            properties['S_VidStep'] = S_VidStep
        if S_VlanPriority is not None:
            properties['S_VlanPriority'] = S_VlanPriority
        if C_VlanPriority is not None:
            properties['C_VlanPriority'] = C_VlanPriority
        if VlanType is not None:
            properties['VlanType'] = VlanType
        if C_Vlan_Tpid is not None:
            properties['C_Vlan_Tpid'] = C_Vlan_Tpid
        if S_Vlan_Tpid is not None:
            properties['S_Vlan_Tpid'] = S_Vlan_Tpid
        if CCPriority is not None:
            properties['CCPriority'] = CCPriority
        if LBPriority is not None:
            properties['LBPriority'] = LBPriority
        if LTPriority is not None:
            properties['LTPriority'] = LTPriority

        # call base class function, and it will send message to renix server to create a class.
        super(Dot1agWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, MaIdFormat=None, MaIdNumber=None, MaName=None, MaStep=None, MdIdLevelSet=None, MdIdFormat=None, MdIdStart=None, MdName=None, MepNumberPerMa=None, MepIdStart=None, MepIdStep=None, MacAddressStart=None, MacAddressStep=None, C_VidStart=None, C_VidStep=None, S_VidStart=None, S_VidStep=None, S_VlanPriority=None, C_VlanPriority=None, VlanType=None, C_Vlan_Tpid=None, S_Vlan_Tpid=None, CCPriority=None, LBPriority=None, LTPriority=None, **kwargs):
        properties = kwargs.copy()
        if MaIdFormat is not None:
            self._MaIdFormat = MaIdFormat
            properties['MaIdFormat'] = MaIdFormat
        if MaIdNumber is not None:
            self._MaIdNumber = MaIdNumber
            properties['MaIdNumber'] = MaIdNumber
        if MaName is not None:
            self._MaName = MaName
            properties['MaName'] = MaName
        if MaStep is not None:
            self._MaStep = MaStep
            properties['MaStep'] = MaStep
        if MdIdLevelSet is not None:
            self._MdIdLevelSet = MdIdLevelSet
            properties['MdIdLevelSet'] = MdIdLevelSet
        if MdIdFormat is not None:
            self._MdIdFormat = MdIdFormat
            properties['MdIdFormat'] = MdIdFormat
        if MdIdStart is not None:
            self._MdIdStart = MdIdStart
            properties['MdIdStart'] = MdIdStart
        if MdName is not None:
            self._MdName = MdName
            properties['MdName'] = MdName
        if MepNumberPerMa is not None:
            self._MepNumberPerMa = MepNumberPerMa
            properties['MepNumberPerMa'] = MepNumberPerMa
        if MepIdStart is not None:
            self._MepIdStart = MepIdStart
            properties['MepIdStart'] = MepIdStart
        if MepIdStep is not None:
            self._MepIdStep = MepIdStep
            properties['MepIdStep'] = MepIdStep
        if MacAddressStart is not None:
            self._MacAddressStart = MacAddressStart
            properties['MacAddressStart'] = MacAddressStart
        if MacAddressStep is not None:
            self._MacAddressStep = MacAddressStep
            properties['MacAddressStep'] = MacAddressStep
        if C_VidStart is not None:
            self._C_VidStart = C_VidStart
            properties['C_VidStart'] = C_VidStart
        if C_VidStep is not None:
            self._C_VidStep = C_VidStep
            properties['C_VidStep'] = C_VidStep
        if S_VidStart is not None:
            self._S_VidStart = S_VidStart
            properties['S_VidStart'] = S_VidStart
        if S_VidStep is not None:
            self._S_VidStep = S_VidStep
            properties['S_VidStep'] = S_VidStep
        if S_VlanPriority is not None:
            self._S_VlanPriority = S_VlanPriority
            properties['S_VlanPriority'] = S_VlanPriority
        if C_VlanPriority is not None:
            self._C_VlanPriority = C_VlanPriority
            properties['C_VlanPriority'] = C_VlanPriority
        if VlanType is not None:
            self._VlanType = VlanType
            properties['VlanType'] = VlanType
        if C_Vlan_Tpid is not None:
            self._C_Vlan_Tpid = C_Vlan_Tpid
            properties['C_Vlan_Tpid'] = C_Vlan_Tpid
        if S_Vlan_Tpid is not None:
            self._S_Vlan_Tpid = S_Vlan_Tpid
            properties['S_Vlan_Tpid'] = S_Vlan_Tpid
        if CCPriority is not None:
            self._CCPriority = CCPriority
            properties['CCPriority'] = CCPriority
        if LBPriority is not None:
            self._LBPriority = LBPriority
            properties['LBPriority'] = LBPriority
        if LTPriority is not None:
            self._LTPriority = LTPriority
            properties['LTPriority'] = LTPriority

        super(Dot1agWizardConfig, self).edit(**properties)

    @property
    def MaIdFormat(self):
        """
        get the value of property _MaIdFormat
        """
        if self.force_auto_sync:
            self.get('MaIdFormat')
        return self._MaIdFormat

    @property
    def MaIdNumber(self):
        """
        get the value of property _MaIdNumber
        """
        if self.force_auto_sync:
            self.get('MaIdNumber')
        return self._MaIdNumber

    @property
    def MaName(self):
        """
        get the value of property _MaName
        """
        if self.force_auto_sync:
            self.get('MaName')
        return self._MaName

    @property
    def MaStep(self):
        """
        get the value of property _MaStep
        """
        if self.force_auto_sync:
            self.get('MaStep')
        return self._MaStep

    @property
    def MdIdLevelSet(self):
        """
        get the value of property _MdIdLevelSet
        """
        if self.force_auto_sync:
            self.get('MdIdLevelSet')
        return self._MdIdLevelSet

    @property
    def MdIdFormat(self):
        """
        get the value of property _MdIdFormat
        """
        if self.force_auto_sync:
            self.get('MdIdFormat')
        return self._MdIdFormat

    @property
    def MdIdStart(self):
        """
        get the value of property _MdIdStart
        """
        if self.force_auto_sync:
            self.get('MdIdStart')
        return self._MdIdStart

    @property
    def MdName(self):
        """
        get the value of property _MdName
        """
        if self.force_auto_sync:
            self.get('MdName')
        return self._MdName

    @property
    def MepNumberPerMa(self):
        """
        get the value of property _MepNumberPerMa
        """
        if self.force_auto_sync:
            self.get('MepNumberPerMa')
        return self._MepNumberPerMa

    @property
    def MepIdStart(self):
        """
        get the value of property _MepIdStart
        """
        if self.force_auto_sync:
            self.get('MepIdStart')
        return self._MepIdStart

    @property
    def MepIdStep(self):
        """
        get the value of property _MepIdStep
        """
        if self.force_auto_sync:
            self.get('MepIdStep')
        return self._MepIdStep

    @property
    def MacAddressStart(self):
        """
        get the value of property _MacAddressStart
        """
        if self.force_auto_sync:
            self.get('MacAddressStart')
        return self._MacAddressStart

    @property
    def MacAddressStep(self):
        """
        get the value of property _MacAddressStep
        """
        if self.force_auto_sync:
            self.get('MacAddressStep')
        return self._MacAddressStep

    @property
    def C_VidStart(self):
        """
        get the value of property _C_VidStart
        """
        if self.force_auto_sync:
            self.get('C_VidStart')
        return self._C_VidStart

    @property
    def C_VidStep(self):
        """
        get the value of property _C_VidStep
        """
        if self.force_auto_sync:
            self.get('C_VidStep')
        return self._C_VidStep

    @property
    def S_VidStart(self):
        """
        get the value of property _S_VidStart
        """
        if self.force_auto_sync:
            self.get('S_VidStart')
        return self._S_VidStart

    @property
    def S_VidStep(self):
        """
        get the value of property _S_VidStep
        """
        if self.force_auto_sync:
            self.get('S_VidStep')
        return self._S_VidStep

    @property
    def S_VlanPriority(self):
        """
        get the value of property _S_VlanPriority
        """
        if self.force_auto_sync:
            self.get('S_VlanPriority')
        return self._S_VlanPriority

    @property
    def C_VlanPriority(self):
        """
        get the value of property _C_VlanPriority
        """
        if self.force_auto_sync:
            self.get('C_VlanPriority')
        return self._C_VlanPriority

    @property
    def VlanType(self):
        """
        get the value of property _VlanType
        """
        if self.force_auto_sync:
            self.get('VlanType')
        return self._VlanType

    @property
    def C_Vlan_Tpid(self):
        """
        get the value of property _C_Vlan_Tpid
        """
        if self.force_auto_sync:
            self.get('C_Vlan_Tpid')
        return self._C_Vlan_Tpid

    @property
    def S_Vlan_Tpid(self):
        """
        get the value of property _S_Vlan_Tpid
        """
        if self.force_auto_sync:
            self.get('S_Vlan_Tpid')
        return self._S_Vlan_Tpid

    @property
    def CCPriority(self):
        """
        get the value of property _CCPriority
        """
        if self.force_auto_sync:
            self.get('CCPriority')
        return self._CCPriority

    @property
    def LBPriority(self):
        """
        get the value of property _LBPriority
        """
        if self.force_auto_sync:
            self.get('LBPriority')
        return self._LBPriority

    @property
    def LTPriority(self):
        """
        get the value of property _LTPriority
        """
        if self.force_auto_sync:
            self.get('LTPriority')
        return self._LTPriority

    @MaIdFormat.setter
    def MaIdFormat(self, value):
        self._MaIdFormat = value
        self.edit(MaIdFormat=value)

    @MaIdNumber.setter
    def MaIdNumber(self, value):
        self._MaIdNumber = value
        self.edit(MaIdNumber=value)

    @MaName.setter
    def MaName(self, value):
        self._MaName = value
        self.edit(MaName=value)

    @MaStep.setter
    def MaStep(self, value):
        self._MaStep = value
        self.edit(MaStep=value)

    @MdIdLevelSet.setter
    def MdIdLevelSet(self, value):
        self._MdIdLevelSet = value
        self.edit(MdIdLevelSet=value)

    @MdIdFormat.setter
    def MdIdFormat(self, value):
        self._MdIdFormat = value
        self.edit(MdIdFormat=value)

    @MdIdStart.setter
    def MdIdStart(self, value):
        self._MdIdStart = value
        self.edit(MdIdStart=value)

    @MdName.setter
    def MdName(self, value):
        self._MdName = value
        self.edit(MdName=value)

    @MepNumberPerMa.setter
    def MepNumberPerMa(self, value):
        self._MepNumberPerMa = value
        self.edit(MepNumberPerMa=value)

    @MepIdStart.setter
    def MepIdStart(self, value):
        self._MepIdStart = value
        self.edit(MepIdStart=value)

    @MepIdStep.setter
    def MepIdStep(self, value):
        self._MepIdStep = value
        self.edit(MepIdStep=value)

    @MacAddressStart.setter
    def MacAddressStart(self, value):
        self._MacAddressStart = value
        self.edit(MacAddressStart=value)

    @MacAddressStep.setter
    def MacAddressStep(self, value):
        self._MacAddressStep = value
        self.edit(MacAddressStep=value)

    @C_VidStart.setter
    def C_VidStart(self, value):
        self._C_VidStart = value
        self.edit(C_VidStart=value)

    @C_VidStep.setter
    def C_VidStep(self, value):
        self._C_VidStep = value
        self.edit(C_VidStep=value)

    @S_VidStart.setter
    def S_VidStart(self, value):
        self._S_VidStart = value
        self.edit(S_VidStart=value)

    @S_VidStep.setter
    def S_VidStep(self, value):
        self._S_VidStep = value
        self.edit(S_VidStep=value)

    @S_VlanPriority.setter
    def S_VlanPriority(self, value):
        self._S_VlanPriority = value
        self.edit(S_VlanPriority=value)

    @C_VlanPriority.setter
    def C_VlanPriority(self, value):
        self._C_VlanPriority = value
        self.edit(C_VlanPriority=value)

    @VlanType.setter
    def VlanType(self, value):
        self._VlanType = value
        self.edit(VlanType=value)

    @C_Vlan_Tpid.setter
    def C_Vlan_Tpid(self, value):
        self._C_Vlan_Tpid = value
        self.edit(C_Vlan_Tpid=value)

    @S_Vlan_Tpid.setter
    def S_Vlan_Tpid(self, value):
        self._S_Vlan_Tpid = value
        self.edit(S_Vlan_Tpid=value)

    @CCPriority.setter
    def CCPriority(self, value):
        self._CCPriority = value
        self.edit(CCPriority=value)

    @LBPriority.setter
    def LBPriority(self, value):
        self._LBPriority = value
        self.edit(LBPriority=value)

    @LTPriority.setter
    def LTPriority(self, value):
        self._LTPriority = value
        self.edit(LTPriority=value)

    def _set_maidformat_with_str(self, value):
        seperate = value.find(':')
        exec('self._MaIdFormat = EnumMaIdFormat.%s' % value[:seperate])

    def _set_maidnumber_with_str(self, value):
        try:
            self._MaIdNumber = int(value)
        except ValueError:
            self._MaIdNumber = hex(int(value, 16))

    def _set_maname_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MaName = tmp_value.split()

    def _set_mastep_with_str(self, value):
        try:
            self._MaStep = int(value)
        except ValueError:
            self._MaStep = hex(int(value, 16))

    def _set_mdidlevelset_with_str(self, value):
        self._MdIdLevelSet = value

    def _set_mdidformat_with_str(self, value):
        seperate = value.find(':')
        exec('self._MdIdFormat = EnumMdIdFormat.%s' % value[:seperate])

    def _set_mdidstart_with_str(self, value):
        try:
            self._MdIdStart = int(value)
        except ValueError:
            self._MdIdStart = hex(int(value, 16))

    def _set_mdname_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MdName = tmp_value.split()

    def _set_mepnumberperma_with_str(self, value):
        try:
            self._MepNumberPerMa = int(value)
        except ValueError:
            self._MepNumberPerMa = hex(int(value, 16))

    def _set_mepidstart_with_str(self, value):
        try:
            self._MepIdStart = int(value)
        except ValueError:
            self._MepIdStart = hex(int(value, 16))

    def _set_mepidstep_with_str(self, value):
        try:
            self._MepIdStep = int(value)
        except ValueError:
            self._MepIdStep = hex(int(value, 16))

    def _set_macaddressstart_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MacAddressStart = tmp_value.split()

    def _set_macaddressstep_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MacAddressStep = tmp_value.split()

    def _set_c_vidstart_with_str(self, value):
        try:
            self._C_VidStart = int(value)
        except ValueError:
            self._C_VidStart = hex(int(value, 16))

    def _set_c_vidstep_with_str(self, value):
        try:
            self._C_VidStep = int(value)
        except ValueError:
            self._C_VidStep = hex(int(value, 16))

    def _set_s_vidstart_with_str(self, value):
        try:
            self._S_VidStart = int(value)
        except ValueError:
            self._S_VidStart = hex(int(value, 16))

    def _set_s_vidstep_with_str(self, value):
        try:
            self._S_VidStep = int(value)
        except ValueError:
            self._S_VidStep = hex(int(value, 16))

    def _set_s_vlanpriority_with_str(self, value):
        try:
            self._S_VlanPriority = int(value)
        except ValueError:
            self._S_VlanPriority = hex(int(value, 16))

    def _set_c_vlanpriority_with_str(self, value):
        try:
            self._C_VlanPriority = int(value)
        except ValueError:
            self._C_VlanPriority = hex(int(value, 16))

    def _set_vlantype_with_str(self, value):
        seperate = value.find(':')
        exec('self._VlanType = EnumVlanType.%s' % value[:seperate])

    def _set_c_vlan_tpid_with_str(self, value):
        seperate = value.find(':')
        exec('self._C_Vlan_Tpid = EnumEthType.%s' % value[:seperate])

    def _set_s_vlan_tpid_with_str(self, value):
        seperate = value.find(':')
        exec('self._S_Vlan_Tpid = EnumEthType.%s' % value[:seperate])

    def _set_ccpriority_with_str(self, value):
        try:
            self._CCPriority = int(value)
        except ValueError:
            self._CCPriority = hex(int(value, 16))

    def _set_lbpriority_with_str(self, value):
        try:
            self._LBPriority = int(value)
        except ValueError:
            self._LBPriority = hex(int(value, 16))

    def _set_ltpriority_with_str(self, value):
        try:
            self._LTPriority = int(value)
        except ValueError:
            self._LTPriority = hex(int(value, 16))

