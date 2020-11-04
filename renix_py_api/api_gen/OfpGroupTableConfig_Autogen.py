"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .OfpGlobalConfig_Autogen import OfpGlobalConfig


@rom_manager.rom
class OfpGroupTableConfig(OfpGlobalConfig):
    def __init__(self, ID=None, Type=None, **kwargs):
        self._ID = ID  # ID
        self._Type = Type  # Type

        properties = kwargs.copy()
        if ID is not None:
            properties['ID'] = ID
        if Type is not None:
            properties['Type'] = Type

        # call base class function, and it will send message to renix server to create a class.
        super(OfpGroupTableConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ID=None, Type=None, **kwargs):
        properties = kwargs.copy()
        if ID is not None:
            self._ID = ID
            properties['ID'] = ID
        if Type is not None:
            self._Type = Type
            properties['Type'] = Type

        super(OfpGroupTableConfig, self).edit(**properties)

    @property
    def ID(self):
        """
        get the value of property _ID
        """
        if self.force_auto_sync:
            self.get('ID')
        return self._ID

    @property
    def Type(self):
        """
        get the value of property _Type
        """
        if self.force_auto_sync:
            self.get('Type')
        return self._Type

    @ID.setter
    def ID(self, value):
        self._ID = value
        self.edit(ID=value)

    @Type.setter
    def Type(self, value):
        self._Type = value
        self.edit(Type=value)

    def _set_id_with_str(self, value):
        try:
            self._ID = int(value)
        except ValueError:
            self._ID = hex(int(value, 16))

    def _set_type_with_str(self, value):
        seperate = value.find(':')
        exec('self._Type = EnumOfpGroupTable.%s' % value[:seperate])

