"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Port(ROMObject):
    def __init__(self, Location=None, **kwargs):
        self._Location = Location  # Port Location
        self._Online = False  # Online, not editable

        properties = kwargs.copy()
        if Location is not None:
            properties['Location'] = Location

        # call base class function, and it will send message to renix server to create a class.
        super(Port, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Location=None, **kwargs):
        properties = kwargs.copy()
        if Location is not None:
            self._Location = Location
            properties['Location'] = Location

        super(Port, self).edit(**properties)

    @property
    def Location(self):
        """
        get the value of property _Location
        """
        if self.force_auto_sync:
            self.get('Location')
        return self._Location

    @property
    def Online(self):
        """
        get the value of property _Online
        """
        if self.force_auto_sync:
            self.get('Online')
        return self._Online

    @Location.setter
    def Location(self, value):
        self._Location = value
        self.edit(Location=value)

    def _set_location_with_str(self, value):
        self._Location = value

    def _set_online_with_str(self, value):
        self._Online = (value == 'True')

