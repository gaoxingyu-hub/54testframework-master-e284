"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class GetOMRawDataFlowCommand(ROMCommand):
    def __init__(self, PortHandle=None, I2cAddress=None, Page=None, RegisterStart=None, RegisterEnd=None, **kwargs):
        self._PortHandle = PortHandle  # Port Handle
        self._I2cAddress = I2cAddress  # I2c Address
        self._Page = Page  # Page
        self._RegisterStart = RegisterStart  # Register Start(HEX)
        self._RegisterEnd = RegisterEnd  # Register End(HEX)
        self._DataFlow = None  # Values, not editable
        self._OmReadResult = EnumOMReadResult.OK  # OM Read Result, not editable

        properties = kwargs.copy()
        if PortHandle is not None:
            properties['PortHandle'] = PortHandle
        if I2cAddress is not None:
            properties['I2cAddress'] = I2cAddress
        if Page is not None:
            properties['Page'] = Page
        if RegisterStart is not None:
            properties['RegisterStart'] = RegisterStart
        if RegisterEnd is not None:
            properties['RegisterEnd'] = RegisterEnd

        # call base class function, and it will send message to renix server to create a class.
        super(GetOMRawDataFlowCommand, self).__init__(**properties)

    @property
    def PortHandle(self):
        """
        get the value of property _PortHandle
        """
        return self._PortHandle

    @property
    def I2cAddress(self):
        """
        get the value of property _I2cAddress
        """
        return self._I2cAddress

    @property
    def Page(self):
        """
        get the value of property _Page
        """
        return self._Page

    @property
    def RegisterStart(self):
        """
        get the value of property _RegisterStart
        """
        return self._RegisterStart

    @property
    def RegisterEnd(self):
        """
        get the value of property _RegisterEnd
        """
        return self._RegisterEnd

    @property
    def DataFlow(self):
        """
        get the value of property _DataFlow
        """
        return self._DataFlow

    @property
    def OmReadResult(self):
        """
        get the value of property _OmReadResult
        """
        return self._OmReadResult

    @PortHandle.setter
    def PortHandle(self, value):
        self._PortHandle = value

    @I2cAddress.setter
    def I2cAddress(self, value):
        self._I2cAddress = value

    @Page.setter
    def Page(self, value):
        self._Page = value

    @RegisterStart.setter
    def RegisterStart(self, value):
        self._RegisterStart = value

    @RegisterEnd.setter
    def RegisterEnd(self, value):
        self._RegisterEnd = value

    def _set_porthandle_with_str(self, value):
        self._PortHandle = value

    def _set_i2caddress_with_str(self, value):
        seperate = value.find(':')
        exec('self._I2cAddress = EnumI2cAddress.%s' % value[:seperate])

    def _set_page_with_str(self, value):
        try:
            self._Page = int(value)
        except ValueError:
            self._Page = hex(int(value, 16))

    def _set_registerstart_with_str(self, value):
        try:
            self._RegisterStart = int(value)
        except ValueError:
            self._RegisterStart = hex(int(value, 16))

    def _set_registerend_with_str(self, value):
        try:
            self._RegisterEnd = int(value)
        except ValueError:
            self._RegisterEnd = hex(int(value, 16))

    def _set_dataflow_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._DataFlow = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._DataFlow.append(int(str_value))
            except ValueError:
                self._DataFlow.append(hex(int(str_value, 16)))

    def _set_omreadresult_with_str(self, value):
        seperate = value.find(':')
        exec('self._OmReadResult = EnumOMReadResult.%s' % value[:seperate])

