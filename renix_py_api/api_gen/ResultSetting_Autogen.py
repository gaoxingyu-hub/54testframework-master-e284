"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class ResultSetting(ROMObject):
    def __init__(self, ResultDirectory=None, Timestamp=None, **kwargs):
        self._ResultDirectory = ResultDirectory  # Result Directory
        self._Timestamp = Timestamp  # Time Stamp

        properties = kwargs.copy()
        if ResultDirectory is not None:
            properties['ResultDirectory'] = ResultDirectory
        if Timestamp is not None:
            properties['Timestamp'] = Timestamp

        # call base class function, and it will send message to renix server to create a class.
        super(ResultSetting, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ResultDirectory=None, Timestamp=None, **kwargs):
        properties = kwargs.copy()
        if ResultDirectory is not None:
            self._ResultDirectory = ResultDirectory
            properties['ResultDirectory'] = ResultDirectory
        if Timestamp is not None:
            self._Timestamp = Timestamp
            properties['Timestamp'] = Timestamp

        super(ResultSetting, self).edit(**properties)

    @property
    def ResultDirectory(self):
        """
        get the value of property _ResultDirectory
        """
        if self.force_auto_sync:
            self.get('ResultDirectory')
        return self._ResultDirectory

    @property
    def Timestamp(self):
        """
        get the value of property _Timestamp
        """
        if self.force_auto_sync:
            self.get('Timestamp')
        return self._Timestamp

    @ResultDirectory.setter
    def ResultDirectory(self, value):
        self._ResultDirectory = value
        self.edit(ResultDirectory=value)

    @Timestamp.setter
    def Timestamp(self, value):
        self._Timestamp = value
        self.edit(Timestamp=value)

    def _set_resultdirectory_with_str(self, value):
        self._ResultDirectory = value

    def _set_timestamp_with_str(self, value):
        self._Timestamp = value

