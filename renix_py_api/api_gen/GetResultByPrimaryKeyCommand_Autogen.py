"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class GetResultByPrimaryKeyCommand(ROMCommand):
    def __init__(self, InternalPrimaryKey=None, **kwargs):
        self._InternalPrimaryKey = InternalPrimaryKey  # Internal Primary Key
        self._ResultObject = ''  # Result Object, not editable

        properties = kwargs.copy()
        if InternalPrimaryKey is not None:
            properties['InternalPrimaryKey'] = InternalPrimaryKey

        # call base class function, and it will send message to renix server to create a class.
        super(GetResultByPrimaryKeyCommand, self).__init__(**properties)

    @property
    def InternalPrimaryKey(self):
        """
        get the value of property _InternalPrimaryKey
        """
        return self._InternalPrimaryKey

    @property
    def ResultObject(self):
        """
        get the value of property _ResultObject
        """
        return self._ResultObject

    @InternalPrimaryKey.setter
    def InternalPrimaryKey(self, value):
        self._InternalPrimaryKey = value

    def _set_internalprimarykey_with_str(self, value):
        self._InternalPrimaryKey = value

    def _set_resultobject_with_str(self, value):
        self._ResultObject = value

    def _set_output_property(self, value):
        self._set_resultobject_with_str(value)

