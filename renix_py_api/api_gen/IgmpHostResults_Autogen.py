"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class IgmpHostResults(Result):
    def __init__(self, **kwargs):
        self._IgmpHostBlockId = ''  # Host Block, not editable
        self._IgmpTxFrames = 0  # Tx Frames, not editable
        self._IgmpRxFrames = 0  # Rx Frames, not editable
        self._IgmpRxUnknownTypes = 0  # Rx Unknown types, not editable
        self._IgmpRxChecksumErrors = 0  # Rx IGMP Checksum Errors, not editable
        self._IgmpRxLengthErrors = 0  # Rx IGMP Length Errors, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(IgmpHostResults, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def IgmpHostBlockId(self):
        """
        get the value of property _IgmpHostBlockId
        """
        if self.force_auto_sync:
            self.get('IgmpHostBlockId')
        return self._IgmpHostBlockId

    @property
    def IgmpTxFrames(self):
        """
        get the value of property _IgmpTxFrames
        """
        if self.force_auto_sync:
            self.get('IgmpTxFrames')
        return self._IgmpTxFrames

    @property
    def IgmpRxFrames(self):
        """
        get the value of property _IgmpRxFrames
        """
        if self.force_auto_sync:
            self.get('IgmpRxFrames')
        return self._IgmpRxFrames

    @property
    def IgmpRxUnknownTypes(self):
        """
        get the value of property _IgmpRxUnknownTypes
        """
        if self.force_auto_sync:
            self.get('IgmpRxUnknownTypes')
        return self._IgmpRxUnknownTypes

    @property
    def IgmpRxChecksumErrors(self):
        """
        get the value of property _IgmpRxChecksumErrors
        """
        if self.force_auto_sync:
            self.get('IgmpRxChecksumErrors')
        return self._IgmpRxChecksumErrors

    @property
    def IgmpRxLengthErrors(self):
        """
        get the value of property _IgmpRxLengthErrors
        """
        if self.force_auto_sync:
            self.get('IgmpRxLengthErrors')
        return self._IgmpRxLengthErrors

    def _set_igmphostblockid_with_str(self, value):
        self._IgmpHostBlockId = value

    def _set_igmptxframes_with_str(self, value):
        try:
            self._IgmpTxFrames = int(value)
        except ValueError:
            self._IgmpTxFrames = hex(int(value, 16))

    def _set_igmprxframes_with_str(self, value):
        try:
            self._IgmpRxFrames = int(value)
        except ValueError:
            self._IgmpRxFrames = hex(int(value, 16))

    def _set_igmprxunknowntypes_with_str(self, value):
        try:
            self._IgmpRxUnknownTypes = int(value)
        except ValueError:
            self._IgmpRxUnknownTypes = hex(int(value, 16))

    def _set_igmprxchecksumerrors_with_str(self, value):
        try:
            self._IgmpRxChecksumErrors = int(value)
        except ValueError:
            self._IgmpRxChecksumErrors = hex(int(value, 16))

    def _set_igmprxlengtherrors_with_str(self, value):
        try:
            self._IgmpRxLengthErrors = int(value)
        except ValueError:
            self._IgmpRxLengthErrors = hex(int(value, 16))

