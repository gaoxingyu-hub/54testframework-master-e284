"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .CaptureCondition_Autogen import CaptureCondition


@rom_manager.rom
class CaptureByteCondition(CaptureCondition):
    def __init__(self, Mask=None, Data=None, Offset=None, **kwargs):
        self._Mask = Mask  # Mask (hex)
        self._Data = Data  # Data (hex)
        self._Offset = Offset  # Offset

        properties = kwargs.copy()
        if Mask is not None:
            properties['Mask'] = Mask
        if Data is not None:
            properties['Data'] = Data
        if Offset is not None:
            properties['Offset'] = Offset

        # call base class function, and it will send message to renix server to create a class.
        super(CaptureByteCondition, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Mask=None, Data=None, Offset=None, **kwargs):
        properties = kwargs.copy()
        if Mask is not None:
            self._Mask = Mask
            properties['Mask'] = Mask
        if Data is not None:
            self._Data = Data
            properties['Data'] = Data
        if Offset is not None:
            self._Offset = Offset
            properties['Offset'] = Offset

        super(CaptureByteCondition, self).edit(**properties)

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

    def _set_mask_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Mask = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._Mask.append(int(str_value))
            except ValueError:
                self._Mask.append(hex(int(str_value, 16)))

    def _set_data_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Data = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._Data.append(int(str_value))
            except ValueError:
                self._Data.append(hex(int(str_value, 16)))

    def _set_offset_with_str(self, value):
        try:
            self._Offset = int(value)
        except ValueError:
            self._Offset = hex(int(value, 16))

