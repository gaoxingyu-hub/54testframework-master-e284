"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class LdpLoadConfig(ROMObject):
    def __init__(self, LsrEstablishRate=None, LsrAdvertiseLspRate=None, LsrReleaseLspRate=None, FecPerLdpMsg=None, **kwargs):
        self._LsrEstablishRate = LsrEstablishRate  # LSR Establish Session Rate
        self._LsrAdvertiseLspRate = LsrAdvertiseLspRate  # LSR Advertise Lsp Rate
        self._LsrReleaseLspRate = LsrReleaseLspRate  # LSR Release Lsp Rate
        self._FecPerLdpMsg = FecPerLdpMsg  # FECs per LDP Message

        properties = kwargs.copy()
        if LsrEstablishRate is not None:
            properties['LsrEstablishRate'] = LsrEstablishRate
        if LsrAdvertiseLspRate is not None:
            properties['LsrAdvertiseLspRate'] = LsrAdvertiseLspRate
        if LsrReleaseLspRate is not None:
            properties['LsrReleaseLspRate'] = LsrReleaseLspRate
        if FecPerLdpMsg is not None:
            properties['FecPerLdpMsg'] = FecPerLdpMsg

        # call base class function, and it will send message to renix server to create a class.
        super(LdpLoadConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, LsrEstablishRate=None, LsrAdvertiseLspRate=None, LsrReleaseLspRate=None, FecPerLdpMsg=None, **kwargs):
        properties = kwargs.copy()
        if LsrEstablishRate is not None:
            self._LsrEstablishRate = LsrEstablishRate
            properties['LsrEstablishRate'] = LsrEstablishRate
        if LsrAdvertiseLspRate is not None:
            self._LsrAdvertiseLspRate = LsrAdvertiseLspRate
            properties['LsrAdvertiseLspRate'] = LsrAdvertiseLspRate
        if LsrReleaseLspRate is not None:
            self._LsrReleaseLspRate = LsrReleaseLspRate
            properties['LsrReleaseLspRate'] = LsrReleaseLspRate
        if FecPerLdpMsg is not None:
            self._FecPerLdpMsg = FecPerLdpMsg
            properties['FecPerLdpMsg'] = FecPerLdpMsg

        super(LdpLoadConfig, self).edit(**properties)

    @property
    def LsrEstablishRate(self):
        """
        get the value of property _LsrEstablishRate
        """
        if self.force_auto_sync:
            self.get('LsrEstablishRate')
        return self._LsrEstablishRate

    @property
    def LsrAdvertiseLspRate(self):
        """
        get the value of property _LsrAdvertiseLspRate
        """
        if self.force_auto_sync:
            self.get('LsrAdvertiseLspRate')
        return self._LsrAdvertiseLspRate

    @property
    def LsrReleaseLspRate(self):
        """
        get the value of property _LsrReleaseLspRate
        """
        if self.force_auto_sync:
            self.get('LsrReleaseLspRate')
        return self._LsrReleaseLspRate

    @property
    def FecPerLdpMsg(self):
        """
        get the value of property _FecPerLdpMsg
        """
        if self.force_auto_sync:
            self.get('FecPerLdpMsg')
        return self._FecPerLdpMsg

    @LsrEstablishRate.setter
    def LsrEstablishRate(self, value):
        self._LsrEstablishRate = value
        self.edit(LsrEstablishRate=value)

    @LsrAdvertiseLspRate.setter
    def LsrAdvertiseLspRate(self, value):
        self._LsrAdvertiseLspRate = value
        self.edit(LsrAdvertiseLspRate=value)

    @LsrReleaseLspRate.setter
    def LsrReleaseLspRate(self, value):
        self._LsrReleaseLspRate = value
        self.edit(LsrReleaseLspRate=value)

    @FecPerLdpMsg.setter
    def FecPerLdpMsg(self, value):
        self._FecPerLdpMsg = value
        self.edit(FecPerLdpMsg=value)

    def _set_lsrestablishrate_with_str(self, value):
        try:
            self._LsrEstablishRate = int(value)
        except ValueError:
            self._LsrEstablishRate = hex(int(value, 16))

    def _set_lsradvertiselsprate_with_str(self, value):
        try:
            self._LsrAdvertiseLspRate = int(value)
        except ValueError:
            self._LsrAdvertiseLspRate = hex(int(value, 16))

    def _set_lsrreleaselsprate_with_str(self, value):
        try:
            self._LsrReleaseLspRate = int(value)
        except ValueError:
            self._LsrReleaseLspRate = hex(int(value, 16))

    def _set_fecperldpmsg_with_str(self, value):
        try:
            self._FecPerLdpMsg = int(value)
        except ValueError:
            self._FecPerLdpMsg = hex(int(value, 16))

