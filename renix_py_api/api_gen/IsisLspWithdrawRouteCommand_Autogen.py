"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class IsisLspWithdrawRouteCommand(ROMCommand):
    def __init__(self, Ipv4RouteConfigs=None, Ipv6RouteConfigs=None, **kwargs):
        self._Ipv4RouteConfigs = Ipv4RouteConfigs  # IS-IS IPv4 Route Configs
        self._Ipv6RouteConfigs = Ipv6RouteConfigs  # IS-IS IPv6 Route Configs

        properties = kwargs.copy()
        if Ipv4RouteConfigs is not None:
            properties['Ipv4RouteConfigs'] = Ipv4RouteConfigs
        if Ipv6RouteConfigs is not None:
            properties['Ipv6RouteConfigs'] = Ipv6RouteConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(IsisLspWithdrawRouteCommand, self).__init__(**properties)

    @property
    def Ipv4RouteConfigs(self):
        """
        get the value of property _Ipv4RouteConfigs
        """
        return self._Ipv4RouteConfigs

    @property
    def Ipv6RouteConfigs(self):
        """
        get the value of property _Ipv6RouteConfigs
        """
        return self._Ipv6RouteConfigs

    @Ipv4RouteConfigs.setter
    def Ipv4RouteConfigs(self, value):
        self._Ipv4RouteConfigs = value

    @Ipv6RouteConfigs.setter
    def Ipv6RouteConfigs(self, value):
        self._Ipv6RouteConfigs = value

    def _set_ipv4routeconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Ipv4RouteConfigs = tmp_value.split()

    def _set_ipv6routeconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Ipv6RouteConfigs = tmp_value.split()

