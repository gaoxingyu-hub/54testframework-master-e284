"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ResultCommand_Autogen import ResultCommand


@rom_manager.rom
class SubscribeResultCommand(ResultCommand):
    def __init__(self, Interval=None, **kwargs):
        self._Interval = Interval  # Update interval

        properties = kwargs.copy()
        if Interval is not None:
            properties['Interval'] = Interval

        # call base class function, and it will send message to renix server to create a class.
        super(SubscribeResultCommand, self).__init__(**properties)

    @property
    def Interval(self):
        """
        get the value of property _Interval
        """
        return self._Interval

    @Interval.setter
    def Interval(self, value):
        self._Interval = value

    def _set_interval_with_str(self, value):
        try:
            self._Interval = int(value)
        except ValueError:
            self._Interval = hex(int(value, 16))

