"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ReadPhyRegisterCommand(ROMCommand):
    def __init__(self, PortHandle=None, RegisterMode=None, Device=None, Address=None, **kwargs):
        self._PortHandle = PortHandle  # Port Handle
        self._RegisterMode = RegisterMode  # Register Mode
        self._Device = Device  # Register Address
        self._Address = Address  # Register Address
        self._RegisterValue = 0  # Register Value, not editable

        properties = kwargs.copy()
        if PortHandle is not None:
            properties['PortHandle'] = PortHandle
        if RegisterMode is not None:
            properties['RegisterMode'] = RegisterMode
        if Device is not None:
            properties['Device'] = Device
        if Address is not None:
            properties['Address'] = Address

        # call base class function, and it will send message to renix server to create a class.
        super(ReadPhyRegisterCommand, self).__init__(**properties)

    @property
    def PortHandle(self):
        """
        get the value of property _PortHandle
        """
        return self._PortHandle

    @property
    def RegisterMode(self):
        """
        get the value of property _RegisterMode
        """
        return self._RegisterMode

    @property
    def Device(self):
        """
        get the value of property _Device
        """
        return self._Device

    @property
    def Address(self):
        """
        get the value of property _Address
        """
        return self._Address

    @property
    def RegisterValue(self):
        """
        get the value of property _RegisterValue
        """
        return self._RegisterValue

    @PortHandle.setter
    def PortHandle(self, value):
        self._PortHandle = value

    @RegisterMode.setter
    def RegisterMode(self, value):
        self._RegisterMode = value

    @Device.setter
    def Device(self, value):
        self._Device = value

    @Address.setter
    def Address(self, value):
        self._Address = value

    def _set_porthandle_with_str(self, value):
        self._PortHandle = value

    def _set_registermode_with_str(self, value):
        try:
            self._RegisterMode = int(value)
        except ValueError:
            self._RegisterMode = hex(int(value, 16))

    def _set_device_with_str(self, value):
        try:
            self._Device = int(value)
        except ValueError:
            self._Device = hex(int(value, 16))

    def _set_address_with_str(self, value):
        try:
            self._Address = int(value)
        except ValueError:
            self._Address = hex(int(value, 16))

    def _set_registervalue_with_str(self, value):
        try:
            self._RegisterValue = int(value)
        except ValueError:
            self._RegisterValue = hex(int(value, 16))

    def _set_output_property(self, value):
        self._set_registervalue_with_str(value)

