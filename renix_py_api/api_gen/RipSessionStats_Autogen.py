"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class RipSessionStats(Result):
    def __init__(self, **kwargs):
        self._SessionBlockId = ''  # RIP SessionBlock Name, not editable
        self._SessionId = 0  # RIP Session Index, not editable
        self._SessionState = 'Disabled'  # RIP Session State, not editable
        self._TxAdvertised = 0  # Tx Advertised Route Count, not editable
        self._RxAdvertised = 0  # Rx Advertised Route Count, not editable
        self._TxWithdrawn = 0  # Tx Withdrawn Route Count, not editable
        self._RxWithdrawn = 0  # Rx Withdrawn Route Count, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(RipSessionStats, self).__init__(**properties)

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
    def SessionId(self):
        """
        get the value of property _SessionId
        """
        if self.force_auto_sync:
            self.get('SessionId')
        return self._SessionId

    @property
    def SessionState(self):
        """
        get the value of property _SessionState
        """
        if self.force_auto_sync:
            self.get('SessionState')
        return self._SessionState

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

    def _set_sessionid_with_str(self, value):
        try:
            self._SessionId = int(value)
        except ValueError:
            self._SessionId = hex(int(value, 16))

    def _set_sessionstate_with_str(self, value):
        self._SessionState = value

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

