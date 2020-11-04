"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class EthMediaConfig(ROMObject):
    def __init__(self, EthMediaType=None, LineSpeed=None, AutoNegotiation=None, FlowControl=None, Duplex=None, FecType=None, DataPathMode=None, PpmAdjust=None, Mtu=None, **kwargs):
        self._EthMediaType = EthMediaType  # Media Type
        self._LineSpeed = LineSpeed  # Line Speed
        self._AutoNegotiation = AutoNegotiation  # Auto Negotiation
        self._FlowControl = FlowControl  # Flow Control
        self._Duplex = Duplex  # Duplex
        self._FecType = FecType  # FEC Type
        self._DataPathMode = DataPathMode  # Data Path Mode
        self._PpmAdjust = PpmAdjust  # PPM Adjustment
        self._Mtu = Mtu  # MTU

        properties = kwargs.copy()
        if EthMediaType is not None:
            properties['EthMediaType'] = EthMediaType
        if LineSpeed is not None:
            properties['LineSpeed'] = LineSpeed
        if AutoNegotiation is not None:
            properties['AutoNegotiation'] = AutoNegotiation
        if FlowControl is not None:
            properties['FlowControl'] = FlowControl
        if Duplex is not None:
            properties['Duplex'] = Duplex
        if FecType is not None:
            properties['FecType'] = FecType
        if DataPathMode is not None:
            properties['DataPathMode'] = DataPathMode
        if PpmAdjust is not None:
            properties['PpmAdjust'] = PpmAdjust
        if Mtu is not None:
            properties['Mtu'] = Mtu

        # call base class function, and it will send message to renix server to create a class.
        super(EthMediaConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EthMediaType=None, LineSpeed=None, AutoNegotiation=None, FlowControl=None, Duplex=None, FecType=None, DataPathMode=None, PpmAdjust=None, Mtu=None, **kwargs):
        properties = kwargs.copy()
        if EthMediaType is not None:
            self._EthMediaType = EthMediaType
            properties['EthMediaType'] = EthMediaType
        if LineSpeed is not None:
            self._LineSpeed = LineSpeed
            properties['LineSpeed'] = LineSpeed
        if AutoNegotiation is not None:
            self._AutoNegotiation = AutoNegotiation
            properties['AutoNegotiation'] = AutoNegotiation
        if FlowControl is not None:
            self._FlowControl = FlowControl
            properties['FlowControl'] = FlowControl
        if Duplex is not None:
            self._Duplex = Duplex
            properties['Duplex'] = Duplex
        if FecType is not None:
            self._FecType = FecType
            properties['FecType'] = FecType
        if DataPathMode is not None:
            self._DataPathMode = DataPathMode
            properties['DataPathMode'] = DataPathMode
        if PpmAdjust is not None:
            self._PpmAdjust = PpmAdjust
            properties['PpmAdjust'] = PpmAdjust
        if Mtu is not None:
            self._Mtu = Mtu
            properties['Mtu'] = Mtu

        super(EthMediaConfig, self).edit(**properties)

    @property
    def EthMediaType(self):
        """
        get the value of property _EthMediaType
        """
        if self.force_auto_sync:
            self.get('EthMediaType')
        return self._EthMediaType

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

    @property
    def Mtu(self):
        """
        get the value of property _Mtu
        """
        if self.force_auto_sync:
            self.get('Mtu')
        return self._Mtu

    @EthMediaType.setter
    def EthMediaType(self, value):
        self._EthMediaType = value
        self.edit(EthMediaType=value)

    @LineSpeed.setter
    def LineSpeed(self, value):
        self._LineSpeed = value
        self.edit(LineSpeed=value)

    @AutoNegotiation.setter
    def AutoNegotiation(self, value):
        self._AutoNegotiation = value
        self.edit(AutoNegotiation=value)

    @FlowControl.setter
    def FlowControl(self, value):
        self._FlowControl = value
        self.edit(FlowControl=value)

    @Duplex.setter
    def Duplex(self, value):
        self._Duplex = value
        self.edit(Duplex=value)

    @FecType.setter
    def FecType(self, value):
        self._FecType = value
        self.edit(FecType=value)

    @DataPathMode.setter
    def DataPathMode(self, value):
        self._DataPathMode = value
        self.edit(DataPathMode=value)

    @PpmAdjust.setter
    def PpmAdjust(self, value):
        self._PpmAdjust = value
        self.edit(PpmAdjust=value)

    @Mtu.setter
    def Mtu(self, value):
        self._Mtu = value
        self.edit(Mtu=value)

    def _set_ethmediatype_with_str(self, value):
        seperate = value.find(':')
        exec('self._EthMediaType = EnumMediaType.%s' % value[:seperate])

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

    def _set_mtu_with_str(self, value):
        try:
            self._Mtu = int(value)
        except ValueError:
            self._Mtu = hex(int(value, 16))

