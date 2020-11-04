"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class LacpPortConfig(ROMObject):
    def __init__(self, ActorKey=None, ActorPortId=None, ActorPortPriority=None, LacpTimeout=None, LacpActivity=None, ActorSystemId=None, ActorSystemIdStep=None, ActorSystemPriority=None, **kwargs):
        self._ActorKey = ActorKey  # Port Actor Key
        self._ActorPortId = ActorPortId  # Actor Port ID
        self._ActorPortPriority = ActorPortPriority  # Actor Port Priority
        self._LacpState = EnumLacpPortState.DOWN  # LACP Status, not editable
        self._LacpTimeout = LacpTimeout  # LACP Timeout 
        self._LacpActivity = LacpActivity  # LACP Activity 
        self._ActorSystemId = ActorSystemId  # Actor System ID
        self._ActorSystemIdStep = ActorSystemIdStep  # Actor System ID Step
        self._ActorSystemPriority = ActorSystemPriority  # Actor System Priority

        properties = kwargs.copy()
        if ActorKey is not None:
            properties['ActorKey'] = ActorKey
        if ActorPortId is not None:
            properties['ActorPortId'] = ActorPortId
        if ActorPortPriority is not None:
            properties['ActorPortPriority'] = ActorPortPriority
        if LacpTimeout is not None:
            properties['LacpTimeout'] = LacpTimeout
        if LacpActivity is not None:
            properties['LacpActivity'] = LacpActivity
        if ActorSystemId is not None:
            properties['ActorSystemId'] = ActorSystemId
        if ActorSystemIdStep is not None:
            properties['ActorSystemIdStep'] = ActorSystemIdStep
        if ActorSystemPriority is not None:
            properties['ActorSystemPriority'] = ActorSystemPriority

        # call base class function, and it will send message to renix server to create a class.
        super(LacpPortConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ActorKey=None, ActorPortId=None, ActorPortPriority=None, LacpTimeout=None, LacpActivity=None, ActorSystemId=None, ActorSystemIdStep=None, ActorSystemPriority=None, **kwargs):
        properties = kwargs.copy()
        if ActorKey is not None:
            self._ActorKey = ActorKey
            properties['ActorKey'] = ActorKey
        if ActorPortId is not None:
            self._ActorPortId = ActorPortId
            properties['ActorPortId'] = ActorPortId
        if ActorPortPriority is not None:
            self._ActorPortPriority = ActorPortPriority
            properties['ActorPortPriority'] = ActorPortPriority
        if LacpTimeout is not None:
            self._LacpTimeout = LacpTimeout
            properties['LacpTimeout'] = LacpTimeout
        if LacpActivity is not None:
            self._LacpActivity = LacpActivity
            properties['LacpActivity'] = LacpActivity
        if ActorSystemId is not None:
            self._ActorSystemId = ActorSystemId
            properties['ActorSystemId'] = ActorSystemId
        if ActorSystemIdStep is not None:
            self._ActorSystemIdStep = ActorSystemIdStep
            properties['ActorSystemIdStep'] = ActorSystemIdStep
        if ActorSystemPriority is not None:
            self._ActorSystemPriority = ActorSystemPriority
            properties['ActorSystemPriority'] = ActorSystemPriority

        super(LacpPortConfig, self).edit(**properties)

    @property
    def ActorKey(self):
        """
        get the value of property _ActorKey
        """
        if self.force_auto_sync:
            self.get('ActorKey')
        return self._ActorKey

    @property
    def ActorPortId(self):
        """
        get the value of property _ActorPortId
        """
        if self.force_auto_sync:
            self.get('ActorPortId')
        return self._ActorPortId

    @property
    def ActorPortPriority(self):
        """
        get the value of property _ActorPortPriority
        """
        if self.force_auto_sync:
            self.get('ActorPortPriority')
        return self._ActorPortPriority

    @property
    def LacpState(self):
        """
        get the value of property _LacpState
        """
        if self.force_auto_sync:
            self.get('LacpState')
        return self._LacpState

    @property
    def LacpTimeout(self):
        """
        get the value of property _LacpTimeout
        """
        if self.force_auto_sync:
            self.get('LacpTimeout')
        return self._LacpTimeout

    @property
    def LacpActivity(self):
        """
        get the value of property _LacpActivity
        """
        if self.force_auto_sync:
            self.get('LacpActivity')
        return self._LacpActivity

    @property
    def ActorSystemId(self):
        """
        get the value of property _ActorSystemId
        """
        if self.force_auto_sync:
            self.get('ActorSystemId')
        return self._ActorSystemId

    @property
    def ActorSystemIdStep(self):
        """
        get the value of property _ActorSystemIdStep
        """
        if self.force_auto_sync:
            self.get('ActorSystemIdStep')
        return self._ActorSystemIdStep

    @property
    def ActorSystemPriority(self):
        """
        get the value of property _ActorSystemPriority
        """
        if self.force_auto_sync:
            self.get('ActorSystemPriority')
        return self._ActorSystemPriority

    @ActorKey.setter
    def ActorKey(self, value):
        self._ActorKey = value
        self.edit(ActorKey=value)

    @ActorPortId.setter
    def ActorPortId(self, value):
        self._ActorPortId = value
        self.edit(ActorPortId=value)

    @ActorPortPriority.setter
    def ActorPortPriority(self, value):
        self._ActorPortPriority = value
        self.edit(ActorPortPriority=value)

    @LacpTimeout.setter
    def LacpTimeout(self, value):
        self._LacpTimeout = value
        self.edit(LacpTimeout=value)

    @LacpActivity.setter
    def LacpActivity(self, value):
        self._LacpActivity = value
        self.edit(LacpActivity=value)

    @ActorSystemId.setter
    def ActorSystemId(self, value):
        self._ActorSystemId = value
        self.edit(ActorSystemId=value)

    @ActorSystemIdStep.setter
    def ActorSystemIdStep(self, value):
        self._ActorSystemIdStep = value
        self.edit(ActorSystemIdStep=value)

    @ActorSystemPriority.setter
    def ActorSystemPriority(self, value):
        self._ActorSystemPriority = value
        self.edit(ActorSystemPriority=value)

    def _set_actorkey_with_str(self, value):
        try:
            self._ActorKey = int(value)
        except ValueError:
            self._ActorKey = hex(int(value, 16))

    def _set_actorportid_with_str(self, value):
        try:
            self._ActorPortId = int(value)
        except ValueError:
            self._ActorPortId = hex(int(value, 16))

    def _set_actorportpriority_with_str(self, value):
        try:
            self._ActorPortPriority = int(value)
        except ValueError:
            self._ActorPortPriority = hex(int(value, 16))

    def _set_lacpstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._LacpState = EnumLacpPortState.%s' % value[:seperate])

    def _set_lacptimeout_with_str(self, value):
        seperate = value.find(':')
        exec('self._LacpTimeout = EnumLacpTimeout.%s' % value[:seperate])

    def _set_lacpactivity_with_str(self, value):
        seperate = value.find(':')
        exec('self._LacpActivity = EnumLacpActivity.%s' % value[:seperate])

    def _set_actorsystemid_with_str(self, value):
        self._ActorSystemId = value

    def _set_actorsystemidstep_with_str(self, value):
        self._ActorSystemIdStep = value

    def _set_actorsystempriority_with_str(self, value):
        try:
            self._ActorSystemPriority = int(value)
        except ValueError:
            self._ActorSystemPriority = hex(int(value, 16))

