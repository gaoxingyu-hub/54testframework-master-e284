"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L47ClientProfile_Autogen import L47ClientProfile


@rom_manager.rom
class PlaybackStreamClientProfile(L47ClientProfile):
    def __init__(self, MinSourcePort=None, MaxSourcePort=None, Method=None, StreamGroup=None, **kwargs):
        self._MinSourcePort = MinSourcePort  # Min Source Port
        self._MaxSourcePort = MaxSourcePort  # Max Source Port
        self._Method = Method  # Stream Group Creation Method
        self._StreamGroup = StreamGroup  # Stream Group

        properties = kwargs.copy()
        if MinSourcePort is not None:
            properties['MinSourcePort'] = MinSourcePort
        if MaxSourcePort is not None:
            properties['MaxSourcePort'] = MaxSourcePort
        if Method is not None:
            properties['Method'] = Method
        if StreamGroup is not None:
            properties['StreamGroup'] = StreamGroup

        # call base class function, and it will send message to renix server to create a class.
        super(PlaybackStreamClientProfile, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, MinSourcePort=None, MaxSourcePort=None, Method=None, StreamGroup=None, **kwargs):
        properties = kwargs.copy()
        if MinSourcePort is not None:
            self._MinSourcePort = MinSourcePort
            properties['MinSourcePort'] = MinSourcePort
        if MaxSourcePort is not None:
            self._MaxSourcePort = MaxSourcePort
            properties['MaxSourcePort'] = MaxSourcePort
        if Method is not None:
            self._Method = Method
            properties['Method'] = Method
        if StreamGroup is not None:
            self._StreamGroup = StreamGroup
            properties['StreamGroup'] = StreamGroup

        super(PlaybackStreamClientProfile, self).edit(**properties)

    @property
    def MinSourcePort(self):
        """
        get the value of property _MinSourcePort
        """
        if self.force_auto_sync:
            self.get('MinSourcePort')
        return self._MinSourcePort

    @property
    def MaxSourcePort(self):
        """
        get the value of property _MaxSourcePort
        """
        if self.force_auto_sync:
            self.get('MaxSourcePort')
        return self._MaxSourcePort

    @property
    def Method(self):
        """
        get the value of property _Method
        """
        if self.force_auto_sync:
            self.get('Method')
        return self._Method

    @property
    def StreamGroup(self):
        """
        get the value of property _StreamGroup
        """
        if self.force_auto_sync:
            self.get('StreamGroup')
        return self._StreamGroup

    @MinSourcePort.setter
    def MinSourcePort(self, value):
        self._MinSourcePort = value
        self.edit(MinSourcePort=value)

    @MaxSourcePort.setter
    def MaxSourcePort(self, value):
        self._MaxSourcePort = value
        self.edit(MaxSourcePort=value)

    @Method.setter
    def Method(self, value):
        self._Method = value
        self.edit(Method=value)

    @StreamGroup.setter
    def StreamGroup(self, value):
        self._StreamGroup = value
        self.edit(StreamGroup=value)

    def _set_minsourceport_with_str(self, value):
        try:
            self._MinSourcePort = int(value)
        except ValueError:
            self._MinSourcePort = hex(int(value, 16))

    def _set_maxsourceport_with_str(self, value):
        try:
            self._MaxSourcePort = int(value)
        except ValueError:
            self._MaxSourcePort = hex(int(value, 16))

    def _set_method_with_str(self, value):
        seperate = value.find(':')
        exec('self._Method = EnumStreamGroupCreationMethodType.%s' % value[:seperate])

    def _set_streamgroup_with_str(self, value):
        self._StreamGroup = value

