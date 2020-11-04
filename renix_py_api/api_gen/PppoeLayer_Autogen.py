"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .NetworkLayer_Autogen import NetworkLayer


@rom_manager.rom
class PppoeLayer(NetworkLayer):
    def __init__(self, SessionId=None, Step=None, SessionIdList=None, **kwargs):
        self._SessionId = SessionId  # PPPoE Session ID
        self._Step = Step  # PPPoE Session ID Step
        self._SessionIdList = SessionIdList  # PPPoE Session ID List
        self._PeerMacList = None  # Peer MAC Address List, not editable

        properties = kwargs.copy()
        if SessionId is not None:
            properties['SessionId'] = SessionId
        if Step is not None:
            properties['Step'] = Step
        if SessionIdList is not None:
            properties['SessionIdList'] = SessionIdList

        # call base class function, and it will send message to renix server to create a class.
        super(PppoeLayer, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, SessionId=None, Step=None, SessionIdList=None, **kwargs):
        properties = kwargs.copy()
        if SessionId is not None:
            self._SessionId = SessionId
            properties['SessionId'] = SessionId
        if Step is not None:
            self._Step = Step
            properties['Step'] = Step
        if SessionIdList is not None:
            self._SessionIdList = SessionIdList
            properties['SessionIdList'] = SessionIdList

        super(PppoeLayer, self).edit(**properties)

    @property
    def SessionId(self):
        """
        get the value of property _SessionId
        """
        if self.force_auto_sync:
            self.get('SessionId')
        return self._SessionId

    @property
    def Step(self):
        """
        get the value of property _Step
        """
        if self.force_auto_sync:
            self.get('Step')
        return self._Step

    @property
    def SessionIdList(self):
        """
        get the value of property _SessionIdList
        """
        if self.force_auto_sync:
            self.get('SessionIdList')
        return self._SessionIdList

    @property
    def PeerMacList(self):
        """
        get the value of property _PeerMacList
        """
        if self.force_auto_sync:
            self.get('PeerMacList')
        return self._PeerMacList

    @SessionId.setter
    def SessionId(self, value):
        self._SessionId = value
        self.edit(SessionId=value)

    @Step.setter
    def Step(self, value):
        self._Step = value
        self.edit(Step=value)

    @SessionIdList.setter
    def SessionIdList(self, value):
        self._SessionIdList = value
        self.edit(SessionIdList=value)

    def _set_sessionid_with_str(self, value):
        try:
            self._SessionId = int(value)
        except ValueError:
            self._SessionId = hex(int(value, 16))

    def _set_step_with_str(self, value):
        try:
            self._Step = int(value)
        except ValueError:
            self._Step = hex(int(value, 16))

    def _set_sessionidlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._SessionIdList = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._SessionIdList.append(int(str_value))
            except ValueError:
                self._SessionIdList.append(hex(int(str_value, 16)))

    def _set_peermaclist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PeerMacList = tmp_value.split()

