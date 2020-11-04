"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .CreateROMCommand_Autogen import CreateROMCommand


@rom_manager.rom
class CreateOfflinePortsCommand(CreateROMCommand):
    def __init__(self, PortName=None, MediaType=None, LineSpeed=None, **kwargs):
        self._PortName = PortName  # Port Name
        self._MediaType = MediaType  # Media Type
        self._LineSpeed = LineSpeed  # Line Speed

        properties = kwargs.copy()
        if PortName is not None:
            properties['PortName'] = PortName
        if MediaType is not None:
            properties['MediaType'] = MediaType
        if LineSpeed is not None:
            properties['LineSpeed'] = LineSpeed

        # call base class function, and it will send message to renix server to create a class.
        super(CreateOfflinePortsCommand, self).__init__(**properties)

    @property
    def PortName(self):
        """
        get the value of property _PortName
        """
        return self._PortName

    @property
    def MediaType(self):
        """
        get the value of property _MediaType
        """
        return self._MediaType

    @property
    def LineSpeed(self):
        """
        get the value of property _LineSpeed
        """
        return self._LineSpeed

    @PortName.setter
    def PortName(self, value):
        self._PortName = value

    @MediaType.setter
    def MediaType(self, value):
        self._MediaType = value

    @LineSpeed.setter
    def LineSpeed(self, value):
        self._LineSpeed = value

    def _set_portname_with_str(self, value):
        self._PortName = value

    def _set_mediatype_with_str(self, value):
        seperate = value.find(':')
        exec('self._MediaType = EnumMediaType.%s' % value[:seperate])

    def _set_linespeed_with_str(self, value):
        seperate = value.find(':')
        exec('self._LineSpeed = EnumLineSpeed.%s' % value[:seperate])

