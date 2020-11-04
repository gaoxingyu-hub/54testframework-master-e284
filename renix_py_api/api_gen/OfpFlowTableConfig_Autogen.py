"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .OfpGlobalConfig_Autogen import OfpGlobalConfig


@rom_manager.rom
class OfpFlowTableConfig(OfpGlobalConfig):
    def __init__(self, ID=None, TableMissAction=None, **kwargs):
        self._ID = ID  # ID
        self._TableMissAction = TableMissAction  # Table-miss Action

        properties = kwargs.copy()
        if ID is not None:
            properties['ID'] = ID
        if TableMissAction is not None:
            properties['TableMissAction'] = TableMissAction

        # call base class function, and it will send message to renix server to create a class.
        super(OfpFlowTableConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ID=None, TableMissAction=None, **kwargs):
        properties = kwargs.copy()
        if ID is not None:
            self._ID = ID
            properties['ID'] = ID
        if TableMissAction is not None:
            self._TableMissAction = TableMissAction
            properties['TableMissAction'] = TableMissAction

        super(OfpFlowTableConfig, self).edit(**properties)

    @property
    def ID(self):
        """
        get the value of property _ID
        """
        if self.force_auto_sync:
            self.get('ID')
        return self._ID

    @property
    def TableMissAction(self):
        """
        get the value of property _TableMissAction
        """
        if self.force_auto_sync:
            self.get('TableMissAction')
        return self._TableMissAction

    @ID.setter
    def ID(self, value):
        self._ID = value
        self.edit(ID=value)

    @TableMissAction.setter
    def TableMissAction(self, value):
        self._TableMissAction = value
        self.edit(TableMissAction=value)

    def _set_id_with_str(self, value):
        try:
            self._ID = int(value)
        except ValueError:
            self._ID = hex(int(value, 16))

    def _set_tablemissaction_with_str(self, value):
        seperate = value.find(':')
        exec('self._TableMissAction = EnumOfpTableMiss.%s' % value[:seperate])

