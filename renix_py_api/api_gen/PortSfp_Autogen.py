"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class PortSfp(ROMObject):
    def __init__(self, **kwargs):
        self._VendorName = ''  # Vendor Name, not editable
        self._VendorPN = ''  # Vendor Part Number, not editable
        self._VendorSN = ''  # Vendor Serial Number, not editable
        self._VendorRev = ''  # Vendor Revision, not editable
        self._ManufactureDate = ''  # Manufacture Date, not editable
        self._TransceiverType = ''  # Transceiver Type, not editable
        self._TransceiverSpec = ''  # Transceiver Specification, not editable
        self._TransceiverDistance = ''  # Transceiver Distance, not editable
        self._ConnectorType = ''  # Connector Type, not editable
        self._WaveLength = ''  # Wave Length, not editable
        self._Temperature = ''  # Temperature, not editable
        self._TemperatureHighThreshold = ''  # Temperature High Threshold, not editable
        self._TemperatureLowThreshold = ''  # Temperature Low Threshold, not editable
        self._Voltage = ''  # Voltage, not editable
        self._VoltageHighThreshold = ''  # Voltage High Threshold, not editable
        self._VoltageLowThreshold = ''  # Voltage Low Threshold, not editable
        self._Bias = ''  # Bias, not editable
        self._BiasHighThreshold = ''  # Bias High Threshold, not editable
        self._BiasLowThreshold = ''  # Bias Low Threshold, not editable
        self._Power = ''  # Power, not editable
        self._RxPower = ''  # Rx Power, not editable
        self._RxPowerHighThreshold = ''  # Rx Power High Threshold, not editable
        self._RxPowerLowThreshold = ''  # Rx Power Low Threshold, not editable
        self._TxPower = ''  # Tx Power, not editable
        self._TxPowerHighThreshold = ''  # TxPower High Threshold, not editable
        self._TxPowerLowThreshold = ''  # TxPower Low Threshold, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(PortSfp, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(PortSfp, self).edit(**properties)

    @property
    def VendorName(self):
        """
        get the value of property _VendorName
        """
        if self.force_auto_sync:
            self.get('VendorName')
        return self._VendorName

    @property
    def VendorPN(self):
        """
        get the value of property _VendorPN
        """
        if self.force_auto_sync:
            self.get('VendorPN')
        return self._VendorPN

    @property
    def VendorSN(self):
        """
        get the value of property _VendorSN
        """
        if self.force_auto_sync:
            self.get('VendorSN')
        return self._VendorSN

    @property
    def VendorRev(self):
        """
        get the value of property _VendorRev
        """
        if self.force_auto_sync:
            self.get('VendorRev')
        return self._VendorRev

    @property
    def ManufactureDate(self):
        """
        get the value of property _ManufactureDate
        """
        if self.force_auto_sync:
            self.get('ManufactureDate')
        return self._ManufactureDate

    @property
    def TransceiverType(self):
        """
        get the value of property _TransceiverType
        """
        if self.force_auto_sync:
            self.get('TransceiverType')
        return self._TransceiverType

    @property
    def TransceiverSpec(self):
        """
        get the value of property _TransceiverSpec
        """
        if self.force_auto_sync:
            self.get('TransceiverSpec')
        return self._TransceiverSpec

    @property
    def TransceiverDistance(self):
        """
        get the value of property _TransceiverDistance
        """
        if self.force_auto_sync:
            self.get('TransceiverDistance')
        return self._TransceiverDistance

    @property
    def ConnectorType(self):
        """
        get the value of property _ConnectorType
        """
        if self.force_auto_sync:
            self.get('ConnectorType')
        return self._ConnectorType

    @property
    def WaveLength(self):
        """
        get the value of property _WaveLength
        """
        if self.force_auto_sync:
            self.get('WaveLength')
        return self._WaveLength

    @property
    def Temperature(self):
        """
        get the value of property _Temperature
        """
        if self.force_auto_sync:
            self.get('Temperature')
        return self._Temperature

    @property
    def TemperatureHighThreshold(self):
        """
        get the value of property _TemperatureHighThreshold
        """
        if self.force_auto_sync:
            self.get('TemperatureHighThreshold')
        return self._TemperatureHighThreshold

    @property
    def TemperatureLowThreshold(self):
        """
        get the value of property _TemperatureLowThreshold
        """
        if self.force_auto_sync:
            self.get('TemperatureLowThreshold')
        return self._TemperatureLowThreshold

    @property
    def Voltage(self):
        """
        get the value of property _Voltage
        """
        if self.force_auto_sync:
            self.get('Voltage')
        return self._Voltage

    @property
    def VoltageHighThreshold(self):
        """
        get the value of property _VoltageHighThreshold
        """
        if self.force_auto_sync:
            self.get('VoltageHighThreshold')
        return self._VoltageHighThreshold

    @property
    def VoltageLowThreshold(self):
        """
        get the value of property _VoltageLowThreshold
        """
        if self.force_auto_sync:
            self.get('VoltageLowThreshold')
        return self._VoltageLowThreshold

    @property
    def Bias(self):
        """
        get the value of property _Bias
        """
        if self.force_auto_sync:
            self.get('Bias')
        return self._Bias

    @property
    def BiasHighThreshold(self):
        """
        get the value of property _BiasHighThreshold
        """
        if self.force_auto_sync:
            self.get('BiasHighThreshold')
        return self._BiasHighThreshold

    @property
    def BiasLowThreshold(self):
        """
        get the value of property _BiasLowThreshold
        """
        if self.force_auto_sync:
            self.get('BiasLowThreshold')
        return self._BiasLowThreshold

    @property
    def Power(self):
        """
        get the value of property _Power
        """
        if self.force_auto_sync:
            self.get('Power')
        return self._Power

    @property
    def RxPower(self):
        """
        get the value of property _RxPower
        """
        if self.force_auto_sync:
            self.get('RxPower')
        return self._RxPower

    @property
    def RxPowerHighThreshold(self):
        """
        get the value of property _RxPowerHighThreshold
        """
        if self.force_auto_sync:
            self.get('RxPowerHighThreshold')
        return self._RxPowerHighThreshold

    @property
    def RxPowerLowThreshold(self):
        """
        get the value of property _RxPowerLowThreshold
        """
        if self.force_auto_sync:
            self.get('RxPowerLowThreshold')
        return self._RxPowerLowThreshold

    @property
    def TxPower(self):
        """
        get the value of property _TxPower
        """
        if self.force_auto_sync:
            self.get('TxPower')
        return self._TxPower

    @property
    def TxPowerHighThreshold(self):
        """
        get the value of property _TxPowerHighThreshold
        """
        if self.force_auto_sync:
            self.get('TxPowerHighThreshold')
        return self._TxPowerHighThreshold

    @property
    def TxPowerLowThreshold(self):
        """
        get the value of property _TxPowerLowThreshold
        """
        if self.force_auto_sync:
            self.get('TxPowerLowThreshold')
        return self._TxPowerLowThreshold

    def _set_vendorname_with_str(self, value):
        self._VendorName = value

    def _set_vendorpn_with_str(self, value):
        self._VendorPN = value

    def _set_vendorsn_with_str(self, value):
        self._VendorSN = value

    def _set_vendorrev_with_str(self, value):
        self._VendorRev = value

    def _set_manufacturedate_with_str(self, value):
        self._ManufactureDate = value

    def _set_transceivertype_with_str(self, value):
        self._TransceiverType = value

    def _set_transceiverspec_with_str(self, value):
        self._TransceiverSpec = value

    def _set_transceiverdistance_with_str(self, value):
        self._TransceiverDistance = value

    def _set_connectortype_with_str(self, value):
        self._ConnectorType = value

    def _set_wavelength_with_str(self, value):
        self._WaveLength = value

    def _set_temperature_with_str(self, value):
        self._Temperature = value

    def _set_temperaturehighthreshold_with_str(self, value):
        self._TemperatureHighThreshold = value

    def _set_temperaturelowthreshold_with_str(self, value):
        self._TemperatureLowThreshold = value

    def _set_voltage_with_str(self, value):
        self._Voltage = value

    def _set_voltagehighthreshold_with_str(self, value):
        self._VoltageHighThreshold = value

    def _set_voltagelowthreshold_with_str(self, value):
        self._VoltageLowThreshold = value

    def _set_bias_with_str(self, value):
        self._Bias = value

    def _set_biashighthreshold_with_str(self, value):
        self._BiasHighThreshold = value

    def _set_biaslowthreshold_with_str(self, value):
        self._BiasLowThreshold = value

    def _set_power_with_str(self, value):
        self._Power = value

    def _set_rxpower_with_str(self, value):
        self._RxPower = value

    def _set_rxpowerhighthreshold_with_str(self, value):
        self._RxPowerHighThreshold = value

    def _set_rxpowerlowthreshold_with_str(self, value):
        self._RxPowerLowThreshold = value

    def _set_txpower_with_str(self, value):
        self._TxPower = value

    def _set_txpowerhighthreshold_with_str(self, value):
        self._TxPowerHighThreshold = value

    def _set_txpowerlowthreshold_with_str(self, value):
        self._TxPowerLowThreshold = value

