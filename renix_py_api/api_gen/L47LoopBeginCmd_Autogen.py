"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L47Command_Autogen import L47Command


@rom_manager.rom
class L47LoopBeginCmd(L47Command):
    def __init__(self, LoopCount=None, **kwargs):
        self._LoopCount = LoopCount  # Loop Count

        properties = kwargs.copy()
        if LoopCount is not None:
            properties['LoopCount'] = LoopCount

        # call base class function, and it will send message to renix server to create a class.
        super(L47LoopBeginCmd, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, LoopCount=None, **kwargs):
        properties = kwargs.copy()
        if LoopCount is not None:
            self._LoopCount = LoopCount
            properties['LoopCount'] = LoopCount

        super(L47LoopBeginCmd, self).edit(**properties)

    @property
    def LoopCount(self):
        """
        get the value of property _LoopCount
        """
        if self.force_auto_sync:
            self.get('LoopCount')
        return self._LoopCount

    @LoopCount.setter
    def LoopCount(self, value):
        self._LoopCount = value
        self.edit(LoopCount=value)

    def _set_loopcount_with_str(self, value):
        try:
            self._LoopCount = int(value)
        except ValueError:
            self._LoopCount = hex(int(value, 16))

