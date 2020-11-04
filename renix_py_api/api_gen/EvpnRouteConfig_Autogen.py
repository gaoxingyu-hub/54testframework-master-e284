"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class EvpnRouteConfig(ROMObject):
    def __init__(self, Origin=None, AsPath=None, VrfRouteTarget=None, VrfRouteTargetAs=None, VrfRouteTargetNum=None, VrfRouteTargetStepAs=None, VrfRouteTargetStepNum=None, VrfRouteDistinguisherType=None, VrfRouteDistinguisherIp=None, VrfRouteDistinguisherAs=None, VrfRouteDistinguisherNum=None, VrfRouteDistinguisherStepAs=None, VrfRouteDistinguisherStepNum=None, EthernetSegmentType=None, EthernetSegmentIdTop=None, EthernetSegmentIdMid=None, EthernetSegmentIdLow=None, EthernetTagId=None, **kwargs):
        self._Origin = Origin  # ORIGIN
        self._AsPath = AsPath  # AS Path
        self._VrfRouteTarget = VrfRouteTarget  # Route Target
        self._VrfRouteTargetAs = VrfRouteTargetAs  # Route Target As
        self._VrfRouteTargetNum = VrfRouteTargetNum  # Route Target Number
        self._VrfRouteTargetStepAs = VrfRouteTargetStepAs  # Route Target As Step
        self._VrfRouteTargetStepNum = VrfRouteTargetStepNum  # Route Target Number Step
        self._VrfRouteDistinguisherType = VrfRouteDistinguisherType  # Route Distinguisher Format Type
        self._VrfRouteDistinguisherIp = VrfRouteDistinguisherIp  # Route Distinguisher Ip
        self._VrfRouteDistinguisherAs = VrfRouteDistinguisherAs  # Route Distinguisher As
        self._VrfRouteDistinguisherNum = VrfRouteDistinguisherNum  # Route Distinguisher Number
        self._VrfRouteDistinguisherStepAs = VrfRouteDistinguisherStepAs  # Route Distinguisher As step
        self._VrfRouteDistinguisherStepNum = VrfRouteDistinguisherStepNum  # Route Distinguisher Number Step
        self._EthernetSegmentType = EthernetSegmentType  # Ethernet Segment Type
        self._EthernetSegmentIdTop = EthernetSegmentIdTop  # Ethernet Segment Id
        self._EthernetSegmentIdMid = EthernetSegmentIdMid  # Ethernet Segment Id
        self._EthernetSegmentIdLow = EthernetSegmentIdLow  # Ethernet Segment Id
        self._EthernetTagId = EthernetTagId  # Ethernet Tag ID

        properties = kwargs.copy()
        if Origin is not None:
            properties['Origin'] = Origin
        if AsPath is not None:
            properties['AsPath'] = AsPath
        if VrfRouteTarget is not None:
            properties['VrfRouteTarget'] = VrfRouteTarget
        if VrfRouteTargetAs is not None:
            properties['VrfRouteTargetAs'] = VrfRouteTargetAs
        if VrfRouteTargetNum is not None:
            properties['VrfRouteTargetNum'] = VrfRouteTargetNum
        if VrfRouteTargetStepAs is not None:
            properties['VrfRouteTargetStepAs'] = VrfRouteTargetStepAs
        if VrfRouteTargetStepNum is not None:
            properties['VrfRouteTargetStepNum'] = VrfRouteTargetStepNum
        if VrfRouteDistinguisherType is not None:
            properties['VrfRouteDistinguisherType'] = VrfRouteDistinguisherType
        if VrfRouteDistinguisherIp is not None:
            properties['VrfRouteDistinguisherIp'] = VrfRouteDistinguisherIp
        if VrfRouteDistinguisherAs is not None:
            properties['VrfRouteDistinguisherAs'] = VrfRouteDistinguisherAs
        if VrfRouteDistinguisherNum is not None:
            properties['VrfRouteDistinguisherNum'] = VrfRouteDistinguisherNum
        if VrfRouteDistinguisherStepAs is not None:
            properties['VrfRouteDistinguisherStepAs'] = VrfRouteDistinguisherStepAs
        if VrfRouteDistinguisherStepNum is not None:
            properties['VrfRouteDistinguisherStepNum'] = VrfRouteDistinguisherStepNum
        if EthernetSegmentType is not None:
            properties['EthernetSegmentType'] = EthernetSegmentType
        if EthernetSegmentIdTop is not None:
            properties['EthernetSegmentIdTop'] = EthernetSegmentIdTop
        if EthernetSegmentIdMid is not None:
            properties['EthernetSegmentIdMid'] = EthernetSegmentIdMid
        if EthernetSegmentIdLow is not None:
            properties['EthernetSegmentIdLow'] = EthernetSegmentIdLow
        if EthernetTagId is not None:
            properties['EthernetTagId'] = EthernetTagId

        # call base class function, and it will send message to renix server to create a class.
        super(EvpnRouteConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Origin=None, AsPath=None, VrfRouteTarget=None, VrfRouteTargetAs=None, VrfRouteTargetNum=None, VrfRouteTargetStepAs=None, VrfRouteTargetStepNum=None, VrfRouteDistinguisherType=None, VrfRouteDistinguisherIp=None, VrfRouteDistinguisherAs=None, VrfRouteDistinguisherNum=None, VrfRouteDistinguisherStepAs=None, VrfRouteDistinguisherStepNum=None, EthernetSegmentType=None, EthernetSegmentIdTop=None, EthernetSegmentIdMid=None, EthernetSegmentIdLow=None, EthernetTagId=None, **kwargs):
        properties = kwargs.copy()
        if Origin is not None:
            self._Origin = Origin
            properties['Origin'] = Origin
        if AsPath is not None:
            self._AsPath = AsPath
            properties['AsPath'] = AsPath
        if VrfRouteTarget is not None:
            self._VrfRouteTarget = VrfRouteTarget
            properties['VrfRouteTarget'] = VrfRouteTarget
        if VrfRouteTargetAs is not None:
            self._VrfRouteTargetAs = VrfRouteTargetAs
            properties['VrfRouteTargetAs'] = VrfRouteTargetAs
        if VrfRouteTargetNum is not None:
            self._VrfRouteTargetNum = VrfRouteTargetNum
            properties['VrfRouteTargetNum'] = VrfRouteTargetNum
        if VrfRouteTargetStepAs is not None:
            self._VrfRouteTargetStepAs = VrfRouteTargetStepAs
            properties['VrfRouteTargetStepAs'] = VrfRouteTargetStepAs
        if VrfRouteTargetStepNum is not None:
            self._VrfRouteTargetStepNum = VrfRouteTargetStepNum
            properties['VrfRouteTargetStepNum'] = VrfRouteTargetStepNum
        if VrfRouteDistinguisherType is not None:
            self._VrfRouteDistinguisherType = VrfRouteDistinguisherType
            properties['VrfRouteDistinguisherType'] = VrfRouteDistinguisherType
        if VrfRouteDistinguisherIp is not None:
            self._VrfRouteDistinguisherIp = VrfRouteDistinguisherIp
            properties['VrfRouteDistinguisherIp'] = VrfRouteDistinguisherIp
        if VrfRouteDistinguisherAs is not None:
            self._VrfRouteDistinguisherAs = VrfRouteDistinguisherAs
            properties['VrfRouteDistinguisherAs'] = VrfRouteDistinguisherAs
        if VrfRouteDistinguisherNum is not None:
            self._VrfRouteDistinguisherNum = VrfRouteDistinguisherNum
            properties['VrfRouteDistinguisherNum'] = VrfRouteDistinguisherNum
        if VrfRouteDistinguisherStepAs is not None:
            self._VrfRouteDistinguisherStepAs = VrfRouteDistinguisherStepAs
            properties['VrfRouteDistinguisherStepAs'] = VrfRouteDistinguisherStepAs
        if VrfRouteDistinguisherStepNum is not None:
            self._VrfRouteDistinguisherStepNum = VrfRouteDistinguisherStepNum
            properties['VrfRouteDistinguisherStepNum'] = VrfRouteDistinguisherStepNum
        if EthernetSegmentType is not None:
            self._EthernetSegmentType = EthernetSegmentType
            properties['EthernetSegmentType'] = EthernetSegmentType
        if EthernetSegmentIdTop is not None:
            self._EthernetSegmentIdTop = EthernetSegmentIdTop
            properties['EthernetSegmentIdTop'] = EthernetSegmentIdTop
        if EthernetSegmentIdMid is not None:
            self._EthernetSegmentIdMid = EthernetSegmentIdMid
            properties['EthernetSegmentIdMid'] = EthernetSegmentIdMid
        if EthernetSegmentIdLow is not None:
            self._EthernetSegmentIdLow = EthernetSegmentIdLow
            properties['EthernetSegmentIdLow'] = EthernetSegmentIdLow
        if EthernetTagId is not None:
            self._EthernetTagId = EthernetTagId
            properties['EthernetTagId'] = EthernetTagId

        super(EvpnRouteConfig, self).edit(**properties)

    @property
    def Origin(self):
        """
        get the value of property _Origin
        """
        if self.force_auto_sync:
            self.get('Origin')
        return self._Origin

    @property
    def AsPath(self):
        """
        get the value of property _AsPath
        """
        if self.force_auto_sync:
            self.get('AsPath')
        return self._AsPath

    @property
    def VrfRouteTarget(self):
        """
        get the value of property _VrfRouteTarget
        """
        if self.force_auto_sync:
            self.get('VrfRouteTarget')
        return self._VrfRouteTarget

    @property
    def VrfRouteTargetAs(self):
        """
        get the value of property _VrfRouteTargetAs
        """
        if self.force_auto_sync:
            self.get('VrfRouteTargetAs')
        return self._VrfRouteTargetAs

    @property
    def VrfRouteTargetNum(self):
        """
        get the value of property _VrfRouteTargetNum
        """
        if self.force_auto_sync:
            self.get('VrfRouteTargetNum')
        return self._VrfRouteTargetNum

    @property
    def VrfRouteTargetStepAs(self):
        """
        get the value of property _VrfRouteTargetStepAs
        """
        if self.force_auto_sync:
            self.get('VrfRouteTargetStepAs')
        return self._VrfRouteTargetStepAs

    @property
    def VrfRouteTargetStepNum(self):
        """
        get the value of property _VrfRouteTargetStepNum
        """
        if self.force_auto_sync:
            self.get('VrfRouteTargetStepNum')
        return self._VrfRouteTargetStepNum

    @property
    def VrfRouteDistinguisherType(self):
        """
        get the value of property _VrfRouteDistinguisherType
        """
        if self.force_auto_sync:
            self.get('VrfRouteDistinguisherType')
        return self._VrfRouteDistinguisherType

    @property
    def VrfRouteDistinguisherIp(self):
        """
        get the value of property _VrfRouteDistinguisherIp
        """
        if self.force_auto_sync:
            self.get('VrfRouteDistinguisherIp')
        return self._VrfRouteDistinguisherIp

    @property
    def VrfRouteDistinguisherAs(self):
        """
        get the value of property _VrfRouteDistinguisherAs
        """
        if self.force_auto_sync:
            self.get('VrfRouteDistinguisherAs')
        return self._VrfRouteDistinguisherAs

    @property
    def VrfRouteDistinguisherNum(self):
        """
        get the value of property _VrfRouteDistinguisherNum
        """
        if self.force_auto_sync:
            self.get('VrfRouteDistinguisherNum')
        return self._VrfRouteDistinguisherNum

    @property
    def VrfRouteDistinguisherStepAs(self):
        """
        get the value of property _VrfRouteDistinguisherStepAs
        """
        if self.force_auto_sync:
            self.get('VrfRouteDistinguisherStepAs')
        return self._VrfRouteDistinguisherStepAs

    @property
    def VrfRouteDistinguisherStepNum(self):
        """
        get the value of property _VrfRouteDistinguisherStepNum
        """
        if self.force_auto_sync:
            self.get('VrfRouteDistinguisherStepNum')
        return self._VrfRouteDistinguisherStepNum

    @property
    def EthernetSegmentType(self):
        """
        get the value of property _EthernetSegmentType
        """
        if self.force_auto_sync:
            self.get('EthernetSegmentType')
        return self._EthernetSegmentType

    @property
    def EthernetSegmentIdTop(self):
        """
        get the value of property _EthernetSegmentIdTop
        """
        if self.force_auto_sync:
            self.get('EthernetSegmentIdTop')
        return self._EthernetSegmentIdTop

    @property
    def EthernetSegmentIdMid(self):
        """
        get the value of property _EthernetSegmentIdMid
        """
        if self.force_auto_sync:
            self.get('EthernetSegmentIdMid')
        return self._EthernetSegmentIdMid

    @property
    def EthernetSegmentIdLow(self):
        """
        get the value of property _EthernetSegmentIdLow
        """
        if self.force_auto_sync:
            self.get('EthernetSegmentIdLow')
        return self._EthernetSegmentIdLow

    @property
    def EthernetTagId(self):
        """
        get the value of property _EthernetTagId
        """
        if self.force_auto_sync:
            self.get('EthernetTagId')
        return self._EthernetTagId

    @Origin.setter
    def Origin(self, value):
        self._Origin = value
        self.edit(Origin=value)

    @AsPath.setter
    def AsPath(self, value):
        self._AsPath = value
        self.edit(AsPath=value)

    @VrfRouteTarget.setter
    def VrfRouteTarget(self, value):
        self._VrfRouteTarget = value
        self.edit(VrfRouteTarget=value)

    @VrfRouteTargetAs.setter
    def VrfRouteTargetAs(self, value):
        self._VrfRouteTargetAs = value
        self.edit(VrfRouteTargetAs=value)

    @VrfRouteTargetNum.setter
    def VrfRouteTargetNum(self, value):
        self._VrfRouteTargetNum = value
        self.edit(VrfRouteTargetNum=value)

    @VrfRouteTargetStepAs.setter
    def VrfRouteTargetStepAs(self, value):
        self._VrfRouteTargetStepAs = value
        self.edit(VrfRouteTargetStepAs=value)

    @VrfRouteTargetStepNum.setter
    def VrfRouteTargetStepNum(self, value):
        self._VrfRouteTargetStepNum = value
        self.edit(VrfRouteTargetStepNum=value)

    @VrfRouteDistinguisherType.setter
    def VrfRouteDistinguisherType(self, value):
        self._VrfRouteDistinguisherType = value
        self.edit(VrfRouteDistinguisherType=value)

    @VrfRouteDistinguisherIp.setter
    def VrfRouteDistinguisherIp(self, value):
        self._VrfRouteDistinguisherIp = value
        self.edit(VrfRouteDistinguisherIp=value)

    @VrfRouteDistinguisherAs.setter
    def VrfRouteDistinguisherAs(self, value):
        self._VrfRouteDistinguisherAs = value
        self.edit(VrfRouteDistinguisherAs=value)

    @VrfRouteDistinguisherNum.setter
    def VrfRouteDistinguisherNum(self, value):
        self._VrfRouteDistinguisherNum = value
        self.edit(VrfRouteDistinguisherNum=value)

    @VrfRouteDistinguisherStepAs.setter
    def VrfRouteDistinguisherStepAs(self, value):
        self._VrfRouteDistinguisherStepAs = value
        self.edit(VrfRouteDistinguisherStepAs=value)

    @VrfRouteDistinguisherStepNum.setter
    def VrfRouteDistinguisherStepNum(self, value):
        self._VrfRouteDistinguisherStepNum = value
        self.edit(VrfRouteDistinguisherStepNum=value)

    @EthernetSegmentType.setter
    def EthernetSegmentType(self, value):
        self._EthernetSegmentType = value
        self.edit(EthernetSegmentType=value)

    @EthernetSegmentIdTop.setter
    def EthernetSegmentIdTop(self, value):
        self._EthernetSegmentIdTop = value
        self.edit(EthernetSegmentIdTop=value)

    @EthernetSegmentIdMid.setter
    def EthernetSegmentIdMid(self, value):
        self._EthernetSegmentIdMid = value
        self.edit(EthernetSegmentIdMid=value)

    @EthernetSegmentIdLow.setter
    def EthernetSegmentIdLow(self, value):
        self._EthernetSegmentIdLow = value
        self.edit(EthernetSegmentIdLow=value)

    @EthernetTagId.setter
    def EthernetTagId(self, value):
        self._EthernetTagId = value
        self.edit(EthernetTagId=value)

    def _set_origin_with_str(self, value):
        seperate = value.find(':')
        exec('self._Origin = EnumEvpnOrigin.%s' % value[:seperate])

    def _set_aspath_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._AsPath = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._AsPath.append(int(str_value))
            except ValueError:
                self._AsPath.append(hex(int(str_value, 16)))

    def _set_vrfroutetarget_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._VrfRouteTarget = tmp_value.split()

    def _set_vrfroutetargetas_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._VrfRouteTargetAs = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._VrfRouteTargetAs.append(int(str_value))
            except ValueError:
                self._VrfRouteTargetAs.append(hex(int(str_value, 16)))

    def _set_vrfroutetargetnum_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._VrfRouteTargetNum = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._VrfRouteTargetNum.append(int(str_value))
            except ValueError:
                self._VrfRouteTargetNum.append(hex(int(str_value, 16)))

    def _set_vrfroutetargetstepas_with_str(self, value):
        try:
            self._VrfRouteTargetStepAs = int(value)
        except ValueError:
            self._VrfRouteTargetStepAs = hex(int(value, 16))

    def _set_vrfroutetargetstepnum_with_str(self, value):
        try:
            self._VrfRouteTargetStepNum = int(value)
        except ValueError:
            self._VrfRouteTargetStepNum = hex(int(value, 16))

    def _set_vrfroutedistinguishertype_with_str(self, value):
        seperate = value.find(':')
        exec('self._VrfRouteDistinguisherType = EnumRouteDistinguisherType.%s' % value[:seperate])

    def _set_vrfroutedistinguisherip_with_str(self, value):
        self._VrfRouteDistinguisherIp = value

    def _set_vrfroutedistinguisheras_with_str(self, value):
        try:
            self._VrfRouteDistinguisherAs = int(value)
        except ValueError:
            self._VrfRouteDistinguisherAs = hex(int(value, 16))

    def _set_vrfroutedistinguishernum_with_str(self, value):
        try:
            self._VrfRouteDistinguisherNum = int(value)
        except ValueError:
            self._VrfRouteDistinguisherNum = hex(int(value, 16))

    def _set_vrfroutedistinguisherstepas_with_str(self, value):
        try:
            self._VrfRouteDistinguisherStepAs = int(value)
        except ValueError:
            self._VrfRouteDistinguisherStepAs = hex(int(value, 16))

    def _set_vrfroutedistinguisherstepnum_with_str(self, value):
        try:
            self._VrfRouteDistinguisherStepNum = int(value)
        except ValueError:
            self._VrfRouteDistinguisherStepNum = hex(int(value, 16))

    def _set_ethernetsegmenttype_with_str(self, value):
        seperate = value.find(':')
        exec('self._EthernetSegmentType = EnumEthernetSegmentType.%s' % value[:seperate])

    def _set_ethernetsegmentidtop_with_str(self, value):
        try:
            self._EthernetSegmentIdTop = int(value)
        except ValueError:
            self._EthernetSegmentIdTop = hex(int(value, 16))

    def _set_ethernetsegmentidmid_with_str(self, value):
        try:
            self._EthernetSegmentIdMid = int(value)
        except ValueError:
            self._EthernetSegmentIdMid = hex(int(value, 16))

    def _set_ethernetsegmentidlow_with_str(self, value):
        try:
            self._EthernetSegmentIdLow = int(value)
        except ValueError:
            self._EthernetSegmentIdLow = hex(int(value, 16))

    def _set_ethernettagid_with_str(self, value):
        try:
            self._EthernetTagId = int(value)
        except ValueError:
            self._EthernetTagId = hex(int(value, 16))

