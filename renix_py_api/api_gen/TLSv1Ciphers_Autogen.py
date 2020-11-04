"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TLSv1Ciphers(ROMObject):
    def __init__(self, AvailableCiphers=None, **kwargs):
        self._AvailableCiphers = AvailableCiphers  # Ciphers

        properties = kwargs.copy()
        if AvailableCiphers is not None:
            properties['AvailableCiphers'] = AvailableCiphers

        # call base class function, and it will send message to renix server to create a class.
        super(TLSv1Ciphers, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AvailableCiphers=None, **kwargs):
        properties = kwargs.copy()
        if AvailableCiphers is not None:
            self._AvailableCiphers = AvailableCiphers
            properties['AvailableCiphers'] = AvailableCiphers

        super(TLSv1Ciphers, self).edit(**properties)

    @property
    def AvailableCiphers(self):
        """
        get the value of property _AvailableCiphers
        """
        if self.force_auto_sync:
            self.get('AvailableCiphers')
        return self._AvailableCiphers

    @AvailableCiphers.setter
    def AvailableCiphers(self, value):
        self._AvailableCiphers = value
        self.edit(AvailableCiphers=value)

    def _set_availableciphers_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._AvailableCiphers = tmp_value.split()

