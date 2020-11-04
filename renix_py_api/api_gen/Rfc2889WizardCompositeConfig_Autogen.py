"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BenchmarkWizardCompositeConfig_Autogen import BenchmarkWizardCompositeConfig


@rom_manager.rom
class Rfc2889WizardCompositeConfig(BenchmarkWizardCompositeConfig):
    def __init__(self, IsAddressCachingCapacityEnabled=None, IsAddressLearningRateEnabled=None, IsBroadcastFramesForwardingEnabled=None, IsBroadcastFramesLatencyEnabled=None, IsCongestControlEnabled=None, IsErroredFramesFilteringEnabled=None, IsForwardPressureRateEnabled=None, IsForwardingEnabled=None, **kwargs):
        self._IsAddressCachingCapacityEnabled = IsAddressCachingCapacityEnabled  # Rfc2889 Address Caching Capacity Test
        self._IsAddressLearningRateEnabled = IsAddressLearningRateEnabled  # Rfc2889 Address Learning Rate Test
        self._IsBroadcastFramesForwardingEnabled = IsBroadcastFramesForwardingEnabled  # Rfc2889 Broadcast Frame Forwarding Test
        self._IsBroadcastFramesLatencyEnabled = IsBroadcastFramesLatencyEnabled  # Rfc2889 Broadcast Frame Latency Test
        self._IsCongestControlEnabled = IsCongestControlEnabled  # Rfc2889 Congest Control Test
        self._IsErroredFramesFilteringEnabled = IsErroredFramesFilteringEnabled  # Rfc2889 Errored Frames Filtering Test
        self._IsForwardPressureRateEnabled = IsForwardPressureRateEnabled  # Rfc2889 Forward Pressure Rate Test
        self._IsForwardingEnabled = IsForwardingEnabled  # Rfc2889 Forwarding Test

        properties = kwargs.copy()
        if IsAddressCachingCapacityEnabled is not None:
            properties['IsAddressCachingCapacityEnabled'] = IsAddressCachingCapacityEnabled
        if IsAddressLearningRateEnabled is not None:
            properties['IsAddressLearningRateEnabled'] = IsAddressLearningRateEnabled
        if IsBroadcastFramesForwardingEnabled is not None:
            properties['IsBroadcastFramesForwardingEnabled'] = IsBroadcastFramesForwardingEnabled
        if IsBroadcastFramesLatencyEnabled is not None:
            properties['IsBroadcastFramesLatencyEnabled'] = IsBroadcastFramesLatencyEnabled
        if IsCongestControlEnabled is not None:
            properties['IsCongestControlEnabled'] = IsCongestControlEnabled
        if IsErroredFramesFilteringEnabled is not None:
            properties['IsErroredFramesFilteringEnabled'] = IsErroredFramesFilteringEnabled
        if IsForwardPressureRateEnabled is not None:
            properties['IsForwardPressureRateEnabled'] = IsForwardPressureRateEnabled
        if IsForwardingEnabled is not None:
            properties['IsForwardingEnabled'] = IsForwardingEnabled

        # call base class function, and it will send message to renix server to create a class.
        super(Rfc2889WizardCompositeConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, IsAddressCachingCapacityEnabled=None, IsAddressLearningRateEnabled=None, IsBroadcastFramesForwardingEnabled=None, IsBroadcastFramesLatencyEnabled=None, IsCongestControlEnabled=None, IsErroredFramesFilteringEnabled=None, IsForwardPressureRateEnabled=None, IsForwardingEnabled=None, **kwargs):
        properties = kwargs.copy()
        if IsAddressCachingCapacityEnabled is not None:
            self._IsAddressCachingCapacityEnabled = IsAddressCachingCapacityEnabled
            properties['IsAddressCachingCapacityEnabled'] = IsAddressCachingCapacityEnabled
        if IsAddressLearningRateEnabled is not None:
            self._IsAddressLearningRateEnabled = IsAddressLearningRateEnabled
            properties['IsAddressLearningRateEnabled'] = IsAddressLearningRateEnabled
        if IsBroadcastFramesForwardingEnabled is not None:
            self._IsBroadcastFramesForwardingEnabled = IsBroadcastFramesForwardingEnabled
            properties['IsBroadcastFramesForwardingEnabled'] = IsBroadcastFramesForwardingEnabled
        if IsBroadcastFramesLatencyEnabled is not None:
            self._IsBroadcastFramesLatencyEnabled = IsBroadcastFramesLatencyEnabled
            properties['IsBroadcastFramesLatencyEnabled'] = IsBroadcastFramesLatencyEnabled
        if IsCongestControlEnabled is not None:
            self._IsCongestControlEnabled = IsCongestControlEnabled
            properties['IsCongestControlEnabled'] = IsCongestControlEnabled
        if IsErroredFramesFilteringEnabled is not None:
            self._IsErroredFramesFilteringEnabled = IsErroredFramesFilteringEnabled
            properties['IsErroredFramesFilteringEnabled'] = IsErroredFramesFilteringEnabled
        if IsForwardPressureRateEnabled is not None:
            self._IsForwardPressureRateEnabled = IsForwardPressureRateEnabled
            properties['IsForwardPressureRateEnabled'] = IsForwardPressureRateEnabled
        if IsForwardingEnabled is not None:
            self._IsForwardingEnabled = IsForwardingEnabled
            properties['IsForwardingEnabled'] = IsForwardingEnabled

        super(Rfc2889WizardCompositeConfig, self).edit(**properties)

    @property
    def IsAddressCachingCapacityEnabled(self):
        """
        get the value of property _IsAddressCachingCapacityEnabled
        """
        if self.force_auto_sync:
            self.get('IsAddressCachingCapacityEnabled')
        return self._IsAddressCachingCapacityEnabled

    @property
    def IsAddressLearningRateEnabled(self):
        """
        get the value of property _IsAddressLearningRateEnabled
        """
        if self.force_auto_sync:
            self.get('IsAddressLearningRateEnabled')
        return self._IsAddressLearningRateEnabled

    @property
    def IsBroadcastFramesForwardingEnabled(self):
        """
        get the value of property _IsBroadcastFramesForwardingEnabled
        """
        if self.force_auto_sync:
            self.get('IsBroadcastFramesForwardingEnabled')
        return self._IsBroadcastFramesForwardingEnabled

    @property
    def IsBroadcastFramesLatencyEnabled(self):
        """
        get the value of property _IsBroadcastFramesLatencyEnabled
        """
        if self.force_auto_sync:
            self.get('IsBroadcastFramesLatencyEnabled')
        return self._IsBroadcastFramesLatencyEnabled

    @property
    def IsCongestControlEnabled(self):
        """
        get the value of property _IsCongestControlEnabled
        """
        if self.force_auto_sync:
            self.get('IsCongestControlEnabled')
        return self._IsCongestControlEnabled

    @property
    def IsErroredFramesFilteringEnabled(self):
        """
        get the value of property _IsErroredFramesFilteringEnabled
        """
        if self.force_auto_sync:
            self.get('IsErroredFramesFilteringEnabled')
        return self._IsErroredFramesFilteringEnabled

    @property
    def IsForwardPressureRateEnabled(self):
        """
        get the value of property _IsForwardPressureRateEnabled
        """
        if self.force_auto_sync:
            self.get('IsForwardPressureRateEnabled')
        return self._IsForwardPressureRateEnabled

    @property
    def IsForwardingEnabled(self):
        """
        get the value of property _IsForwardingEnabled
        """
        if self.force_auto_sync:
            self.get('IsForwardingEnabled')
        return self._IsForwardingEnabled

    @IsAddressCachingCapacityEnabled.setter
    def IsAddressCachingCapacityEnabled(self, value):
        self._IsAddressCachingCapacityEnabled = value
        self.edit(IsAddressCachingCapacityEnabled=value)

    @IsAddressLearningRateEnabled.setter
    def IsAddressLearningRateEnabled(self, value):
        self._IsAddressLearningRateEnabled = value
        self.edit(IsAddressLearningRateEnabled=value)

    @IsBroadcastFramesForwardingEnabled.setter
    def IsBroadcastFramesForwardingEnabled(self, value):
        self._IsBroadcastFramesForwardingEnabled = value
        self.edit(IsBroadcastFramesForwardingEnabled=value)

    @IsBroadcastFramesLatencyEnabled.setter
    def IsBroadcastFramesLatencyEnabled(self, value):
        self._IsBroadcastFramesLatencyEnabled = value
        self.edit(IsBroadcastFramesLatencyEnabled=value)

    @IsCongestControlEnabled.setter
    def IsCongestControlEnabled(self, value):
        self._IsCongestControlEnabled = value
        self.edit(IsCongestControlEnabled=value)

    @IsErroredFramesFilteringEnabled.setter
    def IsErroredFramesFilteringEnabled(self, value):
        self._IsErroredFramesFilteringEnabled = value
        self.edit(IsErroredFramesFilteringEnabled=value)

    @IsForwardPressureRateEnabled.setter
    def IsForwardPressureRateEnabled(self, value):
        self._IsForwardPressureRateEnabled = value
        self.edit(IsForwardPressureRateEnabled=value)

    @IsForwardingEnabled.setter
    def IsForwardingEnabled(self, value):
        self._IsForwardingEnabled = value
        self.edit(IsForwardingEnabled=value)

    def _set_isaddresscachingcapacityenabled_with_str(self, value):
        self._IsAddressCachingCapacityEnabled = (value == 'True')

    def _set_isaddresslearningrateenabled_with_str(self, value):
        self._IsAddressLearningRateEnabled = (value == 'True')

    def _set_isbroadcastframesforwardingenabled_with_str(self, value):
        self._IsBroadcastFramesForwardingEnabled = (value == 'True')

    def _set_isbroadcastframeslatencyenabled_with_str(self, value):
        self._IsBroadcastFramesLatencyEnabled = (value == 'True')

    def _set_iscongestcontrolenabled_with_str(self, value):
        self._IsCongestControlEnabled = (value == 'True')

    def _set_iserroredframesfilteringenabled_with_str(self, value):
        self._IsErroredFramesFilteringEnabled = (value == 'True')

    def _set_isforwardpressurerateenabled_with_str(self, value):
        self._IsForwardPressureRateEnabled = (value == 'True')

    def _set_isforwardingenabled_with_str(self, value):
        self._IsForwardingEnabled = (value == 'True')

