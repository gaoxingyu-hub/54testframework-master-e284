"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class KeepaliveOption(ROMObject):
    def __init__(self, EnableKeepalive=None, Interval=None, Timeout=None, **kwargs):
        self._EnableKeepalive = EnableKeepalive  # Enable Keepalive
        self._Interval = Interval  # Keepalive Interval (sec)
        self._Timeout = Timeout  # Keepalive Timeout (sec)

        properties = kwargs.copy()
        if EnableKeepalive is not None:
            properties['EnableKeepalive'] = EnableKeepalive
        if Interval is not None:
            properties['Interval'] = Interval
        if Timeout is not None:
            properties['Timeout'] = Timeout

        # call base class function, and it will send message to renix server to create a class.
        super(KeepaliveOption, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EnableKeepalive=None, Interval=None, Timeout=None, **kwargs):
        properties = kwargs.copy()
        if EnableKeepalive is not None:
            self._EnableKeepalive = EnableKeepalive
            properties['EnableKeepalive'] = EnableKeepalive
        if Interval is not None:
            self._Interval = Interval
            properties['Interval'] = Interval
        if Timeout is not None:
            self._Timeout = Timeout
            properties['Timeout'] = Timeout

        super(KeepaliveOption, self).edit(**properties)

    @property
    def EnableKeepalive(self):
        """
        get the value of property _EnableKeepalive
        """
        if self.force_auto_sync:
            self.get('EnableKeepalive')
        return self._EnableKeepalive

    @property
    def Interval(self):
        """
        get the value of property _Interval
        """
        if self.force_auto_sync:
            self.get('Interval')
        return self._Interval

    @property
    def Timeout(self):
        """
        get the value of property _Timeout
        """
        if self.force_auto_sync:
            self.get('Timeout')
        return self._Timeout

    @EnableKeepalive.setter
    def EnableKeepalive(self, value):
        self._EnableKeepalive = value
        self.edit(EnableKeepalive=value)

    @Interval.setter
    def Interval(self, value):
        self._Interval = value
        self.edit(Interval=value)

    @Timeout.setter
    def Timeout(self, value):
        self._Timeout = value
        self.edit(Timeout=value)

    def _set_enablekeepalive_with_str(self, value):
        self._EnableKeepalive = (value == 'True')

    def _set_interval_with_str(self, value):
        try:
            self._Interval = int(value)
        except ValueError:
            self._Interval = hex(int(value, 16))

    def _set_timeout_with_str(self, value):
        try:
            self._Timeout = int(value)
        except ValueError:
            self._Timeout = hex(int(value, 16))

