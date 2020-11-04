"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class VerifyTrafficForwardingCommand(ROMCommand):
    def __init__(self, StreamTemplateHandles=None, VerificationDurationMode=None, VerfictionTxFrameCount=None, VerfictionTxSeconds=None, VerificationTxFrameRate=None, ErrorOnFaiure=None, **kwargs):
        self._StreamTemplateHandles = StreamTemplateHandles  # StreamTemplate Handles
        self._VerificationDurationMode = VerificationDurationMode  # Duration Mode
        self._VerfictionTxFrameCount = VerfictionTxFrameCount  # Verification Tx Frame Count
        self._VerfictionTxSeconds = VerfictionTxSeconds  # Verification Tx Seconds
        self._VerificationTxFrameRate = VerificationTxFrameRate  # Verification Tx Frame Rate
        self._ErrorOnFaiure = ErrorOnFaiure  # Throw Error when Fail

        properties = kwargs.copy()
        if StreamTemplateHandles is not None:
            properties['StreamTemplateHandles'] = StreamTemplateHandles
        if VerificationDurationMode is not None:
            properties['VerificationDurationMode'] = VerificationDurationMode
        if VerfictionTxFrameCount is not None:
            properties['VerfictionTxFrameCount'] = VerfictionTxFrameCount
        if VerfictionTxSeconds is not None:
            properties['VerfictionTxSeconds'] = VerfictionTxSeconds
        if VerificationTxFrameRate is not None:
            properties['VerificationTxFrameRate'] = VerificationTxFrameRate
        if ErrorOnFaiure is not None:
            properties['ErrorOnFaiure'] = ErrorOnFaiure

        # call base class function, and it will send message to renix server to create a class.
        super(VerifyTrafficForwardingCommand, self).__init__(**properties)

    @property
    def StreamTemplateHandles(self):
        """
        get the value of property _StreamTemplateHandles
        """
        return self._StreamTemplateHandles

    @property
    def VerificationDurationMode(self):
        """
        get the value of property _VerificationDurationMode
        """
        return self._VerificationDurationMode

    @property
    def VerfictionTxFrameCount(self):
        """
        get the value of property _VerfictionTxFrameCount
        """
        return self._VerfictionTxFrameCount

    @property
    def VerfictionTxSeconds(self):
        """
        get the value of property _VerfictionTxSeconds
        """
        return self._VerfictionTxSeconds

    @property
    def VerificationTxFrameRate(self):
        """
        get the value of property _VerificationTxFrameRate
        """
        return self._VerificationTxFrameRate

    @property
    def ErrorOnFaiure(self):
        """
        get the value of property _ErrorOnFaiure
        """
        return self._ErrorOnFaiure

    @StreamTemplateHandles.setter
    def StreamTemplateHandles(self, value):
        self._StreamTemplateHandles = value

    @VerificationDurationMode.setter
    def VerificationDurationMode(self, value):
        self._VerificationDurationMode = value

    @VerfictionTxFrameCount.setter
    def VerfictionTxFrameCount(self, value):
        self._VerfictionTxFrameCount = value

    @VerfictionTxSeconds.setter
    def VerfictionTxSeconds(self, value):
        self._VerfictionTxSeconds = value

    @VerificationTxFrameRate.setter
    def VerificationTxFrameRate(self, value):
        self._VerificationTxFrameRate = value

    @ErrorOnFaiure.setter
    def ErrorOnFaiure(self, value):
        self._ErrorOnFaiure = value

    def _set_streamtemplatehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamTemplateHandles = tmp_value.split()

    def _set_verificationdurationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._VerificationDurationMode = EnumDurationMode.%s' % value[:seperate])

    def _set_verfictiontxframecount_with_str(self, value):
        try:
            self._VerfictionTxFrameCount = int(value)
        except ValueError:
            self._VerfictionTxFrameCount = hex(int(value, 16))

    def _set_verfictiontxseconds_with_str(self, value):
        try:
            self._VerfictionTxSeconds = int(value)
        except ValueError:
            self._VerfictionTxSeconds = hex(int(value, 16))

    def _set_verificationtxframerate_with_str(self, value):
        try:
            self._VerificationTxFrameRate = int(value)
        except ValueError:
            self._VerificationTxFrameRate = hex(int(value, 16))

    def _set_erroronfaiure_with_str(self, value):
        self._ErrorOnFaiure = (value == 'True')

