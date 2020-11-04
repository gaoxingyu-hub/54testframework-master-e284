"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class LacpGroupConfig(ROMObject):
    def __init__(self, L2HashOption=None, L3HashOption=None, ActorSystemId=None, ActorSystemPriority=None, MaxActiveNumber=None, MinActiveNumber=None, TransmitAlgorithm=None, **kwargs):
        self._LinkStatus = EnumLacpLinkStatus.DOWN  # Link Status, not editable
        self._L2HashOption = swap_int_to_enum_flag(L2HashOption, EnumLacpL2HashOption)  # L2 Hash Option
        self._L3HashOption = swap_int_to_enum_flag(L3HashOption, EnumLacpL3HashOption)  # L3 Hash Option
        self._ActorSystemId = ActorSystemId  # Actor System ID
        self._ActorSystemPriority = ActorSystemPriority  # Actor System Priority
        self._MaxActiveNumber = MaxActiveNumber  # Max Active Number
        self._MinActiveNumber = MinActiveNumber  # Min Active Number
        self._TransmitAlgorithm = TransmitAlgorithm  # Transmit Algorithm

        properties = kwargs.copy()
        if L2HashOption is not None:
            if isinstance(L2HashOption, Flag):
                properties['L2HashOption'] = L2HashOption.value
            else:
                properties['L2HashOption'] = L2HashOption
        if L3HashOption is not None:
            if isinstance(L3HashOption, Flag):
                properties['L3HashOption'] = L3HashOption.value
            else:
                properties['L3HashOption'] = L3HashOption
        if ActorSystemId is not None:
            properties['ActorSystemId'] = ActorSystemId
        if ActorSystemPriority is not None:
            properties['ActorSystemPriority'] = ActorSystemPriority
        if MaxActiveNumber is not None:
            properties['MaxActiveNumber'] = MaxActiveNumber
        if MinActiveNumber is not None:
            properties['MinActiveNumber'] = MinActiveNumber
        if TransmitAlgorithm is not None:
            properties['TransmitAlgorithm'] = TransmitAlgorithm

        # call base class function, and it will send message to renix server to create a class.
        super(LacpGroupConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, L2HashOption=None, L3HashOption=None, ActorSystemId=None, ActorSystemPriority=None, MaxActiveNumber=None, MinActiveNumber=None, TransmitAlgorithm=None, **kwargs):
        properties = kwargs.copy()
        if L2HashOption is not None:
            self._L2HashOption = swap_int_to_enum_flag(L2HashOption, EnumLacpL2HashOption)
            if isinstance(L2HashOption, Flag):
                properties['L2HashOption'] = L2HashOption.value
            else:
                properties['L2HashOption'] = L2HashOption
        if L3HashOption is not None:
            self._L3HashOption = swap_int_to_enum_flag(L3HashOption, EnumLacpL3HashOption)
            if isinstance(L3HashOption, Flag):
                properties['L3HashOption'] = L3HashOption.value
            else:
                properties['L3HashOption'] = L3HashOption
        if ActorSystemId is not None:
            self._ActorSystemId = ActorSystemId
            properties['ActorSystemId'] = ActorSystemId
        if ActorSystemPriority is not None:
            self._ActorSystemPriority = ActorSystemPriority
            properties['ActorSystemPriority'] = ActorSystemPriority
        if MaxActiveNumber is not None:
            self._MaxActiveNumber = MaxActiveNumber
            properties['MaxActiveNumber'] = MaxActiveNumber
        if MinActiveNumber is not None:
            self._MinActiveNumber = MinActiveNumber
            properties['MinActiveNumber'] = MinActiveNumber
        if TransmitAlgorithm is not None:
            self._TransmitAlgorithm = TransmitAlgorithm
            properties['TransmitAlgorithm'] = TransmitAlgorithm

        super(LacpGroupConfig, self).edit(**properties)

    @property
    def LinkStatus(self):
        """
        get the value of property _LinkStatus
        """
        if self.force_auto_sync:
            self.get('LinkStatus')
        return self._LinkStatus

    @property
    def L2HashOption(self):
        """
        get the value of property _L2HashOption
        """
        if self.force_auto_sync:
            self.get('L2HashOption')
        return self._L2HashOption

    @property
    def L3HashOption(self):
        """
        get the value of property _L3HashOption
        """
        if self.force_auto_sync:
            self.get('L3HashOption')
        return self._L3HashOption

    @property
    def ActorSystemId(self):
        """
        get the value of property _ActorSystemId
        """
        if self.force_auto_sync:
            self.get('ActorSystemId')
        return self._ActorSystemId

    @property
    def ActorSystemPriority(self):
        """
        get the value of property _ActorSystemPriority
        """
        if self.force_auto_sync:
            self.get('ActorSystemPriority')
        return self._ActorSystemPriority

    @property
    def MaxActiveNumber(self):
        """
        get the value of property _MaxActiveNumber
        """
        if self.force_auto_sync:
            self.get('MaxActiveNumber')
        return self._MaxActiveNumber

    @property
    def MinActiveNumber(self):
        """
        get the value of property _MinActiveNumber
        """
        if self.force_auto_sync:
            self.get('MinActiveNumber')
        return self._MinActiveNumber

    @property
    def TransmitAlgorithm(self):
        """
        get the value of property _TransmitAlgorithm
        """
        if self.force_auto_sync:
            self.get('TransmitAlgorithm')
        return self._TransmitAlgorithm

    @L2HashOption.setter
    def L2HashOption(self, value):
        self._L2HashOption = swap_int_to_enum_flag(value, EnumLacpL2HashOption)
        if isinstance(value, Flag):
            self.edit(L2HashOption=value.value)
        else:
            self.edit(L2HashOption=value)

    @L3HashOption.setter
    def L3HashOption(self, value):
        self._L3HashOption = swap_int_to_enum_flag(value, EnumLacpL3HashOption)
        if isinstance(value, Flag):
            self.edit(L3HashOption=value.value)
        else:
            self.edit(L3HashOption=value)

    @ActorSystemId.setter
    def ActorSystemId(self, value):
        self._ActorSystemId = value
        self.edit(ActorSystemId=value)

    @ActorSystemPriority.setter
    def ActorSystemPriority(self, value):
        self._ActorSystemPriority = value
        self.edit(ActorSystemPriority=value)

    @MaxActiveNumber.setter
    def MaxActiveNumber(self, value):
        self._MaxActiveNumber = value
        self.edit(MaxActiveNumber=value)

    @MinActiveNumber.setter
    def MinActiveNumber(self, value):
        self._MinActiveNumber = value
        self.edit(MinActiveNumber=value)

    @TransmitAlgorithm.setter
    def TransmitAlgorithm(self, value):
        self._TransmitAlgorithm = value
        self.edit(TransmitAlgorithm=value)

    def _set_linkstatus_with_str(self, value):
        seperate = value.find(':')
        exec('self._LinkStatus = EnumLacpLinkStatus.%s' % value[:seperate])

    def _set_l2hashoption_with_str(self, value):
        seperate = value.find(':')
        self._L2HashOption = swap_int_to_enum_flag(int(value[seperate+1:]), EnumLacpL2HashOption)

    def _set_l3hashoption_with_str(self, value):
        seperate = value.find(':')
        self._L3HashOption = swap_int_to_enum_flag(int(value[seperate+1:]), EnumLacpL3HashOption)

    def _set_actorsystemid_with_str(self, value):
        self._ActorSystemId = value

    def _set_actorsystempriority_with_str(self, value):
        try:
            self._ActorSystemPriority = int(value)
        except ValueError:
            self._ActorSystemPriority = hex(int(value, 16))

    def _set_maxactivenumber_with_str(self, value):
        try:
            self._MaxActiveNumber = int(value)
        except ValueError:
            self._MaxActiveNumber = hex(int(value, 16))

    def _set_minactivenumber_with_str(self, value):
        try:
            self._MinActiveNumber = int(value)
        except ValueError:
            self._MinActiveNumber = hex(int(value, 16))

    def _set_transmitalgorithm_with_str(self, value):
        seperate = value.find(':')
        exec('self._TransmitAlgorithm = EnumLacpTransmotAlgorithm.%s' % value[:seperate])

