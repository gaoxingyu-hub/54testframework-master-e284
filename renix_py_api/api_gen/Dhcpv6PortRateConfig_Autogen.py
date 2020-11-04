"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dhcpv6PortRateConfig(ROMObject):
    def __init__(self, RequestRate=None, ReleaseRate=None, RenewRate=None, MaxOutstanding=None, SolicitInitialTimeout=None, SolicitMaxTimeout=None, SolicitRetryCount=None, SolicitIndefiniteRetry=None, SolicitDisableRetries=None, RequestInitialTimeout=None, RequestMaxTimeout=None, RequestRetryCount=None, RequestIndefiniteRetry=None, RequestDisableRetries=None, ConfirmInitialTimeout=None, ConfirmMaxTimeout=None, ConfirmMaxDuration=None, RenewInitialTimeout=None, RenewMaxTimeout=None, RenewRetryCount=None, RenewIndefiniteRetry=None, RenewDisableRetries=None, RebindInitialTimeout=None, RebindMaxTimeout=None, RebindRetryCount=None, RebindIndefiniteRetry=None, RebindDisableRetries=None, ReleaseInitialTimeout=None, ReleaseRetryCount=None, ReleaseIndefiniteRetry=None, ReleaseDisableRetries=None, DeclineInitialTimeout=None, DeclineRetryCount=None, DeclineIndefiniteRetry=None, DeclineDisableRetries=None, InfoRequestInitialTimeout=None, InfoRequestMaxTimeout=None, InfoRequestRetryCount=None, InfoRequestIndefiniteRetry=None, InfoRequestDisableRetries=None, **kwargs):
        self._RequestRate = RequestRate  # Request Rate (sessions/sec)
        self._ReleaseRate = ReleaseRate  # Release Rate (sessions/sec)
        self._RenewRate = RenewRate  # Renew Rate (sessions/sec)
        self._MaxOutstanding = MaxOutstanding  # Max Outstanding Session
        self._SolicitInitialTimeout = SolicitInitialTimeout  # Solicit Message Initial Timeout (sec)
        self._SolicitMaxTimeout = SolicitMaxTimeout  # Solicit Message Max Timeout (sec)
        self._SolicitRetryCount = SolicitRetryCount  # Solicit Message Retry Count
        self._SolicitIndefiniteRetry = SolicitIndefiniteRetry  # Solicit Message Indefinite Retry
        self._SolicitDisableRetries = SolicitDisableRetries  # Solicit Message Disable Retries
        self._RequestInitialTimeout = RequestInitialTimeout  # Request Message Initial Timeout (sec)
        self._RequestMaxTimeout = RequestMaxTimeout  # Request Message Max Timeout (sec)
        self._RequestRetryCount = RequestRetryCount  # Request Message Retry Count
        self._RequestIndefiniteRetry = RequestIndefiniteRetry  # Request Message Indefinite Retry
        self._RequestDisableRetries = RequestDisableRetries  # Request Message Disable Retries
        self._ConfirmInitialTimeout = ConfirmInitialTimeout  # Confirm Message Initial Timeout (sec)
        self._ConfirmMaxTimeout = ConfirmMaxTimeout  # Confirm Message Max Timeout (sec)
        self._ConfirmMaxDuration = ConfirmMaxDuration  # Confirm Message Max Duration
        self._RenewInitialTimeout = RenewInitialTimeout  # Renew Message Initial Timeout (sec)
        self._RenewMaxTimeout = RenewMaxTimeout  # Renew Message Max Timeout (sec)
        self._RenewRetryCount = RenewRetryCount  # Renew Message Retry Count
        self._RenewIndefiniteRetry = RenewIndefiniteRetry  # Renew Message Indefinite Retry
        self._RenewDisableRetries = RenewDisableRetries  # Renew Message Disable Retries
        self._RebindInitialTimeout = RebindInitialTimeout  # Rebind Message Initial Timeout (sec)
        self._RebindMaxTimeout = RebindMaxTimeout  # Rebind Message Max Timeout (sec)
        self._RebindRetryCount = RebindRetryCount  # Rebind Message Retry Count
        self._RebindIndefiniteRetry = RebindIndefiniteRetry  # Rebind Message Indefinite Retry
        self._RebindDisableRetries = RebindDisableRetries  # Rebind Message Disable Retries
        self._ReleaseInitialTimeout = ReleaseInitialTimeout  # Release Message Initial Timeout (sec)
        self._ReleaseRetryCount = ReleaseRetryCount  # Release Message Retry Count
        self._ReleaseIndefiniteRetry = ReleaseIndefiniteRetry  # Release Message Indefinite Retry
        self._ReleaseDisableRetries = ReleaseDisableRetries  # Release Message Disable Retries
        self._DeclineInitialTimeout = DeclineInitialTimeout  # Decline Message Initial Timeout (sec)
        self._DeclineRetryCount = DeclineRetryCount  # Decline Message Retry Count
        self._DeclineIndefiniteRetry = DeclineIndefiniteRetry  # Decline Message Indefinite Retry
        self._DeclineDisableRetries = DeclineDisableRetries  # Decline Message Disable Retries
        self._InfoRequestInitialTimeout = InfoRequestInitialTimeout  # Information-Request Message Initial Timeout (sec)
        self._InfoRequestMaxTimeout = InfoRequestMaxTimeout  # Information-Request Message Max Timeout (sec)
        self._InfoRequestRetryCount = InfoRequestRetryCount  # Information-Request Message Retry Count
        self._InfoRequestIndefiniteRetry = InfoRequestIndefiniteRetry  # Information-Request Message Indefinite Retry
        self._InfoRequestDisableRetries = InfoRequestDisableRetries  # Information-Request Message Disable Retries

        properties = kwargs.copy()
        if RequestRate is not None:
            properties['RequestRate'] = RequestRate
        if ReleaseRate is not None:
            properties['ReleaseRate'] = ReleaseRate
        if RenewRate is not None:
            properties['RenewRate'] = RenewRate
        if MaxOutstanding is not None:
            properties['MaxOutstanding'] = MaxOutstanding
        if SolicitInitialTimeout is not None:
            properties['SolicitInitialTimeout'] = SolicitInitialTimeout
        if SolicitMaxTimeout is not None:
            properties['SolicitMaxTimeout'] = SolicitMaxTimeout
        if SolicitRetryCount is not None:
            properties['SolicitRetryCount'] = SolicitRetryCount
        if SolicitIndefiniteRetry is not None:
            properties['SolicitIndefiniteRetry'] = SolicitIndefiniteRetry
        if SolicitDisableRetries is not None:
            properties['SolicitDisableRetries'] = SolicitDisableRetries
        if RequestInitialTimeout is not None:
            properties['RequestInitialTimeout'] = RequestInitialTimeout
        if RequestMaxTimeout is not None:
            properties['RequestMaxTimeout'] = RequestMaxTimeout
        if RequestRetryCount is not None:
            properties['RequestRetryCount'] = RequestRetryCount
        if RequestIndefiniteRetry is not None:
            properties['RequestIndefiniteRetry'] = RequestIndefiniteRetry
        if RequestDisableRetries is not None:
            properties['RequestDisableRetries'] = RequestDisableRetries
        if ConfirmInitialTimeout is not None:
            properties['ConfirmInitialTimeout'] = ConfirmInitialTimeout
        if ConfirmMaxTimeout is not None:
            properties['ConfirmMaxTimeout'] = ConfirmMaxTimeout
        if ConfirmMaxDuration is not None:
            properties['ConfirmMaxDuration'] = ConfirmMaxDuration
        if RenewInitialTimeout is not None:
            properties['RenewInitialTimeout'] = RenewInitialTimeout
        if RenewMaxTimeout is not None:
            properties['RenewMaxTimeout'] = RenewMaxTimeout
        if RenewRetryCount is not None:
            properties['RenewRetryCount'] = RenewRetryCount
        if RenewIndefiniteRetry is not None:
            properties['RenewIndefiniteRetry'] = RenewIndefiniteRetry
        if RenewDisableRetries is not None:
            properties['RenewDisableRetries'] = RenewDisableRetries
        if RebindInitialTimeout is not None:
            properties['RebindInitialTimeout'] = RebindInitialTimeout
        if RebindMaxTimeout is not None:
            properties['RebindMaxTimeout'] = RebindMaxTimeout
        if RebindRetryCount is not None:
            properties['RebindRetryCount'] = RebindRetryCount
        if RebindIndefiniteRetry is not None:
            properties['RebindIndefiniteRetry'] = RebindIndefiniteRetry
        if RebindDisableRetries is not None:
            properties['RebindDisableRetries'] = RebindDisableRetries
        if ReleaseInitialTimeout is not None:
            properties['ReleaseInitialTimeout'] = ReleaseInitialTimeout
        if ReleaseRetryCount is not None:
            properties['ReleaseRetryCount'] = ReleaseRetryCount
        if ReleaseIndefiniteRetry is not None:
            properties['ReleaseIndefiniteRetry'] = ReleaseIndefiniteRetry
        if ReleaseDisableRetries is not None:
            properties['ReleaseDisableRetries'] = ReleaseDisableRetries
        if DeclineInitialTimeout is not None:
            properties['DeclineInitialTimeout'] = DeclineInitialTimeout
        if DeclineRetryCount is not None:
            properties['DeclineRetryCount'] = DeclineRetryCount
        if DeclineIndefiniteRetry is not None:
            properties['DeclineIndefiniteRetry'] = DeclineIndefiniteRetry
        if DeclineDisableRetries is not None:
            properties['DeclineDisableRetries'] = DeclineDisableRetries
        if InfoRequestInitialTimeout is not None:
            properties['InfoRequestInitialTimeout'] = InfoRequestInitialTimeout
        if InfoRequestMaxTimeout is not None:
            properties['InfoRequestMaxTimeout'] = InfoRequestMaxTimeout
        if InfoRequestRetryCount is not None:
            properties['InfoRequestRetryCount'] = InfoRequestRetryCount
        if InfoRequestIndefiniteRetry is not None:
            properties['InfoRequestIndefiniteRetry'] = InfoRequestIndefiniteRetry
        if InfoRequestDisableRetries is not None:
            properties['InfoRequestDisableRetries'] = InfoRequestDisableRetries

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv6PortRateConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RequestRate=None, ReleaseRate=None, RenewRate=None, MaxOutstanding=None, SolicitInitialTimeout=None, SolicitMaxTimeout=None, SolicitRetryCount=None, SolicitIndefiniteRetry=None, SolicitDisableRetries=None, RequestInitialTimeout=None, RequestMaxTimeout=None, RequestRetryCount=None, RequestIndefiniteRetry=None, RequestDisableRetries=None, ConfirmInitialTimeout=None, ConfirmMaxTimeout=None, ConfirmMaxDuration=None, RenewInitialTimeout=None, RenewMaxTimeout=None, RenewRetryCount=None, RenewIndefiniteRetry=None, RenewDisableRetries=None, RebindInitialTimeout=None, RebindMaxTimeout=None, RebindRetryCount=None, RebindIndefiniteRetry=None, RebindDisableRetries=None, ReleaseInitialTimeout=None, ReleaseRetryCount=None, ReleaseIndefiniteRetry=None, ReleaseDisableRetries=None, DeclineInitialTimeout=None, DeclineRetryCount=None, DeclineIndefiniteRetry=None, DeclineDisableRetries=None, InfoRequestInitialTimeout=None, InfoRequestMaxTimeout=None, InfoRequestRetryCount=None, InfoRequestIndefiniteRetry=None, InfoRequestDisableRetries=None, **kwargs):
        properties = kwargs.copy()
        if RequestRate is not None:
            self._RequestRate = RequestRate
            properties['RequestRate'] = RequestRate
        if ReleaseRate is not None:
            self._ReleaseRate = ReleaseRate
            properties['ReleaseRate'] = ReleaseRate
        if RenewRate is not None:
            self._RenewRate = RenewRate
            properties['RenewRate'] = RenewRate
        if MaxOutstanding is not None:
            self._MaxOutstanding = MaxOutstanding
            properties['MaxOutstanding'] = MaxOutstanding
        if SolicitInitialTimeout is not None:
            self._SolicitInitialTimeout = SolicitInitialTimeout
            properties['SolicitInitialTimeout'] = SolicitInitialTimeout
        if SolicitMaxTimeout is not None:
            self._SolicitMaxTimeout = SolicitMaxTimeout
            properties['SolicitMaxTimeout'] = SolicitMaxTimeout
        if SolicitRetryCount is not None:
            self._SolicitRetryCount = SolicitRetryCount
            properties['SolicitRetryCount'] = SolicitRetryCount
        if SolicitIndefiniteRetry is not None:
            self._SolicitIndefiniteRetry = SolicitIndefiniteRetry
            properties['SolicitIndefiniteRetry'] = SolicitIndefiniteRetry
        if SolicitDisableRetries is not None:
            self._SolicitDisableRetries = SolicitDisableRetries
            properties['SolicitDisableRetries'] = SolicitDisableRetries
        if RequestInitialTimeout is not None:
            self._RequestInitialTimeout = RequestInitialTimeout
            properties['RequestInitialTimeout'] = RequestInitialTimeout
        if RequestMaxTimeout is not None:
            self._RequestMaxTimeout = RequestMaxTimeout
            properties['RequestMaxTimeout'] = RequestMaxTimeout
        if RequestRetryCount is not None:
            self._RequestRetryCount = RequestRetryCount
            properties['RequestRetryCount'] = RequestRetryCount
        if RequestIndefiniteRetry is not None:
            self._RequestIndefiniteRetry = RequestIndefiniteRetry
            properties['RequestIndefiniteRetry'] = RequestIndefiniteRetry
        if RequestDisableRetries is not None:
            self._RequestDisableRetries = RequestDisableRetries
            properties['RequestDisableRetries'] = RequestDisableRetries
        if ConfirmInitialTimeout is not None:
            self._ConfirmInitialTimeout = ConfirmInitialTimeout
            properties['ConfirmInitialTimeout'] = ConfirmInitialTimeout
        if ConfirmMaxTimeout is not None:
            self._ConfirmMaxTimeout = ConfirmMaxTimeout
            properties['ConfirmMaxTimeout'] = ConfirmMaxTimeout
        if ConfirmMaxDuration is not None:
            self._ConfirmMaxDuration = ConfirmMaxDuration
            properties['ConfirmMaxDuration'] = ConfirmMaxDuration
        if RenewInitialTimeout is not None:
            self._RenewInitialTimeout = RenewInitialTimeout
            properties['RenewInitialTimeout'] = RenewInitialTimeout
        if RenewMaxTimeout is not None:
            self._RenewMaxTimeout = RenewMaxTimeout
            properties['RenewMaxTimeout'] = RenewMaxTimeout
        if RenewRetryCount is not None:
            self._RenewRetryCount = RenewRetryCount
            properties['RenewRetryCount'] = RenewRetryCount
        if RenewIndefiniteRetry is not None:
            self._RenewIndefiniteRetry = RenewIndefiniteRetry
            properties['RenewIndefiniteRetry'] = RenewIndefiniteRetry
        if RenewDisableRetries is not None:
            self._RenewDisableRetries = RenewDisableRetries
            properties['RenewDisableRetries'] = RenewDisableRetries
        if RebindInitialTimeout is not None:
            self._RebindInitialTimeout = RebindInitialTimeout
            properties['RebindInitialTimeout'] = RebindInitialTimeout
        if RebindMaxTimeout is not None:
            self._RebindMaxTimeout = RebindMaxTimeout
            properties['RebindMaxTimeout'] = RebindMaxTimeout
        if RebindRetryCount is not None:
            self._RebindRetryCount = RebindRetryCount
            properties['RebindRetryCount'] = RebindRetryCount
        if RebindIndefiniteRetry is not None:
            self._RebindIndefiniteRetry = RebindIndefiniteRetry
            properties['RebindIndefiniteRetry'] = RebindIndefiniteRetry
        if RebindDisableRetries is not None:
            self._RebindDisableRetries = RebindDisableRetries
            properties['RebindDisableRetries'] = RebindDisableRetries
        if ReleaseInitialTimeout is not None:
            self._ReleaseInitialTimeout = ReleaseInitialTimeout
            properties['ReleaseInitialTimeout'] = ReleaseInitialTimeout
        if ReleaseRetryCount is not None:
            self._ReleaseRetryCount = ReleaseRetryCount
            properties['ReleaseRetryCount'] = ReleaseRetryCount
        if ReleaseIndefiniteRetry is not None:
            self._ReleaseIndefiniteRetry = ReleaseIndefiniteRetry
            properties['ReleaseIndefiniteRetry'] = ReleaseIndefiniteRetry
        if ReleaseDisableRetries is not None:
            self._ReleaseDisableRetries = ReleaseDisableRetries
            properties['ReleaseDisableRetries'] = ReleaseDisableRetries
        if DeclineInitialTimeout is not None:
            self._DeclineInitialTimeout = DeclineInitialTimeout
            properties['DeclineInitialTimeout'] = DeclineInitialTimeout
        if DeclineRetryCount is not None:
            self._DeclineRetryCount = DeclineRetryCount
            properties['DeclineRetryCount'] = DeclineRetryCount
        if DeclineIndefiniteRetry is not None:
            self._DeclineIndefiniteRetry = DeclineIndefiniteRetry
            properties['DeclineIndefiniteRetry'] = DeclineIndefiniteRetry
        if DeclineDisableRetries is not None:
            self._DeclineDisableRetries = DeclineDisableRetries
            properties['DeclineDisableRetries'] = DeclineDisableRetries
        if InfoRequestInitialTimeout is not None:
            self._InfoRequestInitialTimeout = InfoRequestInitialTimeout
            properties['InfoRequestInitialTimeout'] = InfoRequestInitialTimeout
        if InfoRequestMaxTimeout is not None:
            self._InfoRequestMaxTimeout = InfoRequestMaxTimeout
            properties['InfoRequestMaxTimeout'] = InfoRequestMaxTimeout
        if InfoRequestRetryCount is not None:
            self._InfoRequestRetryCount = InfoRequestRetryCount
            properties['InfoRequestRetryCount'] = InfoRequestRetryCount
        if InfoRequestIndefiniteRetry is not None:
            self._InfoRequestIndefiniteRetry = InfoRequestIndefiniteRetry
            properties['InfoRequestIndefiniteRetry'] = InfoRequestIndefiniteRetry
        if InfoRequestDisableRetries is not None:
            self._InfoRequestDisableRetries = InfoRequestDisableRetries
            properties['InfoRequestDisableRetries'] = InfoRequestDisableRetries

        super(Dhcpv6PortRateConfig, self).edit(**properties)

    @property
    def RequestRate(self):
        """
        get the value of property _RequestRate
        """
        if self.force_auto_sync:
            self.get('RequestRate')
        return self._RequestRate

    @property
    def ReleaseRate(self):
        """
        get the value of property _ReleaseRate
        """
        if self.force_auto_sync:
            self.get('ReleaseRate')
        return self._ReleaseRate

    @property
    def RenewRate(self):
        """
        get the value of property _RenewRate
        """
        if self.force_auto_sync:
            self.get('RenewRate')
        return self._RenewRate

    @property
    def MaxOutstanding(self):
        """
        get the value of property _MaxOutstanding
        """
        if self.force_auto_sync:
            self.get('MaxOutstanding')
        return self._MaxOutstanding

    @property
    def SolicitInitialTimeout(self):
        """
        get the value of property _SolicitInitialTimeout
        """
        if self.force_auto_sync:
            self.get('SolicitInitialTimeout')
        return self._SolicitInitialTimeout

    @property
    def SolicitMaxTimeout(self):
        """
        get the value of property _SolicitMaxTimeout
        """
        if self.force_auto_sync:
            self.get('SolicitMaxTimeout')
        return self._SolicitMaxTimeout

    @property
    def SolicitRetryCount(self):
        """
        get the value of property _SolicitRetryCount
        """
        if self.force_auto_sync:
            self.get('SolicitRetryCount')
        return self._SolicitRetryCount

    @property
    def SolicitIndefiniteRetry(self):
        """
        get the value of property _SolicitIndefiniteRetry
        """
        if self.force_auto_sync:
            self.get('SolicitIndefiniteRetry')
        return self._SolicitIndefiniteRetry

    @property
    def SolicitDisableRetries(self):
        """
        get the value of property _SolicitDisableRetries
        """
        if self.force_auto_sync:
            self.get('SolicitDisableRetries')
        return self._SolicitDisableRetries

    @property
    def RequestInitialTimeout(self):
        """
        get the value of property _RequestInitialTimeout
        """
        if self.force_auto_sync:
            self.get('RequestInitialTimeout')
        return self._RequestInitialTimeout

    @property
    def RequestMaxTimeout(self):
        """
        get the value of property _RequestMaxTimeout
        """
        if self.force_auto_sync:
            self.get('RequestMaxTimeout')
        return self._RequestMaxTimeout

    @property
    def RequestRetryCount(self):
        """
        get the value of property _RequestRetryCount
        """
        if self.force_auto_sync:
            self.get('RequestRetryCount')
        return self._RequestRetryCount

    @property
    def RequestIndefiniteRetry(self):
        """
        get the value of property _RequestIndefiniteRetry
        """
        if self.force_auto_sync:
            self.get('RequestIndefiniteRetry')
        return self._RequestIndefiniteRetry

    @property
    def RequestDisableRetries(self):
        """
        get the value of property _RequestDisableRetries
        """
        if self.force_auto_sync:
            self.get('RequestDisableRetries')
        return self._RequestDisableRetries

    @property
    def ConfirmInitialTimeout(self):
        """
        get the value of property _ConfirmInitialTimeout
        """
        if self.force_auto_sync:
            self.get('ConfirmInitialTimeout')
        return self._ConfirmInitialTimeout

    @property
    def ConfirmMaxTimeout(self):
        """
        get the value of property _ConfirmMaxTimeout
        """
        if self.force_auto_sync:
            self.get('ConfirmMaxTimeout')
        return self._ConfirmMaxTimeout

    @property
    def ConfirmMaxDuration(self):
        """
        get the value of property _ConfirmMaxDuration
        """
        if self.force_auto_sync:
            self.get('ConfirmMaxDuration')
        return self._ConfirmMaxDuration

    @property
    def RenewInitialTimeout(self):
        """
        get the value of property _RenewInitialTimeout
        """
        if self.force_auto_sync:
            self.get('RenewInitialTimeout')
        return self._RenewInitialTimeout

    @property
    def RenewMaxTimeout(self):
        """
        get the value of property _RenewMaxTimeout
        """
        if self.force_auto_sync:
            self.get('RenewMaxTimeout')
        return self._RenewMaxTimeout

    @property
    def RenewRetryCount(self):
        """
        get the value of property _RenewRetryCount
        """
        if self.force_auto_sync:
            self.get('RenewRetryCount')
        return self._RenewRetryCount

    @property
    def RenewIndefiniteRetry(self):
        """
        get the value of property _RenewIndefiniteRetry
        """
        if self.force_auto_sync:
            self.get('RenewIndefiniteRetry')
        return self._RenewIndefiniteRetry

    @property
    def RenewDisableRetries(self):
        """
        get the value of property _RenewDisableRetries
        """
        if self.force_auto_sync:
            self.get('RenewDisableRetries')
        return self._RenewDisableRetries

    @property
    def RebindInitialTimeout(self):
        """
        get the value of property _RebindInitialTimeout
        """
        if self.force_auto_sync:
            self.get('RebindInitialTimeout')
        return self._RebindInitialTimeout

    @property
    def RebindMaxTimeout(self):
        """
        get the value of property _RebindMaxTimeout
        """
        if self.force_auto_sync:
            self.get('RebindMaxTimeout')
        return self._RebindMaxTimeout

    @property
    def RebindRetryCount(self):
        """
        get the value of property _RebindRetryCount
        """
        if self.force_auto_sync:
            self.get('RebindRetryCount')
        return self._RebindRetryCount

    @property
    def RebindIndefiniteRetry(self):
        """
        get the value of property _RebindIndefiniteRetry
        """
        if self.force_auto_sync:
            self.get('RebindIndefiniteRetry')
        return self._RebindIndefiniteRetry

    @property
    def RebindDisableRetries(self):
        """
        get the value of property _RebindDisableRetries
        """
        if self.force_auto_sync:
            self.get('RebindDisableRetries')
        return self._RebindDisableRetries

    @property
    def ReleaseInitialTimeout(self):
        """
        get the value of property _ReleaseInitialTimeout
        """
        if self.force_auto_sync:
            self.get('ReleaseInitialTimeout')
        return self._ReleaseInitialTimeout

    @property
    def ReleaseRetryCount(self):
        """
        get the value of property _ReleaseRetryCount
        """
        if self.force_auto_sync:
            self.get('ReleaseRetryCount')
        return self._ReleaseRetryCount

    @property
    def ReleaseIndefiniteRetry(self):
        """
        get the value of property _ReleaseIndefiniteRetry
        """
        if self.force_auto_sync:
            self.get('ReleaseIndefiniteRetry')
        return self._ReleaseIndefiniteRetry

    @property
    def ReleaseDisableRetries(self):
        """
        get the value of property _ReleaseDisableRetries
        """
        if self.force_auto_sync:
            self.get('ReleaseDisableRetries')
        return self._ReleaseDisableRetries

    @property
    def DeclineInitialTimeout(self):
        """
        get the value of property _DeclineInitialTimeout
        """
        if self.force_auto_sync:
            self.get('DeclineInitialTimeout')
        return self._DeclineInitialTimeout

    @property
    def DeclineRetryCount(self):
        """
        get the value of property _DeclineRetryCount
        """
        if self.force_auto_sync:
            self.get('DeclineRetryCount')
        return self._DeclineRetryCount

    @property
    def DeclineIndefiniteRetry(self):
        """
        get the value of property _DeclineIndefiniteRetry
        """
        if self.force_auto_sync:
            self.get('DeclineIndefiniteRetry')
        return self._DeclineIndefiniteRetry

    @property
    def DeclineDisableRetries(self):
        """
        get the value of property _DeclineDisableRetries
        """
        if self.force_auto_sync:
            self.get('DeclineDisableRetries')
        return self._DeclineDisableRetries

    @property
    def InfoRequestInitialTimeout(self):
        """
        get the value of property _InfoRequestInitialTimeout
        """
        if self.force_auto_sync:
            self.get('InfoRequestInitialTimeout')
        return self._InfoRequestInitialTimeout

    @property
    def InfoRequestMaxTimeout(self):
        """
        get the value of property _InfoRequestMaxTimeout
        """
        if self.force_auto_sync:
            self.get('InfoRequestMaxTimeout')
        return self._InfoRequestMaxTimeout

    @property
    def InfoRequestRetryCount(self):
        """
        get the value of property _InfoRequestRetryCount
        """
        if self.force_auto_sync:
            self.get('InfoRequestRetryCount')
        return self._InfoRequestRetryCount

    @property
    def InfoRequestIndefiniteRetry(self):
        """
        get the value of property _InfoRequestIndefiniteRetry
        """
        if self.force_auto_sync:
            self.get('InfoRequestIndefiniteRetry')
        return self._InfoRequestIndefiniteRetry

    @property
    def InfoRequestDisableRetries(self):
        """
        get the value of property _InfoRequestDisableRetries
        """
        if self.force_auto_sync:
            self.get('InfoRequestDisableRetries')
        return self._InfoRequestDisableRetries

    @RequestRate.setter
    def RequestRate(self, value):
        self._RequestRate = value
        self.edit(RequestRate=value)

    @ReleaseRate.setter
    def ReleaseRate(self, value):
        self._ReleaseRate = value
        self.edit(ReleaseRate=value)

    @RenewRate.setter
    def RenewRate(self, value):
        self._RenewRate = value
        self.edit(RenewRate=value)

    @MaxOutstanding.setter
    def MaxOutstanding(self, value):
        self._MaxOutstanding = value
        self.edit(MaxOutstanding=value)

    @SolicitInitialTimeout.setter
    def SolicitInitialTimeout(self, value):
        self._SolicitInitialTimeout = value
        self.edit(SolicitInitialTimeout=value)

    @SolicitMaxTimeout.setter
    def SolicitMaxTimeout(self, value):
        self._SolicitMaxTimeout = value
        self.edit(SolicitMaxTimeout=value)

    @SolicitRetryCount.setter
    def SolicitRetryCount(self, value):
        self._SolicitRetryCount = value
        self.edit(SolicitRetryCount=value)

    @SolicitIndefiniteRetry.setter
    def SolicitIndefiniteRetry(self, value):
        self._SolicitIndefiniteRetry = value
        self.edit(SolicitIndefiniteRetry=value)

    @SolicitDisableRetries.setter
    def SolicitDisableRetries(self, value):
        self._SolicitDisableRetries = value
        self.edit(SolicitDisableRetries=value)

    @RequestInitialTimeout.setter
    def RequestInitialTimeout(self, value):
        self._RequestInitialTimeout = value
        self.edit(RequestInitialTimeout=value)

    @RequestMaxTimeout.setter
    def RequestMaxTimeout(self, value):
        self._RequestMaxTimeout = value
        self.edit(RequestMaxTimeout=value)

    @RequestRetryCount.setter
    def RequestRetryCount(self, value):
        self._RequestRetryCount = value
        self.edit(RequestRetryCount=value)

    @RequestIndefiniteRetry.setter
    def RequestIndefiniteRetry(self, value):
        self._RequestIndefiniteRetry = value
        self.edit(RequestIndefiniteRetry=value)

    @RequestDisableRetries.setter
    def RequestDisableRetries(self, value):
        self._RequestDisableRetries = value
        self.edit(RequestDisableRetries=value)

    @ConfirmInitialTimeout.setter
    def ConfirmInitialTimeout(self, value):
        self._ConfirmInitialTimeout = value
        self.edit(ConfirmInitialTimeout=value)

    @ConfirmMaxTimeout.setter
    def ConfirmMaxTimeout(self, value):
        self._ConfirmMaxTimeout = value
        self.edit(ConfirmMaxTimeout=value)

    @ConfirmMaxDuration.setter
    def ConfirmMaxDuration(self, value):
        self._ConfirmMaxDuration = value
        self.edit(ConfirmMaxDuration=value)

    @RenewInitialTimeout.setter
    def RenewInitialTimeout(self, value):
        self._RenewInitialTimeout = value
        self.edit(RenewInitialTimeout=value)

    @RenewMaxTimeout.setter
    def RenewMaxTimeout(self, value):
        self._RenewMaxTimeout = value
        self.edit(RenewMaxTimeout=value)

    @RenewRetryCount.setter
    def RenewRetryCount(self, value):
        self._RenewRetryCount = value
        self.edit(RenewRetryCount=value)

    @RenewIndefiniteRetry.setter
    def RenewIndefiniteRetry(self, value):
        self._RenewIndefiniteRetry = value
        self.edit(RenewIndefiniteRetry=value)

    @RenewDisableRetries.setter
    def RenewDisableRetries(self, value):
        self._RenewDisableRetries = value
        self.edit(RenewDisableRetries=value)

    @RebindInitialTimeout.setter
    def RebindInitialTimeout(self, value):
        self._RebindInitialTimeout = value
        self.edit(RebindInitialTimeout=value)

    @RebindMaxTimeout.setter
    def RebindMaxTimeout(self, value):
        self._RebindMaxTimeout = value
        self.edit(RebindMaxTimeout=value)

    @RebindRetryCount.setter
    def RebindRetryCount(self, value):
        self._RebindRetryCount = value
        self.edit(RebindRetryCount=value)

    @RebindIndefiniteRetry.setter
    def RebindIndefiniteRetry(self, value):
        self._RebindIndefiniteRetry = value
        self.edit(RebindIndefiniteRetry=value)

    @RebindDisableRetries.setter
    def RebindDisableRetries(self, value):
        self._RebindDisableRetries = value
        self.edit(RebindDisableRetries=value)

    @ReleaseInitialTimeout.setter
    def ReleaseInitialTimeout(self, value):
        self._ReleaseInitialTimeout = value
        self.edit(ReleaseInitialTimeout=value)

    @ReleaseRetryCount.setter
    def ReleaseRetryCount(self, value):
        self._ReleaseRetryCount = value
        self.edit(ReleaseRetryCount=value)

    @ReleaseIndefiniteRetry.setter
    def ReleaseIndefiniteRetry(self, value):
        self._ReleaseIndefiniteRetry = value
        self.edit(ReleaseIndefiniteRetry=value)

    @ReleaseDisableRetries.setter
    def ReleaseDisableRetries(self, value):
        self._ReleaseDisableRetries = value
        self.edit(ReleaseDisableRetries=value)

    @DeclineInitialTimeout.setter
    def DeclineInitialTimeout(self, value):
        self._DeclineInitialTimeout = value
        self.edit(DeclineInitialTimeout=value)

    @DeclineRetryCount.setter
    def DeclineRetryCount(self, value):
        self._DeclineRetryCount = value
        self.edit(DeclineRetryCount=value)

    @DeclineIndefiniteRetry.setter
    def DeclineIndefiniteRetry(self, value):
        self._DeclineIndefiniteRetry = value
        self.edit(DeclineIndefiniteRetry=value)

    @DeclineDisableRetries.setter
    def DeclineDisableRetries(self, value):
        self._DeclineDisableRetries = value
        self.edit(DeclineDisableRetries=value)

    @InfoRequestInitialTimeout.setter
    def InfoRequestInitialTimeout(self, value):
        self._InfoRequestInitialTimeout = value
        self.edit(InfoRequestInitialTimeout=value)

    @InfoRequestMaxTimeout.setter
    def InfoRequestMaxTimeout(self, value):
        self._InfoRequestMaxTimeout = value
        self.edit(InfoRequestMaxTimeout=value)

    @InfoRequestRetryCount.setter
    def InfoRequestRetryCount(self, value):
        self._InfoRequestRetryCount = value
        self.edit(InfoRequestRetryCount=value)

    @InfoRequestIndefiniteRetry.setter
    def InfoRequestIndefiniteRetry(self, value):
        self._InfoRequestIndefiniteRetry = value
        self.edit(InfoRequestIndefiniteRetry=value)

    @InfoRequestDisableRetries.setter
    def InfoRequestDisableRetries(self, value):
        self._InfoRequestDisableRetries = value
        self.edit(InfoRequestDisableRetries=value)

    def _set_requestrate_with_str(self, value):
        try:
            self._RequestRate = int(value)
        except ValueError:
            self._RequestRate = hex(int(value, 16))

    def _set_releaserate_with_str(self, value):
        try:
            self._ReleaseRate = int(value)
        except ValueError:
            self._ReleaseRate = hex(int(value, 16))

    def _set_renewrate_with_str(self, value):
        try:
            self._RenewRate = int(value)
        except ValueError:
            self._RenewRate = hex(int(value, 16))

    def _set_maxoutstanding_with_str(self, value):
        try:
            self._MaxOutstanding = int(value)
        except ValueError:
            self._MaxOutstanding = hex(int(value, 16))

    def _set_solicitinitialtimeout_with_str(self, value):
        try:
            self._SolicitInitialTimeout = int(value)
        except ValueError:
            self._SolicitInitialTimeout = hex(int(value, 16))

    def _set_solicitmaxtimeout_with_str(self, value):
        try:
            self._SolicitMaxTimeout = int(value)
        except ValueError:
            self._SolicitMaxTimeout = hex(int(value, 16))

    def _set_solicitretrycount_with_str(self, value):
        try:
            self._SolicitRetryCount = int(value)
        except ValueError:
            self._SolicitRetryCount = hex(int(value, 16))

    def _set_solicitindefiniteretry_with_str(self, value):
        self._SolicitIndefiniteRetry = (value == 'True')

    def _set_solicitdisableretries_with_str(self, value):
        self._SolicitDisableRetries = (value == 'True')

    def _set_requestinitialtimeout_with_str(self, value):
        try:
            self._RequestInitialTimeout = int(value)
        except ValueError:
            self._RequestInitialTimeout = hex(int(value, 16))

    def _set_requestmaxtimeout_with_str(self, value):
        try:
            self._RequestMaxTimeout = int(value)
        except ValueError:
            self._RequestMaxTimeout = hex(int(value, 16))

    def _set_requestretrycount_with_str(self, value):
        try:
            self._RequestRetryCount = int(value)
        except ValueError:
            self._RequestRetryCount = hex(int(value, 16))

    def _set_requestindefiniteretry_with_str(self, value):
        self._RequestIndefiniteRetry = (value == 'True')

    def _set_requestdisableretries_with_str(self, value):
        self._RequestDisableRetries = (value == 'True')

    def _set_confirminitialtimeout_with_str(self, value):
        try:
            self._ConfirmInitialTimeout = int(value)
        except ValueError:
            self._ConfirmInitialTimeout = hex(int(value, 16))

    def _set_confirmmaxtimeout_with_str(self, value):
        try:
            self._ConfirmMaxTimeout = int(value)
        except ValueError:
            self._ConfirmMaxTimeout = hex(int(value, 16))

    def _set_confirmmaxduration_with_str(self, value):
        try:
            self._ConfirmMaxDuration = int(value)
        except ValueError:
            self._ConfirmMaxDuration = hex(int(value, 16))

    def _set_renewinitialtimeout_with_str(self, value):
        try:
            self._RenewInitialTimeout = int(value)
        except ValueError:
            self._RenewInitialTimeout = hex(int(value, 16))

    def _set_renewmaxtimeout_with_str(self, value):
        try:
            self._RenewMaxTimeout = int(value)
        except ValueError:
            self._RenewMaxTimeout = hex(int(value, 16))

    def _set_renewretrycount_with_str(self, value):
        try:
            self._RenewRetryCount = int(value)
        except ValueError:
            self._RenewRetryCount = hex(int(value, 16))

    def _set_renewindefiniteretry_with_str(self, value):
        self._RenewIndefiniteRetry = (value == 'True')

    def _set_renewdisableretries_with_str(self, value):
        self._RenewDisableRetries = (value == 'True')

    def _set_rebindinitialtimeout_with_str(self, value):
        try:
            self._RebindInitialTimeout = int(value)
        except ValueError:
            self._RebindInitialTimeout = hex(int(value, 16))

    def _set_rebindmaxtimeout_with_str(self, value):
        try:
            self._RebindMaxTimeout = int(value)
        except ValueError:
            self._RebindMaxTimeout = hex(int(value, 16))

    def _set_rebindretrycount_with_str(self, value):
        try:
            self._RebindRetryCount = int(value)
        except ValueError:
            self._RebindRetryCount = hex(int(value, 16))

    def _set_rebindindefiniteretry_with_str(self, value):
        self._RebindIndefiniteRetry = (value == 'True')

    def _set_rebinddisableretries_with_str(self, value):
        self._RebindDisableRetries = (value == 'True')

    def _set_releaseinitialtimeout_with_str(self, value):
        try:
            self._ReleaseInitialTimeout = int(value)
        except ValueError:
            self._ReleaseInitialTimeout = hex(int(value, 16))

    def _set_releaseretrycount_with_str(self, value):
        try:
            self._ReleaseRetryCount = int(value)
        except ValueError:
            self._ReleaseRetryCount = hex(int(value, 16))

    def _set_releaseindefiniteretry_with_str(self, value):
        self._ReleaseIndefiniteRetry = (value == 'True')

    def _set_releasedisableretries_with_str(self, value):
        self._ReleaseDisableRetries = (value == 'True')

    def _set_declineinitialtimeout_with_str(self, value):
        try:
            self._DeclineInitialTimeout = int(value)
        except ValueError:
            self._DeclineInitialTimeout = hex(int(value, 16))

    def _set_declineretrycount_with_str(self, value):
        try:
            self._DeclineRetryCount = int(value)
        except ValueError:
            self._DeclineRetryCount = hex(int(value, 16))

    def _set_declineindefiniteretry_with_str(self, value):
        self._DeclineIndefiniteRetry = (value == 'True')

    def _set_declinedisableretries_with_str(self, value):
        self._DeclineDisableRetries = (value == 'True')

    def _set_inforequestinitialtimeout_with_str(self, value):
        try:
            self._InfoRequestInitialTimeout = int(value)
        except ValueError:
            self._InfoRequestInitialTimeout = hex(int(value, 16))

    def _set_inforequestmaxtimeout_with_str(self, value):
        try:
            self._InfoRequestMaxTimeout = int(value)
        except ValueError:
            self._InfoRequestMaxTimeout = hex(int(value, 16))

    def _set_inforequestretrycount_with_str(self, value):
        try:
            self._InfoRequestRetryCount = int(value)
        except ValueError:
            self._InfoRequestRetryCount = hex(int(value, 16))

    def _set_inforequestindefiniteretry_with_str(self, value):
        self._InfoRequestIndefiniteRetry = (value == 'True')

    def _set_inforequestdisableretries_with_str(self, value):
        self._InfoRequestDisableRetries = (value == 'True')

