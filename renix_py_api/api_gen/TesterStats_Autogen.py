"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class TesterStats(Result):
    def __init__(self, **kwargs):
        self._Stat1 = 0  # Stat1, not editable
        self._Stat2 = 0  # Stat2, not editable
        self._Stat3 = ''  # Stat3, not editable
        self._Stat5 = ''  # Stat5, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(TesterStats, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def Stat1(self):
        """
        get the value of property _Stat1
        """
        if self.force_auto_sync:
            self.get('Stat1')
        return self._Stat1

    @property
    def Stat2(self):
        """
        get the value of property _Stat2
        """
        if self.force_auto_sync:
            self.get('Stat2')
        return self._Stat2

    @property
    def Stat3(self):
        """
        get the value of property _Stat3
        """
        if self.force_auto_sync:
            self.get('Stat3')
        return self._Stat3

    @property
    def Stat5(self):
        """
        get the value of property _Stat5
        """
        if self.force_auto_sync:
            self.get('Stat5')
        return self._Stat5

    def _set_stat1_with_str(self, value):
        try:
            self._Stat1 = int(value)
        except ValueError:
            self._Stat1 = hex(int(value, 16))

    def _set_stat2_with_str(self, value):
        try:
            self._Stat2 = int(value)
        except ValueError:
            self._Stat2 = hex(int(value, 16))

    def _set_stat3_with_str(self, value):
        self._Stat3 = value

    def _set_stat5_with_str(self, value):
        self._Stat5 = value

