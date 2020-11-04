"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Dot1xUploadCertificateCommand(ROMCommand):
    def __init__(self, Dot1xConfig=None, CertificateFolder=None, **kwargs):
        self._Dot1xConfig = Dot1xConfig  # 802.1x Client Protocol Configs
        self._CertificateFolder = CertificateFolder  # Certificate Folder

        properties = kwargs.copy()
        if Dot1xConfig is not None:
            properties['Dot1xConfig'] = Dot1xConfig
        if CertificateFolder is not None:
            properties['CertificateFolder'] = CertificateFolder

        # call base class function, and it will send message to renix server to create a class.
        super(Dot1xUploadCertificateCommand, self).__init__(**properties)

    @property
    def Dot1xConfig(self):
        """
        get the value of property _Dot1xConfig
        """
        return self._Dot1xConfig

    @property
    def CertificateFolder(self):
        """
        get the value of property _CertificateFolder
        """
        return self._CertificateFolder

    @Dot1xConfig.setter
    def Dot1xConfig(self, value):
        self._Dot1xConfig = value

    @CertificateFolder.setter
    def CertificateFolder(self, value):
        self._CertificateFolder = value

    def _set_dot1xconfig_with_str(self, value):
        self._Dot1xConfig = value

    def _set_certificatefolder_with_str(self, value):
        self._CertificateFolder = value

