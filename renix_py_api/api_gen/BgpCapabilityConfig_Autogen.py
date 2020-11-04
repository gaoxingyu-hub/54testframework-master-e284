"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class BgpCapabilityConfig(ROMObject):
    def __init__(self, CapabilityCode=None, CapabilityValue=None, **kwargs):
        self._CapabilityCode = CapabilityCode  # Capability Code
        self._CapabilityLength = 0  # Capability Length, not editable
        self._CapabilityValue = CapabilityValue  # Capability Value

        properties = kwargs.copy()
        if CapabilityCode is not None:
            properties['CapabilityCode'] = CapabilityCode
        if CapabilityValue is not None:
            properties['CapabilityValue'] = CapabilityValue

        # call base class function, and it will send message to renix server to create a class.
        super(BgpCapabilityConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, CapabilityCode=None, CapabilityValue=None, **kwargs):
        properties = kwargs.copy()
        if CapabilityCode is not None:
            self._CapabilityCode = CapabilityCode
            properties['CapabilityCode'] = CapabilityCode
        if CapabilityValue is not None:
            self._CapabilityValue = CapabilityValue
            properties['CapabilityValue'] = CapabilityValue

        super(BgpCapabilityConfig, self).edit(**properties)

    @property
    def CapabilityCode(self):
        """
        get the value of property _CapabilityCode
        """
        if self.force_auto_sync:
            self.get('CapabilityCode')
        return self._CapabilityCode

    @property
    def CapabilityLength(self):
        """
        get the value of property _CapabilityLength
        """
        if self.force_auto_sync:
            self.get('CapabilityLength')
        return self._CapabilityLength

    @property
    def CapabilityValue(self):
        """
        get the value of property _CapabilityValue
        """
        if self.force_auto_sync:
            self.get('CapabilityValue')
        return self._CapabilityValue

    @CapabilityCode.setter
    def CapabilityCode(self, value):
        self._CapabilityCode = value
        self.edit(CapabilityCode=value)

    @CapabilityValue.setter
    def CapabilityValue(self, value):
        self._CapabilityValue = value
        self.edit(CapabilityValue=value)

    def _set_capabilitycode_with_str(self, value):
        try:
            self._CapabilityCode = int(value)
        except ValueError:
            self._CapabilityCode = hex(int(value, 16))

    def _set_capabilitylength_with_str(self, value):
        try:
            self._CapabilityLength = int(value)
        except ValueError:
            self._CapabilityLength = hex(int(value, 16))

    def _set_capabilityvalue_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._CapabilityValue = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._CapabilityValue.append(int(str_value))
            except ValueError:
                self._CapabilityValue.append(hex(int(str_value, 16)))

