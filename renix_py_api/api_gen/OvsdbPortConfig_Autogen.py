"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class OvsdbPortConfig(ROMObject):
    def __init__(self, OvsdbConnectionType=None, PrivateKey=None, Certificate=None, CaCertificate=None, ConnectRate=None, **kwargs):
        self._OvsdbConnectionType = OvsdbConnectionType  # OVSDB Connection Type
        self._PrivateKey = PrivateKey  # Private Key
        self._Certificate = Certificate  # Certificate
        self._CaCertificate = CaCertificate  # CA Certificate
        self._ConnectRate = ConnectRate  # Connection Rate

        properties = kwargs.copy()
        if OvsdbConnectionType is not None:
            properties['OvsdbConnectionType'] = OvsdbConnectionType
        if PrivateKey is not None:
            properties['PrivateKey'] = PrivateKey
        if Certificate is not None:
            properties['Certificate'] = Certificate
        if CaCertificate is not None:
            properties['CaCertificate'] = CaCertificate
        if ConnectRate is not None:
            properties['ConnectRate'] = ConnectRate

        # call base class function, and it will send message to renix server to create a class.
        super(OvsdbPortConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, OvsdbConnectionType=None, PrivateKey=None, Certificate=None, CaCertificate=None, ConnectRate=None, **kwargs):
        properties = kwargs.copy()
        if OvsdbConnectionType is not None:
            self._OvsdbConnectionType = OvsdbConnectionType
            properties['OvsdbConnectionType'] = OvsdbConnectionType
        if PrivateKey is not None:
            self._PrivateKey = PrivateKey
            properties['PrivateKey'] = PrivateKey
        if Certificate is not None:
            self._Certificate = Certificate
            properties['Certificate'] = Certificate
        if CaCertificate is not None:
            self._CaCertificate = CaCertificate
            properties['CaCertificate'] = CaCertificate
        if ConnectRate is not None:
            self._ConnectRate = ConnectRate
            properties['ConnectRate'] = ConnectRate

        super(OvsdbPortConfig, self).edit(**properties)

    @property
    def OvsdbConnectionType(self):
        """
        get the value of property _OvsdbConnectionType
        """
        if self.force_auto_sync:
            self.get('OvsdbConnectionType')
        return self._OvsdbConnectionType

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

    @property
    def ConnectRate(self):
        """
        get the value of property _ConnectRate
        """
        if self.force_auto_sync:
            self.get('ConnectRate')
        return self._ConnectRate

    @OvsdbConnectionType.setter
    def OvsdbConnectionType(self, value):
        self._OvsdbConnectionType = value
        self.edit(OvsdbConnectionType=value)

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

    @ConnectRate.setter
    def ConnectRate(self, value):
        self._ConnectRate = value
        self.edit(ConnectRate=value)

    def _set_ovsdbconnectiontype_with_str(self, value):
        seperate = value.find(':')
        exec('self._OvsdbConnectionType = EnumOvsdbConnectionType.%s' % value[:seperate])

    def _set_privatekey_with_str(self, value):
        self._PrivateKey = value

    def _set_certificate_with_str(self, value):
        self._Certificate = value

    def _set_cacertificate_with_str(self, value):
        self._CaCertificate = value

    def _set_connectrate_with_str(self, value):
        try:
            self._ConnectRate = int(value)
        except ValueError:
            self._ConnectRate = hex(int(value, 16))

