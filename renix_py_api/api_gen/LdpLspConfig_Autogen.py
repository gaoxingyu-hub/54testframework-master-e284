"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class LdpLspConfig(ROMObject):
    def __init__(self, FecType=None, FirstIp=None, Prefix=None, IpCount=None, Increment=None, ModifierBit=None, **kwargs):
        self._FecType = FecType  # FEC Type
        self._FirstIp = FirstIp  # First Prefix Address
        self._Prefix = Prefix  # Prefix Length
        self._IpCount = IpCount  # Count
        self._Increment = Increment  # Increment
        self._ModifierBit = ModifierBit  # Modifier Bit

        properties = kwargs.copy()
        if FecType is not None:
            properties['FecType'] = FecType
        if FirstIp is not None:
            properties['FirstIp'] = FirstIp
        if Prefix is not None:
            properties['Prefix'] = Prefix
        if IpCount is not None:
            properties['IpCount'] = IpCount
        if Increment is not None:
            properties['Increment'] = Increment
        if ModifierBit is not None:
            properties['ModifierBit'] = ModifierBit

        # call base class function, and it will send message to renix server to create a class.
        super(LdpLspConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, FecType=None, FirstIp=None, Prefix=None, IpCount=None, Increment=None, ModifierBit=None, **kwargs):
        properties = kwargs.copy()
        if FecType is not None:
            self._FecType = FecType
            properties['FecType'] = FecType
        if FirstIp is not None:
            self._FirstIp = FirstIp
            properties['FirstIp'] = FirstIp
        if Prefix is not None:
            self._Prefix = Prefix
            properties['Prefix'] = Prefix
        if IpCount is not None:
            self._IpCount = IpCount
            properties['IpCount'] = IpCount
        if Increment is not None:
            self._Increment = Increment
            properties['Increment'] = Increment
        if ModifierBit is not None:
            self._ModifierBit = ModifierBit
            properties['ModifierBit'] = ModifierBit

        super(LdpLspConfig, self).edit(**properties)

    @property
    def FecType(self):
        """
        get the value of property _FecType
        """
        if self.force_auto_sync:
            self.get('FecType')
        return self._FecType

    @property
    def FirstIp(self):
        """
        get the value of property _FirstIp
        """
        if self.force_auto_sync:
            self.get('FirstIp')
        return self._FirstIp

    @property
    def Prefix(self):
        """
        get the value of property _Prefix
        """
        if self.force_auto_sync:
            self.get('Prefix')
        return self._Prefix

    @property
    def IpCount(self):
        """
        get the value of property _IpCount
        """
        if self.force_auto_sync:
            self.get('IpCount')
        return self._IpCount

    @property
    def Increment(self):
        """
        get the value of property _Increment
        """
        if self.force_auto_sync:
            self.get('Increment')
        return self._Increment

    @property
    def ModifierBit(self):
        """
        get the value of property _ModifierBit
        """
        if self.force_auto_sync:
            self.get('ModifierBit')
        return self._ModifierBit

    @FecType.setter
    def FecType(self, value):
        self._FecType = value
        self.edit(FecType=value)

    @FirstIp.setter
    def FirstIp(self, value):
        self._FirstIp = value
        self.edit(FirstIp=value)

    @Prefix.setter
    def Prefix(self, value):
        self._Prefix = value
        self.edit(Prefix=value)

    @IpCount.setter
    def IpCount(self, value):
        self._IpCount = value
        self.edit(IpCount=value)

    @Increment.setter
    def Increment(self, value):
        self._Increment = value
        self.edit(Increment=value)

    @ModifierBit.setter
    def ModifierBit(self, value):
        self._ModifierBit = value
        self.edit(ModifierBit=value)

    def _set_fectype_with_str(self, value):
        seperate = value.find(':')
        exec('self._FecType = EnumFECType.%s' % value[:seperate])

    def _set_firstip_with_str(self, value):
        self._FirstIp = value

    def _set_prefix_with_str(self, value):
        try:
            self._Prefix = int(value)
        except ValueError:
            self._Prefix = hex(int(value, 16))

    def _set_ipcount_with_str(self, value):
        try:
            self._IpCount = int(value)
        except ValueError:
            self._IpCount = hex(int(value, 16))

    def _set_increment_with_str(self, value):
        try:
            self._Increment = int(value)
        except ValueError:
            self._Increment = hex(int(value, 16))

    def _set_modifierbit_with_str(self, value):
        try:
            self._ModifierBit = int(value)
        except ValueError:
            self._ModifierBit = hex(int(value, 16))

