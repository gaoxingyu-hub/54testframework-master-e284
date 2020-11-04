"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class PppoePortStatistic(Result):
    def __init__(self, **kwargs):
        self._PortHandle = ''  # Port Name, not editable
        self._SessionBlockCount = 0  # Session Block Count, not editable
        self._SessionCount = 0  # Session Count, not editable
        self._SessionsUp = 0  # Sessions Up, not editable
        self._SuccessfulConnects = 0  # Successful Connections, not editable
        self._FailedConnects = 0  # Failed Connections, not editable
        self._SucessfulDisconnects = 0  # Successful Disconnections, not editable
        self._FailedDisconnects = 0  # Failed Disconnections, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(PppoePortStatistic, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def PortHandle(self):
        """
        get the value of property _PortHandle
        """
        if self.force_auto_sync:
            self.get('PortHandle')
        return self._PortHandle

    @property
    def SessionBlockCount(self):
        """
        get the value of property _SessionBlockCount
        """
        if self.force_auto_sync:
            self.get('SessionBlockCount')
        return self._SessionBlockCount

    @property
    def SessionCount(self):
        """
        get the value of property _SessionCount
        """
        if self.force_auto_sync:
            self.get('SessionCount')
        return self._SessionCount

    @property
    def SessionsUp(self):
        """
        get the value of property _SessionsUp
        """
        if self.force_auto_sync:
            self.get('SessionsUp')
        return self._SessionsUp

    @property
    def SuccessfulConnects(self):
        """
        get the value of property _SuccessfulConnects
        """
        if self.force_auto_sync:
            self.get('SuccessfulConnects')
        return self._SuccessfulConnects

    @property
    def FailedConnects(self):
        """
        get the value of property _FailedConnects
        """
        if self.force_auto_sync:
            self.get('FailedConnects')
        return self._FailedConnects

    @property
    def SucessfulDisconnects(self):
        """
        get the value of property _SucessfulDisconnects
        """
        if self.force_auto_sync:
            self.get('SucessfulDisconnects')
        return self._SucessfulDisconnects

    @property
    def FailedDisconnects(self):
        """
        get the value of property _FailedDisconnects
        """
        if self.force_auto_sync:
            self.get('FailedDisconnects')
        return self._FailedDisconnects

    def _set_porthandle_with_str(self, value):
        self._PortHandle = value

    def _set_sessionblockcount_with_str(self, value):
        try:
            self._SessionBlockCount = int(value)
        except ValueError:
            self._SessionBlockCount = hex(int(value, 16))

    def _set_sessioncount_with_str(self, value):
        try:
            self._SessionCount = int(value)
        except ValueError:
            self._SessionCount = hex(int(value, 16))

    def _set_sessionsup_with_str(self, value):
        try:
            self._SessionsUp = int(value)
        except ValueError:
            self._SessionsUp = hex(int(value, 16))

    def _set_successfulconnects_with_str(self, value):
        try:
            self._SuccessfulConnects = int(value)
        except ValueError:
            self._SuccessfulConnects = hex(int(value, 16))

    def _set_failedconnects_with_str(self, value):
        try:
            self._FailedConnects = int(value)
        except ValueError:
            self._FailedConnects = hex(int(value, 16))

    def _set_sucessfuldisconnects_with_str(self, value):
        try:
            self._SucessfulDisconnects = int(value)
        except ValueError:
            self._SucessfulDisconnects = hex(int(value, 16))

    def _set_faileddisconnects_with_str(self, value):
        try:
            self._FailedDisconnects = int(value)
        except ValueError:
            self._FailedDisconnects = hex(int(value, 16))

