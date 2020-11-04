"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class SimplePacketFilter(ROMObject):
    def __init__(self, DataMode=None, Mask=None, Data=None, Offset=None, **kwargs):
        self._DataMode = DataMode  # Data Mode
        self._Mask = Mask  # Filter Hex String Data Mask
        self._Data = Data  # Filter Hex or Template String Data
        self._Offset = Offset  # Filter Data Offset in 128

        properties = kwargs.copy()
        if DataMode is not None:
            properties['DataMode'] = DataMode
        if Mask is not None:
            properties['Mask'] = Mask
        if Data is not None:
            properties['Data'] = Data
        if Offset is not None:
            properties['Offset'] = Offset

        # call base class function, and it will send message to renix server to create a class.
        super(SimplePacketFilter, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, DataMode=None, Mask=None, Data=None, Offset=None, **kwargs):
        properties = kwargs.copy()
        if DataMode is not None:
            self._DataMode = DataMode
            properties['DataMode'] = DataMode
        if Mask is not None:
            self._Mask = Mask
            properties['Mask'] = Mask
        if Data is not None:
            self._Data = Data
            properties['Data'] = Data
        if Offset is not None:
            self._Offset = Offset
            properties['Offset'] = Offset

        super(SimplePacketFilter, self).edit(**properties)

    @property
    def DataMode(self):
        """
        get the value of property _DataMode
        """
        if self.force_auto_sync:
            self.get('DataMode')
        return self._DataMode

    @property
    def Mask(self):
        """
        get the value of property _Mask
        """
        if self.force_auto_sync:
            self.get('Mask')
        return self._Mask

    @property
    def Data(self):
        """
        get the value of property _Data
        """
        if self.force_auto_sync:
            self.get('Data')
        return self._Data

    @property
    def Offset(self):
        """
        get the value of property _Offset
        """
        if self.force_auto_sync:
            self.get('Offset')
        return self._Offset

    @DataMode.setter
    def DataMode(self, value):
        self._DataMode = value
        self.edit(DataMode=value)

    @Mask.setter
    def Mask(self, value):
        self._Mask = value
        self.edit(Mask=value)

    @Data.setter
    def Data(self, value):
        self._Data = value
        self.edit(Data=value)

    @Offset.setter
    def Offset(self, value):
        self._Offset = value
        self.edit(Offset=value)

    def _set_datamode_with_str(self, value):
        seperate = value.find(':')
        exec('self._DataMode = EnumDataMode.%s' % value[:seperate])

    def _set_mask_with_str(self, value):
        self._Mask = value

    def _set_data_with_str(self, value):
        self._Data = value

    def _set_offset_with_str(self, value):
        try:
            self._Offset = int(value)
        except ValueError:
            self._Offset = hex(int(value, 16))

