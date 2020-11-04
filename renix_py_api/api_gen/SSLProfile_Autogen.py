"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class SSLProfile(ROMObject):
    def __init__(self, Version=None, RecordSize=None, CACertFile=None, UserCertFile=None, UserPassPhrase=None, PeerAuthType=None, Ciphers=None, **kwargs):
        self._Version = swap_int_to_enum_flag(Version, EnumSSLVersion)  # Version
        self._RecordSize = RecordSize  # SSL Record Size
        self._CACertFile = CACertFile  # CA Certificate
        self._UserCertFile = UserCertFile  # User Certificate
        self._UserPassPhrase = UserPassPhrase  # User Pass Phrase
        self._PeerAuthType = PeerAuthType  # Peer Authentication Type
        self._Ciphers = Ciphers  # Ciphers

        properties = kwargs.copy()
        if Version is not None:
            if isinstance(Version, Flag):
                properties['Version'] = Version.value
            else:
                properties['Version'] = Version
        if RecordSize is not None:
            properties['RecordSize'] = RecordSize
        if CACertFile is not None:
            properties['CACertFile'] = CACertFile
        if UserCertFile is not None:
            properties['UserCertFile'] = UserCertFile
        if UserPassPhrase is not None:
            properties['UserPassPhrase'] = UserPassPhrase
        if PeerAuthType is not None:
            properties['PeerAuthType'] = PeerAuthType
        if Ciphers is not None:
            properties['Ciphers'] = Ciphers

        # call base class function, and it will send message to renix server to create a class.
        super(SSLProfile, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Version=None, RecordSize=None, CACertFile=None, UserCertFile=None, UserPassPhrase=None, PeerAuthType=None, Ciphers=None, **kwargs):
        properties = kwargs.copy()
        if Version is not None:
            self._Version = swap_int_to_enum_flag(Version, EnumSSLVersion)
            if isinstance(Version, Flag):
                properties['Version'] = Version.value
            else:
                properties['Version'] = Version
        if RecordSize is not None:
            self._RecordSize = RecordSize
            properties['RecordSize'] = RecordSize
        if CACertFile is not None:
            self._CACertFile = CACertFile
            properties['CACertFile'] = CACertFile
        if UserCertFile is not None:
            self._UserCertFile = UserCertFile
            properties['UserCertFile'] = UserCertFile
        if UserPassPhrase is not None:
            self._UserPassPhrase = UserPassPhrase
            properties['UserPassPhrase'] = UserPassPhrase
        if PeerAuthType is not None:
            self._PeerAuthType = PeerAuthType
            properties['PeerAuthType'] = PeerAuthType
        if Ciphers is not None:
            self._Ciphers = Ciphers
            properties['Ciphers'] = Ciphers

        super(SSLProfile, self).edit(**properties)

    @property
    def Version(self):
        """
        get the value of property _Version
        """
        if self.force_auto_sync:
            self.get('Version')
        return self._Version

    @property
    def RecordSize(self):
        """
        get the value of property _RecordSize
        """
        if self.force_auto_sync:
            self.get('RecordSize')
        return self._RecordSize

    @property
    def CACertFile(self):
        """
        get the value of property _CACertFile
        """
        if self.force_auto_sync:
            self.get('CACertFile')
        return self._CACertFile

    @property
    def UserCertFile(self):
        """
        get the value of property _UserCertFile
        """
        if self.force_auto_sync:
            self.get('UserCertFile')
        return self._UserCertFile

    @property
    def UserPassPhrase(self):
        """
        get the value of property _UserPassPhrase
        """
        if self.force_auto_sync:
            self.get('UserPassPhrase')
        return self._UserPassPhrase

    @property
    def PeerAuthType(self):
        """
        get the value of property _PeerAuthType
        """
        if self.force_auto_sync:
            self.get('PeerAuthType')
        return self._PeerAuthType

    @property
    def Ciphers(self):
        """
        get the value of property _Ciphers
        """
        if self.force_auto_sync:
            self.get('Ciphers')
        return self._Ciphers

    @Version.setter
    def Version(self, value):
        self._Version = swap_int_to_enum_flag(value, EnumSSLVersion)
        if isinstance(value, Flag):
            self.edit(Version=value.value)
        else:
            self.edit(Version=value)

    @RecordSize.setter
    def RecordSize(self, value):
        self._RecordSize = value
        self.edit(RecordSize=value)

    @CACertFile.setter
    def CACertFile(self, value):
        self._CACertFile = value
        self.edit(CACertFile=value)

    @UserCertFile.setter
    def UserCertFile(self, value):
        self._UserCertFile = value
        self.edit(UserCertFile=value)

    @UserPassPhrase.setter
    def UserPassPhrase(self, value):
        self._UserPassPhrase = value
        self.edit(UserPassPhrase=value)

    @PeerAuthType.setter
    def PeerAuthType(self, value):
        self._PeerAuthType = value
        self.edit(PeerAuthType=value)

    @Ciphers.setter
    def Ciphers(self, value):
        self._Ciphers = value
        self.edit(Ciphers=value)

    def _set_version_with_str(self, value):
        seperate = value.find(':')
        self._Version = swap_int_to_enum_flag(int(value[seperate+1:]), EnumSSLVersion)

    def _set_recordsize_with_str(self, value):
        try:
            self._RecordSize = int(value)
        except ValueError:
            self._RecordSize = hex(int(value, 16))

    def _set_cacertfile_with_str(self, value):
        self._CACertFile = value

    def _set_usercertfile_with_str(self, value):
        self._UserCertFile = value

    def _set_userpassphrase_with_str(self, value):
        self._UserPassPhrase = value

    def _set_peerauthtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._PeerAuthType = EnumPeerAuthType.%s' % value[:seperate])

    def _set_ciphers_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Ciphers = tmp_value.split()

