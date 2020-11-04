"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .CaptureFilter_Autogen import CaptureFilter


@rom_manager.rom
class CapturePduFilter(CaptureFilter):
    def __init__(self, LogicExpression=None, **kwargs):
        self._LogicExpression = LogicExpression  # Expression

        properties = kwargs.copy()
        if LogicExpression is not None:
            properties['LogicExpression'] = LogicExpression

        # call base class function, and it will send message to renix server to create a class.
        super(CapturePduFilter, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, LogicExpression=None, **kwargs):
        properties = kwargs.copy()
        if LogicExpression is not None:
            self._LogicExpression = LogicExpression
            properties['LogicExpression'] = LogicExpression

        super(CapturePduFilter, self).edit(**properties)

    @property
    def LogicExpression(self):
        """
        get the value of property _LogicExpression
        """
        if self.force_auto_sync:
            self.get('LogicExpression')
        return self._LogicExpression

    @LogicExpression.setter
    def LogicExpression(self, value):
        self._LogicExpression = value
        self.edit(LogicExpression=value)

    def _set_logicexpression_with_str(self, value):
        self._LogicExpression = value

