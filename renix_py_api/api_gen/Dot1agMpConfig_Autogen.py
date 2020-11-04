"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dot1agMpConfig(ROMObject):
    def __init__(self, MpType=None, Rdi=None, EnableLbResponse=None, EnableLtResponse=None, EnableOverrideMdLevel=None, OverrideMdLevel=None, EnableOverrideCcPeriod=None, OverrideCcPeriod=None, **kwargs):
        self._MpType = MpType  # MP Type
        self._Rdi = Rdi  # RDI
        self._Vlan = 100  # VLAN ID, not editable
        self._EnableLbResponse = EnableLbResponse  # Enable LB Response
        self._EnableLtResponse = EnableLtResponse  # Enable LT Response
        self._EnableOverrideMdLevel = EnableOverrideMdLevel  # Enable Override MD level
        self._OverrideMdLevel = OverrideMdLevel  # Override MD Level
        self._EnableOverrideCcPeriod = EnableOverrideCcPeriod  # Enable Override CC Period
        self._OverrideCcPeriod = OverrideCcPeriod  # Override CC Period

        properties = kwargs.copy()
        if MpType is not None:
            properties['MpType'] = MpType
        if Rdi is not None:
            properties['Rdi'] = Rdi
        if EnableLbResponse is not None:
            properties['EnableLbResponse'] = EnableLbResponse
        if EnableLtResponse is not None:
            properties['EnableLtResponse'] = EnableLtResponse
        if EnableOverrideMdLevel is not None:
            properties['EnableOverrideMdLevel'] = EnableOverrideMdLevel
        if OverrideMdLevel is not None:
            properties['OverrideMdLevel'] = OverrideMdLevel
        if EnableOverrideCcPeriod is not None:
            properties['EnableOverrideCcPeriod'] = EnableOverrideCcPeriod
        if OverrideCcPeriod is not None:
            properties['OverrideCcPeriod'] = OverrideCcPeriod

        # call base class function, and it will send message to renix server to create a class.
        super(Dot1agMpConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, MpType=None, Rdi=None, EnableLbResponse=None, EnableLtResponse=None, EnableOverrideMdLevel=None, OverrideMdLevel=None, EnableOverrideCcPeriod=None, OverrideCcPeriod=None, **kwargs):
        properties = kwargs.copy()
        if MpType is not None:
            self._MpType = MpType
            properties['MpType'] = MpType
        if Rdi is not None:
            self._Rdi = Rdi
            properties['Rdi'] = Rdi
        if EnableLbResponse is not None:
            self._EnableLbResponse = EnableLbResponse
            properties['EnableLbResponse'] = EnableLbResponse
        if EnableLtResponse is not None:
            self._EnableLtResponse = EnableLtResponse
            properties['EnableLtResponse'] = EnableLtResponse
        if EnableOverrideMdLevel is not None:
            self._EnableOverrideMdLevel = EnableOverrideMdLevel
            properties['EnableOverrideMdLevel'] = EnableOverrideMdLevel
        if OverrideMdLevel is not None:
            self._OverrideMdLevel = OverrideMdLevel
            properties['OverrideMdLevel'] = OverrideMdLevel
        if EnableOverrideCcPeriod is not None:
            self._EnableOverrideCcPeriod = EnableOverrideCcPeriod
            properties['EnableOverrideCcPeriod'] = EnableOverrideCcPeriod
        if OverrideCcPeriod is not None:
            self._OverrideCcPeriod = OverrideCcPeriod
            properties['OverrideCcPeriod'] = OverrideCcPeriod

        super(Dot1agMpConfig, self).edit(**properties)

    @property
    def MpType(self):
        """
        get the value of property _MpType
        """
        if self.force_auto_sync:
            self.get('MpType')
        return self._MpType

    @property
    def Rdi(self):
        """
        get the value of property _Rdi
        """
        if self.force_auto_sync:
            self.get('Rdi')
        return self._Rdi

    @property
    def Vlan(self):
        """
        get the value of property _Vlan
        """
        if self.force_auto_sync:
            self.get('Vlan')
        return self._Vlan

    @property
    def EnableLbResponse(self):
        """
        get the value of property _EnableLbResponse
        """
        if self.force_auto_sync:
            self.get('EnableLbResponse')
        return self._EnableLbResponse

    @property
    def EnableLtResponse(self):
        """
        get the value of property _EnableLtResponse
        """
        if self.force_auto_sync:
            self.get('EnableLtResponse')
        return self._EnableLtResponse

    @property
    def EnableOverrideMdLevel(self):
        """
        get the value of property _EnableOverrideMdLevel
        """
        if self.force_auto_sync:
            self.get('EnableOverrideMdLevel')
        return self._EnableOverrideMdLevel

    @property
    def OverrideMdLevel(self):
        """
        get the value of property _OverrideMdLevel
        """
        if self.force_auto_sync:
            self.get('OverrideMdLevel')
        return self._OverrideMdLevel

    @property
    def EnableOverrideCcPeriod(self):
        """
        get the value of property _EnableOverrideCcPeriod
        """
        if self.force_auto_sync:
            self.get('EnableOverrideCcPeriod')
        return self._EnableOverrideCcPeriod

    @property
    def OverrideCcPeriod(self):
        """
        get the value of property _OverrideCcPeriod
        """
        if self.force_auto_sync:
            self.get('OverrideCcPeriod')
        return self._OverrideCcPeriod

    @MpType.setter
    def MpType(self, value):
        self._MpType = value
        self.edit(MpType=value)

    @Rdi.setter
    def Rdi(self, value):
        self._Rdi = value
        self.edit(Rdi=value)

    @EnableLbResponse.setter
    def EnableLbResponse(self, value):
        self._EnableLbResponse = value
        self.edit(EnableLbResponse=value)

    @EnableLtResponse.setter
    def EnableLtResponse(self, value):
        self._EnableLtResponse = value
        self.edit(EnableLtResponse=value)

    @EnableOverrideMdLevel.setter
    def EnableOverrideMdLevel(self, value):
        self._EnableOverrideMdLevel = value
        self.edit(EnableOverrideMdLevel=value)

    @OverrideMdLevel.setter
    def OverrideMdLevel(self, value):
        self._OverrideMdLevel = value
        self.edit(OverrideMdLevel=value)

    @EnableOverrideCcPeriod.setter
    def EnableOverrideCcPeriod(self, value):
        self._EnableOverrideCcPeriod = value
        self.edit(EnableOverrideCcPeriod=value)

    @OverrideCcPeriod.setter
    def OverrideCcPeriod(self, value):
        self._OverrideCcPeriod = value
        self.edit(OverrideCcPeriod=value)

    def _set_mptype_with_str(self, value):
        seperate = value.find(':')
        exec('self._MpType = EnumMpType.%s' % value[:seperate])

    def _set_rdi_with_str(self, value):
        seperate = value.find(':')
        exec('self._Rdi = EnumRdiValue.%s' % value[:seperate])

    def _set_vlan_with_str(self, value):
        try:
            self._Vlan = int(value)
        except ValueError:
            self._Vlan = hex(int(value, 16))

    def _set_enablelbresponse_with_str(self, value):
        self._EnableLbResponse = (value == 'True')

    def _set_enableltresponse_with_str(self, value):
        self._EnableLtResponse = (value == 'True')

    def _set_enableoverridemdlevel_with_str(self, value):
        self._EnableOverrideMdLevel = (value == 'True')

    def _set_overridemdlevel_with_str(self, value):
        seperate = value.find(':')
        exec('self._OverrideMdLevel = EnumMdLevel.%s' % value[:seperate])

    def _set_enableoverrideccperiod_with_str(self, value):
        self._EnableOverrideCcPeriod = (value == 'True')

    def _set_overrideccperiod_with_str(self, value):
        seperate = value.find(':')
        exec('self._OverrideCcPeriod = EnumCCPeriod.%s' % value[:seperate])

