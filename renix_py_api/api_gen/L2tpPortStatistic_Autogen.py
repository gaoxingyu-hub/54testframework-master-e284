"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class L2tpPortStatistic(Result):
    def __init__(self, **kwargs):
        self._PortName = ''  # Port Name, not editable
        self._LacCount = 0  # LAC Count, not editable
        self._LnsCount = 0  # LNS Count, not editable
        self._TunnelCount = 0  # Tunnel Count, not editable
        self._SessionCount = 0  # Session Count, not editable
        self._TunnelUp = 0  # Tunnel Up, not editable
        self._TunnelDown = 0  # Tunnel Down, not editable
        self._SessionUp = 0  # Session Up, not editable
        self._SessionDown = 0  # Session Down, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(L2tpPortStatistic, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def PortName(self):
        """
        get the value of property _PortName
        """
        if self.force_auto_sync:
            self.get('PortName')
        return self._PortName

    @property
    def LacCount(self):
        """
        get the value of property _LacCount
        """
        if self.force_auto_sync:
            self.get('LacCount')
        return self._LacCount

    @property
    def LnsCount(self):
        """
        get the value of property _LnsCount
        """
        if self.force_auto_sync:
            self.get('LnsCount')
        return self._LnsCount

    @property
    def TunnelCount(self):
        """
        get the value of property _TunnelCount
        """
        if self.force_auto_sync:
            self.get('TunnelCount')
        return self._TunnelCount

    @property
    def SessionCount(self):
        """
        get the value of property _SessionCount
        """
        if self.force_auto_sync:
            self.get('SessionCount')
        return self._SessionCount

    @property
    def TunnelUp(self):
        """
        get the value of property _TunnelUp
        """
        if self.force_auto_sync:
            self.get('TunnelUp')
        return self._TunnelUp

    @property
    def TunnelDown(self):
        """
        get the value of property _TunnelDown
        """
        if self.force_auto_sync:
            self.get('TunnelDown')
        return self._TunnelDown

    @property
    def SessionUp(self):
        """
        get the value of property _SessionUp
        """
        if self.force_auto_sync:
            self.get('SessionUp')
        return self._SessionUp

    @property
    def SessionDown(self):
        """
        get the value of property _SessionDown
        """
        if self.force_auto_sync:
            self.get('SessionDown')
        return self._SessionDown

    def _set_portname_with_str(self, value):
        self._PortName = value

    def _set_laccount_with_str(self, value):
        try:
            self._LacCount = int(value)
        except ValueError:
            self._LacCount = hex(int(value, 16))

    def _set_lnscount_with_str(self, value):
        try:
            self._LnsCount = int(value)
        except ValueError:
            self._LnsCount = hex(int(value, 16))

    def _set_tunnelcount_with_str(self, value):
        try:
            self._TunnelCount = int(value)
        except ValueError:
            self._TunnelCount = hex(int(value, 16))

    def _set_sessioncount_with_str(self, value):
        try:
            self._SessionCount = int(value)
        except ValueError:
            self._SessionCount = hex(int(value, 16))

    def _set_tunnelup_with_str(self, value):
        try:
            self._TunnelUp = int(value)
        except ValueError:
            self._TunnelUp = hex(int(value, 16))

    def _set_tunneldown_with_str(self, value):
        try:
            self._TunnelDown = int(value)
        except ValueError:
            self._TunnelDown = hex(int(value, 16))

    def _set_sessionup_with_str(self, value):
        try:
            self._SessionUp = int(value)
        except ValueError:
            self._SessionUp = hex(int(value, 16))

    def _set_sessiondown_with_str(self, value):
        try:
            self._SessionDown = int(value)
        except ValueError:
            self._SessionDown = hex(int(value, 16))

