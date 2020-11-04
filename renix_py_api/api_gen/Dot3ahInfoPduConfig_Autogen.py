"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dot3ahInfoPduConfig(ROMObject):
    def __init__(self, PduTime=None, LostLinkTime=None, OamModeType=None, OrgUniqueId=None, OamVersion=None, VendorSpecInfo=None, EnableOverrideRevision=None, OverrideRevision=None, EnableVarRetrieval=None, EnableInterpLinkEvent=None, EnableLoopBack=None, EnableUnidirMode=None, **kwargs):
        self._PduTime = PduTime  # PDU Time (sec)
        self._LostLinkTime = LostLinkTime  # Lost Link Time (sec)
        self._OamModeType = OamModeType  # OAM Mode
        self._OrgUniqueId = OrgUniqueId  # Organization Unique ID
        self._OamVersion = OamVersion  # OAM Version
        self._VendorSpecInfo = VendorSpecInfo  # Vendor Specific Info
        self._EnableOverrideRevision = EnableOverrideRevision  # Enable Override Revision
        self._OverrideRevision = OverrideRevision  # Override Revision
        self._EnableVarRetrieval = EnableVarRetrieval  # Enable Variable Retrieval
        self._EnableInterpLinkEvent = EnableInterpLinkEvent  # Enable Interpret Link Event
        self._EnableLoopBack = EnableLoopBack  # Enable Loopback
        self._EnableUnidirMode = EnableUnidirMode  # Enable Unidirectional Mode

        properties = kwargs.copy()
        if PduTime is not None:
            properties['PduTime'] = PduTime
        if LostLinkTime is not None:
            properties['LostLinkTime'] = LostLinkTime
        if OamModeType is not None:
            properties['OamModeType'] = OamModeType
        if OrgUniqueId is not None:
            properties['OrgUniqueId'] = OrgUniqueId
        if OamVersion is not None:
            properties['OamVersion'] = OamVersion
        if VendorSpecInfo is not None:
            properties['VendorSpecInfo'] = VendorSpecInfo
        if EnableOverrideRevision is not None:
            properties['EnableOverrideRevision'] = EnableOverrideRevision
        if OverrideRevision is not None:
            properties['OverrideRevision'] = OverrideRevision
        if EnableVarRetrieval is not None:
            properties['EnableVarRetrieval'] = EnableVarRetrieval
        if EnableInterpLinkEvent is not None:
            properties['EnableInterpLinkEvent'] = EnableInterpLinkEvent
        if EnableLoopBack is not None:
            properties['EnableLoopBack'] = EnableLoopBack
        if EnableUnidirMode is not None:
            properties['EnableUnidirMode'] = EnableUnidirMode

        # call base class function, and it will send message to renix server to create a class.
        super(Dot3ahInfoPduConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PduTime=None, LostLinkTime=None, OamModeType=None, OrgUniqueId=None, OamVersion=None, VendorSpecInfo=None, EnableOverrideRevision=None, OverrideRevision=None, EnableVarRetrieval=None, EnableInterpLinkEvent=None, EnableLoopBack=None, EnableUnidirMode=None, **kwargs):
        properties = kwargs.copy()
        if PduTime is not None:
            self._PduTime = PduTime
            properties['PduTime'] = PduTime
        if LostLinkTime is not None:
            self._LostLinkTime = LostLinkTime
            properties['LostLinkTime'] = LostLinkTime
        if OamModeType is not None:
            self._OamModeType = OamModeType
            properties['OamModeType'] = OamModeType
        if OrgUniqueId is not None:
            self._OrgUniqueId = OrgUniqueId
            properties['OrgUniqueId'] = OrgUniqueId
        if OamVersion is not None:
            self._OamVersion = OamVersion
            properties['OamVersion'] = OamVersion
        if VendorSpecInfo is not None:
            self._VendorSpecInfo = VendorSpecInfo
            properties['VendorSpecInfo'] = VendorSpecInfo
        if EnableOverrideRevision is not None:
            self._EnableOverrideRevision = EnableOverrideRevision
            properties['EnableOverrideRevision'] = EnableOverrideRevision
        if OverrideRevision is not None:
            self._OverrideRevision = OverrideRevision
            properties['OverrideRevision'] = OverrideRevision
        if EnableVarRetrieval is not None:
            self._EnableVarRetrieval = EnableVarRetrieval
            properties['EnableVarRetrieval'] = EnableVarRetrieval
        if EnableInterpLinkEvent is not None:
            self._EnableInterpLinkEvent = EnableInterpLinkEvent
            properties['EnableInterpLinkEvent'] = EnableInterpLinkEvent
        if EnableLoopBack is not None:
            self._EnableLoopBack = EnableLoopBack
            properties['EnableLoopBack'] = EnableLoopBack
        if EnableUnidirMode is not None:
            self._EnableUnidirMode = EnableUnidirMode
            properties['EnableUnidirMode'] = EnableUnidirMode

        super(Dot3ahInfoPduConfig, self).edit(**properties)

    @property
    def PduTime(self):
        """
        get the value of property _PduTime
        """
        if self.force_auto_sync:
            self.get('PduTime')
        return self._PduTime

    @property
    def LostLinkTime(self):
        """
        get the value of property _LostLinkTime
        """
        if self.force_auto_sync:
            self.get('LostLinkTime')
        return self._LostLinkTime

    @property
    def OamModeType(self):
        """
        get the value of property _OamModeType
        """
        if self.force_auto_sync:
            self.get('OamModeType')
        return self._OamModeType

    @property
    def OrgUniqueId(self):
        """
        get the value of property _OrgUniqueId
        """
        if self.force_auto_sync:
            self.get('OrgUniqueId')
        return self._OrgUniqueId

    @property
    def OamVersion(self):
        """
        get the value of property _OamVersion
        """
        if self.force_auto_sync:
            self.get('OamVersion')
        return self._OamVersion

    @property
    def VendorSpecInfo(self):
        """
        get the value of property _VendorSpecInfo
        """
        if self.force_auto_sync:
            self.get('VendorSpecInfo')
        return self._VendorSpecInfo

    @property
    def EnableOverrideRevision(self):
        """
        get the value of property _EnableOverrideRevision
        """
        if self.force_auto_sync:
            self.get('EnableOverrideRevision')
        return self._EnableOverrideRevision

    @property
    def OverrideRevision(self):
        """
        get the value of property _OverrideRevision
        """
        if self.force_auto_sync:
            self.get('OverrideRevision')
        return self._OverrideRevision

    @property
    def EnableVarRetrieval(self):
        """
        get the value of property _EnableVarRetrieval
        """
        if self.force_auto_sync:
            self.get('EnableVarRetrieval')
        return self._EnableVarRetrieval

    @property
    def EnableInterpLinkEvent(self):
        """
        get the value of property _EnableInterpLinkEvent
        """
        if self.force_auto_sync:
            self.get('EnableInterpLinkEvent')
        return self._EnableInterpLinkEvent

    @property
    def EnableLoopBack(self):
        """
        get the value of property _EnableLoopBack
        """
        if self.force_auto_sync:
            self.get('EnableLoopBack')
        return self._EnableLoopBack

    @property
    def EnableUnidirMode(self):
        """
        get the value of property _EnableUnidirMode
        """
        if self.force_auto_sync:
            self.get('EnableUnidirMode')
        return self._EnableUnidirMode

    @PduTime.setter
    def PduTime(self, value):
        self._PduTime = value
        self.edit(PduTime=value)

    @LostLinkTime.setter
    def LostLinkTime(self, value):
        self._LostLinkTime = value
        self.edit(LostLinkTime=value)

    @OamModeType.setter
    def OamModeType(self, value):
        self._OamModeType = value
        self.edit(OamModeType=value)

    @OrgUniqueId.setter
    def OrgUniqueId(self, value):
        self._OrgUniqueId = value
        self.edit(OrgUniqueId=value)

    @OamVersion.setter
    def OamVersion(self, value):
        self._OamVersion = value
        self.edit(OamVersion=value)

    @VendorSpecInfo.setter
    def VendorSpecInfo(self, value):
        self._VendorSpecInfo = value
        self.edit(VendorSpecInfo=value)

    @EnableOverrideRevision.setter
    def EnableOverrideRevision(self, value):
        self._EnableOverrideRevision = value
        self.edit(EnableOverrideRevision=value)

    @OverrideRevision.setter
    def OverrideRevision(self, value):
        self._OverrideRevision = value
        self.edit(OverrideRevision=value)

    @EnableVarRetrieval.setter
    def EnableVarRetrieval(self, value):
        self._EnableVarRetrieval = value
        self.edit(EnableVarRetrieval=value)

    @EnableInterpLinkEvent.setter
    def EnableInterpLinkEvent(self, value):
        self._EnableInterpLinkEvent = value
        self.edit(EnableInterpLinkEvent=value)

    @EnableLoopBack.setter
    def EnableLoopBack(self, value):
        self._EnableLoopBack = value
        self.edit(EnableLoopBack=value)

    @EnableUnidirMode.setter
    def EnableUnidirMode(self, value):
        self._EnableUnidirMode = value
        self.edit(EnableUnidirMode=value)

    def _set_pdutime_with_str(self, value):
        try:
            self._PduTime = int(value)
        except ValueError:
            self._PduTime = hex(int(value, 16))

    def _set_lostlinktime_with_str(self, value):
        try:
            self._LostLinkTime = int(value)
        except ValueError:
            self._LostLinkTime = hex(int(value, 16))

    def _set_oammodetype_with_str(self, value):
        seperate = value.find(':')
        exec('self._OamModeType = EnumOamModeType.%s' % value[:seperate])

    def _set_orguniqueid_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._OrgUniqueId = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._OrgUniqueId.append(int(str_value))
            except ValueError:
                self._OrgUniqueId.append(hex(int(str_value, 16)))

    def _set_oamversion_with_str(self, value):
        try:
            self._OamVersion = int(value)
        except ValueError:
            self._OamVersion = hex(int(value, 16))

    def _set_vendorspecinfo_with_str(self, value):
        try:
            self._VendorSpecInfo = int(value)
        except ValueError:
            self._VendorSpecInfo = hex(int(value, 16))

    def _set_enableoverriderevision_with_str(self, value):
        self._EnableOverrideRevision = (value == 'True')

    def _set_overriderevision_with_str(self, value):
        try:
            self._OverrideRevision = int(value)
        except ValueError:
            self._OverrideRevision = hex(int(value, 16))

    def _set_enablevarretrieval_with_str(self, value):
        self._EnableVarRetrieval = (value == 'True')

    def _set_enableinterplinkevent_with_str(self, value):
        self._EnableInterpLinkEvent = (value == 'True')

    def _set_enableloopback_with_str(self, value):
        self._EnableLoopBack = (value == 'True')

    def _set_enableunidirmode_with_str(self, value):
        self._EnableUnidirMode = (value == 'True')

