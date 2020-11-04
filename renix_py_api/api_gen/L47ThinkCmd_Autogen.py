"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L47Command_Autogen import L47Command


@rom_manager.rom
class L47ThinkCmd(L47Command):
    def __init__(self, ThinkTime=None, **kwargs):
        self._ThinkTime = ThinkTime  # Think Time (ms)

        properties = kwargs.copy()
        if ThinkTime is not None:
            properties['ThinkTime'] = ThinkTime

        # call base class function, and it will send message to renix server to create a class.
        super(L47ThinkCmd, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ThinkTime=None, **kwargs):
        properties = kwargs.copy()
        if ThinkTime is not None:
            self._ThinkTime = ThinkTime
            properties['ThinkTime'] = ThinkTime

        super(L47ThinkCmd, self).edit(**properties)

    @property
    def ThinkTime(self):
        """
        get the value of property _ThinkTime
        """
        if self.force_auto_sync:
            self.get('ThinkTime')
        return self._ThinkTime

    @ThinkTime.setter
    def ThinkTime(self, value):
        self._ThinkTime = value
        self.edit(ThinkTime=value)

    def _set_thinktime_with_str(self, value):
        try:
            self._ThinkTime = int(value)
        except ValueError:
            self._ThinkTime = hex(int(value, 16))

