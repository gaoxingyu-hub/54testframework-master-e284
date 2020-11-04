"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class OfpPortConfig(ROMObject):
    def __init__(self, PrivateKey=None, Certificate=None, CaCertificate=None, **kwargs):
        self._PrivateKey = PrivateKey  # Private Key
        self._Certificate = Certificate  # Certificate
        self._CaCertificate = CaCertificate  # CA Certificate

        properties = kwargs.copy()
        if PrivateKey is not None:
            properties['PrivateKey'] = PrivateKey
        if Certificate is not None:
            properties['Certificate'] = Certificate
        if CaCertificate is not None:
            properties['CaCertificate'] = CaCertificate

        # call base class function, and it will send message to renix server to create a class.
        super(OfpPortConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PrivateKey=None, Certificate=None, CaCertificate=None, **kwargs):
        properties = kwargs.copy()
        if PrivateKey is not None:
            self._PrivateKey = PrivateKey
            properties['PrivateKey'] = PrivateKey
        if Certificate is not None:
            self._Certificate = Certificate
            properties['Certificate'] = Certificate
        if CaCertificate is not None:
            self._CaCertificate = CaCertificate
            properties['CaCertificate'] = CaCertificate

        super(OfpPortConfig, self).edit(**properties)

    @property
    def PrivateKey(self):
        """
        get the value of property _PrivateKey
        """
        if self.force_auto_sync:
            self.get('PrivateKey')
        return self._PrivateKey

    @property
    def Certificate(self):
        """
        get the value of property _Certificate
        """
        if self.force_auto_sync:
            self.get('Certificate')
        return self._Certificate

    @property
    def CaCertificate(self):
        """
        get the value of property _CaCertificate
        """
        if self.force_auto_sync:
            self.get('CaCertificate')
        return self._CaCertificate

    @PrivateKey.setter
    def PrivateKey(self, value):
        self._PrivateKey = value
        self.edit(PrivateKey=value)

    @Certificate.setter
    def Certificate(self, value):
        self._Certificate = value
        self.edit(Certificate=value)

    @CaCertificate.setter
    def CaCertificate(self, value):
        self._CaCertificate = value
        self.edit(CaCertificate=value)

    def _set_privatekey_with_str(self, value):
        self._PrivateKey = value

    def _set_certificate_with_str(self, value):
        self._Certificate = value

    def _set_cacertificate_with_str(self, value):
        self._CaCertificate = value

