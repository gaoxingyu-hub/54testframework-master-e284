"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .NetworkLayer_Autogen import NetworkLayer


@rom_manager.rom
class L2tpLayer(NetworkLayer):
    def __init__(self, TunnelId=None, TunnelIdStep=None, TunnelIdList=None, SessionId=None, SessionIdStep=None, SessionIdList=None, **kwargs):
        self._TunnelId = TunnelId  # L2TP Tunnel ID
        self._TunnelIdStep = TunnelIdStep  # L2TP Tunnel ID Step
        self._TunnelIdList = TunnelIdList  # L2TP Tunnel ID List
        self._SessionId = SessionId  # L2TP Session ID
        self._SessionIdStep = SessionIdStep  # L2TP Session ID Step
        self._SessionIdList = SessionIdList  # L2TP Session ID List

        properties = kwargs.copy()
        if TunnelId is not None:
            properties['TunnelId'] = TunnelId
        if TunnelIdStep is not None:
            properties['TunnelIdStep'] = TunnelIdStep
        if TunnelIdList is not None:
            properties['TunnelIdList'] = TunnelIdList
        if SessionId is not None:
            properties['SessionId'] = SessionId
        if SessionIdStep is not None:
            properties['SessionIdStep'] = SessionIdStep
        if SessionIdList is not None:
            properties['SessionIdList'] = SessionIdList

        # call base class function, and it will send message to renix server to create a class.
        super(L2tpLayer, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TunnelId=None, TunnelIdStep=None, TunnelIdList=None, SessionId=None, SessionIdStep=None, SessionIdList=None, **kwargs):
        properties = kwargs.copy()
        if TunnelId is not None:
            self._TunnelId = TunnelId
            properties['TunnelId'] = TunnelId
        if TunnelIdStep is not None:
            self._TunnelIdStep = TunnelIdStep
            properties['TunnelIdStep'] = TunnelIdStep
        if TunnelIdList is not None:
            self._TunnelIdList = TunnelIdList
            properties['TunnelIdList'] = TunnelIdList
        if SessionId is not None:
            self._SessionId = SessionId
            properties['SessionId'] = SessionId
        if SessionIdStep is not None:
            self._SessionIdStep = SessionIdStep
            properties['SessionIdStep'] = SessionIdStep
        if SessionIdList is not None:
            self._SessionIdList = SessionIdList
            properties['SessionIdList'] = SessionIdList

        super(L2tpLayer, self).edit(**properties)

    @property
    def TunnelId(self):
        """
        get the value of property _TunnelId
        """
        if self.force_auto_sync:
            self.get('TunnelId')
        return self._TunnelId

    @property
    def TunnelIdStep(self):
        """
        get the value of property _TunnelIdStep
        """
        if self.force_auto_sync:
            self.get('TunnelIdStep')
        return self._TunnelIdStep

    @property
    def TunnelIdList(self):
        """
        get the value of property _TunnelIdList
        """
        if self.force_auto_sync:
            self.get('TunnelIdList')
        return self._TunnelIdList

    @property
    def SessionId(self):
        """
        get the value of property _SessionId
        """
        if self.force_auto_sync:
            self.get('SessionId')
        return self._SessionId

    @property
    def SessionIdStep(self):
        """
        get the value of property _SessionIdStep
        """
        if self.force_auto_sync:
            self.get('SessionIdStep')
        return self._SessionIdStep

    @property
    def SessionIdList(self):
        """
        get the value of property _SessionIdList
        """
        if self.force_auto_sync:
            self.get('SessionIdList')
        return self._SessionIdList

    @TunnelId.setter
    def TunnelId(self, value):
        self._TunnelId = value
        self.edit(TunnelId=value)

    @TunnelIdStep.setter
    def TunnelIdStep(self, value):
        self._TunnelIdStep = value
        self.edit(TunnelIdStep=value)

    @TunnelIdList.setter
    def TunnelIdList(self, value):
        self._TunnelIdList = value
        self.edit(TunnelIdList=value)

    @SessionId.setter
    def SessionId(self, value):
        self._SessionId = value
        self.edit(SessionId=value)

    @SessionIdStep.setter
    def SessionIdStep(self, value):
        self._SessionIdStep = value
        self.edit(SessionIdStep=value)

    @SessionIdList.setter
    def SessionIdList(self, value):
        self._SessionIdList = value
        self.edit(SessionIdList=value)

    def _set_tunnelid_with_str(self, value):
        try:
            self._TunnelId = int(value)
        except ValueError:
            self._TunnelId = hex(int(value, 16))

    def _set_tunnelidstep_with_str(self, value):
        try:
            self._TunnelIdStep = int(value)
        except ValueError:
            self._TunnelIdStep = hex(int(value, 16))

    def _set_tunnelidlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._TunnelIdList = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._TunnelIdList.append(int(str_value))
            except ValueError:
                self._TunnelIdList.append(hex(int(str_value, 16)))

    def _set_sessionid_with_str(self, value):
        try:
            self._SessionId = int(value)
        except ValueError:
            self._SessionId = hex(int(value, 16))

    def _set_sessionidstep_with_str(self, value):
        try:
            self._SessionIdStep = int(value)
        except ValueError:
            self._SessionIdStep = hex(int(value, 16))

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

