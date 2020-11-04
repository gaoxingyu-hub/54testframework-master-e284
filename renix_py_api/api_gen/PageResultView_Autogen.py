"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ResultView_Autogen import ResultView


@rom_manager.rom
class PageResultView(ResultView):
    def __init__(self, CurrentPage=None, RecordPerPage=None, **kwargs):
        self._CurrentPage = CurrentPage  # Current Page
        self._RecordCount = 0  # Record Count, not editable
        self._RecordPerPage = RecordPerPage  # Result Record per Page

        properties = kwargs.copy()
        if CurrentPage is not None:
            properties['CurrentPage'] = CurrentPage
        if RecordPerPage is not None:
            properties['RecordPerPage'] = RecordPerPage

        # call base class function, and it will send message to renix server to create a class.
        super(PageResultView, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, CurrentPage=None, RecordPerPage=None, **kwargs):
        properties = kwargs.copy()
        if CurrentPage is not None:
            self._CurrentPage = CurrentPage
            properties['CurrentPage'] = CurrentPage
        if RecordPerPage is not None:
            self._RecordPerPage = RecordPerPage
            properties['RecordPerPage'] = RecordPerPage

        super(PageResultView, self).edit(**properties)

    @property
    def CurrentPage(self):
        """
        get the value of property _CurrentPage
        """
        if self.force_auto_sync:
            self.get('CurrentPage')
        return self._CurrentPage

    @property
    def RecordCount(self):
        """
        get the value of property _RecordCount
        """
        if self.force_auto_sync:
            self.get('RecordCount')
        return self._RecordCount

    @property
    def RecordPerPage(self):
        """
        get the value of property _RecordPerPage
        """
        if self.force_auto_sync:
            self.get('RecordPerPage')
        return self._RecordPerPage

    @CurrentPage.setter
    def CurrentPage(self, value):
        self._CurrentPage = value
        self.edit(CurrentPage=value)

    @RecordPerPage.setter
    def RecordPerPage(self, value):
        self._RecordPerPage = value
        self.edit(RecordPerPage=value)

    def _set_currentpage_with_str(self, value):
        try:
            self._CurrentPage = int(value)
        except ValueError:
            self._CurrentPage = hex(int(value, 16))

    def _set_recordcount_with_str(self, value):
        try:
            self._RecordCount = int(value)
        except ValueError:
            self._RecordCount = hex(int(value, 16))

    def _set_recordperpage_with_str(self, value):
        try:
            self._RecordPerPage = int(value)
        except ValueError:
            self._RecordPerPage = hex(int(value, 16))

