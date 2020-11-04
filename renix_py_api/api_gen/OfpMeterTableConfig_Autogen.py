"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .OfpGlobalConfig_Autogen import OfpGlobalConfig


@rom_manager.rom
class OfpMeterTableConfig(OfpGlobalConfig):
    def __init__(self, ID=None, BandUnit=None, EnableBurstSize=None, EnableStatistics=None, **kwargs):
        self._ID = ID  # ID
        self._BandUnit = BandUnit  # Band Unit
        self._EnableBurstSize = EnableBurstSize  # Enable Burst Size
        self._EnableStatistics = EnableStatistics  # Enable Statistics

        properties = kwargs.copy()
        if ID is not None:
            properties['ID'] = ID
        if BandUnit is not None:
            properties['BandUnit'] = BandUnit
        if EnableBurstSize is not None:
            properties['EnableBurstSize'] = EnableBurstSize
        if EnableStatistics is not None:
            properties['EnableStatistics'] = EnableStatistics

        # call base class function, and it will send message to renix server to create a class.
        super(OfpMeterTableConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ID=None, BandUnit=None, EnableBurstSize=None, EnableStatistics=None, **kwargs):
        properties = kwargs.copy()
        if ID is not None:
            self._ID = ID
            properties['ID'] = ID
        if BandUnit is not None:
            self._BandUnit = BandUnit
            properties['BandUnit'] = BandUnit
        if EnableBurstSize is not None:
            self._EnableBurstSize = EnableBurstSize
            properties['EnableBurstSize'] = EnableBurstSize
        if EnableStatistics is not None:
            self._EnableStatistics = EnableStatistics
            properties['EnableStatistics'] = EnableStatistics

        super(OfpMeterTableConfig, self).edit(**properties)

    @property
    def ID(self):
        """
        get the value of property _ID
        """
        if self.force_auto_sync:
            self.get('ID')
        return self._ID

    @property
    def BandUnit(self):
        """
        get the value of property _BandUnit
        """
        if self.force_auto_sync:
            self.get('BandUnit')
        return self._BandUnit

    @property
    def EnableBurstSize(self):
        """
        get the value of property _EnableBurstSize
        """
        if self.force_auto_sync:
            self.get('EnableBurstSize')
        return self._EnableBurstSize

    @property
    def EnableStatistics(self):
        """
        get the value of property _EnableStatistics
        """
        if self.force_auto_sync:
            self.get('EnableStatistics')
        return self._EnableStatistics

    @ID.setter
    def ID(self, value):
        self._ID = value
        self.edit(ID=value)

    @BandUnit.setter
    def BandUnit(self, value):
        self._BandUnit = value
        self.edit(BandUnit=value)

    @EnableBurstSize.setter
    def EnableBurstSize(self, value):
        self._EnableBurstSize = value
        self.edit(EnableBurstSize=value)

    @EnableStatistics.setter
    def EnableStatistics(self, value):
        self._EnableStatistics = value
        self.edit(EnableStatistics=value)

    def _set_id_with_str(self, value):
        try:
            self._ID = int(value)
        except ValueError:
            self._ID = hex(int(value, 16))

    def _set_bandunit_with_str(self, value):
        seperate = value.find(':')
        exec('self._BandUnit = EnumOfpBandUnit.%s' % value[:seperate])

    def _set_enableburstsize_with_str(self, value):
        self._EnableBurstSize = (value == 'True')

    def _set_enablestatistics_with_str(self, value):
        self._EnableStatistics = (value == 'True')

