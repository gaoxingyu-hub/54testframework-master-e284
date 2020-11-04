"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BenchmarkWizardCompositeConfig_Autogen import BenchmarkWizardCompositeConfig


@rom_manager.rom
class AsymmetricWizardCompositeConfig(BenchmarkWizardCompositeConfig):
    def __init__(self, IsFrameLossEnabled=None, IsLatencyEnabled=None, IsThroughputEnabled=None, EnabledSeqence=None, **kwargs):
        self._IsFrameLossEnabled = IsFrameLossEnabled  # Asymmetric Frame Loss Test
        self._IsLatencyEnabled = IsLatencyEnabled  # Asymmetric Latency Test
        self._IsThroughputEnabled = IsThroughputEnabled  # Asymmetric Throughput Test
        self._EnabledSeqence = EnabledSeqence  # Enabled Asymmetric Test Sequence

        properties = kwargs.copy()
        if IsFrameLossEnabled is not None:
            properties['IsFrameLossEnabled'] = IsFrameLossEnabled
        if IsLatencyEnabled is not None:
            properties['IsLatencyEnabled'] = IsLatencyEnabled
        if IsThroughputEnabled is not None:
            properties['IsThroughputEnabled'] = IsThroughputEnabled
        if EnabledSeqence is not None:
            properties['EnabledSeqence'] = EnabledSeqence

        # call base class function, and it will send message to renix server to create a class.
        super(AsymmetricWizardCompositeConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, IsFrameLossEnabled=None, IsLatencyEnabled=None, IsThroughputEnabled=None, EnabledSeqence=None, **kwargs):
        properties = kwargs.copy()
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

        super(AsymmetricWizardCompositeConfig, self).edit(**properties)

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

    def _set_isframelossenabled_with_str(self, value):
        self._IsFrameLossEnabled = (value == 'True')

    def _set_islatencyenabled_with_str(self, value):
        self._IsLatencyEnabled = (value == 'True')

    def _set_isthroughputenabled_with_str(self, value):
        self._IsThroughputEnabled = (value == 'True')

    def _set_enabledseqence_with_str(self, value):
        self._EnabledSeqence = value

