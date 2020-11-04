"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .PimBaseGroupConfig_Autogen import PimBaseGroupConfig


@rom_manager.rom
class PimIpv6GroupConfig(PimBaseGroupConfig):
    def __init__(self, GroupType=None, GroupAddr=None, GroupCount=None, GroupModifierStep=None, GroupModifierBit=None, RpAddr=None, JoinSrcAddr=None, JoinMaskLen=None, PruneSrcAddr=None, PruneMaskLen=None, **kwargs):
        self._GroupCheck = False  # Checked, not editable
        self._GroupType = GroupType  # Group Type
        self._GroupAddr = GroupAddr  # Multicast Group Address
        self._GroupCount = GroupCount  # Count
        self._GroupModifierStep = GroupModifierStep  # Modifier Step
        self._GroupModifierBit = GroupModifierBit  # Modifier Bit
        self._RpAddr = RpAddr  # RP Address
        self._JoinSrcAddr = JoinSrcAddr  # Join Source Address
        self._JoinMaskLen = JoinMaskLen  # Join Mask Length
        self._PruneSrcAddr = PruneSrcAddr  # Prune Source Address
        self._PruneMaskLen = PruneMaskLen  # Prune Mask Length

        properties = kwargs.copy()
        if GroupType is not None:
            properties['GroupType'] = GroupType
        if GroupAddr is not None:
            properties['GroupAddr'] = GroupAddr
        if GroupCount is not None:
            properties['GroupCount'] = GroupCount
        if GroupModifierStep is not None:
            properties['GroupModifierStep'] = GroupModifierStep
        if GroupModifierBit is not None:
            properties['GroupModifierBit'] = GroupModifierBit
        if RpAddr is not None:
            properties['RpAddr'] = RpAddr
        if JoinSrcAddr is not None:
            properties['JoinSrcAddr'] = JoinSrcAddr
        if JoinMaskLen is not None:
            properties['JoinMaskLen'] = JoinMaskLen
        if PruneSrcAddr is not None:
            properties['PruneSrcAddr'] = PruneSrcAddr
        if PruneMaskLen is not None:
            properties['PruneMaskLen'] = PruneMaskLen

        # call base class function, and it will send message to renix server to create a class.
        super(PimIpv6GroupConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, GroupType=None, GroupAddr=None, GroupCount=None, GroupModifierStep=None, GroupModifierBit=None, RpAddr=None, JoinSrcAddr=None, JoinMaskLen=None, PruneSrcAddr=None, PruneMaskLen=None, **kwargs):
        properties = kwargs.copy()
        if GroupType is not None:
            self._GroupType = GroupType
            properties['GroupType'] = GroupType
        if GroupAddr is not None:
            self._GroupAddr = GroupAddr
            properties['GroupAddr'] = GroupAddr
        if GroupCount is not None:
            self._GroupCount = GroupCount
            properties['GroupCount'] = GroupCount
        if GroupModifierStep is not None:
            self._GroupModifierStep = GroupModifierStep
            properties['GroupModifierStep'] = GroupModifierStep
        if GroupModifierBit is not None:
            self._GroupModifierBit = GroupModifierBit
            properties['GroupModifierBit'] = GroupModifierBit
        if RpAddr is not None:
            self._RpAddr = RpAddr
            properties['RpAddr'] = RpAddr
        if JoinSrcAddr is not None:
            self._JoinSrcAddr = JoinSrcAddr
            properties['JoinSrcAddr'] = JoinSrcAddr
        if JoinMaskLen is not None:
            self._JoinMaskLen = JoinMaskLen
            properties['JoinMaskLen'] = JoinMaskLen
        if PruneSrcAddr is not None:
            self._PruneSrcAddr = PruneSrcAddr
            properties['PruneSrcAddr'] = PruneSrcAddr
        if PruneMaskLen is not None:
            self._PruneMaskLen = PruneMaskLen
            properties['PruneMaskLen'] = PruneMaskLen

        super(PimIpv6GroupConfig, self).edit(**properties)

    @property
    def GroupCheck(self):
        """
        get the value of property _GroupCheck
        """
        if self.force_auto_sync:
            self.get('GroupCheck')
        return self._GroupCheck

    @property
    def GroupType(self):
        """
        get the value of property _GroupType
        """
        if self.force_auto_sync:
            self.get('GroupType')
        return self._GroupType

    @property
    def GroupAddr(self):
        """
        get the value of property _GroupAddr
        """
        if self.force_auto_sync:
            self.get('GroupAddr')
        return self._GroupAddr

    @property
    def GroupCount(self):
        """
        get the value of property _GroupCount
        """
        if self.force_auto_sync:
            self.get('GroupCount')
        return self._GroupCount

    @property
    def GroupModifierStep(self):
        """
        get the value of property _GroupModifierStep
        """
        if self.force_auto_sync:
            self.get('GroupModifierStep')
        return self._GroupModifierStep

    @property
    def GroupModifierBit(self):
        """
        get the value of property _GroupModifierBit
        """
        if self.force_auto_sync:
            self.get('GroupModifierBit')
        return self._GroupModifierBit

    @property
    def RpAddr(self):
        """
        get the value of property _RpAddr
        """
        if self.force_auto_sync:
            self.get('RpAddr')
        return self._RpAddr

    @property
    def JoinSrcAddr(self):
        """
        get the value of property _JoinSrcAddr
        """
        if self.force_auto_sync:
            self.get('JoinSrcAddr')
        return self._JoinSrcAddr

    @property
    def JoinMaskLen(self):
        """
        get the value of property _JoinMaskLen
        """
        if self.force_auto_sync:
            self.get('JoinMaskLen')
        return self._JoinMaskLen

    @property
    def PruneSrcAddr(self):
        """
        get the value of property _PruneSrcAddr
        """
        if self.force_auto_sync:
            self.get('PruneSrcAddr')
        return self._PruneSrcAddr

    @property
    def PruneMaskLen(self):
        """
        get the value of property _PruneMaskLen
        """
        if self.force_auto_sync:
            self.get('PruneMaskLen')
        return self._PruneMaskLen

    @GroupType.setter
    def GroupType(self, value):
        self._GroupType = value
        self.edit(GroupType=value)

    @GroupAddr.setter
    def GroupAddr(self, value):
        self._GroupAddr = value
        self.edit(GroupAddr=value)

    @GroupCount.setter
    def GroupCount(self, value):
        self._GroupCount = value
        self.edit(GroupCount=value)

    @GroupModifierStep.setter
    def GroupModifierStep(self, value):
        self._GroupModifierStep = value
        self.edit(GroupModifierStep=value)

    @GroupModifierBit.setter
    def GroupModifierBit(self, value):
        self._GroupModifierBit = value
        self.edit(GroupModifierBit=value)

    @RpAddr.setter
    def RpAddr(self, value):
        self._RpAddr = value
        self.edit(RpAddr=value)

    @JoinSrcAddr.setter
    def JoinSrcAddr(self, value):
        self._JoinSrcAddr = value
        self.edit(JoinSrcAddr=value)

    @JoinMaskLen.setter
    def JoinMaskLen(self, value):
        self._JoinMaskLen = value
        self.edit(JoinMaskLen=value)

    @PruneSrcAddr.setter
    def PruneSrcAddr(self, value):
        self._PruneSrcAddr = value
        self.edit(PruneSrcAddr=value)

    @PruneMaskLen.setter
    def PruneMaskLen(self, value):
        self._PruneMaskLen = value
        self.edit(PruneMaskLen=value)

    def _set_groupcheck_with_str(self, value):
        self._GroupCheck = (value == 'True')

    def _set_grouptype_with_str(self, value):
        seperate = value.find(':')
        exec('self._GroupType = EnumGroupType.%s' % value[:seperate])

    def _set_groupaddr_with_str(self, value):
        self._GroupAddr = value

    def _set_groupcount_with_str(self, value):
        try:
            self._GroupCount = int(value)
        except ValueError:
            self._GroupCount = hex(int(value, 16))

    def _set_groupmodifierstep_with_str(self, value):
        try:
            self._GroupModifierStep = int(value)
        except ValueError:
            self._GroupModifierStep = hex(int(value, 16))

    def _set_groupmodifierbit_with_str(self, value):
        try:
            self._GroupModifierBit = int(value)
        except ValueError:
            self._GroupModifierBit = hex(int(value, 16))

    def _set_rpaddr_with_str(self, value):
        self._RpAddr = value

    def _set_joinsrcaddr_with_str(self, value):
        self._JoinSrcAddr = value

    def _set_joinmasklen_with_str(self, value):
        try:
            self._JoinMaskLen = int(value)
        except ValueError:
            self._JoinMaskLen = hex(int(value, 16))

    def _set_prunesrcaddr_with_str(self, value):
        self._PruneSrcAddr = value

    def _set_prunemasklen_with_str(self, value):
        try:
            self._PruneMaskLen = int(value)
        except ValueError:
            self._PruneMaskLen = hex(int(value, 16))

