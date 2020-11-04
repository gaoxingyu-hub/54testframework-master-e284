"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class RomLogRecord(ROMObject):
    def __init__(self, Record=None, **kwargs):
        self._Record = Record  # Log Record

        properties = kwargs.copy()
        if Record is not None:
            properties['Record'] = Record

        # call base class function, and it will send message to renix server to create a class.
        super(RomLogRecord, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Record=None, **kwargs):
        properties = kwargs.copy()
        if Record is not None:
            self._Record = Record
            properties['Record'] = Record

        super(RomLogRecord, self).edit(**properties)

    @property
    def Record(self):
        """
        get the value of property _Record
        """
        if self.force_auto_sync:
            self.get('Record')
        return self._Record

    @Record.setter
    def Record(self, value):
        self._Record = value
        self.edit(Record=value)

    def _set_record_with_str(self, value):
        self._Record = value

