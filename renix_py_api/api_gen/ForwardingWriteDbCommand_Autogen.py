"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc2889WriteDbCommandBurstSize_Autogen import Rfc2889WriteDbCommandBurstSize


@rom_manager.rom
class ForwardingWriteDbCommand(Rfc2889WriteDbCommandBurstSize):
    def __init__(self, StreamTemplateList=None, AcceptableFrameLoss=None, **kwargs):
        self._StreamTemplateList = StreamTemplateList  # Stream Template List
        self._AcceptableFrameLoss = AcceptableFrameLoss  # Acceptable Frame Loss(%)

        properties = kwargs.copy()
        if StreamTemplateList is not None:
            properties['StreamTemplateList'] = StreamTemplateList
        if AcceptableFrameLoss is not None:
            properties['AcceptableFrameLoss'] = AcceptableFrameLoss

        # call base class function, and it will send message to renix server to create a class.
        super(ForwardingWriteDbCommand, self).__init__(**properties)

    @property
    def StreamTemplateList(self):
        """
        get the value of property _StreamTemplateList
        """
        return self._StreamTemplateList

    @property
    def AcceptableFrameLoss(self):
        """
        get the value of property _AcceptableFrameLoss
        """
        return self._AcceptableFrameLoss

    @StreamTemplateList.setter
    def StreamTemplateList(self, value):
        self._StreamTemplateList = value

    @AcceptableFrameLoss.setter
    def AcceptableFrameLoss(self, value):
        self._AcceptableFrameLoss = value

    def _set_streamtemplatelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamTemplateList = tmp_value.split()

    def _set_acceptableframeloss_with_str(self, value):
        self._AcceptableFrameLoss = float(value)

