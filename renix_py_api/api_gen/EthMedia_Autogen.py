"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Media_Autogen import Media


@rom_manager.rom
class EthMedia(Media):
    def __init__(self, **kwargs):
        self._EthMediaType = EnumMediaType.COPPER  # Media Type, not editable
        self._LinkStatus = EnumLinkStatus.DOWN  # Link Status, not editable
        self._LineSpeed = EnumLineSpeed.SPEED_1G  # Line Speed, not editable
        self._AutoNegotiation = True  # Auto Negotiation, not editable
        self._FlowControl = EnumFlowControl.DISABLE  # Flow Control, not editable
        self._Duplex = EnumDuplex.FULL  # Duplex, not editable
        self._FecType = EnumFecType.TYPE_OFF  # FEC Type, not editable
        self._DataPathMode = EnumDataPath.NORMAL  # Data Path Mode, not editable
        self._PpmAdjust = 0  # PPM Adjustment, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(EthMedia, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(EthMedia, self).edit(**properties)

    @property
    def EthMediaType(self):
        """
        get the value of property _EthMediaType
        """
        if self.force_auto_sync:
            self.get('EthMediaType')
        return self._EthMediaType

    @property
    def LinkStatus(self):
        """
        get the value of property _LinkStatus
        """
        if self.force_auto_sync:
            self.get('LinkStatus')
        return self._LinkStatus

    @property
    def LineSpeed(self):
        """
        get the value of property _LineSpeed
        """
        if self.force_auto_sync:
            self.get('LineSpeed')
        return self._LineSpeed

    @property
    def AutoNegotiation(self):
        """
        get the value of property _AutoNegotiation
        """
        if self.force_auto_sync:
            self.get('AutoNegotiation')
        return self._AutoNegotiation

    @property
    def FlowControl(self):
        """
        get the value of property _FlowControl
        """
        if self.force_auto_sync:
            self.get('FlowControl')
        return self._FlowControl

    @property
    def Duplex(self):
        """
        get the value of property _Duplex
        """
        if self.force_auto_sync:
            self.get('Duplex')
        return self._Duplex

    @property
    def FecType(self):
        """
        get the value of property _FecType
        """
        if self.force_auto_sync:
            self.get('FecType')
        return self._FecType

    @property
    def DataPathMode(self):
        """
        get the value of property _DataPathMode
        """
        if self.force_auto_sync:
            self.get('DataPathMode')
        return self._DataPathMode

    @property
    def PpmAdjust(self):
        """
        get the value of property _PpmAdjust
        """
        if self.force_auto_sync:
            self.get('PpmAdjust')
        return self._PpmAdjust

    def _set_ethmediatype_with_str(self, value):
        seperate = value.find(':')
        exec('self._EthMediaType = EnumMediaType.%s' % value[:seperate])

    def _set_linkstatus_with_str(self, value):
        seperate = value.find(':')
        exec('self._LinkStatus = EnumLinkStatus.%s' % value[:seperate])

    def _set_linespeed_with_str(self, value):
        seperate = value.find(':')
        exec('self._LineSpeed = EnumLineSpeed.%s' % value[:seperate])

    def _set_autonegotiation_with_str(self, value):
        self._AutoNegotiation = (value == 'True')

    def _set_flowcontrol_with_str(self, value):
        seperate = value.find(':')
        exec('self._FlowControl = EnumFlowControl.%s' % value[:seperate])

    def _set_duplex_with_str(self, value):
        seperate = value.find(':')
        exec('self._Duplex = EnumDuplex.%s' % value[:seperate])

    def _set_fectype_with_str(self, value):
        seperate = value.find(':')
        exec('self._FecType = EnumFecType.%s' % value[:seperate])

    def _set_datapathmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._DataPathMode = EnumDataPath.%s' % value[:seperate])

    def _set_ppmadjust_with_str(self, value):
        try:
            self._PpmAdjust = int(value)
        except ValueError:
            self._PpmAdjust = hex(int(value, 16))

