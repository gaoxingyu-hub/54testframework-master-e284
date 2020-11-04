"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class PimGroupStats(Result):
    def __init__(self, **kwargs):
        self._GroupID = ''  # Group Name, not editable
        self._SessionID = ''  # Session Name, not editable
        self._TxAnyG = 0  # Tx AnyG, not editable
        self._TxSG = 0  # Tx SG, not editable
        self._TxRP = 0  # Tx RP, not editable
        self._TxRpt = 0  # Tx RPT, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(PimGroupStats, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def GroupID(self):
        """
        get the value of property _GroupID
        """
        if self.force_auto_sync:
            self.get('GroupID')
        return self._GroupID

    @property
    def SessionID(self):
        """
        get the value of property _SessionID
        """
        if self.force_auto_sync:
            self.get('SessionID')
        return self._SessionID

    @property
    def TxAnyG(self):
        """
        get the value of property _TxAnyG
        """
        if self.force_auto_sync:
            self.get('TxAnyG')
        return self._TxAnyG

    @property
    def TxSG(self):
        """
        get the value of property _TxSG
        """
        if self.force_auto_sync:
            self.get('TxSG')
        return self._TxSG

    @property
    def TxRP(self):
        """
        get the value of property _TxRP
        """
        if self.force_auto_sync:
            self.get('TxRP')
        return self._TxRP

    @property
    def TxRpt(self):
        """
        get the value of property _TxRpt
        """
        if self.force_auto_sync:
            self.get('TxRpt')
        return self._TxRpt

    def _set_groupid_with_str(self, value):
        self._GroupID = value

    def _set_sessionid_with_str(self, value):
        self._SessionID = value

    def _set_txanyg_with_str(self, value):
        try:
            self._TxAnyG = int(value)
        except ValueError:
            self._TxAnyG = hex(int(value, 16))

    def _set_txsg_with_str(self, value):
        try:
            self._TxSG = int(value)
        except ValueError:
            self._TxSG = hex(int(value, 16))

    def _set_txrp_with_str(self, value):
        try:
            self._TxRP = int(value)
        except ValueError:
            self._TxRP = hex(int(value, 16))

    def _set_txrpt_with_str(self, value):
        try:
            self._TxRpt = int(value)
        except ValueError:
            self._TxRpt = hex(int(value, 16))

