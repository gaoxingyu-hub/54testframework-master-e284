"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class StpProtocolConfig(L23ProtocolConfig):
    def __init__(self, StpProtocolType=None, RootType=None, RootPriority=None, RootMacAddress=None, RootPathCost=None, BridgePriority=None, BridgeMacAddress=None, PortNumber=None, PortPriority=None, MessageAge=None, MaxAgeTime=None, HelloTime=None, ForwardDelay=None, BpduRate=None, **kwargs):
        self._StpProtocolType = StpProtocolType  # Protocol Type
        self._RootType = RootType  # Root Type
        self._RootPriority = RootPriority  # Root Priority
        self._RootMacAddress = RootMacAddress  # Root MAC Address
        self._RootPathCost = RootPathCost  # Root Path Cost
        self._ElectedRootId = '00:00:00:00:00:00:00'  # Elected Root, not editable
        self._BridgePriority = BridgePriority  # Bridge Priority
        self._BridgeMacAddress = BridgeMacAddress  # Bridge MAC Address
        self._PortNumber = PortNumber  # Port Number
        self._PortPriority = PortPriority  # Port Priority
        self._MessageAge = MessageAge  # Message Age (sec)
        self._MaxAgeTime = MaxAgeTime  # Max Age Time
        self._HelloTime = HelloTime  # Hello Time
        self._ForwardDelay = ForwardDelay  # Forward Delay
        self._BpduRate = BpduRate  # BPDU Rate

        properties = kwargs.copy()
        if StpProtocolType is not None:
            properties['StpProtocolType'] = StpProtocolType
        if RootType is not None:
            properties['RootType'] = RootType
        if RootPriority is not None:
            properties['RootPriority'] = RootPriority
        if RootMacAddress is not None:
            properties['RootMacAddress'] = RootMacAddress
        if RootPathCost is not None:
            properties['RootPathCost'] = RootPathCost
        if BridgePriority is not None:
            properties['BridgePriority'] = BridgePriority
        if BridgeMacAddress is not None:
            properties['BridgeMacAddress'] = BridgeMacAddress
        if PortNumber is not None:
            properties['PortNumber'] = PortNumber
        if PortPriority is not None:
            properties['PortPriority'] = PortPriority
        if MessageAge is not None:
            properties['MessageAge'] = MessageAge
        if MaxAgeTime is not None:
            properties['MaxAgeTime'] = MaxAgeTime
        if HelloTime is not None:
            properties['HelloTime'] = HelloTime
        if ForwardDelay is not None:
            properties['ForwardDelay'] = ForwardDelay
        if BpduRate is not None:
            properties['BpduRate'] = BpduRate

        # call base class function, and it will send message to renix server to create a class.
        super(StpProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, StpProtocolType=None, RootType=None, RootPriority=None, RootMacAddress=None, RootPathCost=None, BridgePriority=None, BridgeMacAddress=None, PortNumber=None, PortPriority=None, MessageAge=None, MaxAgeTime=None, HelloTime=None, ForwardDelay=None, BpduRate=None, **kwargs):
        properties = kwargs.copy()
        if StpProtocolType is not None:
            self._StpProtocolType = StpProtocolType
            properties['StpProtocolType'] = StpProtocolType
        if RootType is not None:
            self._RootType = RootType
            properties['RootType'] = RootType
        if RootPriority is not None:
            self._RootPriority = RootPriority
            properties['RootPriority'] = RootPriority
        if RootMacAddress is not None:
            self._RootMacAddress = RootMacAddress
            properties['RootMacAddress'] = RootMacAddress
        if RootPathCost is not None:
            self._RootPathCost = RootPathCost
            properties['RootPathCost'] = RootPathCost
        if BridgePriority is not None:
            self._BridgePriority = BridgePriority
            properties['BridgePriority'] = BridgePriority
        if BridgeMacAddress is not None:
            self._BridgeMacAddress = BridgeMacAddress
            properties['BridgeMacAddress'] = BridgeMacAddress
        if PortNumber is not None:
            self._PortNumber = PortNumber
            properties['PortNumber'] = PortNumber
        if PortPriority is not None:
            self._PortPriority = PortPriority
            properties['PortPriority'] = PortPriority
        if MessageAge is not None:
            self._MessageAge = MessageAge
            properties['MessageAge'] = MessageAge
        if MaxAgeTime is not None:
            self._MaxAgeTime = MaxAgeTime
            properties['MaxAgeTime'] = MaxAgeTime
        if HelloTime is not None:
            self._HelloTime = HelloTime
            properties['HelloTime'] = HelloTime
        if ForwardDelay is not None:
            self._ForwardDelay = ForwardDelay
            properties['ForwardDelay'] = ForwardDelay
        if BpduRate is not None:
            self._BpduRate = BpduRate
            properties['BpduRate'] = BpduRate

        super(StpProtocolConfig, self).edit(**properties)

    @property
    def StpProtocolType(self):
        """
        get the value of property _StpProtocolType
        """
        if self.force_auto_sync:
            self.get('StpProtocolType')
        return self._StpProtocolType

    @property
    def RootType(self):
        """
        get the value of property _RootType
        """
        if self.force_auto_sync:
            self.get('RootType')
        return self._RootType

    @property
    def RootPriority(self):
        """
        get the value of property _RootPriority
        """
        if self.force_auto_sync:
            self.get('RootPriority')
        return self._RootPriority

    @property
    def RootMacAddress(self):
        """
        get the value of property _RootMacAddress
        """
        if self.force_auto_sync:
            self.get('RootMacAddress')
        return self._RootMacAddress

    @property
    def RootPathCost(self):
        """
        get the value of property _RootPathCost
        """
        if self.force_auto_sync:
            self.get('RootPathCost')
        return self._RootPathCost

    @property
    def ElectedRootId(self):
        """
        get the value of property _ElectedRootId
        """
        if self.force_auto_sync:
            self.get('ElectedRootId')
        return self._ElectedRootId

    @property
    def BridgePriority(self):
        """
        get the value of property _BridgePriority
        """
        if self.force_auto_sync:
            self.get('BridgePriority')
        return self._BridgePriority

    @property
    def BridgeMacAddress(self):
        """
        get the value of property _BridgeMacAddress
        """
        if self.force_auto_sync:
            self.get('BridgeMacAddress')
        return self._BridgeMacAddress

    @property
    def PortNumber(self):
        """
        get the value of property _PortNumber
        """
        if self.force_auto_sync:
            self.get('PortNumber')
        return self._PortNumber

    @property
    def PortPriority(self):
        """
        get the value of property _PortPriority
        """
        if self.force_auto_sync:
            self.get('PortPriority')
        return self._PortPriority

    @property
    def MessageAge(self):
        """
        get the value of property _MessageAge
        """
        if self.force_auto_sync:
            self.get('MessageAge')
        return self._MessageAge

    @property
    def MaxAgeTime(self):
        """
        get the value of property _MaxAgeTime
        """
        if self.force_auto_sync:
            self.get('MaxAgeTime')
        return self._MaxAgeTime

    @property
    def HelloTime(self):
        """
        get the value of property _HelloTime
        """
        if self.force_auto_sync:
            self.get('HelloTime')
        return self._HelloTime

    @property
    def ForwardDelay(self):
        """
        get the value of property _ForwardDelay
        """
        if self.force_auto_sync:
            self.get('ForwardDelay')
        return self._ForwardDelay

    @property
    def BpduRate(self):
        """
        get the value of property _BpduRate
        """
        if self.force_auto_sync:
            self.get('BpduRate')
        return self._BpduRate

    @StpProtocolType.setter
    def StpProtocolType(self, value):
        self._StpProtocolType = value
        self.edit(StpProtocolType=value)

    @RootType.setter
    def RootType(self, value):
        self._RootType = value
        self.edit(RootType=value)

    @RootPriority.setter
    def RootPriority(self, value):
        self._RootPriority = value
        self.edit(RootPriority=value)

    @RootMacAddress.setter
    def RootMacAddress(self, value):
        self._RootMacAddress = value
        self.edit(RootMacAddress=value)

    @RootPathCost.setter
    def RootPathCost(self, value):
        self._RootPathCost = value
        self.edit(RootPathCost=value)

    @BridgePriority.setter
    def BridgePriority(self, value):
        self._BridgePriority = value
        self.edit(BridgePriority=value)

    @BridgeMacAddress.setter
    def BridgeMacAddress(self, value):
        self._BridgeMacAddress = value
        self.edit(BridgeMacAddress=value)

    @PortNumber.setter
    def PortNumber(self, value):
        self._PortNumber = value
        self.edit(PortNumber=value)

    @PortPriority.setter
    def PortPriority(self, value):
        self._PortPriority = value
        self.edit(PortPriority=value)

    @MessageAge.setter
    def MessageAge(self, value):
        self._MessageAge = value
        self.edit(MessageAge=value)

    @MaxAgeTime.setter
    def MaxAgeTime(self, value):
        self._MaxAgeTime = value
        self.edit(MaxAgeTime=value)

    @HelloTime.setter
    def HelloTime(self, value):
        self._HelloTime = value
        self.edit(HelloTime=value)

    @ForwardDelay.setter
    def ForwardDelay(self, value):
        self._ForwardDelay = value
        self.edit(ForwardDelay=value)

    @BpduRate.setter
    def BpduRate(self, value):
        self._BpduRate = value
        self.edit(BpduRate=value)

    def _set_stpprotocoltype_with_str(self, value):
        seperate = value.find(':')
        exec('self._StpProtocolType = EnumStpProtocolType.%s' % value[:seperate])

    def _set_roottype_with_str(self, value):
        seperate = value.find(':')
        exec('self._RootType = EnumStpRootType.%s' % value[:seperate])

    def _set_rootpriority_with_str(self, value):
        seperate = value.find(':')
        exec('self._RootPriority = EnumRootPriority.%s' % value[:seperate])

    def _set_rootmacaddress_with_str(self, value):
        self._RootMacAddress = value

    def _set_rootpathcost_with_str(self, value):
        try:
            self._RootPathCost = int(value)
        except ValueError:
            self._RootPathCost = hex(int(value, 16))

    def _set_electedrootid_with_str(self, value):
        self._ElectedRootId = value

    def _set_bridgepriority_with_str(self, value):
        seperate = value.find(':')
        exec('self._BridgePriority = EnumRootPriority.%s' % value[:seperate])

    def _set_bridgemacaddress_with_str(self, value):
        self._BridgeMacAddress = value

    def _set_portnumber_with_str(self, value):
        try:
            self._PortNumber = int(value)
        except ValueError:
            self._PortNumber = hex(int(value, 16))

    def _set_portpriority_with_str(self, value):
        seperate = value.find(':')
        exec('self._PortPriority = EnumPortPriority.%s' % value[:seperate])

    def _set_messageage_with_str(self, value):
        try:
            self._MessageAge = int(value)
        except ValueError:
            self._MessageAge = hex(int(value, 16))

    def _set_maxagetime_with_str(self, value):
        try:
            self._MaxAgeTime = int(value)
        except ValueError:
            self._MaxAgeTime = hex(int(value, 16))

    def _set_hellotime_with_str(self, value):
        try:
            self._HelloTime = int(value)
        except ValueError:
            self._HelloTime = hex(int(value, 16))

    def _set_forwarddelay_with_str(self, value):
        try:
            self._ForwardDelay = int(value)
        except ValueError:
            self._ForwardDelay = hex(int(value, 16))

    def _set_bpdurate_with_str(self, value):
        try:
            self._BpduRate = int(value)
        except ValueError:
            self._BpduRate = hex(int(value, 16))

