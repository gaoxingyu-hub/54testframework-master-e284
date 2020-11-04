"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class OvsdbResults(Result):
    def __init__(self, **kwargs):
        self._OvsdbHandle = ''  # OVSDB Handle, not editable
        self._State = 'Stopped'  # OVSDB State, not editable
        self._ReadCount = 0  # Read Count, not editable
        self._WriteCount = 0  # Write Count, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(OvsdbResults, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def OvsdbHandle(self):
        """
        get the value of property _OvsdbHandle
        """
        if self.force_auto_sync:
            self.get('OvsdbHandle')
        return self._OvsdbHandle

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def ReadCount(self):
        """
        get the value of property _ReadCount
        """
        if self.force_auto_sync:
            self.get('ReadCount')
        return self._ReadCount

    @property
    def WriteCount(self):
        """
        get the value of property _WriteCount
        """
        if self.force_auto_sync:
            self.get('WriteCount')
        return self._WriteCount

    def _set_ovsdbhandle_with_str(self, value):
        self._OvsdbHandle = value

    def _set_state_with_str(self, value):
        self._State = value

    def _set_readcount_with_str(self, value):
        try:
            self._ReadCount = int(value)
        except ValueError:
            self._ReadCount = hex(int(value, 16))

    def _set_writecount_with_str(self, value):
        try:
            self._WriteCount = int(value)
        except ValueError:
            self._WriteCount = hex(int(value, 16))

