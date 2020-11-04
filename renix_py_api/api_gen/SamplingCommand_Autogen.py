"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SamplingCommand(ROMCommand):
    def __init__(self, ObjectName=None, Interval=None, **kwargs):
        self._ObjectName = ObjectName  # Object Name
        self._Interval = Interval  # Sampling Interval
        self._FileName = ''  # File Name, not editable

        properties = kwargs.copy()
        if ObjectName is not None:
            properties['ObjectName'] = ObjectName
        if Interval is not None:
            properties['Interval'] = Interval

        # call base class function, and it will send message to renix server to create a class.
        super(SamplingCommand, self).__init__(**properties)

    @property
    def ObjectName(self):
        """
        get the value of property _ObjectName
        """
        return self._ObjectName

    @property
    def Interval(self):
        """
        get the value of property _Interval
        """
        return self._Interval

    @property
    def FileName(self):
        """
        get the value of property _FileName
        """
        return self._FileName

    @ObjectName.setter
    def ObjectName(self, value):
        self._ObjectName = value

    @Interval.setter
    def Interval(self, value):
        self._Interval = value

    def _set_objectname_with_str(self, value):
        self._ObjectName = value

    def _set_interval_with_str(self, value):
        try:
            self._Interval = int(value)
        except ValueError:
            self._Interval = hex(int(value, 16))

    def _set_filename_with_str(self, value):
        self._FileName = value

    def _set_output_property(self, value):
        self._set_filename_with_str(value)

