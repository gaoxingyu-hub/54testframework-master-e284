"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class CheckPlCountCommand(ROMCommand):
    def __init__(self, ClListenPort=None, **kwargs):
        self._ClListenPort = ClListenPort  # Renix Server Listen Port
        self._ConnectDetail = EnumCheckPlDetail.CAN_CONNECT  # Connect details, not editable

        properties = kwargs.copy()
        if ClListenPort is not None:
            properties['ClListenPort'] = ClListenPort

        # call base class function, and it will send message to renix server to create a class.
        super(CheckPlCountCommand, self).__init__(**properties)

    @property
    def ClListenPort(self):
        """
        get the value of property _ClListenPort
        """
        return self._ClListenPort

    @property
    def ConnectDetail(self):
        """
        get the value of property _ConnectDetail
        """
        return self._ConnectDetail

    @ClListenPort.setter
    def ClListenPort(self, value):
        self._ClListenPort = value

    def _set_cllistenport_with_str(self, value):
        try:
            self._ClListenPort = int(value)
        except ValueError:
            self._ClListenPort = hex(int(value, 16))

    def _set_connectdetail_with_str(self, value):
        seperate = value.find(':')
        exec('self._ConnectDetail = EnumCheckPlDetail.%s' % value[:seperate])

    def _set_output_property(self, value):
        self._set_connectdetail_with_str(value)

