"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class IgmpPortAggregatedResults(Result):
    def __init__(self, **kwargs):
        self._IgmpPortId = ''  # Port, not editable
        self._IgmpTxFrames = 0  # Tx Frames, not editable
        self._IgmpRxFrames = 0  # Rx Frames, not editable
        self._IgmpTxV1Reports = 0  # Tx V1 Reports, not editable
        self._IgmpTxV2Reports = 0  # Tx V2 Reports, not editable
        self._IgmpTxLeaveGroups = 0  # Tx Leave Groups, not editable
        self._IgmpTxV3Reports = 0  # Tx V3 Reports, not editable
        self._IgmpTxV3ModeInclude = 0  # Tx V3 MODE_IS_INCLUDE, not editable
        self._IgmpTxV3ModeExclude = 0  # Tx V3 MODE_IS_EXCLUDE, not editable
        self._IgmpTxV3ModeChangeToInclude = 0  # Tx V3 CHANGE_TO_INCLUDE_MODE, not editable
        self._IgmpTxV3ModeChangeToExclude = 0  # Tx V3 CHANGE_TO_EXCLUDE_MODE, not editable
        self._IgmpTxV3ModeAllowNewSources = 0  # Tx V3 ALLOW_NEW_SOURCES, not editable
        self._IgmpTxV3ModeBlockOldSources = 0  # Tx V3 BLOCK_OLD_SOURCES, not editable
        self._IgmpRxV1Queries = 0  # Rx V1 Queries, not editable
        self._IgmpRxV2Queries = 0  # Rx V2 Queries, not editable
        self._IgmpRxV3Queries = 0  # Rx V3 Queries, not editable
        self._IgmpRxGeneralQueries = 0  # Rx General Queries, not editable
        self._IgmpRxGroupSpecificQueries = 0  # Rx Group Specific Queries, not editable
        self._IgmpRxGroupAndSourceSpecificQueries = 0  # Rx Group and Source Specific Queries, not editable
        self._IgmpRxUnknownTypes = 0  # Rx Unknown types, not editable
        self._IgmpRxChecksumErrors = 0  # Rx IGMP Checksum Errors, not editable
        self._IgmpRxLengthErrors = 0  # Rx IGMP Length Errors, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(IgmpPortAggregatedResults, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def IgmpPortId(self):
        """
        get the value of property _IgmpPortId
        """
        if self.force_auto_sync:
            self.get('IgmpPortId')
        return self._IgmpPortId

    @property
    def IgmpTxFrames(self):
        """
        get the value of property _IgmpTxFrames
        """
        if self.force_auto_sync:
            self.get('IgmpTxFrames')
        return self._IgmpTxFrames

    @property
    def IgmpRxFrames(self):
        """
        get the value of property _IgmpRxFrames
        """
        if self.force_auto_sync:
            self.get('IgmpRxFrames')
        return self._IgmpRxFrames

    @property
    def IgmpTxV1Reports(self):
        """
        get the value of property _IgmpTxV1Reports
        """
        if self.force_auto_sync:
            self.get('IgmpTxV1Reports')
        return self._IgmpTxV1Reports

    @property
    def IgmpTxV2Reports(self):
        """
        get the value of property _IgmpTxV2Reports
        """
        if self.force_auto_sync:
            self.get('IgmpTxV2Reports')
        return self._IgmpTxV2Reports

    @property
    def IgmpTxLeaveGroups(self):
        """
        get the value of property _IgmpTxLeaveGroups
        """
        if self.force_auto_sync:
            self.get('IgmpTxLeaveGroups')
        return self._IgmpTxLeaveGroups

    @property
    def IgmpTxV3Reports(self):
        """
        get the value of property _IgmpTxV3Reports
        """
        if self.force_auto_sync:
            self.get('IgmpTxV3Reports')
        return self._IgmpTxV3Reports

    @property
    def IgmpTxV3ModeInclude(self):
        """
        get the value of property _IgmpTxV3ModeInclude
        """
        if self.force_auto_sync:
            self.get('IgmpTxV3ModeInclude')
        return self._IgmpTxV3ModeInclude

    @property
    def IgmpTxV3ModeExclude(self):
        """
        get the value of property _IgmpTxV3ModeExclude
        """
        if self.force_auto_sync:
            self.get('IgmpTxV3ModeExclude')
        return self._IgmpTxV3ModeExclude

    @property
    def IgmpTxV3ModeChangeToInclude(self):
        """
        get the value of property _IgmpTxV3ModeChangeToInclude
        """
        if self.force_auto_sync:
            self.get('IgmpTxV3ModeChangeToInclude')
        return self._IgmpTxV3ModeChangeToInclude

    @property
    def IgmpTxV3ModeChangeToExclude(self):
        """
        get the value of property _IgmpTxV3ModeChangeToExclude
        """
        if self.force_auto_sync:
            self.get('IgmpTxV3ModeChangeToExclude')
        return self._IgmpTxV3ModeChangeToExclude

    @property
    def IgmpTxV3ModeAllowNewSources(self):
        """
        get the value of property _IgmpTxV3ModeAllowNewSources
        """
        if self.force_auto_sync:
            self.get('IgmpTxV3ModeAllowNewSources')
        return self._IgmpTxV3ModeAllowNewSources

    @property
    def IgmpTxV3ModeBlockOldSources(self):
        """
        get the value of property _IgmpTxV3ModeBlockOldSources
        """
        if self.force_auto_sync:
            self.get('IgmpTxV3ModeBlockOldSources')
        return self._IgmpTxV3ModeBlockOldSources

    @property
    def IgmpRxV1Queries(self):
        """
        get the value of property _IgmpRxV1Queries
        """
        if self.force_auto_sync:
            self.get('IgmpRxV1Queries')
        return self._IgmpRxV1Queries

    @property
    def IgmpRxV2Queries(self):
        """
        get the value of property _IgmpRxV2Queries
        """
        if self.force_auto_sync:
            self.get('IgmpRxV2Queries')
        return self._IgmpRxV2Queries

    @property
    def IgmpRxV3Queries(self):
        """
        get the value of property _IgmpRxV3Queries
        """
        if self.force_auto_sync:
            self.get('IgmpRxV3Queries')
        return self._IgmpRxV3Queries

    @property
    def IgmpRxGeneralQueries(self):
        """
        get the value of property _IgmpRxGeneralQueries
        """
        if self.force_auto_sync:
            self.get('IgmpRxGeneralQueries')
        return self._IgmpRxGeneralQueries

    @property
    def IgmpRxGroupSpecificQueries(self):
        """
        get the value of property _IgmpRxGroupSpecificQueries
        """
        if self.force_auto_sync:
            self.get('IgmpRxGroupSpecificQueries')
        return self._IgmpRxGroupSpecificQueries

    @property
    def IgmpRxGroupAndSourceSpecificQueries(self):
        """
        get the value of property _IgmpRxGroupAndSourceSpecificQueries
        """
        if self.force_auto_sync:
            self.get('IgmpRxGroupAndSourceSpecificQueries')
        return self._IgmpRxGroupAndSourceSpecificQueries

    @property
    def IgmpRxUnknownTypes(self):
        """
        get the value of property _IgmpRxUnknownTypes
        """
        if self.force_auto_sync:
            self.get('IgmpRxUnknownTypes')
        return self._IgmpRxUnknownTypes

    @property
    def IgmpRxChecksumErrors(self):
        """
        get the value of property _IgmpRxChecksumErrors
        """
        if self.force_auto_sync:
            self.get('IgmpRxChecksumErrors')
        return self._IgmpRxChecksumErrors

    @property
    def IgmpRxLengthErrors(self):
        """
        get the value of property _IgmpRxLengthErrors
        """
        if self.force_auto_sync:
            self.get('IgmpRxLengthErrors')
        return self._IgmpRxLengthErrors

    def _set_igmpportid_with_str(self, value):
        self._IgmpPortId = value

    def _set_igmptxframes_with_str(self, value):
        try:
            self._IgmpTxFrames = int(value)
        except ValueError:
            self._IgmpTxFrames = hex(int(value, 16))

    def _set_igmprxframes_with_str(self, value):
        try:
            self._IgmpRxFrames = int(value)
        except ValueError:
            self._IgmpRxFrames = hex(int(value, 16))

    def _set_igmptxv1reports_with_str(self, value):
        try:
            self._IgmpTxV1Reports = int(value)
        except ValueError:
            self._IgmpTxV1Reports = hex(int(value, 16))

    def _set_igmptxv2reports_with_str(self, value):
        try:
            self._IgmpTxV2Reports = int(value)
        except ValueError:
            self._IgmpTxV2Reports = hex(int(value, 16))

    def _set_igmptxleavegroups_with_str(self, value):
        try:
            self._IgmpTxLeaveGroups = int(value)
        except ValueError:
            self._IgmpTxLeaveGroups = hex(int(value, 16))

    def _set_igmptxv3reports_with_str(self, value):
        try:
            self._IgmpTxV3Reports = int(value)
        except ValueError:
            self._IgmpTxV3Reports = hex(int(value, 16))

    def _set_igmptxv3modeinclude_with_str(self, value):
        try:
            self._IgmpTxV3ModeInclude = int(value)
        except ValueError:
            self._IgmpTxV3ModeInclude = hex(int(value, 16))

    def _set_igmptxv3modeexclude_with_str(self, value):
        try:
            self._IgmpTxV3ModeExclude = int(value)
        except ValueError:
            self._IgmpTxV3ModeExclude = hex(int(value, 16))

    def _set_igmptxv3modechangetoinclude_with_str(self, value):
        try:
            self._IgmpTxV3ModeChangeToInclude = int(value)
        except ValueError:
            self._IgmpTxV3ModeChangeToInclude = hex(int(value, 16))

    def _set_igmptxv3modechangetoexclude_with_str(self, value):
        try:
            self._IgmpTxV3ModeChangeToExclude = int(value)
        except ValueError:
            self._IgmpTxV3ModeChangeToExclude = hex(int(value, 16))

    def _set_igmptxv3modeallownewsources_with_str(self, value):
        try:
            self._IgmpTxV3ModeAllowNewSources = int(value)
        except ValueError:
            self._IgmpTxV3ModeAllowNewSources = hex(int(value, 16))

    def _set_igmptxv3modeblockoldsources_with_str(self, value):
        try:
            self._IgmpTxV3ModeBlockOldSources = int(value)
        except ValueError:
            self._IgmpTxV3ModeBlockOldSources = hex(int(value, 16))

    def _set_igmprxv1queries_with_str(self, value):
        try:
            self._IgmpRxV1Queries = int(value)
        except ValueError:
            self._IgmpRxV1Queries = hex(int(value, 16))

    def _set_igmprxv2queries_with_str(self, value):
        try:
            self._IgmpRxV2Queries = int(value)
        except ValueError:
            self._IgmpRxV2Queries = hex(int(value, 16))

    def _set_igmprxv3queries_with_str(self, value):
        try:
            self._IgmpRxV3Queries = int(value)
        except ValueError:
            self._IgmpRxV3Queries = hex(int(value, 16))

    def _set_igmprxgeneralqueries_with_str(self, value):
        try:
            self._IgmpRxGeneralQueries = int(value)
        except ValueError:
            self._IgmpRxGeneralQueries = hex(int(value, 16))

    def _set_igmprxgroupspecificqueries_with_str(self, value):
        try:
            self._IgmpRxGroupSpecificQueries = int(value)
        except ValueError:
            self._IgmpRxGroupSpecificQueries = hex(int(value, 16))

    def _set_igmprxgroupandsourcespecificqueries_with_str(self, value):
        try:
            self._IgmpRxGroupAndSourceSpecificQueries = int(value)
        except ValueError:
            self._IgmpRxGroupAndSourceSpecificQueries = hex(int(value, 16))

    def _set_igmprxunknowntypes_with_str(self, value):
        try:
            self._IgmpRxUnknownTypes = int(value)
        except ValueError:
            self._IgmpRxUnknownTypes = hex(int(value, 16))

    def _set_igmprxchecksumerrors_with_str(self, value):
        try:
            self._IgmpRxChecksumErrors = int(value)
        except ValueError:
            self._IgmpRxChecksumErrors = hex(int(value, 16))

    def _set_igmprxlengtherrors_with_str(self, value):
        try:
            self._IgmpRxLengthErrors = int(value)
        except ValueError:
            self._IgmpRxLengthErrors = hex(int(value, 16))

