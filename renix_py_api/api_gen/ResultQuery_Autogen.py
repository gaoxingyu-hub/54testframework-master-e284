"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class ResultQuery(ROMObject):
    def __init__(self, Interval=None, Sql=None, Columns=None, **kwargs):
        self._State = QueryState.STOPPED  # State, not editable
        self._Interval = Interval  # Update interval
        self._Sql = Sql  # Query sql statement
        self._Columns = Columns  # Column names

        properties = kwargs.copy()
        if Interval is not None:
            properties['Interval'] = Interval
        if Sql is not None:
            properties['Sql'] = Sql
        if Columns is not None:
            properties['Columns'] = Columns

        # call base class function, and it will send message to renix server to create a class.
        super(ResultQuery, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Interval=None, Sql=None, Columns=None, **kwargs):
        properties = kwargs.copy()
        if Interval is not None:
            self._Interval = Interval
            properties['Interval'] = Interval
        if Sql is not None:
            self._Sql = Sql
            properties['Sql'] = Sql
        if Columns is not None:
            self._Columns = Columns
            properties['Columns'] = Columns

        super(ResultQuery, self).edit(**properties)

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def Interval(self):
        """
        get the value of property _Interval
        """
        if self.force_auto_sync:
            self.get('Interval')
        return self._Interval

    @property
    def Sql(self):
        """
        get the value of property _Sql
        """
        if self.force_auto_sync:
            self.get('Sql')
        return self._Sql

    @property
    def Columns(self):
        """
        get the value of property _Columns
        """
        if self.force_auto_sync:
            self.get('Columns')
        return self._Columns

    @Interval.setter
    def Interval(self, value):
        self._Interval = value
        self.edit(Interval=value)

    @Sql.setter
    def Sql(self, value):
        self._Sql = value
        self.edit(Sql=value)

    @Columns.setter
    def Columns(self, value):
        self._Columns = value
        self.edit(Columns=value)

    def _set_state_with_str(self, value):
        seperate = value.find(':')
        exec('self._State = QueryState.%s' % value[:seperate])

    def _set_interval_with_str(self, value):
        try:
            self._Interval = int(value)
        except ValueError:
            self._Interval = hex(int(value, 16))

    def _set_sql_with_str(self, value):
        self._Sql = value

    def _set_columns_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Columns = tmp_value.split()

