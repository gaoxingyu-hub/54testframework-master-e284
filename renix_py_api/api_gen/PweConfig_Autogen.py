"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .MplsL2VpnConfig_Autogen import MplsL2VpnConfig


@rom_manager.rom
class PweConfig(MplsL2VpnConfig):
    def __init__(self, PseudowiresCount=None, Mtu=None, GroupId=None, EnableOverride=None, EnableOverlapVcIdsOnDifferentPes=None, EnableCBit=None, EnableCreateProviderHostsForUnusedVpns=None, EnableIncludeStatusTlv=None, StatusCode=None, StartVcId=None, StepVcId=None, EnableBgpAutoDiscovery=None, Agi=None, AgiIncrement=None, Saii=None, SaiiIncrement=None, Taii=None, TaiiIncrement=None, DutAsNumber=None, Rt=None, RtIncrement=None, Rd=None, RdIncrement=None, **kwargs):
        self._PseudowiresCount = PseudowiresCount  # Pseudowires Count
        self._Mtu = Mtu  # MTU
        self._GroupId = GroupId  # Group Id
        self._EnableOverride = EnableOverride  # Override
        self._Encapsulation = EnumMplsPseudowiresEncapsulation.EthernetVlan  # Encapsulation, not editable
        self._EnableOverlapVcIdsOnDifferentPes = EnableOverlapVcIdsOnDifferentPes  # Overlap VC IDs on different PEs
        self._EnableCBit = EnableCBit  # C-Bit
        self._EnableCreateProviderHostsForUnusedVpns = EnableCreateProviderHostsForUnusedVpns  # Create Provider Hosts for Unused VPNs
        self._EnableIncludeStatusTlv = EnableIncludeStatusTlv  # Include Status TLV
        self._StatusCode = StatusCode  # Status Code
        self._FecType = EnumMplsFecType.FEC128  # FEC Type, not editable
        self._StartVcId = StartVcId  # Start VC ID
        self._StepVcId = StepVcId  # Step VC ID
        self._EnableBgpAutoDiscovery = EnableBgpAutoDiscovery  # Enable BGP Auto Discovery
        self._Agi = Agi  # AGI
        self._AgiIncrement = AgiIncrement  # AGI Increment
        self._Saii = Saii  # SAII
        self._SaiiIncrement = SaiiIncrement  # SAII Increment
        self._Taii = Taii  # TAII
        self._TaiiIncrement = TaiiIncrement  # TAII Increment
        self._DutAsNumber = DutAsNumber  # DUT AS Number
        self._RdAssignment = EnumMplsRdAssignment.UseRT  # RD Assignment, not editable
        self._AgiAssignment = EnumMplsAgiAssignment.UseRT  # AGI Assignment, not editable
        self._Rt = Rt  # RT
        self._RtIncrement = RtIncrement  # RT Increment
        self._Rd = Rd  # RD
        self._RdIncrement = RdIncrement  # RD Increment

        properties = kwargs.copy()
        if PseudowiresCount is not None:
            properties['PseudowiresCount'] = PseudowiresCount
        if Mtu is not None:
            properties['Mtu'] = Mtu
        if GroupId is not None:
            properties['GroupId'] = GroupId
        if EnableOverride is not None:
            properties['EnableOverride'] = EnableOverride
        if EnableOverlapVcIdsOnDifferentPes is not None:
            properties['EnableOverlapVcIdsOnDifferentPes'] = EnableOverlapVcIdsOnDifferentPes
        if EnableCBit is not None:
            properties['EnableCBit'] = EnableCBit
        if EnableCreateProviderHostsForUnusedVpns is not None:
            properties['EnableCreateProviderHostsForUnusedVpns'] = EnableCreateProviderHostsForUnusedVpns
        if EnableIncludeStatusTlv is not None:
            properties['EnableIncludeStatusTlv'] = EnableIncludeStatusTlv
        if StatusCode is not None:
            properties['StatusCode'] = StatusCode
        if StartVcId is not None:
            properties['StartVcId'] = StartVcId
        if StepVcId is not None:
            properties['StepVcId'] = StepVcId
        if EnableBgpAutoDiscovery is not None:
            properties['EnableBgpAutoDiscovery'] = EnableBgpAutoDiscovery
        if Agi is not None:
            properties['Agi'] = Agi
        if AgiIncrement is not None:
            properties['AgiIncrement'] = AgiIncrement
        if Saii is not None:
            properties['Saii'] = Saii
        if SaiiIncrement is not None:
            properties['SaiiIncrement'] = SaiiIncrement
        if Taii is not None:
            properties['Taii'] = Taii
        if TaiiIncrement is not None:
            properties['TaiiIncrement'] = TaiiIncrement
        if DutAsNumber is not None:
            properties['DutAsNumber'] = DutAsNumber
        if Rt is not None:
            properties['Rt'] = Rt
        if RtIncrement is not None:
            properties['RtIncrement'] = RtIncrement
        if Rd is not None:
            properties['Rd'] = Rd
        if RdIncrement is not None:
            properties['RdIncrement'] = RdIncrement

        # call base class function, and it will send message to renix server to create a class.
        super(PweConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PseudowiresCount=None, Mtu=None, GroupId=None, EnableOverride=None, EnableOverlapVcIdsOnDifferentPes=None, EnableCBit=None, EnableCreateProviderHostsForUnusedVpns=None, EnableIncludeStatusTlv=None, StatusCode=None, StartVcId=None, StepVcId=None, EnableBgpAutoDiscovery=None, Agi=None, AgiIncrement=None, Saii=None, SaiiIncrement=None, Taii=None, TaiiIncrement=None, DutAsNumber=None, Rt=None, RtIncrement=None, Rd=None, RdIncrement=None, **kwargs):
        properties = kwargs.copy()
        if PseudowiresCount is not None:
            self._PseudowiresCount = PseudowiresCount
            properties['PseudowiresCount'] = PseudowiresCount
        if Mtu is not None:
            self._Mtu = Mtu
            properties['Mtu'] = Mtu
        if GroupId is not None:
            self._GroupId = GroupId
            properties['GroupId'] = GroupId
        if EnableOverride is not None:
            self._EnableOverride = EnableOverride
            properties['EnableOverride'] = EnableOverride
        if EnableOverlapVcIdsOnDifferentPes is not None:
            self._EnableOverlapVcIdsOnDifferentPes = EnableOverlapVcIdsOnDifferentPes
            properties['EnableOverlapVcIdsOnDifferentPes'] = EnableOverlapVcIdsOnDifferentPes
        if EnableCBit is not None:
            self._EnableCBit = EnableCBit
            properties['EnableCBit'] = EnableCBit
        if EnableCreateProviderHostsForUnusedVpns is not None:
            self._EnableCreateProviderHostsForUnusedVpns = EnableCreateProviderHostsForUnusedVpns
            properties['EnableCreateProviderHostsForUnusedVpns'] = EnableCreateProviderHostsForUnusedVpns
        if EnableIncludeStatusTlv is not None:
            self._EnableIncludeStatusTlv = EnableIncludeStatusTlv
            properties['EnableIncludeStatusTlv'] = EnableIncludeStatusTlv
        if StatusCode is not None:
            self._StatusCode = StatusCode
            properties['StatusCode'] = StatusCode
        if StartVcId is not None:
            self._StartVcId = StartVcId
            properties['StartVcId'] = StartVcId
        if StepVcId is not None:
            self._StepVcId = StepVcId
            properties['StepVcId'] = StepVcId
        if EnableBgpAutoDiscovery is not None:
            self._EnableBgpAutoDiscovery = EnableBgpAutoDiscovery
            properties['EnableBgpAutoDiscovery'] = EnableBgpAutoDiscovery
        if Agi is not None:
            self._Agi = Agi
            properties['Agi'] = Agi
        if AgiIncrement is not None:
            self._AgiIncrement = AgiIncrement
            properties['AgiIncrement'] = AgiIncrement
        if Saii is not None:
            self._Saii = Saii
            properties['Saii'] = Saii
        if SaiiIncrement is not None:
            self._SaiiIncrement = SaiiIncrement
            properties['SaiiIncrement'] = SaiiIncrement
        if Taii is not None:
            self._Taii = Taii
            properties['Taii'] = Taii
        if TaiiIncrement is not None:
            self._TaiiIncrement = TaiiIncrement
            properties['TaiiIncrement'] = TaiiIncrement
        if DutAsNumber is not None:
            self._DutAsNumber = DutAsNumber
            properties['DutAsNumber'] = DutAsNumber
        if Rt is not None:
            self._Rt = Rt
            properties['Rt'] = Rt
        if RtIncrement is not None:
            self._RtIncrement = RtIncrement
            properties['RtIncrement'] = RtIncrement
        if Rd is not None:
            self._Rd = Rd
            properties['Rd'] = Rd
        if RdIncrement is not None:
            self._RdIncrement = RdIncrement
            properties['RdIncrement'] = RdIncrement

        super(PweConfig, self).edit(**properties)

    @property
    def PseudowiresCount(self):
        """
        get the value of property _PseudowiresCount
        """
        if self.force_auto_sync:
            self.get('PseudowiresCount')
        return self._PseudowiresCount

    @property
    def Mtu(self):
        """
        get the value of property _Mtu
        """
        if self.force_auto_sync:
            self.get('Mtu')
        return self._Mtu

    @property
    def GroupId(self):
        """
        get the value of property _GroupId
        """
        if self.force_auto_sync:
            self.get('GroupId')
        return self._GroupId

    @property
    def EnableOverride(self):
        """
        get the value of property _EnableOverride
        """
        if self.force_auto_sync:
            self.get('EnableOverride')
        return self._EnableOverride

    @property
    def Encapsulation(self):
        """
        get the value of property _Encapsulation
        """
        if self.force_auto_sync:
            self.get('Encapsulation')
        return self._Encapsulation

    @property
    def EnableOverlapVcIdsOnDifferentPes(self):
        """
        get the value of property _EnableOverlapVcIdsOnDifferentPes
        """
        if self.force_auto_sync:
            self.get('EnableOverlapVcIdsOnDifferentPes')
        return self._EnableOverlapVcIdsOnDifferentPes

    @property
    def EnableCBit(self):
        """
        get the value of property _EnableCBit
        """
        if self.force_auto_sync:
            self.get('EnableCBit')
        return self._EnableCBit

    @property
    def EnableCreateProviderHostsForUnusedVpns(self):
        """
        get the value of property _EnableCreateProviderHostsForUnusedVpns
        """
        if self.force_auto_sync:
            self.get('EnableCreateProviderHostsForUnusedVpns')
        return self._EnableCreateProviderHostsForUnusedVpns

    @property
    def EnableIncludeStatusTlv(self):
        """
        get the value of property _EnableIncludeStatusTlv
        """
        if self.force_auto_sync:
            self.get('EnableIncludeStatusTlv')
        return self._EnableIncludeStatusTlv

    @property
    def StatusCode(self):
        """
        get the value of property _StatusCode
        """
        if self.force_auto_sync:
            self.get('StatusCode')
        return self._StatusCode

    @property
    def FecType(self):
        """
        get the value of property _FecType
        """
        if self.force_auto_sync:
            self.get('FecType')
        return self._FecType

    @property
    def StartVcId(self):
        """
        get the value of property _StartVcId
        """
        if self.force_auto_sync:
            self.get('StartVcId')
        return self._StartVcId

    @property
    def StepVcId(self):
        """
        get the value of property _StepVcId
        """
        if self.force_auto_sync:
            self.get('StepVcId')
        return self._StepVcId

    @property
    def EnableBgpAutoDiscovery(self):
        """
        get the value of property _EnableBgpAutoDiscovery
        """
        if self.force_auto_sync:
            self.get('EnableBgpAutoDiscovery')
        return self._EnableBgpAutoDiscovery

    @property
    def Agi(self):
        """
        get the value of property _Agi
        """
        if self.force_auto_sync:
            self.get('Agi')
        return self._Agi

    @property
    def AgiIncrement(self):
        """
        get the value of property _AgiIncrement
        """
        if self.force_auto_sync:
            self.get('AgiIncrement')
        return self._AgiIncrement

    @property
    def Saii(self):
        """
        get the value of property _Saii
        """
        if self.force_auto_sync:
            self.get('Saii')
        return self._Saii

    @property
    def SaiiIncrement(self):
        """
        get the value of property _SaiiIncrement
        """
        if self.force_auto_sync:
            self.get('SaiiIncrement')
        return self._SaiiIncrement

    @property
    def Taii(self):
        """
        get the value of property _Taii
        """
        if self.force_auto_sync:
            self.get('Taii')
        return self._Taii

    @property
    def TaiiIncrement(self):
        """
        get the value of property _TaiiIncrement
        """
        if self.force_auto_sync:
            self.get('TaiiIncrement')
        return self._TaiiIncrement

    @property
    def DutAsNumber(self):
        """
        get the value of property _DutAsNumber
        """
        if self.force_auto_sync:
            self.get('DutAsNumber')
        return self._DutAsNumber

    @property
    def RdAssignment(self):
        """
        get the value of property _RdAssignment
        """
        if self.force_auto_sync:
            self.get('RdAssignment')
        return self._RdAssignment

    @property
    def AgiAssignment(self):
        """
        get the value of property _AgiAssignment
        """
        if self.force_auto_sync:
            self.get('AgiAssignment')
        return self._AgiAssignment

    @property
    def Rt(self):
        """
        get the value of property _Rt
        """
        if self.force_auto_sync:
            self.get('Rt')
        return self._Rt

    @property
    def RtIncrement(self):
        """
        get the value of property _RtIncrement
        """
        if self.force_auto_sync:
            self.get('RtIncrement')
        return self._RtIncrement

    @property
    def Rd(self):
        """
        get the value of property _Rd
        """
        if self.force_auto_sync:
            self.get('Rd')
        return self._Rd

    @property
    def RdIncrement(self):
        """
        get the value of property _RdIncrement
        """
        if self.force_auto_sync:
            self.get('RdIncrement')
        return self._RdIncrement

    @PseudowiresCount.setter
    def PseudowiresCount(self, value):
        self._PseudowiresCount = value
        self.edit(PseudowiresCount=value)

    @Mtu.setter
    def Mtu(self, value):
        self._Mtu = value
        self.edit(Mtu=value)

    @GroupId.setter
    def GroupId(self, value):
        self._GroupId = value
        self.edit(GroupId=value)

    @EnableOverride.setter
    def EnableOverride(self, value):
        self._EnableOverride = value
        self.edit(EnableOverride=value)

    @EnableOverlapVcIdsOnDifferentPes.setter
    def EnableOverlapVcIdsOnDifferentPes(self, value):
        self._EnableOverlapVcIdsOnDifferentPes = value
        self.edit(EnableOverlapVcIdsOnDifferentPes=value)

    @EnableCBit.setter
    def EnableCBit(self, value):
        self._EnableCBit = value
        self.edit(EnableCBit=value)

    @EnableCreateProviderHostsForUnusedVpns.setter
    def EnableCreateProviderHostsForUnusedVpns(self, value):
        self._EnableCreateProviderHostsForUnusedVpns = value
        self.edit(EnableCreateProviderHostsForUnusedVpns=value)

    @EnableIncludeStatusTlv.setter
    def EnableIncludeStatusTlv(self, value):
        self._EnableIncludeStatusTlv = value
        self.edit(EnableIncludeStatusTlv=value)

    @StatusCode.setter
    def StatusCode(self, value):
        self._StatusCode = value
        self.edit(StatusCode=value)

    @StartVcId.setter
    def StartVcId(self, value):
        self._StartVcId = value
        self.edit(StartVcId=value)

    @StepVcId.setter
    def StepVcId(self, value):
        self._StepVcId = value
        self.edit(StepVcId=value)

    @EnableBgpAutoDiscovery.setter
    def EnableBgpAutoDiscovery(self, value):
        self._EnableBgpAutoDiscovery = value
        self.edit(EnableBgpAutoDiscovery=value)

    @Agi.setter
    def Agi(self, value):
        self._Agi = value
        self.edit(Agi=value)

    @AgiIncrement.setter
    def AgiIncrement(self, value):
        self._AgiIncrement = value
        self.edit(AgiIncrement=value)

    @Saii.setter
    def Saii(self, value):
        self._Saii = value
        self.edit(Saii=value)

    @SaiiIncrement.setter
    def SaiiIncrement(self, value):
        self._SaiiIncrement = value
        self.edit(SaiiIncrement=value)

    @Taii.setter
    def Taii(self, value):
        self._Taii = value
        self.edit(Taii=value)

    @TaiiIncrement.setter
    def TaiiIncrement(self, value):
        self._TaiiIncrement = value
        self.edit(TaiiIncrement=value)

    @DutAsNumber.setter
    def DutAsNumber(self, value):
        self._DutAsNumber = value
        self.edit(DutAsNumber=value)

    @Rt.setter
    def Rt(self, value):
        self._Rt = value
        self.edit(Rt=value)

    @RtIncrement.setter
    def RtIncrement(self, value):
        self._RtIncrement = value
        self.edit(RtIncrement=value)

    @Rd.setter
    def Rd(self, value):
        self._Rd = value
        self.edit(Rd=value)

    @RdIncrement.setter
    def RdIncrement(self, value):
        self._RdIncrement = value
        self.edit(RdIncrement=value)

    def _set_pseudowirescount_with_str(self, value):
        try:
            self._PseudowiresCount = int(value)
        except ValueError:
            self._PseudowiresCount = hex(int(value, 16))

    def _set_mtu_with_str(self, value):
        try:
            self._Mtu = int(value)
        except ValueError:
            self._Mtu = hex(int(value, 16))

    def _set_groupid_with_str(self, value):
        try:
            self._GroupId = int(value)
        except ValueError:
            self._GroupId = hex(int(value, 16))

    def _set_enableoverride_with_str(self, value):
        self._EnableOverride = (value == 'True')

    def _set_encapsulation_with_str(self, value):
        seperate = value.find(':')
        exec('self._Encapsulation = EnumMplsPseudowiresEncapsulation.%s' % value[:seperate])

    def _set_enableoverlapvcidsondifferentpes_with_str(self, value):
        self._EnableOverlapVcIdsOnDifferentPes = (value == 'True')

    def _set_enablecbit_with_str(self, value):
        self._EnableCBit = (value == 'True')

    def _set_enablecreateproviderhostsforunusedvpns_with_str(self, value):
        self._EnableCreateProviderHostsForUnusedVpns = (value == 'True')

    def _set_enableincludestatustlv_with_str(self, value):
        self._EnableIncludeStatusTlv = (value == 'True')

    def _set_statuscode_with_str(self, value):
        try:
            self._StatusCode = int(value)
        except ValueError:
            self._StatusCode = hex(int(value, 16))

    def _set_fectype_with_str(self, value):
        seperate = value.find(':')
        exec('self._FecType = EnumMplsFecType.%s' % value[:seperate])

    def _set_startvcid_with_str(self, value):
        try:
            self._StartVcId = int(value)
        except ValueError:
            self._StartVcId = hex(int(value, 16))

    def _set_stepvcid_with_str(self, value):
        try:
            self._StepVcId = int(value)
        except ValueError:
            self._StepVcId = hex(int(value, 16))

    def _set_enablebgpautodiscovery_with_str(self, value):
        self._EnableBgpAutoDiscovery = (value == 'True')

    def _set_agi_with_str(self, value):
        self._Agi = value

    def _set_agiincrement_with_str(self, value):
        self._AgiIncrement = value

    def _set_saii_with_str(self, value):
        self._Saii = value

    def _set_saiiincrement_with_str(self, value):
        self._SaiiIncrement = value

    def _set_taii_with_str(self, value):
        self._Taii = value

    def _set_taiiincrement_with_str(self, value):
        self._TaiiIncrement = value

    def _set_dutasnumber_with_str(self, value):
        try:
            self._DutAsNumber = int(value)
        except ValueError:
            self._DutAsNumber = hex(int(value, 16))

    def _set_rdassignment_with_str(self, value):
        seperate = value.find(':')
        exec('self._RdAssignment = EnumMplsRdAssignment.%s' % value[:seperate])

    def _set_agiassignment_with_str(self, value):
        seperate = value.find(':')
        exec('self._AgiAssignment = EnumMplsAgiAssignment.%s' % value[:seperate])

    def _set_rt_with_str(self, value):
        self._Rt = value

    def _set_rtincrement_with_str(self, value):
        self._RtIncrement = value

    def _set_rd_with_str(self, value):
        self._Rd = value

    def _set_rdincrement_with_str(self, value):
        self._RdIncrement = value

