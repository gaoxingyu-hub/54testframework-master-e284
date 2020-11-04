"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class RipSessionBlockStats(Result):
    def __init__(self, **kwargs):
        self._SessionBlockId = ''  # RIP SessionBlock Name, not editable
        self._SessionCount = 0  # RIP Session Count, not editable
        self._TxAdvertised = 0  # Tx Advertised Route Count, not editable
        self._RxAdvertised = 0  # Rx Advertised Route Count, not editable
        self._TxWithdrawn = 0  # Tx Withdrawn Route Count, not editable
        self._RxWithdrawn = 0  # Rx Withdrawn Route Count, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(RipSessionBlockStats, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def SessionBlockId(self):
        """
        get the value of property _SessionBlockId
        """
        if self.force_auto_sync:
            self.get('SessionBlockId')
        return self._SessionBlockId

    @property
    def SessionCount(self):
        """
        get the value of property _SessionCount
        """
        if self.force_auto_sync:
            self.get('SessionCount')
        return self._SessionCount

    @property
    def TxAdvertised(self):
        """
        get the value of property _TxAdvertised
        """
        if self.force_auto_sync:
            self.get('TxAdvertised')
        return self._TxAdvertised

    @property
    def RxAdvertised(self):
        """
        get the value of property _RxAdvertised
        """
        if self.force_auto_sync:
            self.get('RxAdvertised')
        return self._RxAdvertised

    @property
    def TxWithdrawn(self):
        """
        get the value of property _TxWithdrawn
        """
        if self.force_auto_sync:
            self.get('TxWithdrawn')
        return self._TxWithdrawn

    @property
    def RxWithdrawn(self):
        """
        get the value of property _RxWithdrawn
        """
        if self.force_auto_sync:
            self.get('RxWithdrawn')
        return self._RxWithdrawn

    def _set_sessionblockid_with_str(self, value):
        self._SessionBlockId = value

    def _set_sessioncount_with_str(self, value):
        try:
            self._SessionCount = int(value)
        except ValueError:
            self._SessionCount = hex(int(value, 16))

    def _set_txadvertised_with_str(self, value):
        try:
            self._TxAdvertised = int(value)
        except ValueError:
            self._TxAdvertised = hex(int(value, 16))

    def _set_rxadvertised_with_str(self, value):
        try:
            self._RxAdvertised = int(value)
        except ValueError:
            self._RxAdvertised = hex(int(value, 16))

    def _set_txwithdrawn_with_str(self, value):
        try:
            self._TxWithdrawn = int(value)
        except ValueError:
            self._TxWithdrawn = hex(int(value, 16))

    def _set_rxwithdrawn_with_str(self, value):
        try:
            self._RxWithdrawn = int(value)
        except ValueError:
            self._RxWithdrawn = hex(int(value, 16))

