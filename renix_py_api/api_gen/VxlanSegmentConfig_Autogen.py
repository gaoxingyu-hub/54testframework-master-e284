"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class VxlanSegmentConfig(ROMObject):
    def __init__(self, StartVni=None, VniCount=None, VniStep=None, CommunicationType=None, EnableL3Vni=None, StartL3Vni=None, L3VniStep=None, **kwargs):
        self._StartVni = StartVni  # Start VNI
        self._VniCount = VniCount  # VNI Count
        self._VniStep = VniStep  # VNI Step
        self._CommunicationType = CommunicationType  # Communication Type
        self._EnableL3Vni = EnableL3Vni  # Enable L3VNI
        self._StartL3Vni = StartL3Vni  # Start L3VNI
        self._L3VniStep = L3VniStep  # L3VNI Step

        properties = kwargs.copy()
        if StartVni is not None:
            properties['StartVni'] = StartVni
        if VniCount is not None:
            properties['VniCount'] = VniCount
        if VniStep is not None:
            properties['VniStep'] = VniStep
        if CommunicationType is not None:
            properties['CommunicationType'] = CommunicationType
        if EnableL3Vni is not None:
            properties['EnableL3Vni'] = EnableL3Vni
        if StartL3Vni is not None:
            properties['StartL3Vni'] = StartL3Vni
        if L3VniStep is not None:
            properties['L3VniStep'] = L3VniStep

        # call base class function, and it will send message to renix server to create a class.
        super(VxlanSegmentConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, StartVni=None, VniCount=None, VniStep=None, CommunicationType=None, EnableL3Vni=None, StartL3Vni=None, L3VniStep=None, **kwargs):
        properties = kwargs.copy()
        if StartVni is not None:
            self._StartVni = StartVni
            properties['StartVni'] = StartVni
        if VniCount is not None:
            self._VniCount = VniCount
            properties['VniCount'] = VniCount
        if VniStep is not None:
            self._VniStep = VniStep
            properties['VniStep'] = VniStep
        if CommunicationType is not None:
            self._CommunicationType = CommunicationType
            properties['CommunicationType'] = CommunicationType
        if EnableL3Vni is not None:
            self._EnableL3Vni = EnableL3Vni
            properties['EnableL3Vni'] = EnableL3Vni
        if StartL3Vni is not None:
            self._StartL3Vni = StartL3Vni
            properties['StartL3Vni'] = StartL3Vni
        if L3VniStep is not None:
            self._L3VniStep = L3VniStep
            properties['L3VniStep'] = L3VniStep

        super(VxlanSegmentConfig, self).edit(**properties)

    @property
    def StartVni(self):
        """
        get the value of property _StartVni
        """
        if self.force_auto_sync:
            self.get('StartVni')
        return self._StartVni

    @property
    def VniCount(self):
        """
        get the value of property _VniCount
        """
        if self.force_auto_sync:
            self.get('VniCount')
        return self._VniCount

    @property
    def VniStep(self):
        """
        get the value of property _VniStep
        """
        if self.force_auto_sync:
            self.get('VniStep')
        return self._VniStep

    @property
    def CommunicationType(self):
        """
        get the value of property _CommunicationType
        """
        if self.force_auto_sync:
            self.get('CommunicationType')
        return self._CommunicationType

    @property
    def EnableL3Vni(self):
        """
        get the value of property _EnableL3Vni
        """
        if self.force_auto_sync:
            self.get('EnableL3Vni')
        return self._EnableL3Vni

    @property
    def StartL3Vni(self):
        """
        get the value of property _StartL3Vni
        """
        if self.force_auto_sync:
            self.get('StartL3Vni')
        return self._StartL3Vni

    @property
    def L3VniStep(self):
        """
        get the value of property _L3VniStep
        """
        if self.force_auto_sync:
            self.get('L3VniStep')
        return self._L3VniStep

    @StartVni.setter
    def StartVni(self, value):
        self._StartVni = value
        self.edit(StartVni=value)

    @VniCount.setter
    def VniCount(self, value):
        self._VniCount = value
        self.edit(VniCount=value)

    @VniStep.setter
    def VniStep(self, value):
        self._VniStep = value
        self.edit(VniStep=value)

    @CommunicationType.setter
    def CommunicationType(self, value):
        self._CommunicationType = value
        self.edit(CommunicationType=value)

    @EnableL3Vni.setter
    def EnableL3Vni(self, value):
        self._EnableL3Vni = value
        self.edit(EnableL3Vni=value)

    @StartL3Vni.setter
    def StartL3Vni(self, value):
        self._StartL3Vni = value
        self.edit(StartL3Vni=value)

    @L3VniStep.setter
    def L3VniStep(self, value):
        self._L3VniStep = value
        self.edit(L3VniStep=value)

    def _set_startvni_with_str(self, value):
        try:
            self._StartVni = int(value)
        except ValueError:
            self._StartVni = hex(int(value, 16))

    def _set_vnicount_with_str(self, value):
        try:
            self._VniCount = int(value)
        except ValueError:
            self._VniCount = hex(int(value, 16))

    def _set_vnistep_with_str(self, value):
        try:
            self._VniStep = int(value)
        except ValueError:
            self._VniStep = hex(int(value, 16))

    def _set_communicationtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._CommunicationType = EnumCommunicationType.%s' % value[:seperate])

    def _set_enablel3vni_with_str(self, value):
        self._EnableL3Vni = (value == 'True')

    def _set_startl3vni_with_str(self, value):
        try:
            self._StartL3Vni = int(value)
        except ValueError:
            self._StartL3Vni = hex(int(value, 16))

    def _set_l3vnistep_with_str(self, value):
        try:
            self._L3VniStep = int(value)
        except ValueError:
            self._L3VniStep = hex(int(value, 16))

