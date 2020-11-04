"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SwitchMediaCommand(ROMCommand):
    def __init__(self, MediaHandle=None, MediaType=None, **kwargs):
        self._MediaHandle = MediaHandle  # Media Handle
        self._MediaType = MediaType  # Media Type

        properties = kwargs.copy()
        if MediaHandle is not None:
            properties['MediaHandle'] = MediaHandle
        if MediaType is not None:
            properties['MediaType'] = MediaType

        # call base class function, and it will send message to renix server to create a class.
        super(SwitchMediaCommand, self).__init__(**properties)

    @property
    def MediaHandle(self):
        """
        get the value of property _MediaHandle
        """
        return self._MediaHandle

    @property
    def MediaType(self):
        """
        get the value of property _MediaType
        """
        return self._MediaType

    @MediaHandle.setter
    def MediaHandle(self, value):
        self._MediaHandle = value

    @MediaType.setter
    def MediaType(self, value):
        self._MediaType = value

    def _set_mediahandle_with_str(self, value):
        self._MediaHandle = value

    def _set_mediatype_with_str(self, value):
        seperate = value.find(':')
        exec('self._MediaType = EnumMediaType.%s' % value[:seperate])

