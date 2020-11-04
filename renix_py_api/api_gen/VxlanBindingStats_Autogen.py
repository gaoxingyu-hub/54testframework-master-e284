"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class VxlanBindingStats(Result):
    def __init__(self, **kwargs):
        self._VtepId = ''  # VTEP Name, not editable
        self._VtepState = 'Stopped'  # VTEP State, not editable
        self._TotalVmCount = 0  # Total VM Count, not editable
        self._ResolvedVmCount = 0  # Resolved VM Count, not editable
        self._UnresolvedVmCount = 0  # Unresolved VM Count, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(VxlanBindingStats, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def VtepId(self):
        """
        get the value of property _VtepId
        """
        if self.force_auto_sync:
            self.get('VtepId')
        return self._VtepId

    @property
    def VtepState(self):
        """
        get the value of property _VtepState
        """
        if self.force_auto_sync:
            self.get('VtepState')
        return self._VtepState

    @property
    def TotalVmCount(self):
        """
        get the value of property _TotalVmCount
        """
        if self.force_auto_sync:
            self.get('TotalVmCount')
        return self._TotalVmCount

    @property
    def ResolvedVmCount(self):
        """
        get the value of property _ResolvedVmCount
        """
        if self.force_auto_sync:
            self.get('ResolvedVmCount')
        return self._ResolvedVmCount

    @property
    def UnresolvedVmCount(self):
        """
        get the value of property _UnresolvedVmCount
        """
        if self.force_auto_sync:
            self.get('UnresolvedVmCount')
        return self._UnresolvedVmCount

    def _set_vtepid_with_str(self, value):
        self._VtepId = value

    def _set_vtepstate_with_str(self, value):
        self._VtepState = value

    def _set_totalvmcount_with_str(self, value):
        try:
            self._TotalVmCount = int(value)
        except ValueError:
            self._TotalVmCount = hex(int(value, 16))

    def _set_resolvedvmcount_with_str(self, value):
        try:
            self._ResolvedVmCount = int(value)
        except ValueError:
            self._ResolvedVmCount = hex(int(value, 16))

    def _set_unresolvedvmcount_with_str(self, value):
        try:
            self._UnresolvedVmCount = int(value)
        except ValueError:
            self._UnresolvedVmCount = hex(int(value, 16))

