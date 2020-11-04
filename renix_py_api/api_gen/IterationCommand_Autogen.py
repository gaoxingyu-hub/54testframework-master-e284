"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .TrafficTestCommand_Autogen import TrafficTestCommand


@rom_manager.rom
class IterationCommand(TrafficTestCommand):
    def __init__(self, NeedCommit=None, **kwargs):
        self._NeedCommit = NeedCommit  # Should Apply

        properties = kwargs.copy()
        if NeedCommit is not None:
            properties['NeedCommit'] = NeedCommit

        # call base class function, and it will send message to renix server to create a class.
        super(IterationCommand, self).__init__(**properties)

    @property
    def NeedCommit(self):
        """
        get the value of property _NeedCommit
        """
        return self._NeedCommit

    @NeedCommit.setter
    def NeedCommit(self, value):
        self._NeedCommit = value

    def _set_needcommit_with_str(self, value):
        self._NeedCommit = (value == 'True')

