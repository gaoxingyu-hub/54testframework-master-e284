"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .StartAddressLearnCommand_Autogen import StartAddressLearnCommand


@rom_manager.rom
class StartAddressLearnCapacityCommand(StartAddressLearnCommand):
    def __init__(self, AddrMaxValue=None, AddrMinValue=None, AddrInitValue=None, AddrResolution=None, LearnRate=None, **kwargs):
        self._AddrMaxValue = AddrMaxValue  # Maximum
        self._AddrMinValue = AddrMinValue  # Minimum
        self._AddrInitValue = AddrInitValue  # Initial
        self._AddrResolution = AddrResolution  # Resolution
        self._LearnRate = LearnRate  # Learning Rate (frames/sec)

        properties = kwargs.copy()
        if AddrMaxValue is not None:
            properties['AddrMaxValue'] = AddrMaxValue
        if AddrMinValue is not None:
            properties['AddrMinValue'] = AddrMinValue
        if AddrInitValue is not None:
            properties['AddrInitValue'] = AddrInitValue
        if AddrResolution is not None:
            properties['AddrResolution'] = AddrResolution
        if LearnRate is not None:
            properties['LearnRate'] = LearnRate

        # call base class function, and it will send message to renix server to create a class.
        super(StartAddressLearnCapacityCommand, self).__init__(**properties)

    @property
    def AddrMaxValue(self):
        """
        get the value of property _AddrMaxValue
        """
        return self._AddrMaxValue

    @property
    def AddrMinValue(self):
        """
        get the value of property _AddrMinValue
        """
        return self._AddrMinValue

    @property
    def AddrInitValue(self):
        """
        get the value of property _AddrInitValue
        """
        return self._AddrInitValue

    @property
    def AddrResolution(self):
        """
        get the value of property _AddrResolution
        """
        return self._AddrResolution

    @property
    def LearnRate(self):
        """
        get the value of property _LearnRate
        """
        return self._LearnRate

    @AddrMaxValue.setter
    def AddrMaxValue(self, value):
        self._AddrMaxValue = value

    @AddrMinValue.setter
    def AddrMinValue(self, value):
        self._AddrMinValue = value

    @AddrInitValue.setter
    def AddrInitValue(self, value):
        self._AddrInitValue = value

    @AddrResolution.setter
    def AddrResolution(self, value):
        self._AddrResolution = value

    @LearnRate.setter
    def LearnRate(self, value):
        self._LearnRate = value

    def _set_addrmaxvalue_with_str(self, value):
        try:
            self._AddrMaxValue = int(value)
        except ValueError:
            self._AddrMaxValue = hex(int(value, 16))

    def _set_addrminvalue_with_str(self, value):
        try:
            self._AddrMinValue = int(value)
        except ValueError:
            self._AddrMinValue = hex(int(value, 16))

    def _set_addrinitvalue_with_str(self, value):
        try:
            self._AddrInitValue = int(value)
        except ValueError:
            self._AddrInitValue = hex(int(value, 16))

    def _set_addrresolution_with_str(self, value):
        try:
            self._AddrResolution = int(value)
        except ValueError:
            self._AddrResolution = hex(int(value, 16))

    def _set_learnrate_with_str(self, value):
        try:
            self._LearnRate = int(value)
        except ValueError:
            self._LearnRate = hex(int(value, 16))

