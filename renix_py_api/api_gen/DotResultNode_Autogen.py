"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class DotResultNode(ROMObject):
    def __init__(self, ResultView=None, NodeDescription=None, ResultStatus=None, **kwargs):
        self._ResultView = ResultView  # Result View Handle
        self._NodeDescription = NodeDescription  # Description
        self._ResultStatus = ResultStatus  # Result Status

        properties = kwargs.copy()
        if ResultView is not None:
            properties['ResultView'] = ResultView
        if NodeDescription is not None:
            properties['NodeDescription'] = NodeDescription
        if ResultStatus is not None:
            properties['ResultStatus'] = ResultStatus

        # call base class function, and it will send message to renix server to create a class.
        super(DotResultNode, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ResultView=None, NodeDescription=None, ResultStatus=None, **kwargs):
        properties = kwargs.copy()
        if ResultView is not None:
            self._ResultView = ResultView
            properties['ResultView'] = ResultView
        if NodeDescription is not None:
            self._NodeDescription = NodeDescription
            properties['NodeDescription'] = NodeDescription
        if ResultStatus is not None:
            self._ResultStatus = ResultStatus
            properties['ResultStatus'] = ResultStatus

        super(DotResultNode, self).edit(**properties)

    @property
    def ResultView(self):
        """
        get the value of property _ResultView
        """
        if self.force_auto_sync:
            self.get('ResultView')
        return self._ResultView

    @property
    def NodeDescription(self):
        """
        get the value of property _NodeDescription
        """
        if self.force_auto_sync:
            self.get('NodeDescription')
        return self._NodeDescription

    @property
    def ResultStatus(self):
        """
        get the value of property _ResultStatus
        """
        if self.force_auto_sync:
            self.get('ResultStatus')
        return self._ResultStatus

    @ResultView.setter
    def ResultView(self, value):
        self._ResultView = value
        self.edit(ResultView=value)

    @NodeDescription.setter
    def NodeDescription(self, value):
        self._NodeDescription = value
        self.edit(NodeDescription=value)

    @ResultStatus.setter
    def ResultStatus(self, value):
        self._ResultStatus = value
        self.edit(ResultStatus=value)

    def _set_resultview_with_str(self, value):
        self._ResultView = value

    def _set_nodedescription_with_str(self, value):
        self._NodeDescription = value

    def _set_resultstatus_with_str(self, value):
        seperate = value.find(':')
        exec('self._ResultStatus = EnumResultStatus.%s' % value[:seperate])

