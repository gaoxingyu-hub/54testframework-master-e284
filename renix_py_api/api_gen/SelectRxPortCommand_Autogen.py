"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SelectRxPortCommand(ROMCommand):
    def __init__(self, StreamList=None, RxPortList=None, Mode=None, ExcludeTxPort=None, **kwargs):
        self._StreamList = StreamList  # Stream Handles
        self._RxPortList = RxPortList  # Rx Port
        self._Mode = Mode  # Select Mode
        self._ExcludeTxPort = ExcludeTxPort  # Exclude Tx Port

        properties = kwargs.copy()
        if StreamList is not None:
            properties['StreamList'] = StreamList
        if RxPortList is not None:
            properties['RxPortList'] = RxPortList
        if Mode is not None:
            properties['Mode'] = Mode
        if ExcludeTxPort is not None:
            properties['ExcludeTxPort'] = ExcludeTxPort

        # call base class function, and it will send message to renix server to create a class.
        super(SelectRxPortCommand, self).__init__(**properties)

    @property
    def StreamList(self):
        """
        get the value of property _StreamList
        """
        return self._StreamList

    @property
    def RxPortList(self):
        """
        get the value of property _RxPortList
        """
        return self._RxPortList

    @property
    def Mode(self):
        """
        get the value of property _Mode
        """
        return self._Mode

    @property
    def ExcludeTxPort(self):
        """
        get the value of property _ExcludeTxPort
        """
        return self._ExcludeTxPort

    @StreamList.setter
    def StreamList(self, value):
        self._StreamList = value

    @RxPortList.setter
    def RxPortList(self, value):
        self._RxPortList = value

    @Mode.setter
    def Mode(self, value):
        self._Mode = value

    @ExcludeTxPort.setter
    def ExcludeTxPort(self, value):
        self._ExcludeTxPort = value

    def _set_streamlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamList = tmp_value.split()

    def _set_rxportlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._RxPortList = tmp_value.split()

    def _set_mode_with_str(self, value):
        seperate = value.find(':')
        exec('self._Mode = EnumRxPortSelectMode.%s' % value[:seperate])

    def _set_excludetxport_with_str(self, value):
        self._ExcludeTxPort = (value == 'True')

