"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class SmartScripter(ROMObject):
    def __init__(self, IgnoreFailure=None, AutoCommit=None, EnableStepMode=None, AutoOpenAnalyzer=None, **kwargs):
        self._State = EnumSmartScripterState.IDLE  # State, not editable
        self._Verdict = EnumSmartScripterVertict.NONE  # Verdict, not editable
        self._Reason = ''  # Failed Reason, not editable
        self._IgnoreFailure = IgnoreFailure  # Ignore Failure
        self._AutoCommit = AutoCommit  # Automatically Commit
        self._EnableStepMode = EnableStepMode  # Enable Step Mode
        self._AutoOpenAnalyzer = AutoOpenAnalyzer  # Open Analyzer Automatically
        self._StartTime = ''  # Start Time, not editable
        self._ElapsedTime = ''  # Elapsed Time, not editable

        properties = kwargs.copy()
        if IgnoreFailure is not None:
            properties['IgnoreFailure'] = IgnoreFailure
        if AutoCommit is not None:
            properties['AutoCommit'] = AutoCommit
        if EnableStepMode is not None:
            properties['EnableStepMode'] = EnableStepMode
        if AutoOpenAnalyzer is not None:
            properties['AutoOpenAnalyzer'] = AutoOpenAnalyzer

        # call base class function, and it will send message to renix server to create a class.
        super(SmartScripter, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, IgnoreFailure=None, AutoCommit=None, EnableStepMode=None, AutoOpenAnalyzer=None, **kwargs):
        properties = kwargs.copy()
        if IgnoreFailure is not None:
            self._IgnoreFailure = IgnoreFailure
            properties['IgnoreFailure'] = IgnoreFailure
        if AutoCommit is not None:
            self._AutoCommit = AutoCommit
            properties['AutoCommit'] = AutoCommit
        if EnableStepMode is not None:
            self._EnableStepMode = EnableStepMode
            properties['EnableStepMode'] = EnableStepMode
        if AutoOpenAnalyzer is not None:
            self._AutoOpenAnalyzer = AutoOpenAnalyzer
            properties['AutoOpenAnalyzer'] = AutoOpenAnalyzer

        super(SmartScripter, self).edit(**properties)

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def Verdict(self):
        """
        get the value of property _Verdict
        """
        if self.force_auto_sync:
            self.get('Verdict')
        return self._Verdict

    @property
    def Reason(self):
        """
        get the value of property _Reason
        """
        if self.force_auto_sync:
            self.get('Reason')
        return self._Reason

    @property
    def IgnoreFailure(self):
        """
        get the value of property _IgnoreFailure
        """
        if self.force_auto_sync:
            self.get('IgnoreFailure')
        return self._IgnoreFailure

    @property
    def AutoCommit(self):
        """
        get the value of property _AutoCommit
        """
        if self.force_auto_sync:
            self.get('AutoCommit')
        return self._AutoCommit

    @property
    def EnableStepMode(self):
        """
        get the value of property _EnableStepMode
        """
        if self.force_auto_sync:
            self.get('EnableStepMode')
        return self._EnableStepMode

    @property
    def AutoOpenAnalyzer(self):
        """
        get the value of property _AutoOpenAnalyzer
        """
        if self.force_auto_sync:
            self.get('AutoOpenAnalyzer')
        return self._AutoOpenAnalyzer

    @property
    def StartTime(self):
        """
        get the value of property _StartTime
        """
        if self.force_auto_sync:
            self.get('StartTime')
        return self._StartTime

    @property
    def ElapsedTime(self):
        """
        get the value of property _ElapsedTime
        """
        if self.force_auto_sync:
            self.get('ElapsedTime')
        return self._ElapsedTime

    @IgnoreFailure.setter
    def IgnoreFailure(self, value):
        self._IgnoreFailure = value
        self.edit(IgnoreFailure=value)

    @AutoCommit.setter
    def AutoCommit(self, value):
        self._AutoCommit = value
        self.edit(AutoCommit=value)

    @EnableStepMode.setter
    def EnableStepMode(self, value):
        self._EnableStepMode = value
        self.edit(EnableStepMode=value)

    @AutoOpenAnalyzer.setter
    def AutoOpenAnalyzer(self, value):
        self._AutoOpenAnalyzer = value
        self.edit(AutoOpenAnalyzer=value)

    def _set_state_with_str(self, value):
        seperate = value.find(':')
        exec('self._State = EnumSmartScripterState.%s' % value[:seperate])

    def _set_verdict_with_str(self, value):
        seperate = value.find(':')
        exec('self._Verdict = EnumSmartScripterVertict.%s' % value[:seperate])

    def _set_reason_with_str(self, value):
        self._Reason = value

    def _set_ignorefailure_with_str(self, value):
        self._IgnoreFailure = (value == 'True')

    def _set_autocommit_with_str(self, value):
        self._AutoCommit = (value == 'True')

    def _set_enablestepmode_with_str(self, value):
        self._EnableStepMode = (value == 'True')

    def _set_autoopenanalyzer_with_str(self, value):
        self._AutoOpenAnalyzer = (value == 'True')

    def _set_starttime_with_str(self, value):
        self._StartTime = value

    def _set_elapsedtime_with_str(self, value):
        self._ElapsedTime = value

