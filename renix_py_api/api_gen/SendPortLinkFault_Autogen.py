"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class SendPortLinkFault(ROMObject):
    def __init__(self, Mode=None, Duration=None, **kwargs):
        self._Mode = Mode  # Mode
        self._Duration = Duration  # Duration Time (ms)
        self._Running = False  # Link Fault Running, not editable

        properties = kwargs.copy()
        if Mode is not None:
            properties['Mode'] = Mode
        if Duration is not None:
            properties['Duration'] = Duration

        # call base class function, and it will send message to renix server to create a class.
        super(SendPortLinkFault, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Mode=None, Duration=None, **kwargs):
        properties = kwargs.copy()
        if Mode is not None:
            self._Mode = Mode
            properties['Mode'] = Mode
        if Duration is not None:
            self._Duration = Duration
            properties['Duration'] = Duration

        super(SendPortLinkFault, self).edit(**properties)

    @property
    def Mode(self):
        """
        get the value of property _Mode
        """
        if self.force_auto_sync:
            self.get('Mode')
        return self._Mode

    @property
    def Duration(self):
        """
        get the value of property _Duration
        """
        if self.force_auto_sync:
            self.get('Duration')
        return self._Duration

    @property
    def Running(self):
        """
        get the value of property _Running
        """
        if self.force_auto_sync:
            self.get('Running')
        return self._Running

    @Mode.setter
    def Mode(self, value):
        self._Mode = value
        self.edit(Mode=value)

    @Duration.setter
    def Duration(self, value):
        self._Duration = value
        self.edit(Duration=value)

    def _set_mode_with_str(self, value):
        seperate = value.find(':')
        exec('self._Mode = EnumLinkFaultMode.%s' % value[:seperate])

    def _set_duration_with_str(self, value):
        try:
            self._Duration = int(value)
        except ValueError:
            self._Duration = hex(int(value, 16))

    def _set_running_with_str(self, value):
        if value == 'None':
            self._Running = None
            return
        self._Running = (value == 'True')

