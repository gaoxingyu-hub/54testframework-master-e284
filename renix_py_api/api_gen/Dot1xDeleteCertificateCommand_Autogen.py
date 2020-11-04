"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Dot1xDeleteCertificateCommand(ROMCommand):
    def __init__(self, Dot1xConfig=None, **kwargs):
        self._Dot1xConfig = Dot1xConfig  # 802.1x Client Protocol Configs

        properties = kwargs.copy()
        if Dot1xConfig is not None:
            properties['Dot1xConfig'] = Dot1xConfig

        # call base class function, and it will send message to renix server to create a class.
        super(Dot1xDeleteCertificateCommand, self).__init__(**properties)

    @property
    def Dot1xConfig(self):
        """
        get the value of property _Dot1xConfig
        """
        return self._Dot1xConfig

    @Dot1xConfig.setter
    def Dot1xConfig(self, value):
        self._Dot1xConfig = value

    def _set_dot1xconfig_with_str(self, value):
        self._Dot1xConfig = value

