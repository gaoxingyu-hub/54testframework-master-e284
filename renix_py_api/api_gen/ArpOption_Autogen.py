"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class ArpOption(ROMObject):
    def __init__(self, EnableAutoArp=None, StopOnArpFail=None, AutoArpWaitTime=None, **kwargs):
        self._EnableAutoArp = EnableAutoArp  # Enable Auto ARP/ND
        self._StopOnArpFail = StopOnArpFail  # Stop On ARP/ND Fail
        self._AutoArpWaitTime = AutoArpWaitTime  # Wait Time (sec)

        properties = kwargs.copy()
        if EnableAutoArp is not None:
            properties['EnableAutoArp'] = EnableAutoArp
        if StopOnArpFail is not None:
            properties['StopOnArpFail'] = StopOnArpFail
        if AutoArpWaitTime is not None:
            properties['AutoArpWaitTime'] = AutoArpWaitTime

        # call base class function, and it will send message to renix server to create a class.
        super(ArpOption, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EnableAutoArp=None, StopOnArpFail=None, AutoArpWaitTime=None, **kwargs):
        properties = kwargs.copy()
        if EnableAutoArp is not None:
            self._EnableAutoArp = EnableAutoArp
            properties['EnableAutoArp'] = EnableAutoArp
        if StopOnArpFail is not None:
            self._StopOnArpFail = StopOnArpFail
            properties['StopOnArpFail'] = StopOnArpFail
        if AutoArpWaitTime is not None:
            self._AutoArpWaitTime = AutoArpWaitTime
            properties['AutoArpWaitTime'] = AutoArpWaitTime

        super(ArpOption, self).edit(**properties)

    @property
    def EnableAutoArp(self):
        """
        get the value of property _EnableAutoArp
        """
        if self.force_auto_sync:
            self.get('EnableAutoArp')
        return self._EnableAutoArp

    @property
    def StopOnArpFail(self):
        """
        get the value of property _StopOnArpFail
        """
        if self.force_auto_sync:
            self.get('StopOnArpFail')
        return self._StopOnArpFail

    @property
    def AutoArpWaitTime(self):
        """
        get the value of property _AutoArpWaitTime
        """
        if self.force_auto_sync:
            self.get('AutoArpWaitTime')
        return self._AutoArpWaitTime

    @EnableAutoArp.setter
    def EnableAutoArp(self, value):
        self._EnableAutoArp = value
        self.edit(EnableAutoArp=value)

    @StopOnArpFail.setter
    def StopOnArpFail(self, value):
        self._StopOnArpFail = value
        self.edit(StopOnArpFail=value)

    @AutoArpWaitTime.setter
    def AutoArpWaitTime(self, value):
        self._AutoArpWaitTime = value
        self.edit(AutoArpWaitTime=value)

    def _set_enableautoarp_with_str(self, value):
        self._EnableAutoArp = (value == 'True')

    def _set_stoponarpfail_with_str(self, value):
        self._StopOnArpFail = (value == 'True')

    def _set_autoarpwaittime_with_str(self, value):
        try:
            self._AutoArpWaitTime = int(value)
        except ValueError:
            self._AutoArpWaitTime = hex(int(value, 16))

