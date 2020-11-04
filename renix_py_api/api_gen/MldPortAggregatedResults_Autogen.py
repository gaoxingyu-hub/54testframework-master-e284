"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class MldPortAggregatedResults(Result):
    def __init__(self, **kwargs):
        self._MldPortId = ''  # Port, not editable
        self._MldTxFrames = 0  # Tx Frames, not editable
        self._MldRxFrames = 0  # Rx Frames, not editable
        self._MldTxV1Reports = 0  # Tx V1 Reports, not editable
        self._MldStopListenGroups = 0  # Tx Stop Listen Groups, not editable
        self._MldTxV2Reports = 0  # Tx V2 Reports, not editable
        self._MldTxV2ModeInclude = 0  # Tx V2 MODE_IS_INCLUDE, not editable
        self._MldTxV2ModeExclude = 0  # Tx V2 MODE_IS_EXCLUDE, not editable
        self._MldTxV2ModeChangeToInclude = 0  # Tx V2 CHANGE_TO_INCLUDE_MODE, not editable
        self._MldTxV2ModeChangeToExclude = 0  # Tx V2 CHANGE_TO_EXCLUDE_MODE, not editable
        self._MldTxV2ModeAllowNewSources = 0  # Tx V2 ALLOW_NEW_SOURCES, not editable
        self._MldTxV2ModeBlockOldSources = 0  # Tx V2 BLOCK_OLD_SOURCES, not editable
        self._MldRxV1Queries = 0  # Rx V1 Queries, not editable
        self._MldRxV2Queries = 0  # Rx V2 Queries, not editable
        self._MldRxGeneralQueries = 0  # Rx General Queries, not editable
        self._MldRxGroupSpecificQueries = 0  # Rx Group Specific Queries, not editable
        self._MldRxGroupAndSourceSpecificQueries = 0  # Rx Group and Source Specific Queries, not editable
        self._MldRxUnknownTypes = 0  # Rx Unknown types, not editable
        self._MldRxChecksumErrors = 0  # Rx MLD Checksum Errors, not editable
        self._MldRxLengthErrors = 0  # Rx MLD Length Errors, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(MldPortAggregatedResults, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def MldPortId(self):
        """
        get the value of property _MldPortId
        """
        if self.force_auto_sync:
            self.get('MldPortId')
        return self._MldPortId

    @property
    def MldTxFrames(self):
        """
        get the value of property _MldTxFrames
        """
        if self.force_auto_sync:
            self.get('MldTxFrames')
        return self._MldTxFrames

    @property
    def MldRxFrames(self):
        """
        get the value of property _MldRxFrames
        """
        if self.force_auto_sync:
            self.get('MldRxFrames')
        return self._MldRxFrames

    @property
    def MldTxV1Reports(self):
        """
        get the value of property _MldTxV1Reports
        """
        if self.force_auto_sync:
            self.get('MldTxV1Reports')
        return self._MldTxV1Reports

    @property
    def MldStopListenGroups(self):
        """
        get the value of property _MldStopListenGroups
        """
        if self.force_auto_sync:
            self.get('MldStopListenGroups')
        return self._MldStopListenGroups

    @property
    def MldTxV2Reports(self):
        """
        get the value of property _MldTxV2Reports
        """
        if self.force_auto_sync:
            self.get('MldTxV2Reports')
        return self._MldTxV2Reports

    @property
    def MldTxV2ModeInclude(self):
        """
        get the value of property _MldTxV2ModeInclude
        """
        if self.force_auto_sync:
            self.get('MldTxV2ModeInclude')
        return self._MldTxV2ModeInclude

    @property
    def MldTxV2ModeExclude(self):
        """
        get the value of property _MldTxV2ModeExclude
        """
        if self.force_auto_sync:
            self.get('MldTxV2ModeExclude')
        return self._MldTxV2ModeExclude

    @property
    def MldTxV2ModeChangeToInclude(self):
        """
        get the value of property _MldTxV2ModeChangeToInclude
        """
        if self.force_auto_sync:
            self.get('MldTxV2ModeChangeToInclude')
        return self._MldTxV2ModeChangeToInclude

    @property
    def MldTxV2ModeChangeToExclude(self):
        """
        get the value of property _MldTxV2ModeChangeToExclude
        """
        if self.force_auto_sync:
            self.get('MldTxV2ModeChangeToExclude')
        return self._MldTxV2ModeChangeToExclude

    @property
    def MldTxV2ModeAllowNewSources(self):
        """
        get the value of property _MldTxV2ModeAllowNewSources
        """
        if self.force_auto_sync:
            self.get('MldTxV2ModeAllowNewSources')
        return self._MldTxV2ModeAllowNewSources

    @property
    def MldTxV2ModeBlockOldSources(self):
        """
        get the value of property _MldTxV2ModeBlockOldSources
        """
        if self.force_auto_sync:
            self.get('MldTxV2ModeBlockOldSources')
        return self._MldTxV2ModeBlockOldSources

    @property
    def MldRxV1Queries(self):
        """
        get the value of property _MldRxV1Queries
        """
        if self.force_auto_sync:
            self.get('MldRxV1Queries')
        return self._MldRxV1Queries

    @property
    def MldRxV2Queries(self):
        """
        get the value of property _MldRxV2Queries
        """
        if self.force_auto_sync:
            self.get('MldRxV2Queries')
        return self._MldRxV2Queries

    @property
    def MldRxGeneralQueries(self):
        """
        get the value of property _MldRxGeneralQueries
        """
        if self.force_auto_sync:
            self.get('MldRxGeneralQueries')
        return self._MldRxGeneralQueries

    @property
    def MldRxGroupSpecificQueries(self):
        """
        get the value of property _MldRxGroupSpecificQueries
        """
        if self.force_auto_sync:
            self.get('MldRxGroupSpecificQueries')
        return self._MldRxGroupSpecificQueries

    @property
    def MldRxGroupAndSourceSpecificQueries(self):
        """
        get the value of property _MldRxGroupAndSourceSpecificQueries
        """
        if self.force_auto_sync:
            self.get('MldRxGroupAndSourceSpecificQueries')
        return self._MldRxGroupAndSourceSpecificQueries

    @property
    def MldRxUnknownTypes(self):
        """
        get the value of property _MldRxUnknownTypes
        """
        if self.force_auto_sync:
            self.get('MldRxUnknownTypes')
        return self._MldRxUnknownTypes

    @property
    def MldRxChecksumErrors(self):
        """
        get the value of property _MldRxChecksumErrors
        """
        if self.force_auto_sync:
            self.get('MldRxChecksumErrors')
        return self._MldRxChecksumErrors

    @property
    def MldRxLengthErrors(self):
        """
        get the value of property _MldRxLengthErrors
        """
        if self.force_auto_sync:
            self.get('MldRxLengthErrors')
        return self._MldRxLengthErrors

    def _set_mldportid_with_str(self, value):
        self._MldPortId = value

    def _set_mldtxframes_with_str(self, value):
        try:
            self._MldTxFrames = int(value)
        except ValueError:
            self._MldTxFrames = hex(int(value, 16))

    def _set_mldrxframes_with_str(self, value):
        try:
            self._MldRxFrames = int(value)
        except ValueError:
            self._MldRxFrames = hex(int(value, 16))

    def _set_mldtxv1reports_with_str(self, value):
        try:
            self._MldTxV1Reports = int(value)
        except ValueError:
            self._MldTxV1Reports = hex(int(value, 16))

    def _set_mldstoplistengroups_with_str(self, value):
        try:
            self._MldStopListenGroups = int(value)
        except ValueError:
            self._MldStopListenGroups = hex(int(value, 16))

    def _set_mldtxv2reports_with_str(self, value):
        try:
            self._MldTxV2Reports = int(value)
        except ValueError:
            self._MldTxV2Reports = hex(int(value, 16))

    def _set_mldtxv2modeinclude_with_str(self, value):
        try:
            self._MldTxV2ModeInclude = int(value)
        except ValueError:
            self._MldTxV2ModeInclude = hex(int(value, 16))

    def _set_mldtxv2modeexclude_with_str(self, value):
        try:
            self._MldTxV2ModeExclude = int(value)
        except ValueError:
            self._MldTxV2ModeExclude = hex(int(value, 16))

    def _set_mldtxv2modechangetoinclude_with_str(self, value):
        try:
            self._MldTxV2ModeChangeToInclude = int(value)
        except ValueError:
            self._MldTxV2ModeChangeToInclude = hex(int(value, 16))

    def _set_mldtxv2modechangetoexclude_with_str(self, value):
        try:
            self._MldTxV2ModeChangeToExclude = int(value)
        except ValueError:
            self._MldTxV2ModeChangeToExclude = hex(int(value, 16))

    def _set_mldtxv2modeallownewsources_with_str(self, value):
        try:
            self._MldTxV2ModeAllowNewSources = int(value)
        except ValueError:
            self._MldTxV2ModeAllowNewSources = hex(int(value, 16))

    def _set_mldtxv2modeblockoldsources_with_str(self, value):
        try:
            self._MldTxV2ModeBlockOldSources = int(value)
        except ValueError:
            self._MldTxV2ModeBlockOldSources = hex(int(value, 16))

    def _set_mldrxv1queries_with_str(self, value):
        try:
            self._MldRxV1Queries = int(value)
        except ValueError:
            self._MldRxV1Queries = hex(int(value, 16))

    def _set_mldrxv2queries_with_str(self, value):
        try:
            self._MldRxV2Queries = int(value)
        except ValueError:
            self._MldRxV2Queries = hex(int(value, 16))

    def _set_mldrxgeneralqueries_with_str(self, value):
        try:
            self._MldRxGeneralQueries = int(value)
        except ValueError:
            self._MldRxGeneralQueries = hex(int(value, 16))

    def _set_mldrxgroupspecificqueries_with_str(self, value):
        try:
            self._MldRxGroupSpecificQueries = int(value)
        except ValueError:
            self._MldRxGroupSpecificQueries = hex(int(value, 16))

    def _set_mldrxgroupandsourcespecificqueries_with_str(self, value):
        try:
            self._MldRxGroupAndSourceSpecificQueries = int(value)
        except ValueError:
            self._MldRxGroupAndSourceSpecificQueries = hex(int(value, 16))

    def _set_mldrxunknowntypes_with_str(self, value):
        try:
            self._MldRxUnknownTypes = int(value)
        except ValueError:
            self._MldRxUnknownTypes = hex(int(value, 16))

    def _set_mldrxchecksumerrors_with_str(self, value):
        try:
            self._MldRxChecksumErrors = int(value)
        except ValueError:
            self._MldRxChecksumErrors = hex(int(value, 16))

    def _set_mldrxlengtherrors_with_str(self, value):
        try:
            self._MldRxLengthErrors = int(value)
        except ValueError:
            self._MldRxLengthErrors = hex(int(value, 16))

