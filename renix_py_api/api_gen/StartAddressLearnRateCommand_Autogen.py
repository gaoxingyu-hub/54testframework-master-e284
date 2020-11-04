"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .StartAddressLearnCommand_Autogen import StartAddressLearnCommand


@rom_manager.rom
class StartAddressLearnRateCommand(StartAddressLearnCommand):
    def __init__(self, RateMaxValue=None, RateMinValue=None, RateInitValue=None, RateResolution=None, AddressNumber=None, **kwargs):
        self._RateMaxValue = RateMaxValue  # Maximum
        self._RateMinValue = RateMinValue  # Minimum
        self._RateInitValue = RateInitValue  # Initial
        self._RateResolution = RateResolution  # Resolution
        self._AddressNumber = AddressNumber  # Address Learn Number

        properties = kwargs.copy()
        if RateMaxValue is not None:
            properties['RateMaxValue'] = RateMaxValue
        if RateMinValue is not None:
            properties['RateMinValue'] = RateMinValue
        if RateInitValue is not None:
            properties['RateInitValue'] = RateInitValue
        if RateResolution is not None:
            properties['RateResolution'] = RateResolution
        if AddressNumber is not None:
            properties['AddressNumber'] = AddressNumber

        # call base class function, and it will send message to renix server to create a class.
        super(StartAddressLearnRateCommand, self).__init__(**properties)

    @property
    def RateMaxValue(self):
        """
        get the value of property _RateMaxValue
        """
        return self._RateMaxValue

    @property
    def RateMinValue(self):
        """
        get the value of property _RateMinValue
        """
        return self._RateMinValue

    @property
    def RateInitValue(self):
        """
        get the value of property _RateInitValue
        """
        return self._RateInitValue

    @property
    def RateResolution(self):
        """
        get the value of property _RateResolution
        """
        return self._RateResolution

    @property
    def AddressNumber(self):
        """
        get the value of property _AddressNumber
        """
        return self._AddressNumber

    @RateMaxValue.setter
    def RateMaxValue(self, value):
        self._RateMaxValue = value

    @RateMinValue.setter
    def RateMinValue(self, value):
        self._RateMinValue = value

    @RateInitValue.setter
    def RateInitValue(self, value):
        self._RateInitValue = value

    @RateResolution.setter
    def RateResolution(self, value):
        self._RateResolution = value

    @AddressNumber.setter
    def AddressNumber(self, value):
        self._AddressNumber = value

    def _set_ratemaxvalue_with_str(self, value):
        try:
            self._RateMaxValue = int(value)
        except ValueError:
            self._RateMaxValue = hex(int(value, 16))

    def _set_rateminvalue_with_str(self, value):
        try:
            self._RateMinValue = int(value)
        except ValueError:
            self._RateMinValue = hex(int(value, 16))

    def _set_rateinitvalue_with_str(self, value):
        try:
            self._RateInitValue = int(value)
        except ValueError:
            self._RateInitValue = hex(int(value, 16))

    def _set_rateresolution_with_str(self, value):
        try:
            self._RateResolution = int(value)
        except ValueError:
            self._RateResolution = hex(int(value, 16))

    def _set_addressnumber_with_str(self, value):
        try:
            self._AddressNumber = int(value)
        except ValueError:
            self._AddressNumber = hex(int(value, 16))

