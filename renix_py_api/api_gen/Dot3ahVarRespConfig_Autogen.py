"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Dot3ahVarCommonConfig_Autogen import Dot3ahVarCommonConfig


@rom_manager.rom
class Dot3ahVarRespConfig(Dot3ahVarCommonConfig):
    def __init__(self, Indication=None, Width=None, Data=None, **kwargs):
        self._Indication = Indication  # Indication
        self._Width = Width  # Width
        self._Data = Data  # Data

        properties = kwargs.copy()
        if Indication is not None:
            properties['Indication'] = Indication
        if Width is not None:
            properties['Width'] = Width
        if Data is not None:
            properties['Data'] = Data

        # call base class function, and it will send message to renix server to create a class.
        super(Dot3ahVarRespConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Indication=None, Width=None, Data=None, **kwargs):
        properties = kwargs.copy()
        if Indication is not None:
            self._Indication = Indication
            properties['Indication'] = Indication
        if Width is not None:
            self._Width = Width
            properties['Width'] = Width
        if Data is not None:
            self._Data = Data
            properties['Data'] = Data

        super(Dot3ahVarRespConfig, self).edit(**properties)

    @property
    def Indication(self):
        """
        get the value of property _Indication
        """
        if self.force_auto_sync:
            self.get('Indication')
        return self._Indication

    @property
    def Width(self):
        """
        get the value of property _Width
        """
        if self.force_auto_sync:
            self.get('Width')
        return self._Width

    @property
    def Data(self):
        """
        get the value of property _Data
        """
        if self.force_auto_sync:
            self.get('Data')
        return self._Data

    @Indication.setter
    def Indication(self, value):
        self._Indication = value
        self.edit(Indication=value)

    @Width.setter
    def Width(self, value):
        self._Width = value
        self.edit(Width=value)

    @Data.setter
    def Data(self, value):
        self._Data = value
        self.edit(Data=value)

    def _set_indication_with_str(self, value):
        self._Indication = (value == 'True')

    def _set_width_with_str(self, value):
        try:
            self._Width = int(value)
        except ValueError:
            self._Width = hex(int(value, 16))

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

