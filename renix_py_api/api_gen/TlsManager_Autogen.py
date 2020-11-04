"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TlsManager(ROMObject):
    def __init__(self, CaCertFile=None, CertFile=None, PrivateKey=None, **kwargs):
        self._CaCertFile = CaCertFile  # CA Certificate
        self._CertFile = CertFile  # Certificate
        self._PrivateKey = PrivateKey  # Private Key

        properties = kwargs.copy()
        if CaCertFile is not None:
            properties['CaCertFile'] = CaCertFile
        if CertFile is not None:
            properties['CertFile'] = CertFile
        if PrivateKey is not None:
            properties['PrivateKey'] = PrivateKey

        # call base class function, and it will send message to renix server to create a class.
        super(TlsManager, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, CaCertFile=None, CertFile=None, PrivateKey=None, **kwargs):
        properties = kwargs.copy()
        if CaCertFile is not None:
            self._CaCertFile = CaCertFile
            properties['CaCertFile'] = CaCertFile
        if CertFile is not None:
            self._CertFile = CertFile
            properties['CertFile'] = CertFile
        if PrivateKey is not None:
            self._PrivateKey = PrivateKey
            properties['PrivateKey'] = PrivateKey

        super(TlsManager, self).edit(**properties)

    @property
    def CaCertFile(self):
        """
        get the value of property _CaCertFile
        """
        if self.force_auto_sync:
            self.get('CaCertFile')
        return self._CaCertFile

    @property
    def CertFile(self):
        """
        get the value of property _CertFile
        """
        if self.force_auto_sync:
            self.get('CertFile')
        return self._CertFile

    @property
    def PrivateKey(self):
        """
        get the value of property _PrivateKey
        """
        if self.force_auto_sync:
            self.get('PrivateKey')
        return self._PrivateKey

    @CaCertFile.setter
    def CaCertFile(self, value):
        self._CaCertFile = value
        self.edit(CaCertFile=value)

    @CertFile.setter
    def CertFile(self, value):
        self._CertFile = value
        self.edit(CertFile=value)

    @PrivateKey.setter
    def PrivateKey(self, value):
        self._PrivateKey = value
        self.edit(PrivateKey=value)

    def _set_cacertfile_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._CaCertFile = tmp_value.split()

    def _set_certfile_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._CertFile = tmp_value.split()

    def _set_privatekey_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PrivateKey = tmp_value.split()

