"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dot1agMaConfig(ROMObject):
    def __init__(self, OperationMode=None, MaidType=None, MdName=None, MdLevel=None, PrimaryVid=None, CcPeriod=None, LckPeriod=None, CcPriority=None, LbPriority=None, LtPriority=None, **kwargs):
        self._OperationMode = OperationMode  # Operation Mode
        self._MaidType = MaidType  # MAID Type
        self._MdName = MdName  # MD Name
        self._MdLevel = MdLevel  # MD Level
        self._Maid = ''  # MA ID, not editable
        self._PrimaryVid = PrimaryVid  # Primary VID
        self._CcPeriod = CcPeriod  # CC Period
        self._LckPeriod = LckPeriod  # LCK Period
        self._CcPriority = CcPriority  # CC Priority
        self._LbPriority = LbPriority  # LB Priority
        self._LtPriority = LtPriority  # LT Priority

        properties = kwargs.copy()
        if OperationMode is not None:
            properties['OperationMode'] = OperationMode
        if MaidType is not None:
            properties['MaidType'] = MaidType
        if MdName is not None:
            properties['MdName'] = MdName
        if MdLevel is not None:
            properties['MdLevel'] = MdLevel
        if PrimaryVid is not None:
            properties['PrimaryVid'] = PrimaryVid
        if CcPeriod is not None:
            properties['CcPeriod'] = CcPeriod
        if LckPeriod is not None:
            properties['LckPeriod'] = LckPeriod
        if CcPriority is not None:
            properties['CcPriority'] = CcPriority
        if LbPriority is not None:
            properties['LbPriority'] = LbPriority
        if LtPriority is not None:
            properties['LtPriority'] = LtPriority

        # call base class function, and it will send message to renix server to create a class.
        super(Dot1agMaConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, OperationMode=None, MaidType=None, MdName=None, MdLevel=None, PrimaryVid=None, CcPeriod=None, LckPeriod=None, CcPriority=None, LbPriority=None, LtPriority=None, **kwargs):
        properties = kwargs.copy()
        if OperationMode is not None:
            self._OperationMode = OperationMode
            properties['OperationMode'] = OperationMode
        if MaidType is not None:
            self._MaidType = MaidType
            properties['MaidType'] = MaidType
        if MdName is not None:
            self._MdName = MdName
            properties['MdName'] = MdName
        if MdLevel is not None:
            self._MdLevel = MdLevel
            properties['MdLevel'] = MdLevel
        if PrimaryVid is not None:
            self._PrimaryVid = PrimaryVid
            properties['PrimaryVid'] = PrimaryVid
        if CcPeriod is not None:
            self._CcPeriod = CcPeriod
            properties['CcPeriod'] = CcPeriod
        if LckPeriod is not None:
            self._LckPeriod = LckPeriod
            properties['LckPeriod'] = LckPeriod
        if CcPriority is not None:
            self._CcPriority = CcPriority
            properties['CcPriority'] = CcPriority
        if LbPriority is not None:
            self._LbPriority = LbPriority
            properties['LbPriority'] = LbPriority
        if LtPriority is not None:
            self._LtPriority = LtPriority
            properties['LtPriority'] = LtPriority

        super(Dot1agMaConfig, self).edit(**properties)

    @property
    def OperationMode(self):
        """
        get the value of property _OperationMode
        """
        if self.force_auto_sync:
            self.get('OperationMode')
        return self._OperationMode

    @property
    def MaidType(self):
        """
        get the value of property _MaidType
        """
        if self.force_auto_sync:
            self.get('MaidType')
        return self._MaidType

    @property
    def MdName(self):
        """
        get the value of property _MdName
        """
        if self.force_auto_sync:
            self.get('MdName')
        return self._MdName

    @property
    def MdLevel(self):
        """
        get the value of property _MdLevel
        """
        if self.force_auto_sync:
            self.get('MdLevel')
        return self._MdLevel

    @property
    def Maid(self):
        """
        get the value of property _Maid
        """
        if self.force_auto_sync:
            self.get('Maid')
        return self._Maid

    @property
    def PrimaryVid(self):
        """
        get the value of property _PrimaryVid
        """
        if self.force_auto_sync:
            self.get('PrimaryVid')
        return self._PrimaryVid

    @property
    def CcPeriod(self):
        """
        get the value of property _CcPeriod
        """
        if self.force_auto_sync:
            self.get('CcPeriod')
        return self._CcPeriod

    @property
    def LckPeriod(self):
        """
        get the value of property _LckPeriod
        """
        if self.force_auto_sync:
            self.get('LckPeriod')
        return self._LckPeriod

    @property
    def CcPriority(self):
        """
        get the value of property _CcPriority
        """
        if self.force_auto_sync:
            self.get('CcPriority')
        return self._CcPriority

    @property
    def LbPriority(self):
        """
        get the value of property _LbPriority
        """
        if self.force_auto_sync:
            self.get('LbPriority')
        return self._LbPriority

    @property
    def LtPriority(self):
        """
        get the value of property _LtPriority
        """
        if self.force_auto_sync:
            self.get('LtPriority')
        return self._LtPriority

    @OperationMode.setter
    def OperationMode(self, value):
        self._OperationMode = value
        self.edit(OperationMode=value)

    @MaidType.setter
    def MaidType(self, value):
        self._MaidType = value
        self.edit(MaidType=value)

    @MdName.setter
    def MdName(self, value):
        self._MdName = value
        self.edit(MdName=value)

    @MdLevel.setter
    def MdLevel(self, value):
        self._MdLevel = value
        self.edit(MdLevel=value)

    @PrimaryVid.setter
    def PrimaryVid(self, value):
        self._PrimaryVid = value
        self.edit(PrimaryVid=value)

    @CcPeriod.setter
    def CcPeriod(self, value):
        self._CcPeriod = value
        self.edit(CcPeriod=value)

    @LckPeriod.setter
    def LckPeriod(self, value):
        self._LckPeriod = value
        self.edit(LckPeriod=value)

    @CcPriority.setter
    def CcPriority(self, value):
        self._CcPriority = value
        self.edit(CcPriority=value)

    @LbPriority.setter
    def LbPriority(self, value):
        self._LbPriority = value
        self.edit(LbPriority=value)

    @LtPriority.setter
    def LtPriority(self, value):
        self._LtPriority = value
        self.edit(LtPriority=value)

    def _set_operationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._OperationMode = EnumOpMode.%s' % value[:seperate])

    def _set_maidtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._MaidType = EnumMAIDType.%s' % value[:seperate])

    def _set_mdname_with_str(self, value):
        self._MdName = value

    def _set_mdlevel_with_str(self, value):
        seperate = value.find(':')
        exec('self._MdLevel = EnumMdLevel.%s' % value[:seperate])

    def _set_maid_with_str(self, value):
        self._Maid = value

    def _set_primaryvid_with_str(self, value):
        try:
            self._PrimaryVid = int(value)
        except ValueError:
            self._PrimaryVid = hex(int(value, 16))

    def _set_ccperiod_with_str(self, value):
        seperate = value.find(':')
        exec('self._CcPeriod = EnumCCPeriod.%s' % value[:seperate])

    def _set_lckperiod_with_str(self, value):
        seperate = value.find(':')
        exec('self._LckPeriod = EnumLCKPeriod.%s' % value[:seperate])

    def _set_ccpriority_with_str(self, value):
        seperate = value.find(':')
        exec('self._CcPriority = EnumMdLevel.%s' % value[:seperate])

    def _set_lbpriority_with_str(self, value):
        seperate = value.find(':')
        exec('self._LbPriority = EnumMdLevel.%s' % value[:seperate])

    def _set_ltpriority_with_str(self, value):
        seperate = value.find(':')
        exec('self._LtPriority = EnumMdLevel.%s' % value[:seperate])

