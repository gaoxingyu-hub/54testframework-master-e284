"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dot1agCommandConfig(ROMObject):
    def __init__(self, TxType=None, TxRate=None, InitTransactionId=None, **kwargs):
        self._TxType = TxType  # Tx Type
        self._TxRate = TxRate  # Tx Rate
        self._InitTransactionId = InitTransactionId  # Initial Transaction ID

        properties = kwargs.copy()
        if TxType is not None:
            properties['TxType'] = TxType
        if TxRate is not None:
            properties['TxRate'] = TxRate
        if InitTransactionId is not None:
            properties['InitTransactionId'] = InitTransactionId

        # call base class function, and it will send message to renix server to create a class.
        super(Dot1agCommandConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TxType=None, TxRate=None, InitTransactionId=None, **kwargs):
        properties = kwargs.copy()
        if TxType is not None:
            self._TxType = TxType
            properties['TxType'] = TxType
        if TxRate is not None:
            self._TxRate = TxRate
            properties['TxRate'] = TxRate
        if InitTransactionId is not None:
            self._InitTransactionId = InitTransactionId
            properties['InitTransactionId'] = InitTransactionId

        super(Dot1agCommandConfig, self).edit(**properties)

    @property
    def TxType(self):
        """
        get the value of property _TxType
        """
        if self.force_auto_sync:
            self.get('TxType')
        return self._TxType

    @property
    def TxRate(self):
        """
        get the value of property _TxRate
        """
        if self.force_auto_sync:
            self.get('TxRate')
        return self._TxRate

    @property
    def InitTransactionId(self):
        """
        get the value of property _InitTransactionId
        """
        if self.force_auto_sync:
            self.get('InitTransactionId')
        return self._InitTransactionId

    @TxType.setter
    def TxType(self, value):
        self._TxType = value
        self.edit(TxType=value)

    @TxRate.setter
    def TxRate(self, value):
        self._TxRate = value
        self.edit(TxRate=value)

    @InitTransactionId.setter
    def InitTransactionId(self, value):
        self._InitTransactionId = value
        self.edit(InitTransactionId=value)

    def _set_txtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._TxType = EnumTxType.%s' % value[:seperate])

    def _set_txrate_with_str(self, value):
        seperate = value.find(':')
        exec('self._TxRate = EnumTxRate.%s' % value[:seperate])

    def _set_inittransactionid_with_str(self, value):
        try:
            self._InitTransactionId = int(value)
        except ValueError:
            self._InitTransactionId = hex(int(value, 16))

