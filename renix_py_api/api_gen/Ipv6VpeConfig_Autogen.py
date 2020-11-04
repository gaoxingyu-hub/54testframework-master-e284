"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .MplsL3VpnConfig_Autogen import MplsL3VpnConfig


@rom_manager.rom
class Ipv6VpeConfig(MplsL3VpnConfig):
    def __init__(self, CustomerStartRoute=None, CustomerRouteStep=None, ProviderStartRoute=None, ProviderRouteStep=None, **kwargs):
        self._CustomerStartRoute = CustomerStartRoute  # Start Route
        self._CustomerRouteStep = CustomerRouteStep  # Route Step
        self._ProviderStartRoute = ProviderStartRoute  # Start Route
        self._ProviderRouteStep = ProviderRouteStep  # Route Step

        properties = kwargs.copy()
        if CustomerStartRoute is not None:
            properties['CustomerStartRoute'] = CustomerStartRoute
        if CustomerRouteStep is not None:
            properties['CustomerRouteStep'] = CustomerRouteStep
        if ProviderStartRoute is not None:
            properties['ProviderStartRoute'] = ProviderStartRoute
        if ProviderRouteStep is not None:
            properties['ProviderRouteStep'] = ProviderRouteStep

        # call base class function, and it will send message to renix server to create a class.
        super(Ipv6VpeConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, CustomerStartRoute=None, CustomerRouteStep=None, ProviderStartRoute=None, ProviderRouteStep=None, **kwargs):
        properties = kwargs.copy()
        if CustomerStartRoute is not None:
            self._CustomerStartRoute = CustomerStartRoute
            properties['CustomerStartRoute'] = CustomerStartRoute
        if CustomerRouteStep is not None:
            self._CustomerRouteStep = CustomerRouteStep
            properties['CustomerRouteStep'] = CustomerRouteStep
        if ProviderStartRoute is not None:
            self._ProviderStartRoute = ProviderStartRoute
            properties['ProviderStartRoute'] = ProviderStartRoute
        if ProviderRouteStep is not None:
            self._ProviderRouteStep = ProviderRouteStep
            properties['ProviderRouteStep'] = ProviderRouteStep

        super(Ipv6VpeConfig, self).edit(**properties)

    @property
    def CustomerStartRoute(self):
        """
        get the value of property _CustomerStartRoute
        """
        if self.force_auto_sync:
            self.get('CustomerStartRoute')
        return self._CustomerStartRoute

    @property
    def CustomerRouteStep(self):
        """
        get the value of property _CustomerRouteStep
        """
        if self.force_auto_sync:
            self.get('CustomerRouteStep')
        return self._CustomerRouteStep

    @property
    def ProviderStartRoute(self):
        """
        get the value of property _ProviderStartRoute
        """
        if self.force_auto_sync:
            self.get('ProviderStartRoute')
        return self._ProviderStartRoute

    @property
    def ProviderRouteStep(self):
        """
        get the value of property _ProviderRouteStep
        """
        if self.force_auto_sync:
            self.get('ProviderRouteStep')
        return self._ProviderRouteStep

    @CustomerStartRoute.setter
    def CustomerStartRoute(self, value):
        self._CustomerStartRoute = value
        self.edit(CustomerStartRoute=value)

    @CustomerRouteStep.setter
    def CustomerRouteStep(self, value):
        self._CustomerRouteStep = value
        self.edit(CustomerRouteStep=value)

    @ProviderStartRoute.setter
    def ProviderStartRoute(self, value):
        self._ProviderStartRoute = value
        self.edit(ProviderStartRoute=value)

    @ProviderRouteStep.setter
    def ProviderRouteStep(self, value):
        self._ProviderRouteStep = value
        self.edit(ProviderRouteStep=value)

    def _set_customerstartroute_with_str(self, value):
        self._CustomerStartRoute = value

    def _set_customerroutestep_with_str(self, value):
        self._CustomerRouteStep = value

    def _set_providerstartroute_with_str(self, value):
        self._ProviderStartRoute = value

    def _set_providerroutestep_with_str(self, value):
        self._ProviderRouteStep = value

