"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Y1564L4Config(ROMObject):
    def __init__(self, ProtocolTypeOverIp=None, SourcePortValue=None, SourcePortCount=None, SourcePortStep=None, DestinationPortValue=None, DestinationPortCount=None, DestinationPortStep=None, **kwargs):
        self._ProtocolTypeOverIp = ProtocolTypeOverIp  # Protocol Type Over IP
        self._SourcePortValue = SourcePortValue  # Source Port Value
        self._SourcePortCount = SourcePortCount  # Source Port Count
        self._SourcePortStep = SourcePortStep  # Source Port Step
        self._DestinationPortValue = DestinationPortValue  # Destination Port Value
        self._DestinationPortCount = DestinationPortCount  # Destination Port Count
        self._DestinationPortStep = DestinationPortStep  # Destination Port Step

        properties = kwargs.copy()
        if ProtocolTypeOverIp is not None:
            properties['ProtocolTypeOverIp'] = ProtocolTypeOverIp
        if SourcePortValue is not None:
            properties['SourcePortValue'] = SourcePortValue
        if SourcePortCount is not None:
            properties['SourcePortCount'] = SourcePortCount
        if SourcePortStep is not None:
            properties['SourcePortStep'] = SourcePortStep
        if DestinationPortValue is not None:
            properties['DestinationPortValue'] = DestinationPortValue
        if DestinationPortCount is not None:
            properties['DestinationPortCount'] = DestinationPortCount
        if DestinationPortStep is not None:
            properties['DestinationPortStep'] = DestinationPortStep

        # call base class function, and it will send message to renix server to create a class.
        super(Y1564L4Config, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ProtocolTypeOverIp=None, SourcePortValue=None, SourcePortCount=None, SourcePortStep=None, DestinationPortValue=None, DestinationPortCount=None, DestinationPortStep=None, **kwargs):
        properties = kwargs.copy()
        if ProtocolTypeOverIp is not None:
            self._ProtocolTypeOverIp = ProtocolTypeOverIp
            properties['ProtocolTypeOverIp'] = ProtocolTypeOverIp
        if SourcePortValue is not None:
            self._SourcePortValue = SourcePortValue
            properties['SourcePortValue'] = SourcePortValue
        if SourcePortCount is not None:
            self._SourcePortCount = SourcePortCount
            properties['SourcePortCount'] = SourcePortCount
        if SourcePortStep is not None:
            self._SourcePortStep = SourcePortStep
            properties['SourcePortStep'] = SourcePortStep
        if DestinationPortValue is not None:
            self._DestinationPortValue = DestinationPortValue
            properties['DestinationPortValue'] = DestinationPortValue
        if DestinationPortCount is not None:
            self._DestinationPortCount = DestinationPortCount
            properties['DestinationPortCount'] = DestinationPortCount
        if DestinationPortStep is not None:
            self._DestinationPortStep = DestinationPortStep
            properties['DestinationPortStep'] = DestinationPortStep

        super(Y1564L4Config, self).edit(**properties)

    @property
    def ProtocolTypeOverIp(self):
        """
        get the value of property _ProtocolTypeOverIp
        """
        if self.force_auto_sync:
            self.get('ProtocolTypeOverIp')
        return self._ProtocolTypeOverIp

    @property
    def SourcePortValue(self):
        """
        get the value of property _SourcePortValue
        """
        if self.force_auto_sync:
            self.get('SourcePortValue')
        return self._SourcePortValue

    @property
    def SourcePortCount(self):
        """
        get the value of property _SourcePortCount
        """
        if self.force_auto_sync:
            self.get('SourcePortCount')
        return self._SourcePortCount

    @property
    def SourcePortStep(self):
        """
        get the value of property _SourcePortStep
        """
        if self.force_auto_sync:
            self.get('SourcePortStep')
        return self._SourcePortStep

    @property
    def DestinationPortValue(self):
        """
        get the value of property _DestinationPortValue
        """
        if self.force_auto_sync:
            self.get('DestinationPortValue')
        return self._DestinationPortValue

    @property
    def DestinationPortCount(self):
        """
        get the value of property _DestinationPortCount
        """
        if self.force_auto_sync:
            self.get('DestinationPortCount')
        return self._DestinationPortCount

    @property
    def DestinationPortStep(self):
        """
        get the value of property _DestinationPortStep
        """
        if self.force_auto_sync:
            self.get('DestinationPortStep')
        return self._DestinationPortStep

    @ProtocolTypeOverIp.setter
    def ProtocolTypeOverIp(self, value):
        self._ProtocolTypeOverIp = value
        self.edit(ProtocolTypeOverIp=value)

    @SourcePortValue.setter
    def SourcePortValue(self, value):
        self._SourcePortValue = value
        self.edit(SourcePortValue=value)

    @SourcePortCount.setter
    def SourcePortCount(self, value):
        self._SourcePortCount = value
        self.edit(SourcePortCount=value)

    @SourcePortStep.setter
    def SourcePortStep(self, value):
        self._SourcePortStep = value
        self.edit(SourcePortStep=value)

    @DestinationPortValue.setter
    def DestinationPortValue(self, value):
        self._DestinationPortValue = value
        self.edit(DestinationPortValue=value)

    @DestinationPortCount.setter
    def DestinationPortCount(self, value):
        self._DestinationPortCount = value
        self.edit(DestinationPortCount=value)

    @DestinationPortStep.setter
    def DestinationPortStep(self, value):
        self._DestinationPortStep = value
        self.edit(DestinationPortStep=value)

    def _set_protocoltypeoverip_with_str(self, value):
        seperate = value.find(':')
        exec('self._ProtocolTypeOverIp = EnumL4ProtocolType.%s' % value[:seperate])

    def _set_sourceportvalue_with_str(self, value):
        try:
            self._SourcePortValue = int(value)
        except ValueError:
            self._SourcePortValue = hex(int(value, 16))

    def _set_sourceportcount_with_str(self, value):
        try:
            self._SourcePortCount = int(value)
        except ValueError:
            self._SourcePortCount = hex(int(value, 16))

    def _set_sourceportstep_with_str(self, value):
        try:
            self._SourcePortStep = int(value)
        except ValueError:
            self._SourcePortStep = hex(int(value, 16))

    def _set_destinationportvalue_with_str(self, value):
        try:
            self._DestinationPortValue = int(value)
        except ValueError:
            self._DestinationPortValue = hex(int(value, 16))

    def _set_destinationportcount_with_str(self, value):
        try:
            self._DestinationPortCount = int(value)
        except ValueError:
            self._DestinationPortCount = hex(int(value, 16))

    def _set_destinationportstep_with_str(self, value):
        try:
            self._DestinationPortStep = int(value)
        except ValueError:
            self._DestinationPortStep = hex(int(value, 16))

