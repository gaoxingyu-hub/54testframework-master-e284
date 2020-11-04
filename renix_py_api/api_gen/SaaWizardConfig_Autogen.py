"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ProtocolWizardConfig_Autogen import ProtocolWizardConfig


@rom_manager.rom
class SaaWizardConfig(ProtocolWizardConfig):
    def __init__(self, EnableDAD=None, DADTransmitCount=None, DADRetransmitDelay=None, RouterSolicitationRetries=None, RouterSolicitationRetransmitDelay=None, EnableEui64LinkLocal=None, **kwargs):
        self._EnableDAD = EnableDAD  # Duplicate Address Detection
        self._DADTransmitCount = DADTransmitCount  # DAD Transmit Count
        self._DADRetransmitDelay = DADRetransmitDelay  # DAD Retransmit Delay (msec)
        self._RouterSolicitationRetries = RouterSolicitationRetries  # Router Solicitation Retries
        self._RouterSolicitationRetransmitDelay = RouterSolicitationRetransmitDelay  # Router Solicitation Retransmit Delay (msec)
        self._EnableEui64LinkLocal = EnableEui64LinkLocal  # Enable EUI-64 Link Local

        properties = kwargs.copy()
        if EnableDAD is not None:
            properties['EnableDAD'] = EnableDAD
        if DADTransmitCount is not None:
            properties['DADTransmitCount'] = DADTransmitCount
        if DADRetransmitDelay is not None:
            properties['DADRetransmitDelay'] = DADRetransmitDelay
        if RouterSolicitationRetries is not None:
            properties['RouterSolicitationRetries'] = RouterSolicitationRetries
        if RouterSolicitationRetransmitDelay is not None:
            properties['RouterSolicitationRetransmitDelay'] = RouterSolicitationRetransmitDelay
        if EnableEui64LinkLocal is not None:
            properties['EnableEui64LinkLocal'] = EnableEui64LinkLocal

        # call base class function, and it will send message to renix server to create a class.
        super(SaaWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EnableDAD=None, DADTransmitCount=None, DADRetransmitDelay=None, RouterSolicitationRetries=None, RouterSolicitationRetransmitDelay=None, EnableEui64LinkLocal=None, **kwargs):
        properties = kwargs.copy()
        if EnableDAD is not None:
            self._EnableDAD = EnableDAD
            properties['EnableDAD'] = EnableDAD
        if DADTransmitCount is not None:
            self._DADTransmitCount = DADTransmitCount
            properties['DADTransmitCount'] = DADTransmitCount
        if DADRetransmitDelay is not None:
            self._DADRetransmitDelay = DADRetransmitDelay
            properties['DADRetransmitDelay'] = DADRetransmitDelay
        if RouterSolicitationRetries is not None:
            self._RouterSolicitationRetries = RouterSolicitationRetries
            properties['RouterSolicitationRetries'] = RouterSolicitationRetries
        if RouterSolicitationRetransmitDelay is not None:
            self._RouterSolicitationRetransmitDelay = RouterSolicitationRetransmitDelay
            properties['RouterSolicitationRetransmitDelay'] = RouterSolicitationRetransmitDelay
        if EnableEui64LinkLocal is not None:
            self._EnableEui64LinkLocal = EnableEui64LinkLocal
            properties['EnableEui64LinkLocal'] = EnableEui64LinkLocal

        super(SaaWizardConfig, self).edit(**properties)

    @property
    def EnableDAD(self):
        """
        get the value of property _EnableDAD
        """
        if self.force_auto_sync:
            self.get('EnableDAD')
        return self._EnableDAD

    @property
    def DADTransmitCount(self):
        """
        get the value of property _DADTransmitCount
        """
        if self.force_auto_sync:
            self.get('DADTransmitCount')
        return self._DADTransmitCount

    @property
    def DADRetransmitDelay(self):
        """
        get the value of property _DADRetransmitDelay
        """
        if self.force_auto_sync:
            self.get('DADRetransmitDelay')
        return self._DADRetransmitDelay

    @property
    def RouterSolicitationRetries(self):
        """
        get the value of property _RouterSolicitationRetries
        """
        if self.force_auto_sync:
            self.get('RouterSolicitationRetries')
        return self._RouterSolicitationRetries

    @property
    def RouterSolicitationRetransmitDelay(self):
        """
        get the value of property _RouterSolicitationRetransmitDelay
        """
        if self.force_auto_sync:
            self.get('RouterSolicitationRetransmitDelay')
        return self._RouterSolicitationRetransmitDelay

    @property
    def EnableEui64LinkLocal(self):
        """
        get the value of property _EnableEui64LinkLocal
        """
        if self.force_auto_sync:
            self.get('EnableEui64LinkLocal')
        return self._EnableEui64LinkLocal

    @EnableDAD.setter
    def EnableDAD(self, value):
        self._EnableDAD = value
        self.edit(EnableDAD=value)

    @DADTransmitCount.setter
    def DADTransmitCount(self, value):
        self._DADTransmitCount = value
        self.edit(DADTransmitCount=value)

    @DADRetransmitDelay.setter
    def DADRetransmitDelay(self, value):
        self._DADRetransmitDelay = value
        self.edit(DADRetransmitDelay=value)

    @RouterSolicitationRetries.setter
    def RouterSolicitationRetries(self, value):
        self._RouterSolicitationRetries = value
        self.edit(RouterSolicitationRetries=value)

    @RouterSolicitationRetransmitDelay.setter
    def RouterSolicitationRetransmitDelay(self, value):
        self._RouterSolicitationRetransmitDelay = value
        self.edit(RouterSolicitationRetransmitDelay=value)

    @EnableEui64LinkLocal.setter
    def EnableEui64LinkLocal(self, value):
        self._EnableEui64LinkLocal = value
        self.edit(EnableEui64LinkLocal=value)

    def _set_enabledad_with_str(self, value):
        self._EnableDAD = (value == 'True')

    def _set_dadtransmitcount_with_str(self, value):
        try:
            self._DADTransmitCount = int(value)
        except ValueError:
            self._DADTransmitCount = hex(int(value, 16))

    def _set_dadretransmitdelay_with_str(self, value):
        try:
            self._DADRetransmitDelay = int(value)
        except ValueError:
            self._DADRetransmitDelay = hex(int(value, 16))

    def _set_routersolicitationretries_with_str(self, value):
        try:
            self._RouterSolicitationRetries = int(value)
        except ValueError:
            self._RouterSolicitationRetries = hex(int(value, 16))

    def _set_routersolicitationretransmitdelay_with_str(self, value):
        try:
            self._RouterSolicitationRetransmitDelay = int(value)
        except ValueError:
            self._RouterSolicitationRetransmitDelay = hex(int(value, 16))

    def _set_enableeui64linklocal_with_str(self, value):
        self._EnableEui64LinkLocal = (value == 'True')

