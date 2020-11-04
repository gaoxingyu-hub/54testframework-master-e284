"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class LspPingConfig(ROMObject):
    def __init__(self, DestinationIpv4Address=None, PingInterval=None, PingTimeout=None, TimeToLive=None, ExperimentalBits=None, ValidateFecStack=None, NilFecLabel=None, PadData=None, **kwargs):
        self._LspPingType = EnumMplsLspPingType.CoreTunnelLspPing  # LSP Ping Type, not editable
        self._DestinationIpv4Address = DestinationIpv4Address  # Destination IPv4 Address
        self._PingInterval = PingInterval  # Ping Interval
        self._PingTimeout = PingTimeout  # Ping Timeout
        self._TimeToLive = TimeToLive  # Time To Live
        self._ExperimentalBits = ExperimentalBits  # Experimental (exp) Bits
        self._ValidateFecStack = ValidateFecStack  # Validate FEC Stack
        self._NilFecLabel = NilFecLabel  # Nil FEC Label
        self._PadMode = EnumMplsPadMode.TransmitWithoutPadTlv  # Pad Mode, not editable
        self._PadData = PadData  # Pad Data

        properties = kwargs.copy()
        if DestinationIpv4Address is not None:
            properties['DestinationIpv4Address'] = DestinationIpv4Address
        if PingInterval is not None:
            properties['PingInterval'] = PingInterval
        if PingTimeout is not None:
            properties['PingTimeout'] = PingTimeout
        if TimeToLive is not None:
            properties['TimeToLive'] = TimeToLive
        if ExperimentalBits is not None:
            properties['ExperimentalBits'] = ExperimentalBits
        if ValidateFecStack is not None:
            properties['ValidateFecStack'] = ValidateFecStack
        if NilFecLabel is not None:
            properties['NilFecLabel'] = NilFecLabel
        if PadData is not None:
            properties['PadData'] = PadData

        # call base class function, and it will send message to renix server to create a class.
        super(LspPingConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, DestinationIpv4Address=None, PingInterval=None, PingTimeout=None, TimeToLive=None, ExperimentalBits=None, ValidateFecStack=None, NilFecLabel=None, PadData=None, **kwargs):
        properties = kwargs.copy()
        if DestinationIpv4Address is not None:
            self._DestinationIpv4Address = DestinationIpv4Address
            properties['DestinationIpv4Address'] = DestinationIpv4Address
        if PingInterval is not None:
            self._PingInterval = PingInterval
            properties['PingInterval'] = PingInterval
        if PingTimeout is not None:
            self._PingTimeout = PingTimeout
            properties['PingTimeout'] = PingTimeout
        if TimeToLive is not None:
            self._TimeToLive = TimeToLive
            properties['TimeToLive'] = TimeToLive
        if ExperimentalBits is not None:
            self._ExperimentalBits = ExperimentalBits
            properties['ExperimentalBits'] = ExperimentalBits
        if ValidateFecStack is not None:
            self._ValidateFecStack = ValidateFecStack
            properties['ValidateFecStack'] = ValidateFecStack
        if NilFecLabel is not None:
            self._NilFecLabel = NilFecLabel
            properties['NilFecLabel'] = NilFecLabel
        if PadData is not None:
            self._PadData = PadData
            properties['PadData'] = PadData

        super(LspPingConfig, self).edit(**properties)

    @property
    def LspPingType(self):
        """
        get the value of property _LspPingType
        """
        if self.force_auto_sync:
            self.get('LspPingType')
        return self._LspPingType

    @property
    def DestinationIpv4Address(self):
        """
        get the value of property _DestinationIpv4Address
        """
        if self.force_auto_sync:
            self.get('DestinationIpv4Address')
        return self._DestinationIpv4Address

    @property
    def PingInterval(self):
        """
        get the value of property _PingInterval
        """
        if self.force_auto_sync:
            self.get('PingInterval')
        return self._PingInterval

    @property
    def PingTimeout(self):
        """
        get the value of property _PingTimeout
        """
        if self.force_auto_sync:
            self.get('PingTimeout')
        return self._PingTimeout

    @property
    def TimeToLive(self):
        """
        get the value of property _TimeToLive
        """
        if self.force_auto_sync:
            self.get('TimeToLive')
        return self._TimeToLive

    @property
    def ExperimentalBits(self):
        """
        get the value of property _ExperimentalBits
        """
        if self.force_auto_sync:
            self.get('ExperimentalBits')
        return self._ExperimentalBits

    @property
    def ValidateFecStack(self):
        """
        get the value of property _ValidateFecStack
        """
        if self.force_auto_sync:
            self.get('ValidateFecStack')
        return self._ValidateFecStack

    @property
    def NilFecLabel(self):
        """
        get the value of property _NilFecLabel
        """
        if self.force_auto_sync:
            self.get('NilFecLabel')
        return self._NilFecLabel

    @property
    def PadMode(self):
        """
        get the value of property _PadMode
        """
        if self.force_auto_sync:
            self.get('PadMode')
        return self._PadMode

    @property
    def PadData(self):
        """
        get the value of property _PadData
        """
        if self.force_auto_sync:
            self.get('PadData')
        return self._PadData

    @DestinationIpv4Address.setter
    def DestinationIpv4Address(self, value):
        self._DestinationIpv4Address = value
        self.edit(DestinationIpv4Address=value)

    @PingInterval.setter
    def PingInterval(self, value):
        self._PingInterval = value
        self.edit(PingInterval=value)

    @PingTimeout.setter
    def PingTimeout(self, value):
        self._PingTimeout = value
        self.edit(PingTimeout=value)

    @TimeToLive.setter
    def TimeToLive(self, value):
        self._TimeToLive = value
        self.edit(TimeToLive=value)

    @ExperimentalBits.setter
    def ExperimentalBits(self, value):
        self._ExperimentalBits = value
        self.edit(ExperimentalBits=value)

    @ValidateFecStack.setter
    def ValidateFecStack(self, value):
        self._ValidateFecStack = value
        self.edit(ValidateFecStack=value)

    @NilFecLabel.setter
    def NilFecLabel(self, value):
        self._NilFecLabel = value
        self.edit(NilFecLabel=value)

    @PadData.setter
    def PadData(self, value):
        self._PadData = value
        self.edit(PadData=value)

    def _set_lsppingtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._LspPingType = EnumMplsLspPingType.%s' % value[:seperate])

    def _set_destinationipv4address_with_str(self, value):
        self._DestinationIpv4Address = value

    def _set_pinginterval_with_str(self, value):
        try:
            self._PingInterval = int(value)
        except ValueError:
            self._PingInterval = hex(int(value, 16))

    def _set_pingtimeout_with_str(self, value):
        try:
            self._PingTimeout = int(value)
        except ValueError:
            self._PingTimeout = hex(int(value, 16))

    def _set_timetolive_with_str(self, value):
        if value == 'None':
            self._TimeToLive = None
            return
        try:
            self._TimeToLive = int(value)
        except ValueError:
            self._TimeToLive = hex(int(value, 16))

    def _set_experimentalbits_with_str(self, value):
        try:
            self._ExperimentalBits = int(value)
        except ValueError:
            self._ExperimentalBits = hex(int(value, 16))

    def _set_validatefecstack_with_str(self, value):
        self._ValidateFecStack = (value == 'True')

    def _set_nilfeclabel_with_str(self, value):
        self._NilFecLabel = (value == 'True')

    def _set_padmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._PadMode = EnumMplsPadMode.%s' % value[:seperate])

    def _set_paddata_with_str(self, value):
        self._PadData = value

