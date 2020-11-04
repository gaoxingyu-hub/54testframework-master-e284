"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class EditBreakPointCommand(ROMCommand):
    def __init__(self, BreakPointHandle=None, InsertBreakPoint=None, **kwargs):
        self._BreakPointHandle = BreakPointHandle  # Break Point
        self._InsertBreakPoint = InsertBreakPoint  # Insert Break Point

        properties = kwargs.copy()
        if BreakPointHandle is not None:
            properties['BreakPointHandle'] = BreakPointHandle
        if InsertBreakPoint is not None:
            properties['InsertBreakPoint'] = InsertBreakPoint

        # call base class function, and it will send message to renix server to create a class.
        super(EditBreakPointCommand, self).__init__(**properties)

    @property
    def BreakPointHandle(self):
        """
        get the value of property _BreakPointHandle
        """
        return self._BreakPointHandle

    @property
    def InsertBreakPoint(self):
        """
        get the value of property _InsertBreakPoint
        """
        return self._InsertBreakPoint

    @BreakPointHandle.setter
    def BreakPointHandle(self, value):
        self._BreakPointHandle = value

    @InsertBreakPoint.setter
    def InsertBreakPoint(self, value):
        self._InsertBreakPoint = value

    def _set_breakpointhandle_with_str(self, value):
        self._BreakPointHandle = value

    def _set_insertbreakpoint_with_str(self, value):
        self._InsertBreakPoint = (value == 'True')

