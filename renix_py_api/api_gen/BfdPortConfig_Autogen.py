"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class BfdPortConfig(ROMObject):
    def __init__(self, ConnectivityVerificationChannelType=None, ControlChannelType=None, **kwargs):
        self._ConnectivityVerificationChannelType = ConnectivityVerificationChannelType  # CV Channel Type (hex)
        self._ControlChannelType = ControlChannelType  # CC Channel Type (hex)

        properties = kwargs.copy()
        if ConnectivityVerificationChannelType is not None:
            properties['ConnectivityVerificationChannelType'] = ConnectivityVerificationChannelType
        if ControlChannelType is not None:
            properties['ControlChannelType'] = ControlChannelType

        # call base class function, and it will send message to renix server to create a class.
        super(BfdPortConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ConnectivityVerificationChannelType=None, ControlChannelType=None, **kwargs):
        properties = kwargs.copy()
        if ConnectivityVerificationChannelType is not None:
            self._ConnectivityVerificationChannelType = ConnectivityVerificationChannelType
            properties['ConnectivityVerificationChannelType'] = ConnectivityVerificationChannelType
        if ControlChannelType is not None:
            self._ControlChannelType = ControlChannelType
            properties['ControlChannelType'] = ControlChannelType

        super(BfdPortConfig, self).edit(**properties)

    @property
    def ConnectivityVerificationChannelType(self):
        """
        get the value of property _ConnectivityVerificationChannelType
        """
        if self.force_auto_sync:
            self.get('ConnectivityVerificationChannelType')
        return self._ConnectivityVerificationChannelType

    @property
    def ControlChannelType(self):
        """
        get the value of property _ControlChannelType
        """
        if self.force_auto_sync:
            self.get('ControlChannelType')
        return self._ControlChannelType

    @ConnectivityVerificationChannelType.setter
    def ConnectivityVerificationChannelType(self, value):
        self._ConnectivityVerificationChannelType = value
        self.edit(ConnectivityVerificationChannelType=value)

    @ControlChannelType.setter
    def ControlChannelType(self, value):
        self._ControlChannelType = value
        self.edit(ControlChannelType=value)

    def _set_connectivityverificationchanneltype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ConnectivityVerificationChannelType = BfdConnectivityVerificationTypeEnum.%s' % value[:seperate])

    def _set_controlchanneltype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ControlChannelType = BfdControlChannelTypeEnum.%s' % value[:seperate])

