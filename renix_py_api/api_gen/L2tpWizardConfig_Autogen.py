"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ProtocolWizardConfig_Autogen import ProtocolWizardConfig


@rom_manager.rom
class L2tpWizardConfig(ProtocolWizardConfig):
    def __init__(self, EmulationMode=None, HostName=None, EnableAuthentication=None, Password=None, UseGatewayAsRemoteIp=None, RemoteIpv4Address=None, RemoteIpv4AddressStep=None, RemoteIpv6Address=None, RemoteIpv6AddressStep=None, TunnelCountPerNode=None, EnablePpp=None, SessionCountPerTunnel=None, IpVersion=None, **kwargs):
        self._EmulationMode = EmulationMode  # Emulation Mode
        self._HostName = HostName  # Host Name
        self._EnableAuthentication = EnableAuthentication  # Enable Authentication
        self._Password = Password  # Password
        self._UseGatewayAsRemoteIp = UseGatewayAsRemoteIp  # Use Gateway Address as Remote Address
        self._RemoteIpv4Address = RemoteIpv4Address  # Remote IPv4 Address
        self._RemoteIpv4AddressStep = RemoteIpv4AddressStep  # Remote IPv4 Address Step
        self._RemoteIpv6Address = RemoteIpv6Address  # Remote IPv6 Address
        self._RemoteIpv6AddressStep = RemoteIpv6AddressStep  # Remote IPv6 Address Step
        self._TunnelCountPerNode = TunnelCountPerNode  # Tunnel Count per LAC/LNS
        self._EnablePpp = EnablePpp  # Enable PPP
        self._SessionCountPerTunnel = SessionCountPerTunnel  # Session Count per Tunnel
        self._IpVersion = IpVersion  # IP Version

        properties = kwargs.copy()
        if EmulationMode is not None:
            properties['EmulationMode'] = EmulationMode
        if HostName is not None:
            properties['HostName'] = HostName
        if EnableAuthentication is not None:
            properties['EnableAuthentication'] = EnableAuthentication
        if Password is not None:
            properties['Password'] = Password
        if UseGatewayAsRemoteIp is not None:
            properties['UseGatewayAsRemoteIp'] = UseGatewayAsRemoteIp
        if RemoteIpv4Address is not None:
            properties['RemoteIpv4Address'] = RemoteIpv4Address
        if RemoteIpv4AddressStep is not None:
            properties['RemoteIpv4AddressStep'] = RemoteIpv4AddressStep
        if RemoteIpv6Address is not None:
            properties['RemoteIpv6Address'] = RemoteIpv6Address
        if RemoteIpv6AddressStep is not None:
            properties['RemoteIpv6AddressStep'] = RemoteIpv6AddressStep
        if TunnelCountPerNode is not None:
            properties['TunnelCountPerNode'] = TunnelCountPerNode
        if EnablePpp is not None:
            properties['EnablePpp'] = EnablePpp
        if SessionCountPerTunnel is not None:
            properties['SessionCountPerTunnel'] = SessionCountPerTunnel
        if IpVersion is not None:
            properties['IpVersion'] = IpVersion

        # call base class function, and it will send message to renix server to create a class.
        super(L2tpWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EmulationMode=None, HostName=None, EnableAuthentication=None, Password=None, UseGatewayAsRemoteIp=None, RemoteIpv4Address=None, RemoteIpv4AddressStep=None, RemoteIpv6Address=None, RemoteIpv6AddressStep=None, TunnelCountPerNode=None, EnablePpp=None, SessionCountPerTunnel=None, IpVersion=None, **kwargs):
        properties = kwargs.copy()
        if EmulationMode is not None:
            self._EmulationMode = EmulationMode
            properties['EmulationMode'] = EmulationMode
        if HostName is not None:
            self._HostName = HostName
            properties['HostName'] = HostName
        if EnableAuthentication is not None:
            self._EnableAuthentication = EnableAuthentication
            properties['EnableAuthentication'] = EnableAuthentication
        if Password is not None:
            self._Password = Password
            properties['Password'] = Password
        if UseGatewayAsRemoteIp is not None:
            self._UseGatewayAsRemoteIp = UseGatewayAsRemoteIp
            properties['UseGatewayAsRemoteIp'] = UseGatewayAsRemoteIp
        if RemoteIpv4Address is not None:
            self._RemoteIpv4Address = RemoteIpv4Address
            properties['RemoteIpv4Address'] = RemoteIpv4Address
        if RemoteIpv4AddressStep is not None:
            self._RemoteIpv4AddressStep = RemoteIpv4AddressStep
            properties['RemoteIpv4AddressStep'] = RemoteIpv4AddressStep
        if RemoteIpv6Address is not None:
            self._RemoteIpv6Address = RemoteIpv6Address
            properties['RemoteIpv6Address'] = RemoteIpv6Address
        if RemoteIpv6AddressStep is not None:
            self._RemoteIpv6AddressStep = RemoteIpv6AddressStep
            properties['RemoteIpv6AddressStep'] = RemoteIpv6AddressStep
        if TunnelCountPerNode is not None:
            self._TunnelCountPerNode = TunnelCountPerNode
            properties['TunnelCountPerNode'] = TunnelCountPerNode
        if EnablePpp is not None:
            self._EnablePpp = EnablePpp
            properties['EnablePpp'] = EnablePpp
        if SessionCountPerTunnel is not None:
            self._SessionCountPerTunnel = SessionCountPerTunnel
            properties['SessionCountPerTunnel'] = SessionCountPerTunnel
        if IpVersion is not None:
            self._IpVersion = IpVersion
            properties['IpVersion'] = IpVersion

        super(L2tpWizardConfig, self).edit(**properties)

    @property
    def EmulationMode(self):
        """
        get the value of property _EmulationMode
        """
        if self.force_auto_sync:
            self.get('EmulationMode')
        return self._EmulationMode

    @property
    def HostName(self):
        """
        get the value of property _HostName
        """
        if self.force_auto_sync:
            self.get('HostName')
        return self._HostName

    @property
    def EnableAuthentication(self):
        """
        get the value of property _EnableAuthentication
        """
        if self.force_auto_sync:
            self.get('EnableAuthentication')
        return self._EnableAuthentication

    @property
    def Password(self):
        """
        get the value of property _Password
        """
        if self.force_auto_sync:
            self.get('Password')
        return self._Password

    @property
    def UseGatewayAsRemoteIp(self):
        """
        get the value of property _UseGatewayAsRemoteIp
        """
        if self.force_auto_sync:
            self.get('UseGatewayAsRemoteIp')
        return self._UseGatewayAsRemoteIp

    @property
    def RemoteIpv4Address(self):
        """
        get the value of property _RemoteIpv4Address
        """
        if self.force_auto_sync:
            self.get('RemoteIpv4Address')
        return self._RemoteIpv4Address

    @property
    def RemoteIpv4AddressStep(self):
        """
        get the value of property _RemoteIpv4AddressStep
        """
        if self.force_auto_sync:
            self.get('RemoteIpv4AddressStep')
        return self._RemoteIpv4AddressStep

    @property
    def RemoteIpv6Address(self):
        """
        get the value of property _RemoteIpv6Address
        """
        if self.force_auto_sync:
            self.get('RemoteIpv6Address')
        return self._RemoteIpv6Address

    @property
    def RemoteIpv6AddressStep(self):
        """
        get the value of property _RemoteIpv6AddressStep
        """
        if self.force_auto_sync:
            self.get('RemoteIpv6AddressStep')
        return self._RemoteIpv6AddressStep

    @property
    def TunnelCountPerNode(self):
        """
        get the value of property _TunnelCountPerNode
        """
        if self.force_auto_sync:
            self.get('TunnelCountPerNode')
        return self._TunnelCountPerNode

    @property
    def EnablePpp(self):
        """
        get the value of property _EnablePpp
        """
        if self.force_auto_sync:
            self.get('EnablePpp')
        return self._EnablePpp

    @property
    def SessionCountPerTunnel(self):
        """
        get the value of property _SessionCountPerTunnel
        """
        if self.force_auto_sync:
            self.get('SessionCountPerTunnel')
        return self._SessionCountPerTunnel

    @property
    def IpVersion(self):
        """
        get the value of property _IpVersion
        """
        if self.force_auto_sync:
            self.get('IpVersion')
        return self._IpVersion

    @EmulationMode.setter
    def EmulationMode(self, value):
        self._EmulationMode = value
        self.edit(EmulationMode=value)

    @HostName.setter
    def HostName(self, value):
        self._HostName = value
        self.edit(HostName=value)

    @EnableAuthentication.setter
    def EnableAuthentication(self, value):
        self._EnableAuthentication = value
        self.edit(EnableAuthentication=value)

    @Password.setter
    def Password(self, value):
        self._Password = value
        self.edit(Password=value)

    @UseGatewayAsRemoteIp.setter
    def UseGatewayAsRemoteIp(self, value):
        self._UseGatewayAsRemoteIp = value
        self.edit(UseGatewayAsRemoteIp=value)

    @RemoteIpv4Address.setter
    def RemoteIpv4Address(self, value):
        self._RemoteIpv4Address = value
        self.edit(RemoteIpv4Address=value)

    @RemoteIpv4AddressStep.setter
    def RemoteIpv4AddressStep(self, value):
        self._RemoteIpv4AddressStep = value
        self.edit(RemoteIpv4AddressStep=value)

    @RemoteIpv6Address.setter
    def RemoteIpv6Address(self, value):
        self._RemoteIpv6Address = value
        self.edit(RemoteIpv6Address=value)

    @RemoteIpv6AddressStep.setter
    def RemoteIpv6AddressStep(self, value):
        self._RemoteIpv6AddressStep = value
        self.edit(RemoteIpv6AddressStep=value)

    @TunnelCountPerNode.setter
    def TunnelCountPerNode(self, value):
        self._TunnelCountPerNode = value
        self.edit(TunnelCountPerNode=value)

    @EnablePpp.setter
    def EnablePpp(self, value):
        self._EnablePpp = value
        self.edit(EnablePpp=value)

    @SessionCountPerTunnel.setter
    def SessionCountPerTunnel(self, value):
        self._SessionCountPerTunnel = value
        self.edit(SessionCountPerTunnel=value)

    @IpVersion.setter
    def IpVersion(self, value):
        self._IpVersion = value
        self.edit(IpVersion=value)

    def _set_emulationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._EmulationMode = EnumL2tpEmulationMode.%s' % value[:seperate])

    def _set_hostname_with_str(self, value):
        self._HostName = value

    def _set_enableauthentication_with_str(self, value):
        self._EnableAuthentication = (value == 'True')

    def _set_password_with_str(self, value):
        self._Password = value

    def _set_usegatewayasremoteip_with_str(self, value):
        self._UseGatewayAsRemoteIp = (value == 'True')

    def _set_remoteipv4address_with_str(self, value):
        self._RemoteIpv4Address = value

    def _set_remoteipv4addressstep_with_str(self, value):
        self._RemoteIpv4AddressStep = value

    def _set_remoteipv6address_with_str(self, value):
        self._RemoteIpv6Address = value

    def _set_remoteipv6addressstep_with_str(self, value):
        self._RemoteIpv6AddressStep = value

    def _set_tunnelcountpernode_with_str(self, value):
        try:
            self._TunnelCountPerNode = int(value)
        except ValueError:
            self._TunnelCountPerNode = hex(int(value, 16))

    def _set_enableppp_with_str(self, value):
        self._EnablePpp = (value == 'True')

    def _set_sessioncountpertunnel_with_str(self, value):
        try:
            self._SessionCountPerTunnel = int(value)
        except ValueError:
            self._SessionCountPerTunnel = hex(int(value, 16))

    def _set_ipversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._IpVersion = EnumL2tpWizardPppIpVersion.%s' % value[:seperate])

