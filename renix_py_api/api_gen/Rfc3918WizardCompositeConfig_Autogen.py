"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BenchmarkWizardCompositeConfig_Autogen import BenchmarkWizardCompositeConfig


@rom_manager.rom
class Rfc3918WizardCompositeConfig(BenchmarkWizardCompositeConfig):
    def __init__(self, IsMixedClassThroughputEnabled=None, IsScaledGroupForwardingMatrixEnabled=None, IsAggregatedMulticastThroughputEnabled=None, IsMulticastForwardingLatencyEnabled=None, IsMulticastJoinLeaveLatencyEnabled=None, IsMulticastGroupCapacityEnabled=None, EnabledSeqence=None, **kwargs):
        self._IsMixedClassThroughputEnabled = IsMixedClassThroughputEnabled  # Rfc3918 Mixed Class Throughput Test
        self._IsScaledGroupForwardingMatrixEnabled = IsScaledGroupForwardingMatrixEnabled  # Rfc3918 Scaled Group Forwarding Matrix Test
        self._IsAggregatedMulticastThroughputEnabled = IsAggregatedMulticastThroughputEnabled  # Rfc3918 Aggregated Multicast Throughput Test
        self._IsMulticastForwardingLatencyEnabled = IsMulticastForwardingLatencyEnabled  # Rfc3918 Multicast Forwarding Latency Test
        self._IsMulticastJoinLeaveLatencyEnabled = IsMulticastJoinLeaveLatencyEnabled  # Rfc3918 Multicast Join Leave Latency Test
        self._IsMulticastGroupCapacityEnabled = IsMulticastGroupCapacityEnabled  # Rfc3918 Multicast Group Capacity Test
        self._EnabledSeqence = EnabledSeqence  # Enabled 3918 Test Sequence

        properties = kwargs.copy()
        if IsMixedClassThroughputEnabled is not None:
            properties['IsMixedClassThroughputEnabled'] = IsMixedClassThroughputEnabled
        if IsScaledGroupForwardingMatrixEnabled is not None:
            properties['IsScaledGroupForwardingMatrixEnabled'] = IsScaledGroupForwardingMatrixEnabled
        if IsAggregatedMulticastThroughputEnabled is not None:
            properties['IsAggregatedMulticastThroughputEnabled'] = IsAggregatedMulticastThroughputEnabled
        if IsMulticastForwardingLatencyEnabled is not None:
            properties['IsMulticastForwardingLatencyEnabled'] = IsMulticastForwardingLatencyEnabled
        if IsMulticastJoinLeaveLatencyEnabled is not None:
            properties['IsMulticastJoinLeaveLatencyEnabled'] = IsMulticastJoinLeaveLatencyEnabled
        if IsMulticastGroupCapacityEnabled is not None:
            properties['IsMulticastGroupCapacityEnabled'] = IsMulticastGroupCapacityEnabled
        if EnabledSeqence is not None:
            properties['EnabledSeqence'] = EnabledSeqence

        # call base class function, and it will send message to renix server to create a class.
        super(Rfc3918WizardCompositeConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, IsMixedClassThroughputEnabled=None, IsScaledGroupForwardingMatrixEnabled=None, IsAggregatedMulticastThroughputEnabled=None, IsMulticastForwardingLatencyEnabled=None, IsMulticastJoinLeaveLatencyEnabled=None, IsMulticastGroupCapacityEnabled=None, EnabledSeqence=None, **kwargs):
        properties = kwargs.copy()
        if IsMixedClassThroughputEnabled is not None:
            self._IsMixedClassThroughputEnabled = IsMixedClassThroughputEnabled
            properties['IsMixedClassThroughputEnabled'] = IsMixedClassThroughputEnabled
        if IsScaledGroupForwardingMatrixEnabled is not None:
            self._IsScaledGroupForwardingMatrixEnabled = IsScaledGroupForwardingMatrixEnabled
            properties['IsScaledGroupForwardingMatrixEnabled'] = IsScaledGroupForwardingMatrixEnabled
        if IsAggregatedMulticastThroughputEnabled is not None:
            self._IsAggregatedMulticastThroughputEnabled = IsAggregatedMulticastThroughputEnabled
            properties['IsAggregatedMulticastThroughputEnabled'] = IsAggregatedMulticastThroughputEnabled
        if IsMulticastForwardingLatencyEnabled is not None:
            self._IsMulticastForwardingLatencyEnabled = IsMulticastForwardingLatencyEnabled
            properties['IsMulticastForwardingLatencyEnabled'] = IsMulticastForwardingLatencyEnabled
        if IsMulticastJoinLeaveLatencyEnabled is not None:
            self._IsMulticastJoinLeaveLatencyEnabled = IsMulticastJoinLeaveLatencyEnabled
            properties['IsMulticastJoinLeaveLatencyEnabled'] = IsMulticastJoinLeaveLatencyEnabled
        if IsMulticastGroupCapacityEnabled is not None:
            self._IsMulticastGroupCapacityEnabled = IsMulticastGroupCapacityEnabled
            properties['IsMulticastGroupCapacityEnabled'] = IsMulticastGroupCapacityEnabled
        if EnabledSeqence is not None:
            self._EnabledSeqence = EnabledSeqence
            properties['EnabledSeqence'] = EnabledSeqence

        super(Rfc3918WizardCompositeConfig, self).edit(**properties)

    @property
    def IsMixedClassThroughputEnabled(self):
        """
        get the value of property _IsMixedClassThroughputEnabled
        """
        if self.force_auto_sync:
            self.get('IsMixedClassThroughputEnabled')
        return self._IsMixedClassThroughputEnabled

    @property
    def IsScaledGroupForwardingMatrixEnabled(self):
        """
        get the value of property _IsScaledGroupForwardingMatrixEnabled
        """
        if self.force_auto_sync:
            self.get('IsScaledGroupForwardingMatrixEnabled')
        return self._IsScaledGroupForwardingMatrixEnabled

    @property
    def IsAggregatedMulticastThroughputEnabled(self):
        """
        get the value of property _IsAggregatedMulticastThroughputEnabled
        """
        if self.force_auto_sync:
            self.get('IsAggregatedMulticastThroughputEnabled')
        return self._IsAggregatedMulticastThroughputEnabled

    @property
    def IsMulticastForwardingLatencyEnabled(self):
        """
        get the value of property _IsMulticastForwardingLatencyEnabled
        """
        if self.force_auto_sync:
            self.get('IsMulticastForwardingLatencyEnabled')
        return self._IsMulticastForwardingLatencyEnabled

    @property
    def IsMulticastJoinLeaveLatencyEnabled(self):
        """
        get the value of property _IsMulticastJoinLeaveLatencyEnabled
        """
        if self.force_auto_sync:
            self.get('IsMulticastJoinLeaveLatencyEnabled')
        return self._IsMulticastJoinLeaveLatencyEnabled

    @property
    def IsMulticastGroupCapacityEnabled(self):
        """
        get the value of property _IsMulticastGroupCapacityEnabled
        """
        if self.force_auto_sync:
            self.get('IsMulticastGroupCapacityEnabled')
        return self._IsMulticastGroupCapacityEnabled

    @property
    def EnabledSeqence(self):
        """
        get the value of property _EnabledSeqence
        """
        if self.force_auto_sync:
            self.get('EnabledSeqence')
        return self._EnabledSeqence

    @IsMixedClassThroughputEnabled.setter
    def IsMixedClassThroughputEnabled(self, value):
        self._IsMixedClassThroughputEnabled = value
        self.edit(IsMixedClassThroughputEnabled=value)

    @IsScaledGroupForwardingMatrixEnabled.setter
    def IsScaledGroupForwardingMatrixEnabled(self, value):
        self._IsScaledGroupForwardingMatrixEnabled = value
        self.edit(IsScaledGroupForwardingMatrixEnabled=value)

    @IsAggregatedMulticastThroughputEnabled.setter
    def IsAggregatedMulticastThroughputEnabled(self, value):
        self._IsAggregatedMulticastThroughputEnabled = value
        self.edit(IsAggregatedMulticastThroughputEnabled=value)

    @IsMulticastForwardingLatencyEnabled.setter
    def IsMulticastForwardingLatencyEnabled(self, value):
        self._IsMulticastForwardingLatencyEnabled = value
        self.edit(IsMulticastForwardingLatencyEnabled=value)

    @IsMulticastJoinLeaveLatencyEnabled.setter
    def IsMulticastJoinLeaveLatencyEnabled(self, value):
        self._IsMulticastJoinLeaveLatencyEnabled = value
        self.edit(IsMulticastJoinLeaveLatencyEnabled=value)

    @IsMulticastGroupCapacityEnabled.setter
    def IsMulticastGroupCapacityEnabled(self, value):
        self._IsMulticastGroupCapacityEnabled = value
        self.edit(IsMulticastGroupCapacityEnabled=value)

    @EnabledSeqence.setter
    def EnabledSeqence(self, value):
        self._EnabledSeqence = value
        self.edit(EnabledSeqence=value)

    def _set_ismixedclassthroughputenabled_with_str(self, value):
        self._IsMixedClassThroughputEnabled = (value == 'True')

    def _set_isscaledgroupforwardingmatrixenabled_with_str(self, value):
        self._IsScaledGroupForwardingMatrixEnabled = (value == 'True')

    def _set_isaggregatedmulticastthroughputenabled_with_str(self, value):
        self._IsAggregatedMulticastThroughputEnabled = (value == 'True')

    def _set_ismulticastforwardinglatencyenabled_with_str(self, value):
        self._IsMulticastForwardingLatencyEnabled = (value == 'True')

    def _set_ismulticastjoinleavelatencyenabled_with_str(self, value):
        self._IsMulticastJoinLeaveLatencyEnabled = (value == 'True')

    def _set_ismulticastgroupcapacityenabled_with_str(self, value):
        self._IsMulticastGroupCapacityEnabled = (value == 'True')

    def _set_enabledseqence_with_str(self, value):
        self._EnabledSeqence = value

