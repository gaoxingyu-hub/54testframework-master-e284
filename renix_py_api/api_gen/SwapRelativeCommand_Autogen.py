"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SwapRelativeCommand(ROMCommand):
    def __init__(self, ObjectHandle=None, RelationName=None, RelativeHandle1=None, RelativeHandle2=None, **kwargs):
        self._ObjectHandle = ObjectHandle  # Object Handle
        self._RelationName = RelationName  # Relation Name
        self._RelativeHandle1 = RelativeHandle1  # Relative Handle
        self._RelativeHandle2 = RelativeHandle2  # Relative Handle

        properties = kwargs.copy()
        if ObjectHandle is not None:
            properties['ObjectHandle'] = ObjectHandle
        if RelationName is not None:
            properties['RelationName'] = RelationName
        if RelativeHandle1 is not None:
            properties['RelativeHandle1'] = RelativeHandle1
        if RelativeHandle2 is not None:
            properties['RelativeHandle2'] = RelativeHandle2

        # call base class function, and it will send message to renix server to create a class.
        super(SwapRelativeCommand, self).__init__(**properties)

    @property
    def ObjectHandle(self):
        """
        get the value of property _ObjectHandle
        """
        return self._ObjectHandle

    @property
    def RelationName(self):
        """
        get the value of property _RelationName
        """
        return self._RelationName

    @property
    def RelativeHandle1(self):
        """
        get the value of property _RelativeHandle1
        """
        return self._RelativeHandle1

    @property
    def RelativeHandle2(self):
        """
        get the value of property _RelativeHandle2
        """
        return self._RelativeHandle2

    @ObjectHandle.setter
    def ObjectHandle(self, value):
        self._ObjectHandle = value

    @RelationName.setter
    def RelationName(self, value):
        self._RelationName = value

    @RelativeHandle1.setter
    def RelativeHandle1(self, value):
        self._RelativeHandle1 = value

    @RelativeHandle2.setter
    def RelativeHandle2(self, value):
        self._RelativeHandle2 = value

    def _set_objecthandle_with_str(self, value):
        self._ObjectHandle = value

    def _set_relationname_with_str(self, value):
        self._RelationName = value

    def _set_relativehandle1_with_str(self, value):
        self._RelativeHandle1 = value

    def _set_relativehandle2_with_str(self, value):
        self._RelativeHandle2 = value

