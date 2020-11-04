"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class ResultOption(ROMObject):
    def __init__(self, RefreshInterval=None, GridUnitsType=None, ChangeUnitsType=None, DecimalPlaces=None, **kwargs):
        self._RefreshInterval = RefreshInterval  # Result Refresh Interval
        self._GridUnitsType = GridUnitsType  # Grid Units Type
        self._ChangeUnitsType = ChangeUnitsType  # Change Units Type
        self._DecimalPlaces = DecimalPlaces  # Trial Times

        properties = kwargs.copy()
        if RefreshInterval is not None:
            properties['RefreshInterval'] = RefreshInterval
        if GridUnitsType is not None:
            properties['GridUnitsType'] = GridUnitsType
        if ChangeUnitsType is not None:
            properties['ChangeUnitsType'] = ChangeUnitsType
        if DecimalPlaces is not None:
            properties['DecimalPlaces'] = DecimalPlaces

        # call base class function, and it will send message to renix server to create a class.
        super(ResultOption, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RefreshInterval=None, GridUnitsType=None, ChangeUnitsType=None, DecimalPlaces=None, **kwargs):
        properties = kwargs.copy()
        if RefreshInterval is not None:
            self._RefreshInterval = RefreshInterval
            properties['RefreshInterval'] = RefreshInterval
        if GridUnitsType is not None:
            self._GridUnitsType = GridUnitsType
            properties['GridUnitsType'] = GridUnitsType
        if ChangeUnitsType is not None:
            self._ChangeUnitsType = ChangeUnitsType
            properties['ChangeUnitsType'] = ChangeUnitsType
        if DecimalPlaces is not None:
            self._DecimalPlaces = DecimalPlaces
            properties['DecimalPlaces'] = DecimalPlaces

        super(ResultOption, self).edit(**properties)

    @property
    def RefreshInterval(self):
        """
        get the value of property _RefreshInterval
        """
        if self.force_auto_sync:
            self.get('RefreshInterval')
        return self._RefreshInterval

    @property
    def GridUnitsType(self):
        """
        get the value of property _GridUnitsType
        """
        if self.force_auto_sync:
            self.get('GridUnitsType')
        return self._GridUnitsType

    @property
    def ChangeUnitsType(self):
        """
        get the value of property _ChangeUnitsType
        """
        if self.force_auto_sync:
            self.get('ChangeUnitsType')
        return self._ChangeUnitsType

    @property
    def DecimalPlaces(self):
        """
        get the value of property _DecimalPlaces
        """
        if self.force_auto_sync:
            self.get('DecimalPlaces')
        return self._DecimalPlaces

    @RefreshInterval.setter
    def RefreshInterval(self, value):
        self._RefreshInterval = value
        self.edit(RefreshInterval=value)

    @GridUnitsType.setter
    def GridUnitsType(self, value):
        self._GridUnitsType = value
        self.edit(GridUnitsType=value)

    @ChangeUnitsType.setter
    def ChangeUnitsType(self, value):
        self._ChangeUnitsType = value
        self.edit(ChangeUnitsType=value)

    @DecimalPlaces.setter
    def DecimalPlaces(self, value):
        self._DecimalPlaces = value
        self.edit(DecimalPlaces=value)

    def _set_refreshinterval_with_str(self, value):
        try:
            self._RefreshInterval = int(value)
        except ValueError:
            self._RefreshInterval = hex(int(value, 16))

    def _set_gridunitstype_with_str(self, value):
        seperate = value.find(':')
        exec('self._GridUnitsType = EnumUnitsType.%s' % value[:seperate])

    def _set_changeunitstype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ChangeUnitsType = EnumChangeUnitsType.%s' % value[:seperate])

    def _set_decimalplaces_with_str(self, value):
        try:
            self._DecimalPlaces = int(value)
        except ValueError:
            self._DecimalPlaces = hex(int(value, 16))

