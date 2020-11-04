"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BenchmarkWizardCompositeConfig_Autogen import BenchmarkWizardCompositeConfig


@rom_manager.rom
class Rfc2544WizardCompositeConfig(BenchmarkWizardCompositeConfig):
    def __init__(self, IsBackToBackEnabled=None, IsFrameLossEnabled=None, IsLatencyEnabled=None, IsThroughputEnabled=None, EnabledSeqence=None, **kwargs):
        self._IsBackToBackEnabled = IsBackToBackEnabled  # Rfc2544 Back To Bacck Test
        self._IsFrameLossEnabled = IsFrameLossEnabled  # Rfc2544 Back To Bacck Test
        self._IsLatencyEnabled = IsLatencyEnabled  # Rfc2544 Back To Bacck Test
        self._IsThroughputEnabled = IsThroughputEnabled  # Rfc2544 Back To Bacck Test
        self._EnabledSeqence = EnabledSeqence  # Enabled 2544 Test Sequence

        properties = kwargs.copy()
        if IsBackToBackEnabled is not None:
            properties['IsBackToBackEnabled'] = IsBackToBackEnabled
        if IsFrameLossEnabled is not None:
            properties['IsFrameLossEnabled'] = IsFrameLossEnabled
        if IsLatencyEnabled is not None:
            properties['IsLatencyEnabled'] = IsLatencyEnabled
        if IsThroughputEnabled is not None:
            properties['IsThroughputEnabled'] = IsThroughputEnabled
        if EnabledSeqence is not None:
            properties['EnabledSeqence'] = EnabledSeqence

        # call base class function, and it will send message to renix server to create a class.
        super(Rfc2544WizardCompositeConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, IsBackToBackEnabled=None, IsFrameLossEnabled=None, IsLatencyEnabled=None, IsThroughputEnabled=None, EnabledSeqence=None, **kwargs):
        properties = kwargs.copy()
        if IsBackToBackEnabled is not None:
            self._IsBackToBackEnabled = IsBackToBackEnabled
            properties['IsBackToBackEnabled'] = IsBackToBackEnabled
        if IsFrameLossEnabled is not None:
            self._IsFrameLossEnabled = IsFrameLossEnabled
            properties['IsFrameLossEnabled'] = IsFrameLossEnabled
        if IsLatencyEnabled is not None:
            self._IsLatencyEnabled = IsLatencyEnabled
            properties['IsLatencyEnabled'] = IsLatencyEnabled
        if IsThroughputEnabled is not None:
            self._IsThroughputEnabled = IsThroughputEnabled
            properties['IsThroughputEnabled'] = IsThroughputEnabled
        if EnabledSeqence is not None:
            self._EnabledSeqence = EnabledSeqence
            properties['EnabledSeqence'] = EnabledSeqence

        super(Rfc2544WizardCompositeConfig, self).edit(**properties)

    @property
    def IsBackToBackEnabled(self):
        """
        get the value of property _IsBackToBackEnabled
        """
        if self.force_auto_sync:
            self.get('IsBackToBackEnabled')
        return self._IsBackToBackEnabled

    @property
    def IsFrameLossEnabled(self):
        """
        get the value of property _IsFrameLossEnabled
        """
        if self.force_auto_sync:
            self.get('IsFrameLossEnabled')
        return self._IsFrameLossEnabled

    @property
    def IsLatencyEnabled(self):
        """
        get the value of property _IsLatencyEnabled
        """
        if self.force_auto_sync:
            self.get('IsLatencyEnabled')
        return self._IsLatencyEnabled

    @property
    def IsThroughputEnabled(self):
        """
        get the value of property _IsThroughputEnabled
        """
        if self.force_auto_sync:
            self.get('IsThroughputEnabled')
        return self._IsThroughputEnabled

    @property
    def EnabledSeqence(self):
        """
        get the value of property _EnabledSeqence
        """
        if self.force_auto_sync:
            self.get('EnabledSeqence')
        return self._EnabledSeqence

    @IsBackToBackEnabled.setter
    def IsBackToBackEnabled(self, value):
        self._IsBackToBackEnabled = value
        self.edit(IsBackToBackEnabled=value)

    @IsFrameLossEnabled.setter
    def IsFrameLossEnabled(self, value):
        self._IsFrameLossEnabled = value
        self.edit(IsFrameLossEnabled=value)

    @IsLatencyEnabled.setter
    def IsLatencyEnabled(self, value):
        self._IsLatencyEnabled = value
        self.edit(IsLatencyEnabled=value)

    @IsThroughputEnabled.setter
    def IsThroughputEnabled(self, value):
        self._IsThroughputEnabled = value
        self.edit(IsThroughputEnabled=value)

    @EnabledSeqence.setter
    def EnabledSeqence(self, value):
        self._EnabledSeqence = value
        self.edit(EnabledSeqence=value)

    def _set_isbacktobackenabled_with_str(self, value):
        self._IsBackToBackEnabled = (value == 'True')

    def _set_isframelossenabled_with_str(self, value):
        self._IsFrameLossEnabled = (value == 'True')

    def _set_islatencyenabled_with_str(self, value):
        self._IsLatencyEnabled = (value == 'True')

    def _set_isthroughputenabled_with_str(self, value):
        self._IsThroughputEnabled = (value == 'True')

    def _set_enabledseqence_with_str(self, value):
        self._EnabledSeqence = value

