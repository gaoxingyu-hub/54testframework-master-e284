"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class TesterStats12(Result):
    def __init__(self, **kwargs):
        self._Stat11 = 0  # Stat11, not editable
        self._Stat12 = 0  # Stat12, not editable
        self._Stat13 = ''  # Stat13, not editable
        self._Stat15 = ''  # Stat15, not editable
        self._Stat21 = 0  # Stat21, not editable
        self._Stat22 = 0  # Stat22, not editable
        self._Stat23 = ''  # Stat23, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(TesterStats12, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def Stat11(self):
        """
        get the value of property _Stat11
        """
        if self.force_auto_sync:
            self.get('Stat11')
        return self._Stat11

    @property
    def Stat12(self):
        """
        get the value of property _Stat12
        """
        if self.force_auto_sync:
            self.get('Stat12')
        return self._Stat12

    @property
    def Stat13(self):
        """
        get the value of property _Stat13
        """
        if self.force_auto_sync:
            self.get('Stat13')
        return self._Stat13

    @property
    def Stat15(self):
        """
        get the value of property _Stat15
        """
        if self.force_auto_sync:
            self.get('Stat15')
        return self._Stat15

    @property
    def Stat21(self):
        """
        get the value of property _Stat21
        """
        if self.force_auto_sync:
            self.get('Stat21')
        return self._Stat21

    @property
    def Stat22(self):
        """
        get the value of property _Stat22
        """
        if self.force_auto_sync:
            self.get('Stat22')
        return self._Stat22

    @property
    def Stat23(self):
        """
        get the value of property _Stat23
        """
        if self.force_auto_sync:
            self.get('Stat23')
        return self._Stat23

    def _set_stat11_with_str(self, value):
        try:
            self._Stat11 = int(value)
        except ValueError:
            self._Stat11 = hex(int(value, 16))

    def _set_stat12_with_str(self, value):
        try:
            self._Stat12 = int(value)
        except ValueError:
            self._Stat12 = hex(int(value, 16))

    def _set_stat13_with_str(self, value):
        self._Stat13 = value

    def _set_stat15_with_str(self, value):
        self._Stat15 = value

    def _set_stat21_with_str(self, value):
        try:
            self._Stat21 = int(value)
        except ValueError:
            self._Stat21 = hex(int(value, 16))

    def _set_stat22_with_str(self, value):
        self._Stat22 = float(value)

    def _set_stat23_with_str(self, value):
        self._Stat23 = value

