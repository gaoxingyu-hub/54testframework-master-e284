"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class OfpMeterBandConfig(ROMObject):
    def __init__(self, Type=None, Rate=None, BurstSize=None, PrecLevel=None, ExperimenterID=None, **kwargs):
        self._Type = Type  # Type
        self._Rate = Rate  # Rate (per sec)
        self._BurstSize = BurstSize  # Burst Size
        self._PrecLevel = PrecLevel  # Drop Precedence Level
        self._ExperimenterID = ExperimenterID  # Experimenter ID

        properties = kwargs.copy()
        if Type is not None:
            properties['Type'] = Type
        if Rate is not None:
            properties['Rate'] = Rate
        if BurstSize is not None:
            properties['BurstSize'] = BurstSize
        if PrecLevel is not None:
            properties['PrecLevel'] = PrecLevel
        if ExperimenterID is not None:
            properties['ExperimenterID'] = ExperimenterID

        # call base class function, and it will send message to renix server to create a class.
        super(OfpMeterBandConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Type=None, Rate=None, BurstSize=None, PrecLevel=None, ExperimenterID=None, **kwargs):
        properties = kwargs.copy()
        if Type is not None:
            self._Type = Type
            properties['Type'] = Type
        if Rate is not None:
            self._Rate = Rate
            properties['Rate'] = Rate
        if BurstSize is not None:
            self._BurstSize = BurstSize
            properties['BurstSize'] = BurstSize
        if PrecLevel is not None:
            self._PrecLevel = PrecLevel
            properties['PrecLevel'] = PrecLevel
        if ExperimenterID is not None:
            self._ExperimenterID = ExperimenterID
            properties['ExperimenterID'] = ExperimenterID

        super(OfpMeterBandConfig, self).edit(**properties)

    @property
    def Type(self):
        """
        get the value of property _Type
        """
        if self.force_auto_sync:
            self.get('Type')
        return self._Type

    @property
    def Rate(self):
        """
        get the value of property _Rate
        """
        if self.force_auto_sync:
            self.get('Rate')
        return self._Rate

    @property
    def BurstSize(self):
        """
        get the value of property _BurstSize
        """
        if self.force_auto_sync:
            self.get('BurstSize')
        return self._BurstSize

    @property
    def PrecLevel(self):
        """
        get the value of property _PrecLevel
        """
        if self.force_auto_sync:
            self.get('PrecLevel')
        return self._PrecLevel

    @property
    def ExperimenterID(self):
        """
        get the value of property _ExperimenterID
        """
        if self.force_auto_sync:
            self.get('ExperimenterID')
        return self._ExperimenterID

    @Type.setter
    def Type(self, value):
        self._Type = value
        self.edit(Type=value)

    @Rate.setter
    def Rate(self, value):
        self._Rate = value
        self.edit(Rate=value)

    @BurstSize.setter
    def BurstSize(self, value):
        self._BurstSize = value
        self.edit(BurstSize=value)

    @PrecLevel.setter
    def PrecLevel(self, value):
        self._PrecLevel = value
        self.edit(PrecLevel=value)

    @ExperimenterID.setter
    def ExperimenterID(self, value):
        self._ExperimenterID = value
        self.edit(ExperimenterID=value)

    def _set_type_with_str(self, value):
        seperate = value.find(':')
        exec('self._Type = EnumOfpMeterBand.%s' % value[:seperate])

    def _set_rate_with_str(self, value):
        try:
            self._Rate = int(value)
        except ValueError:
            self._Rate = hex(int(value, 16))

    def _set_burstsize_with_str(self, value):
        try:
            self._BurstSize = int(value)
        except ValueError:
            self._BurstSize = hex(int(value, 16))

    def _set_preclevel_with_str(self, value):
        try:
            self._PrecLevel = int(value)
        except ValueError:
            self._PrecLevel = hex(int(value, 16))

    def _set_experimenterid_with_str(self, value):
        try:
            self._ExperimenterID = int(value)
        except ValueError:
            self._ExperimenterID = hex(int(value, 16))

