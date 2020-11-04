"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class IgmpQuerierResults(Result):
    def __init__(self, **kwargs):
        self._QuerierId = ''  # Querier handle, not editable
        self._QuerierTxFrames = 0  # Tx Frames, not editable
        self._QuerierRxFrames = 0  # Rx Frames, not editable
        self._QuerierRxUnknownTypes = 0  # Rx Unknown types, not editable
        self._QuerierRxChecksumErrors = 0  # Rx IGMP Checksum Errors, not editable
        self._QuerierRxLengthErrors = 0  # Rx IGMP Length Errors, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(IgmpQuerierResults, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def QuerierId(self):
        """
        get the value of property _QuerierId
        """
        if self.force_auto_sync:
            self.get('QuerierId')
        return self._QuerierId

    @property
    def QuerierTxFrames(self):
        """
        get the value of property _QuerierTxFrames
        """
        if self.force_auto_sync:
            self.get('QuerierTxFrames')
        return self._QuerierTxFrames

    @property
    def QuerierRxFrames(self):
        """
        get the value of property _QuerierRxFrames
        """
        if self.force_auto_sync:
            self.get('QuerierRxFrames')
        return self._QuerierRxFrames

    @property
    def QuerierRxUnknownTypes(self):
        """
        get the value of property _QuerierRxUnknownTypes
        """
        if self.force_auto_sync:
            self.get('QuerierRxUnknownTypes')
        return self._QuerierRxUnknownTypes

    @property
    def QuerierRxChecksumErrors(self):
        """
        get the value of property _QuerierRxChecksumErrors
        """
        if self.force_auto_sync:
            self.get('QuerierRxChecksumErrors')
        return self._QuerierRxChecksumErrors

    @property
    def QuerierRxLengthErrors(self):
        """
        get the value of property _QuerierRxLengthErrors
        """
        if self.force_auto_sync:
            self.get('QuerierRxLengthErrors')
        return self._QuerierRxLengthErrors

    def _set_querierid_with_str(self, value):
        self._QuerierId = value

    def _set_queriertxframes_with_str(self, value):
        try:
            self._QuerierTxFrames = int(value)
        except ValueError:
            self._QuerierTxFrames = hex(int(value, 16))

    def _set_querierrxframes_with_str(self, value):
        try:
            self._QuerierRxFrames = int(value)
        except ValueError:
            self._QuerierRxFrames = hex(int(value, 16))

    def _set_querierrxunknowntypes_with_str(self, value):
        try:
            self._QuerierRxUnknownTypes = int(value)
        except ValueError:
            self._QuerierRxUnknownTypes = hex(int(value, 16))

    def _set_querierrxchecksumerrors_with_str(self, value):
        try:
            self._QuerierRxChecksumErrors = int(value)
        except ValueError:
            self._QuerierRxChecksumErrors = hex(int(value, 16))

    def _set_querierrxlengtherrors_with_str(self, value):
        try:
            self._QuerierRxLengthErrors = int(value)
        except ValueError:
            self._QuerierRxLengthErrors = hex(int(value, 16))

