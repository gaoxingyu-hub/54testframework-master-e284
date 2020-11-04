"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .WizardConfigBase_Autogen import WizardConfigBase


@rom_manager.rom
class BgpImportRoutesWizardConfig(WizardConfigBase):
    def __init__(self, RoutesFileType=None, MaxImportedRoutes=None, RoutesFilePath=None, **kwargs):
        self._RoutesFileType = RoutesFileType  # BGP RouteTable File Type
        self._MaxImportedRoutes = MaxImportedRoutes  # Max Imported Routes Count
        self._RoutesFilePath = RoutesFilePath  # BGP RouteTable File Path

        properties = kwargs.copy()
        if RoutesFileType is not None:
            properties['RoutesFileType'] = RoutesFileType
        if MaxImportedRoutes is not None:
            properties['MaxImportedRoutes'] = MaxImportedRoutes
        if RoutesFilePath is not None:
            properties['RoutesFilePath'] = RoutesFilePath

        # call base class function, and it will send message to renix server to create a class.
        super(BgpImportRoutesWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RoutesFileType=None, MaxImportedRoutes=None, RoutesFilePath=None, **kwargs):
        properties = kwargs.copy()
        if RoutesFileType is not None:
            self._RoutesFileType = RoutesFileType
            properties['RoutesFileType'] = RoutesFileType
        if MaxImportedRoutes is not None:
            self._MaxImportedRoutes = MaxImportedRoutes
            properties['MaxImportedRoutes'] = MaxImportedRoutes
        if RoutesFilePath is not None:
            self._RoutesFilePath = RoutesFilePath
            properties['RoutesFilePath'] = RoutesFilePath

        super(BgpImportRoutesWizardConfig, self).edit(**properties)

    @property
    def RoutesFileType(self):
        """
        get the value of property _RoutesFileType
        """
        if self.force_auto_sync:
            self.get('RoutesFileType')
        return self._RoutesFileType

    @property
    def MaxImportedRoutes(self):
        """
        get the value of property _MaxImportedRoutes
        """
        if self.force_auto_sync:
            self.get('MaxImportedRoutes')
        return self._MaxImportedRoutes

    @property
    def RoutesFilePath(self):
        """
        get the value of property _RoutesFilePath
        """
        if self.force_auto_sync:
            self.get('RoutesFilePath')
        return self._RoutesFilePath

    @RoutesFileType.setter
    def RoutesFileType(self, value):
        self._RoutesFileType = value
        self.edit(RoutesFileType=value)

    @MaxImportedRoutes.setter
    def MaxImportedRoutes(self, value):
        self._MaxImportedRoutes = value
        self.edit(MaxImportedRoutes=value)

    @RoutesFilePath.setter
    def RoutesFilePath(self, value):
        self._RoutesFilePath = value
        self.edit(RoutesFilePath=value)

    def _set_routesfiletype_with_str(self, value):
        seperate = value.find(':')
        exec('self._RoutesFileType = EnumBgpRoutesFileType.%s' % value[:seperate])

    def _set_maximportedroutes_with_str(self, value):
        try:
            self._MaxImportedRoutes = int(value)
        except ValueError:
            self._MaxImportedRoutes = hex(int(value, 16))

    def _set_routesfilepath_with_str(self, value):
        self._RoutesFilePath = value

