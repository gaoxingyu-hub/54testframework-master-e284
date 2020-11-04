"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class OfpGlobalConfig(ROMObject):
    def __init__(self, Builtin=None, IsDefault=None, **kwargs):
        self._Builtin = Builtin  # Builtin
        self._IsDefault = IsDefault  # Default

        properties = kwargs.copy()
        if Builtin is not None:
            properties['Builtin'] = Builtin
        if IsDefault is not None:
            properties['IsDefault'] = IsDefault

        # call base class function, and it will send message to renix server to create a class.
        super(OfpGlobalConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Builtin=None, IsDefault=None, **kwargs):
        properties = kwargs.copy()
        if Builtin is not None:
            self._Builtin = Builtin
            properties['Builtin'] = Builtin
        if IsDefault is not None:
            self._IsDefault = IsDefault
            properties['IsDefault'] = IsDefault

        super(OfpGlobalConfig, self).edit(**properties)

    @property
    def Builtin(self):
        """
        get the value of property _Builtin
        """
        if self.force_auto_sync:
            self.get('Builtin')
        return self._Builtin

    @property
    def IsDefault(self):
        """
        get the value of property _IsDefault
        """
        if self.force_auto_sync:
            self.get('IsDefault')
        return self._IsDefault

    @Builtin.setter
    def Builtin(self, value):
        self._Builtin = value
        self.edit(Builtin=value)

    @IsDefault.setter
    def IsDefault(self, value):
        self._IsDefault = value
        self.edit(IsDefault=value)

    def _set_builtin_with_str(self, value):
        self._Builtin = (value == 'True')

    def _set_isdefault_with_str(self, value):
        self._IsDefault = (value == 'True')

