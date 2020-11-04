"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class L47TestCaseState(ROMObject):
    def __init__(self, L47RunningState=None, **kwargs):
        self._L47RunningState = L47RunningState  # Layer 4-7 test case running state

        properties = kwargs.copy()
        if L47RunningState is not None:
            properties['L47RunningState'] = L47RunningState

        # call base class function, and it will send message to renix server to create a class.
        super(L47TestCaseState, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, L47RunningState=None, **kwargs):
        properties = kwargs.copy()
        if L47RunningState is not None:
            self._L47RunningState = L47RunningState
            properties['L47RunningState'] = L47RunningState

        super(L47TestCaseState, self).edit(**properties)

    @property
    def L47RunningState(self):
        """
        get the value of property _L47RunningState
        """
        if self.force_auto_sync:
            self.get('L47RunningState')
        return self._L47RunningState

    @L47RunningState.setter
    def L47RunningState(self, value):
        self._L47RunningState = value
        self.edit(L47RunningState=value)

    def _set_l47runningstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._L47RunningState = TestCaseState.%s' % value[:seperate])

