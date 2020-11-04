"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class L47CmdList(ROMObject):
    def __init__(self, ProtoType=None, **kwargs):
        self._ProtoType = ProtoType  # Protocol Type

        properties = kwargs.copy()
        if ProtoType is not None:
            properties['ProtoType'] = ProtoType

        # call base class function, and it will send message to renix server to create a class.
        super(L47CmdList, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ProtoType=None, **kwargs):
        properties = kwargs.copy()
        if ProtoType is not None:
            self._ProtoType = ProtoType
            properties['ProtoType'] = ProtoType

        super(L47CmdList, self).edit(**properties)

    @property
    def ProtoType(self):
        """
        get the value of property _ProtoType
        """
        if self.force_auto_sync:
            self.get('ProtoType')
        return self._ProtoType

    @ProtoType.setter
    def ProtoType(self, value):
        self._ProtoType = value
        self.edit(ProtoType=value)

    def _set_prototype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ProtoType = ProtocolType.%s' % value[:seperate])

