"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class Dot1xProtocolConfig(L23ProtocolConfig):
    def __init__(self, AuthMode=None, Identity=None, Password=None, UseAuthenticatorMac=None, AuthenticatorMac=None, RetryCount=None, RetryTimeout=None, RetransmitCount=None, RetransmitTimeout=None, SupplicantCertificateName=None, CertificatePassword=None, DuplicateUserInfoToInner=None, InnerIdentity=None, InnerPassword=None, InnerTunnelAuthMode=None, EnableClientCertificate=None, **kwargs):
        self._State = EnumDot1xState.DISABLED  # State, not editable
        self._AuthMode = AuthMode  # Authentication Mode
        self._Identity = Identity  # Identity
        self._Password = Password  # Password
        self._UseAuthenticatorMac = UseAuthenticatorMac  # Use Authenticator MAC
        self._AuthenticatorMac = AuthenticatorMac  # Authenticator MAC
        self._RetryCount = RetryCount  # Authentication Retry Count
        self._RetryTimeout = RetryTimeout  # Authentication Retry Timeout (sec)
        self._RetransmitCount = RetransmitCount  # Retransmit Count
        self._RetransmitTimeout = RetransmitTimeout  # Retransmit Timeout
        self._SupplicantCertificateName = SupplicantCertificateName  # Supplicant Certificate Name
        self._CertificatePassword = CertificatePassword  # Certificate Password
        self._DuplicateUserInfoToInner = DuplicateUserInfoToInner  # Duplicate Identity/Password to Inner Tunnel
        self._InnerIdentity = InnerIdentity  # Inner Identity
        self._InnerPassword = InnerPassword  # Inner Password
        self._InnerTunnelAuthMode = InnerTunnelAuthMode  # Inner Tunnel Authentication Mode
        self._EnableClientCertificate = EnableClientCertificate  # Enable Client Certificate

        properties = kwargs.copy()
        if AuthMode is not None:
            properties['AuthMode'] = AuthMode
        if Identity is not None:
            properties['Identity'] = Identity
        if Password is not None:
            properties['Password'] = Password
        if UseAuthenticatorMac is not None:
            properties['UseAuthenticatorMac'] = UseAuthenticatorMac
        if AuthenticatorMac is not None:
            properties['AuthenticatorMac'] = AuthenticatorMac
        if RetryCount is not None:
            properties['RetryCount'] = RetryCount
        if RetryTimeout is not None:
            properties['RetryTimeout'] = RetryTimeout
        if RetransmitCount is not None:
            properties['RetransmitCount'] = RetransmitCount
        if RetransmitTimeout is not None:
            properties['RetransmitTimeout'] = RetransmitTimeout
        if SupplicantCertificateName is not None:
            properties['SupplicantCertificateName'] = SupplicantCertificateName
        if CertificatePassword is not None:
            properties['CertificatePassword'] = CertificatePassword
        if DuplicateUserInfoToInner is not None:
            properties['DuplicateUserInfoToInner'] = DuplicateUserInfoToInner
        if InnerIdentity is not None:
            properties['InnerIdentity'] = InnerIdentity
        if InnerPassword is not None:
            properties['InnerPassword'] = InnerPassword
        if InnerTunnelAuthMode is not None:
            properties['InnerTunnelAuthMode'] = InnerTunnelAuthMode
        if EnableClientCertificate is not None:
            properties['EnableClientCertificate'] = EnableClientCertificate

        # call base class function, and it will send message to renix server to create a class.
        super(Dot1xProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AuthMode=None, Identity=None, Password=None, UseAuthenticatorMac=None, AuthenticatorMac=None, RetryCount=None, RetryTimeout=None, RetransmitCount=None, RetransmitTimeout=None, SupplicantCertificateName=None, CertificatePassword=None, DuplicateUserInfoToInner=None, InnerIdentity=None, InnerPassword=None, InnerTunnelAuthMode=None, EnableClientCertificate=None, **kwargs):
        properties = kwargs.copy()
        if AuthMode is not None:
            self._AuthMode = AuthMode
            properties['AuthMode'] = AuthMode
        if Identity is not None:
            self._Identity = Identity
            properties['Identity'] = Identity
        if Password is not None:
            self._Password = Password
            properties['Password'] = Password
        if UseAuthenticatorMac is not None:
            self._UseAuthenticatorMac = UseAuthenticatorMac
            properties['UseAuthenticatorMac'] = UseAuthenticatorMac
        if AuthenticatorMac is not None:
            self._AuthenticatorMac = AuthenticatorMac
            properties['AuthenticatorMac'] = AuthenticatorMac
        if RetryCount is not None:
            self._RetryCount = RetryCount
            properties['RetryCount'] = RetryCount
        if RetryTimeout is not None:
            self._RetryTimeout = RetryTimeout
            properties['RetryTimeout'] = RetryTimeout
        if RetransmitCount is not None:
            self._RetransmitCount = RetransmitCount
            properties['RetransmitCount'] = RetransmitCount
        if RetransmitTimeout is not None:
            self._RetransmitTimeout = RetransmitTimeout
            properties['RetransmitTimeout'] = RetransmitTimeout
        if SupplicantCertificateName is not None:
            self._SupplicantCertificateName = SupplicantCertificateName
            properties['SupplicantCertificateName'] = SupplicantCertificateName
        if CertificatePassword is not None:
            self._CertificatePassword = CertificatePassword
            properties['CertificatePassword'] = CertificatePassword
        if DuplicateUserInfoToInner is not None:
            self._DuplicateUserInfoToInner = DuplicateUserInfoToInner
            properties['DuplicateUserInfoToInner'] = DuplicateUserInfoToInner
        if InnerIdentity is not None:
            self._InnerIdentity = InnerIdentity
            properties['InnerIdentity'] = InnerIdentity
        if InnerPassword is not None:
            self._InnerPassword = InnerPassword
            properties['InnerPassword'] = InnerPassword
        if InnerTunnelAuthMode is not None:
            self._InnerTunnelAuthMode = InnerTunnelAuthMode
            properties['InnerTunnelAuthMode'] = InnerTunnelAuthMode
        if EnableClientCertificate is not None:
            self._EnableClientCertificate = EnableClientCertificate
            properties['EnableClientCertificate'] = EnableClientCertificate

        super(Dot1xProtocolConfig, self).edit(**properties)

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def AuthMode(self):
        """
        get the value of property _AuthMode
        """
        if self.force_auto_sync:
            self.get('AuthMode')
        return self._AuthMode

    @property
    def Identity(self):
        """
        get the value of property _Identity
        """
        if self.force_auto_sync:
            self.get('Identity')
        return self._Identity

    @property
    def Password(self):
        """
        get the value of property _Password
        """
        if self.force_auto_sync:
            self.get('Password')
        return self._Password

    @property
    def UseAuthenticatorMac(self):
        """
        get the value of property _UseAuthenticatorMac
        """
        if self.force_auto_sync:
            self.get('UseAuthenticatorMac')
        return self._UseAuthenticatorMac

    @property
    def AuthenticatorMac(self):
        """
        get the value of property _AuthenticatorMac
        """
        if self.force_auto_sync:
            self.get('AuthenticatorMac')
        return self._AuthenticatorMac

    @property
    def RetryCount(self):
        """
        get the value of property _RetryCount
        """
        if self.force_auto_sync:
            self.get('RetryCount')
        return self._RetryCount

    @property
    def RetryTimeout(self):
        """
        get the value of property _RetryTimeout
        """
        if self.force_auto_sync:
            self.get('RetryTimeout')
        return self._RetryTimeout

    @property
    def RetransmitCount(self):
        """
        get the value of property _RetransmitCount
        """
        if self.force_auto_sync:
            self.get('RetransmitCount')
        return self._RetransmitCount

    @property
    def RetransmitTimeout(self):
        """
        get the value of property _RetransmitTimeout
        """
        if self.force_auto_sync:
            self.get('RetransmitTimeout')
        return self._RetransmitTimeout

    @property
    def SupplicantCertificateName(self):
        """
        get the value of property _SupplicantCertificateName
        """
        if self.force_auto_sync:
            self.get('SupplicantCertificateName')
        return self._SupplicantCertificateName

    @property
    def CertificatePassword(self):
        """
        get the value of property _CertificatePassword
        """
        if self.force_auto_sync:
            self.get('CertificatePassword')
        return self._CertificatePassword

    @property
    def DuplicateUserInfoToInner(self):
        """
        get the value of property _DuplicateUserInfoToInner
        """
        if self.force_auto_sync:
            self.get('DuplicateUserInfoToInner')
        return self._DuplicateUserInfoToInner

    @property
    def InnerIdentity(self):
        """
        get the value of property _InnerIdentity
        """
        if self.force_auto_sync:
            self.get('InnerIdentity')
        return self._InnerIdentity

    @property
    def InnerPassword(self):
        """
        get the value of property _InnerPassword
        """
        if self.force_auto_sync:
            self.get('InnerPassword')
        return self._InnerPassword

    @property
    def InnerTunnelAuthMode(self):
        """
        get the value of property _InnerTunnelAuthMode
        """
        if self.force_auto_sync:
            self.get('InnerTunnelAuthMode')
        return self._InnerTunnelAuthMode

    @property
    def EnableClientCertificate(self):
        """
        get the value of property _EnableClientCertificate
        """
        if self.force_auto_sync:
            self.get('EnableClientCertificate')
        return self._EnableClientCertificate

    @AuthMode.setter
    def AuthMode(self, value):
        self._AuthMode = value
        self.edit(AuthMode=value)

    @Identity.setter
    def Identity(self, value):
        self._Identity = value
        self.edit(Identity=value)

    @Password.setter
    def Password(self, value):
        self._Password = value
        self.edit(Password=value)

    @UseAuthenticatorMac.setter
    def UseAuthenticatorMac(self, value):
        self._UseAuthenticatorMac = value
        self.edit(UseAuthenticatorMac=value)

    @AuthenticatorMac.setter
    def AuthenticatorMac(self, value):
        self._AuthenticatorMac = value
        self.edit(AuthenticatorMac=value)

    @RetryCount.setter
    def RetryCount(self, value):
        self._RetryCount = value
        self.edit(RetryCount=value)

    @RetryTimeout.setter
    def RetryTimeout(self, value):
        self._RetryTimeout = value
        self.edit(RetryTimeout=value)

    @RetransmitCount.setter
    def RetransmitCount(self, value):
        self._RetransmitCount = value
        self.edit(RetransmitCount=value)

    @RetransmitTimeout.setter
    def RetransmitTimeout(self, value):
        self._RetransmitTimeout = value
        self.edit(RetransmitTimeout=value)

    @SupplicantCertificateName.setter
    def SupplicantCertificateName(self, value):
        self._SupplicantCertificateName = value
        self.edit(SupplicantCertificateName=value)

    @CertificatePassword.setter
    def CertificatePassword(self, value):
        self._CertificatePassword = value
        self.edit(CertificatePassword=value)

    @DuplicateUserInfoToInner.setter
    def DuplicateUserInfoToInner(self, value):
        self._DuplicateUserInfoToInner = value
        self.edit(DuplicateUserInfoToInner=value)

    @InnerIdentity.setter
    def InnerIdentity(self, value):
        self._InnerIdentity = value
        self.edit(InnerIdentity=value)

    @InnerPassword.setter
    def InnerPassword(self, value):
        self._InnerPassword = value
        self.edit(InnerPassword=value)

    @InnerTunnelAuthMode.setter
    def InnerTunnelAuthMode(self, value):
        self._InnerTunnelAuthMode = value
        self.edit(InnerTunnelAuthMode=value)

    @EnableClientCertificate.setter
    def EnableClientCertificate(self, value):
        self._EnableClientCertificate = value
        self.edit(EnableClientCertificate=value)

    def _set_state_with_str(self, value):
        seperate = value.find(':')
        exec('self._State = EnumDot1xState.%s' % value[:seperate])

    def _set_authmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._AuthMode = EnumDot1xAuthMode.%s' % value[:seperate])

    def _set_identity_with_str(self, value):
        self._Identity = value

    def _set_password_with_str(self, value):
        self._Password = value

    def _set_useauthenticatormac_with_str(self, value):
        self._UseAuthenticatorMac = (value == 'True')

    def _set_authenticatormac_with_str(self, value):
        self._AuthenticatorMac = value

    def _set_retrycount_with_str(self, value):
        try:
            self._RetryCount = int(value)
        except ValueError:
            self._RetryCount = hex(int(value, 16))

    def _set_retrytimeout_with_str(self, value):
        try:
            self._RetryTimeout = int(value)
        except ValueError:
            self._RetryTimeout = hex(int(value, 16))

    def _set_retransmitcount_with_str(self, value):
        try:
            self._RetransmitCount = int(value)
        except ValueError:
            self._RetransmitCount = hex(int(value, 16))

    def _set_retransmittimeout_with_str(self, value):
        try:
            self._RetransmitTimeout = int(value)
        except ValueError:
            self._RetransmitTimeout = hex(int(value, 16))

    def _set_supplicantcertificatename_with_str(self, value):
        self._SupplicantCertificateName = value

    def _set_certificatepassword_with_str(self, value):
        self._CertificatePassword = value

    def _set_duplicateuserinfotoinner_with_str(self, value):
        self._DuplicateUserInfoToInner = (value == 'True')

    def _set_inneridentity_with_str(self, value):
        self._InnerIdentity = value

    def _set_innerpassword_with_str(self, value):
        self._InnerPassword = value

    def _set_innertunnelauthmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._InnerTunnelAuthMode = EnumDot1xInnerAuthMode.%s' % value[:seperate])

    def _set_enableclientcertificate_with_str(self, value):
        self._EnableClientCertificate = (value == 'True')

