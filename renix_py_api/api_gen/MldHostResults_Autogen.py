"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class MldHostResults(Result):
    def __init__(self, **kwargs):
        self._MldHostBlockId = ''  # Host Block, not editable
        self._MldTxFrames = 0  # Tx Frames, not editable
        self._MldRxFrames = 0  # Rx Frames, not editable
        self._MldRxUnknownTypes = 0  # Rx Unknown types, not editable
        self._MldRxChecksumErrors = 0  # Rx MLD Checksum Errors, not editable
        self._MldRxLengthErrors = 0  # Rx MLD Length Errors, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(MldHostResults, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def MldHostBlockId(self):
        """
        get the value of property _MldHostBlockId
        """
        if self.force_auto_sync:
            self.get('MldHostBlockId')
        return self._MldHostBlockId

    @property
    def MldTxFrames(self):
        """
        get the value of property _MldTxFrames
        """
        if self.force_auto_sync:
            self.get('MldTxFrames')
        return self._MldTxFrames

    @property
    def MldRxFrames(self):
        """
        get the value of property _MldRxFrames
        """
        if self.force_auto_sync:
            self.get('MldRxFrames')
        return self._MldRxFrames

    @property
    def MldRxUnknownTypes(self):
        """
        get the value of property _MldRxUnknownTypes
        """
        if self.force_auto_sync:
            self.get('MldRxUnknownTypes')
        return self._MldRxUnknownTypes

    @property
    def MldRxChecksumErrors(self):
        """
        get the value of property _MldRxChecksumErrors
        """
        if self.force_auto_sync:
            self.get('MldRxChecksumErrors')
        return self._MldRxChecksumErrors

    @property
    def MldRxLengthErrors(self):
        """
        get the value of property _MldRxLengthErrors
        """
        if self.force_auto_sync:
            self.get('MldRxLengthErrors')
        return self._MldRxLengthErrors

    def _set_mldhostblockid_with_str(self, value):
        self._MldHostBlockId = value

    def _set_mldtxframes_with_str(self, value):
        try:
            self._MldTxFrames = int(value)
        except ValueError:
            self._MldTxFrames = hex(int(value, 16))

    def _set_mldrxframes_with_str(self, value):
        try:
            self._MldRxFrames = int(value)
        except ValueError:
            self._MldRxFrames = hex(int(value, 16))

    def _set_mldrxunknowntypes_with_str(self, value):
        try:
            self._MldRxUnknownTypes = int(value)
        except ValueError:
            self._MldRxUnknownTypes = hex(int(value, 16))

    def _set_mldrxchecksumerrors_with_str(self, value):
        try:
            self._MldRxChecksumErrors = int(value)
        except ValueError:
            self._MldRxChecksumErrors = hex(int(value, 16))

    def _set_mldrxlengtherrors_with_str(self, value):
        try:
            self._MldRxLengthErrors = int(value)
        except ValueError:
            self._MldRxLengthErrors = hex(int(value, 16))

