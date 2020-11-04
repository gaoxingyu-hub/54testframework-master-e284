import enum
from enum import Flag

def swap_int_to_enum_flag(value, enum_cls):
    if value is None:
        return None
    if isinstance(value, Flag) or not issubclass(enum_cls, Flag):
        return value
    ret = None
    for item in enum_cls:
        if item.value & value:
            if ret is None:
                ret = item
            else:
                ret |= item

    return ret


class EnumDynamicClassType(enum.Enum):
    OBJECT = 0
    STATISTIC = 1
    COMMAND = 2


class ROMCommandStateEnum(enum.Enum):
    INIT = 0
    SCHEDULED = 1
    RUNNING = 2
    SUCCESS = 3
    FAIL = 4


class EnumLinkEditType(enum.Enum):
    APPEND = 0
    REMOVE = 1


class EnumSrcDstMapType(enum.Enum):
    MANY_TO_MANY = 0
    ONE_TO_ONE = 1


class EnumBurstGapUnit(enum.Enum):
    NS = 0
    US = 1
    MS = 2
    SEC = 3


class EnumReserveState(enum.Enum):
    AVAILABLE = 0
    RESERVED = 1
    DISCONNECTED = 2


class EnumPortState(enum.Enum):
    PORT_DOWN = 0
    PORT_UP = 1
    PORT_REBOOTING = 2


class EnumLogWhiteList(enum.Enum):
    DisconnectUnexpected = 0


class EnumMediaType(enum.Enum):
    COPPER = 1
    FIBER = 2


class EnumLinkStatus(enum.Enum):
    DOWN = 0
    UP = 1


class EnumLineSpeed(enum.Enum):
    SPEED_UNKNOWN = 0
    SPEED_10M = 256
    SPEED_100M = 512
    SPEED_1G = 1024
    SPEED_2_5G = 16384
    SPEED_5G = 131072
    SPEED_10G = 2048
    SPEED_25G = 32768
    SPEED_40G = 4096
    SPEED_50G = 65536
    SPEED_100G = 8192


class EnumFlowControl(enum.Enum):
    DISABLE = 0
    ENABLE = 1
    AUTO = 2


class EnumDuplex(enum.Enum):
    HALF = 0
    FULL = 1


class EnumFecType(enum.Enum):
    TYPE_OFF = 0
    TYPE_RS_FEC_CLAUSE91 = 1
    TYPE_FEC_CLAUSE74 = 2
    TYPE_RS_FEC_CLAUSE108 = 3
    TYPE_RS_FEC_CONSORTIUM = 4


class EnumDataPath(enum.Enum):
    NORMAL = 0
    LOOPBACK = 1


class EnumModuleCapability(enum.Enum):
    MOD_UNKNOWN = 0
    MOD_10GBASE_LRM = 1
    MOD_10GBASE_LR = 2


class EnumRemoteFaultStatus(enum.Enum):
    NORMAL = 0
    REMOTEFAULT = 1
    LOCALFAULT = 2
    ALIGNFAULT = 4


class EnumPhyMode(enum.Enum):
    MODE_AUTO = 0
    MODE_1000BASEX = 1
    MODE_SGMII = 2


class EnumMaster(enum.Enum):
    ADVERTISE_SINGLE_PORT = 0
    ADVERTISE_MULTI_PORT = 1
    MANUAL_MASTER = 2
    MANUAL_SLAVE = 3


class EnumRemoteFault(enum.Enum):
    NORMAL = 0
    IGNORE = 1


class EnumWanMode(enum.Enum):
    LAN = 0
    WAN = 1


class EnumI2cAddress(enum.Enum):
    I2C_ADDR_A0 = 0
    I2C_ADDR_A2 = 2


class EnumOMReadResult(enum.Enum):
    OK = 0
    PARAMETER_ERROR = 1
    NO_SFP_PLUGIN = 2
    I2C_INVALID = 3


class EnumCardState(enum.Enum):
    CARD_DOWN = 0
    CARD_UP = 1
    CARD_REBOOTING = 2


class EnumChassisState(enum.Enum):
    CHASSIS_DOWN = 0
    CHASSIS_CONNECTING = 1
    CHASSIS_UP = 2
    CHASSIS_DISCONNECTING = 3
    CHASSIS_REBOOTING = 4


class EnumUpgradeState(enum.Enum):
    UPGRADE_NOT_STARTED = 0
    UPGRADE_IN_PROGRESS = 1
    UPGRADE_REBOOTING = 2
    UPGRADE_DONE = 3
    UPGRADE_FAIL = 4


class EnumSynClockRef(enum.Enum):
    SYNC_CLOCK_REF_NONE = 0
    SYNC_CLOCK_REF_1588 = 1
    SYNC_CLOCK_REF_GPS = 2
    SYNC_CLOCK_REF_IRIG_B = 3
    SYNC_CLOCK_REF_SYNC_IN = 4


class EnumPortType(enum.Enum):
    ETHERNET = 0


class EnumIPv6AddrType(enum.Enum):
    NON_LINK_LOCAL = 0
    LINK_LOCAL = 1


class LinkLocalGenTypeEnum(enum.Enum):
    FromGlobal = 0
    EUI64 = 1
    Customized = 2


class EnumCardMode(Flag):
    UNKNOWN = 0x0
    PERFORMANCE = 0x1
    FUNCTIONAL = 0x2


class EnumLinkFaultMode(enum.Enum):
    CONTINUOUS = 1
    DISCONTINUOUS = 2


class EnumTrafficDirection(enum.Enum):
    DOWNSTREAM = 0
    UPSTREAM = 1
    BIDIRECTION = 2


class EnumTrafficType(enum.Enum):
    ETHERNETII = 0
    VLAN = 3
    IPV4 = 1
    IPV6 = 2


class EnumTrafficMesh(enum.Enum):
    ONE_TO_ONE = 0
    MANY_TO_MANY = 1
    FULL_MESH = 2
    CONGESTION = 3
    LEARNING = 4
    BACK_BONE = 5
    PAIR = 6


class EnumEndpointMapping(enum.Enum):
    ROUND_ROBIN = 0
    MANY_TO_MANY = 2


class EnumStreamCreation(enum.Enum):
    CREATE_NEW_STREAMS = 0
    USE_EXISTING_STREAMS = 1


class EnumStreamTransmitMode(enum.Enum):
    CONTINUOUS = 0
    BURST = 1


class EnumStreamBurstGapUnit(enum.Enum):
    NS = 0
    US = 1
    MS = 2
    SEC = 3


class EnumState(enum.Enum):
    DISABLED = 0
    NOTREADY = 1
    READY = 2
    RUNNING = 3
    STOPPED = 4
    PAUSED = 5


class EnumFrameLengthType(enum.Enum):
    FIXED = 0
    INCREMENT = 1
    RANDOM = 2
    AUTO = 3
    DECREMENT = 4
    IMIX = 5


class EnumPayloadType(enum.Enum):
    CYCLE = 0
    INCREMENT = 1
    RANDOM = 2


class EnumFrameGapUnit(enum.Enum):
    NS = 0
    PERCENT = 1
    FRAME_PER_SEC = 2
    BYTE_PER_SEC = 3
    DATABIT_PER_SEC = 4
    LINEBIT_PER_SEC = 5
    INTER_FRAME_GAP_BYTE = 6
    KLINEBIT_PER_SEC = 7
    MLINEBIT_PER_SEC = 8


class EnumRateUnit(enum.Enum):
    FRAME_PER_SEC = 0
    BYTE_PER_SEC = 1
    PERCENT = 2


class EnumTransmitMode(enum.Enum):
    CONTINUOUS = 0
    BURST = 1
    TIME = 2
    STEP = 3
    ONSTREAM = 4


class EnumErrorGen(enum.Enum):
    NO_ERROR = 0
    CRC = 1


class EnumLoadProfileType(enum.Enum):
    PORT_BASE = 0
    STREAM_BASE = 1


class EnumIgnoreLinkState(enum.Enum):
    NO = 0
    YES = 1


class EnumTimeStampPos(enum.Enum):
    TIMESTAMP_HEAD = 0
    TIMESTAMP_TAIL = 1


class QueryState(enum.Enum):
    STOPPED = 0
    RUNNING = 1
    PAUSED = 2


class EnumUnitsType(enum.Enum):
    BPS = 0
    KBPS = 1
    MBPS = 2
    GBPS = 3


class EnumChangeUnitsType(enum.Enum):
    SINGLE = 0
    All = 1


class EnumResultType(enum.Enum):
    AUTO = 0
    PAGED = 1
    NONE_PAGED = 2


class EnumChartObjectType(enum.Enum):
    Port = 0
    Interface = 1
    StreamTemplate = 2


class EnumWriteMode(enum.Enum):
    OVERWRITE = 0
    APPEND = 1


class EnumOutputFormat(enum.Enum):
    CSV = 0


class EnumResultStatus(enum.Enum):
    NONE = 0
    PASSED = 1
    FAILED = 2


class EnumResultViewType(enum.Enum):
    GRID = 1
    CHART = 2
    REPORT = 3
    OTHERS = 4


class EnumDataMode(enum.Enum):
    TEMPLATE_MODE1 = 0
    TEMPLATE_MODE2 = 1
    RAW_DATA_MODE = 2


class EnumSendMode(enum.Enum):
    SYNCHRONOUS = 0
    ASYNCHRONOUS = 1


class EnumFrameLoadUnit(enum.Enum):
    PERCENT = 1
    FRAME_PER_SEC = 2
    BYTE_PER_SEC = 3
    LINEBIT_PER_SEC = 4
    KLINEBIT_PER_SEC = 5
    MLINEBIT_PER_SEC = 6


class EnumRxPortSelectMode(enum.Enum):
    ONE_TO_ONE = 0
    ONE_TO_MANY = 1
    MANY_TO_ONE = 2
    PAIR = 3


class EnumPropertyType(enum.Enum):
    MACADDRESS = 5
    IPV4ADDRESS = 6
    IPV6ADDRESS = 7
    BYTEDATA = 1
    BITDATA = 2
    INTEGER = 0


class EnumLayerState(enum.Enum):
    DISABLED = 0
    READY = 1


class EnumAddressMode(enum.Enum):
    RANGE = 0
    LIST = 1


class EnumOption(enum.Enum):
    LATEST = 0
    ALL = 1


class EnumCongestionControl(enum.Enum):
    NONE = 0
    FREE_BSD = 1
    NEW_RENO = 2
    CUBIC = 3


class EnumArpState(enum.Enum):
    IDLE = 0
    LEARNING = 1
    SUCCESS = 2
    FAIL = 3


class EnumPingConfigState(enum.Enum):
    IDLE = 0
    PING = 1


class ProtocolType(enum.Enum):
    HTTP = 0
    FTP = 1
    DNS = 3
    PLAYBACKPCAP = 4


class EnumLoadType(enum.Enum):
    Users = 0
    UsersSecond = 1
    ConcurrentUsers = 2
    Connections = 3
    ConnectionsSecond = 4
    ConnectionsAttemptsSecond = 5
    ConcurrentConnections = 6
    Transactions = 7
    TransactionsSecond = 8
    Bandwidth = 9


class TestCaseState(enum.Enum):
    RUNNING = 0
    STOP = 1
    IDLE = 3


class LogType(enum.Enum):
    CURRENT = 0
    RECENT1DAY = 1
    RECENT3DAYS = 2
    RECENT7DAYS = 3
    RECENT30DAYS = 4
    ALL = 5


class EnumLoggerLevel(enum.Enum):
    TRACE = 2
    ERROR = 3
    WARNING = 4
    INFO = 6
    DEBUG = 7


class EnumSmartScripterState(enum.Enum):
    IDLE = 0
    RUNNING = 1
    PAUSED = 2
    CAPTURING = 3
    STOPPING = 4


class EnumSmartScripterVertict(enum.Enum):
    NONE = 0
    PASS = 1
    FAILED = 2


class EnumSmartScripterMode(enum.Enum):
    CONTINUE = 0
    STEP = 1


class EnumExpectCondition(enum.Enum):
    PASS = 0
    FAIL = 1


class EnumSleepTimeMode(enum.Enum):
    CEIL = 0
    FLOOR = 1
    NORMAL = 2


class EnumVariableType(enum.Enum):
    INT = 0
    STRING = 1


class EnumWaitOperator(enum.Enum):
    EQUAL = 0
    GREATER_THAN = 1
    LESS_THAN = 2
    GREATER_EQUAL_THAN = 3
    LESS_EQUAL_THAN = 4
    NOTEQAUL = 5


class EnumExecuteShellMode(enum.Enum):
    ASYNC = 0
    SYNC = 1


class EnumBoolean(enum.Enum):
    TRUE = 0
    FALSE = 1


class EnumCompareTarget(enum.Enum):
    NUMERIC = 0
    RESULT_COUNTER = 1
    STRING = 2


class EnumBoolOperator(enum.Enum):
    AND = 0
    OR = 1


class EnumCaptureState(enum.Enum):
    DISABLED = 0
    IDLE = 1
    RUNNING = 2
    DOWNLOADING = 3


class EnumCaptureMode(enum.Enum):
    ALL = 0
    CTRL_PLANE = 1


class EnumCacheCapacity(enum.Enum):
    Cache_Max = 0
    Cache_32KB = 511
    Cache_64KB = 1023
    Cache_128KB = 2047
    Cache_256KB = 4095
    Cache_512KB = 8191
    Cache_1MB = 16383
    Cache_2MB = 32767
    Cache_4MB = 65535
    Cache_8MB = 131071
    Cache_16MB = 262143
    Cache_32MB = 524287
    Cache_64MB = 1048575
    Cache_128MB = 2097151
    Cache_256MB = 4194303
    Cache_512MB = 8388607
    Cache_1GB = 16777215


class EnumFilterMode(enum.Enum):
    NONE = 0
    BYTE = 1
    PDU = 2


class EnumBufferFullAction(enum.Enum):
    STOP = 0
    WRAP = 1


class EnumBuffFullState(enum.Enum):
    NOT_FULL = 0
    FULL = 1


class EnumEventType(enum.Enum):
    START = 0
    STOP = 1
    PAUSE = 2
    RESUME = 3
    QUALIFY = 4


class EnumCaptureOptionLogicRelation(enum.Enum):
    AND = 0
    OR = 1


class EnumCaptureOptionType(enum.Enum):
    IGNORE = 0
    INCLUDE = 1
    EXCLUDE = 2


class EnumRxLearningEncap(enum.Enum):
    NO_ENCAPSULATION = 0
    TX_ENCAPSULATION = 1


class EnumIgmpHostState(enum.Enum):
    NONMEMBER = 0
    JOINING = 1
    MEMBER = 2
    LEAVING = 3


class EnumIgmpMulticastVersion(enum.Enum):
    IGMPV1 = 0
    IGMPV2 = 1
    IGMPV3 = 2


class EnumIgmpDeviceGroupMapping(enum.Enum):
    MANYTOMANY = 0
    ONETOONE = 1
    ROUNDROBIN = 2


class EnumIgmpSourceFilterMode(enum.Enum):
    INCLUDE = 1
    EXCLUDE = 2


class EnumIgmpFilteredSources(enum.Enum):
    NONE = 1
    USEEXISTIINGDEVICE = 2
    CUSTOMRANGE = 3


class EnumMldHostState(enum.Enum):
    NONMEMBER = 0
    JOINING = 1
    MEMBER = 2
    LEAVING = 3


class EnumMldMulticastVersion(enum.Enum):
    MLDV1 = 1
    MLDV2 = 2


class EnumMldDeviceGroupMapping(enum.Enum):
    MANYTOMANY = 0
    ONETOONE = 1
    ROUNDROBIN = 2


class EnumMldSourceFilterMode(enum.Enum):
    INCLUDE = 1
    EXCLUDE = 2


class EnumMldFilteredSources(enum.Enum):
    NONE = 1
    USEEXISTIINGDEVICE = 2
    CUSTOMRANGE = 3


class EnumDhcpv4ClientState(enum.Enum):
    NOT_READY = 0
    IDLE = 1
    BINDING = 2
    BOUND = 3
    RELEASING = 4
    RENEWING = 5
    REBINDING = 6
    REBOOTING = 7


class EnumDhcpv4ClientMode(enum.Enum):
    CLIENT = 0
    RELAY_AGENT = 1


class EnumRequestParameter(Flag):
    SUBNET_MASK = 0x1
    ROUTERS = 0x2
    DOMAIN_NAME_SERVERS = 0x4
    DOMAIN_NAME = 0x8
    STATIC_ROUTES = 0x10
    IP_LEASE_TIME = 0x20
    SERVER_IDENTIFIER = 0x40
    T1 = 0x80
    T2 = 0x100


class EnumDhcpv4BroadcastType(enum.Enum):
    UNICAST = 0
    BROADCAST = 1


class EnumDhcpv4OptionType(enum.Enum):
    HEX = 0
    STRING = 1
    BOOLEAN = 2
    INT8 = 3
    INT16 = 4
    INT32 = 5
    IP = 6


class EnumDhcpv4ClientMessageType(Flag):
    DISCOVER = 0x1
    REQUEST = 0x2


class EnumDhcpv4ServerMessageType(Flag):
    OFFER = 0x1
    ACK = 0x2
    NAK = 0x4


class EnumDhcpv4ServerState(enum.Enum):
    NOT_READY = 0
    DOWN = 1
    UP = 2


class EnumDhcpv6ServerIncludeMsg(Flag):
    ADVERTISE = 0x1
    REPLY = 0x2
    RECONFIGURE = 0x4
    RELAYREPLY = 0x8


class EnumDhcpv6EmulationServerMode(enum.Enum):
    DHCPV6 = 0
    DHCPV6PD = 1


class EnumDhcpv6ServerState(enum.Enum):
    NOTSTART = 0
    UP = 1
    DISABLED = 2


class EnumDhcpv6KeyType(enum.Enum):
    ASCII = 0
    HEX = 1


class EnumDhcpv6EmulationMode(enum.Enum):
    DHCPV6 = 0
    DHCPV6PD = 1
    DHCPV6ANDPD = 2


class EnumDhcpv6BlockSessionState(enum.Enum):
    DISABLED = 0
    IDLE = 1
    BOUND = 2
    SOLICITING = 3
    REQUESTING = 4
    RELEASING = 5
    RENEWING = 6
    REBINDING = 7


class EnumDhcpv6RapidCommitOptMode(enum.Enum):
    DISABLE = 0
    ENABLE = 1
    SERVERSET = 2


class EnumDhcpv6DuidType(enum.Enum):
    LLT = 1
    EN = 2
    LL = 3
    CUSTOM = 4


class EnumDhcpv6DestAddress(enum.Enum):
    ALL = 0
    SERVER = 1


class EnumDhcpv6SourceIPv6Address(enum.Enum):
    LINKLOCAL = 0
    ROUTEADVERTISEMENT = 1


class EnumDhcpv6AuthenticationProtocol(enum.Enum):
    DELAYED = 2
    RECONFIGURATION = 3


class EnumDhcpv6IncludeMsg(Flag):
    SOLICIT = 0x1
    REQUEST = 0x2
    CONFIRM = 0x4
    RENEW = 0x8
    REBIND = 0x10
    RELEASE = 0x20
    INFOREQUEST = 0x40
    RELAYFORWARD = 0x80


class EnumPppoeMode(enum.Enum):
    CLIENT = 0
    SERVER = 1
    PPPoL2TP = 2


class EnumPppoeCpState(enum.Enum):
    NONE = 0
    IDLE = 1
    CONNECTED = 2
    CONNECTING = 3
    DISCONNECTING = 4


class EnumPppoeIpVersion(enum.Enum):
    NONE = 0
    IPV4 = 1
    IPV6 = 2
    IPV4_IPV6 = 3


class EnumPppoeAuthenticationType(enum.Enum):
    NO_AUTHENTICATION = 0
    NEGOTIATION = 1
    CHAP_MD5 = 49699
    PAP = 49187


class EnumPppoeMOFlag(enum.Enum):
    M0_O0 = 0
    M0_O1 = 64
    M1 = 128


class EnumPppoeCustomOptionSubProtocolType(enum.Enum):
    LINK_CONTROL_PROTOCOL = 0
    IP_CONTROL_PROTOCOL = 1
    IPV6_CONTROL_PROTOCOL = 2
    PPPOE_PADI_PADR = 3


class EnumWizardPppoeMode(enum.Enum):
    CLIENT = 0
    SERVER = 1


class EnumL2tpState(enum.Enum):
    NONE = 0
    IDLE = 1
    CONNECTING = 2
    CONNECTED = 3
    DISCONNECTING = 4


class EnumL2tpVersion(enum.Enum):
    L2TPV2 = 2


class EnumL2tpEmulationMode(enum.Enum):
    LAC = 0
    LNS = 1


class EnumL2tpIpEncapsulation(enum.Enum):
    IPV4 = 0
    IPV6 = 1


class EnumL2tpBearCapabilities(enum.Enum):
    DIGITAL = 1
    ANALOG = 2
    BOTH = 3


class EnumL2tpBearType(enum.Enum):
    DIGITAL = 1
    ANALOG = 2


class EnumL2tpFrameCapabilities(enum.Enum):
    SYNC = 1
    ASYNC = 2
    BOTH = 3


class EnumL2tpFrameType(enum.Enum):
    SYNC = 1
    ASYNC = 2


class EnumL2tpLcpProxyMode(enum.Enum):
    NONE = 0
    LCP = 1
    LCP_AUTH = 2


class EnumL2tpWizardPppIpVersion(enum.Enum):
    IPV4 = 1
    IPV6 = 2
    IPV4_IPV6 = 3


class EnumDot1xState(enum.Enum):
    DISABLED = 0
    UNAUTHORIZED = 1
    AUTHENTICATING = 2
    AUTHENTICATED = 3
    FAILED = 4
    LOGGING_OFF = 5


class EnumDot1xAuthMode(enum.Enum):
    MD5 = 0
    TLS = 1
    TTLS = 2


class EnumDot1xInnerAuthMode(enum.Enum):
    AUTO = 0
    GTC = 1
    MS_CHAPV2 = 2
    MD5 = 3


class EnumIgmpRouterState(enum.Enum):
    NOTSTARTED = 0
    UP = 1


class EnumIgmpQuerierVersion(enum.Enum):
    IGMPV1 = 0
    IGMPV2 = 1
    IGMPV3 = 2


class EnumMldRouterState(enum.Enum):
    NOTSTARTED = 0
    UP = 1


class EnumMldQuerierVersion(enum.Enum):
    MLDV1 = 1
    MLDV2 = 2


class EnumIPv6AutoConfigurationState(enum.Enum):
    DISABLED = 0
    IDLE = 1
    ESTABLISHING = 2
    BOUND = 3


class EnumGroupType(enum.Enum):
    ANY_G = 0
    S_G = 1
    S_G_RPT = 2
    ANY_RP = 3


class EnumPimState(enum.Enum):
    DISABLED = 0
    HELLO = 1
    NEIGHBOR = 2
    IDLE = 3
    NOTSTARTED = 4


class EnumSessionMode(enum.Enum):
    SM = 0
    SSM = 1


class EnumPimIpVersion(enum.Enum):
    IPV4 = 0
    IPV6 = 1


class EnumGenIdMode(enum.Enum):
    FIXED = 0
    INCR = 1
    RAND = 2


class EnumBsrState(enum.Enum):
    STOPPED = 0
    SENDING = 1
    IDLE = 2


class BfdConnectivityVerificationTypeEnum(enum.Enum):
    CONNECTIVITY_VERIFICATION_TYPE_0x07 = 7
    CONNECTIVITY_VERIFICATION_TYPE_0x08 = 8
    CONNECTIVITY_VERIFICATION_TYPE_0x23 = 35


class BfdControlChannelTypeEnum(enum.Enum):
    CONTROL_CHANNEL_TYPE_0x07 = 7
    CONTROL_CHANNEL_TYPE_0x22 = 34


class BfdRouterRoleEnum(enum.Enum):
    ACTIVE = 0
    PASSIVE = 1


class BfdProtocolStateEnum(enum.Enum):
    DISABLED = 0
    NOT_STARTED = 1
    IDLE = 2
    RUNNING = 3


class BfdTimeIntervalUnitEnum(enum.Enum):
    MILLISECONDS = 0
    MICROSECONDS = 1


class BfdAuthTypeEnum(enum.Enum):
    NONE = 0
    SIMPLE_PASSWORD = 1
    KEYED_MD5 = 2
    METICULOUS_KEYED_MD5 = 3
    KEYED_SHA1 = 4
    METICULOUS_KEYED_SHA1 = 5


class BfdProtocolDependentSessionEnum(enum.Enum):
    DEPENDENT = 0
    INDEPENDENT = 1


class EnumOspfRouterState(enum.Enum):
    NOTSTART = 0
    P2P = 1
    WAITING = 2
    DR = 3
    BACKUP = 4
    DROTHER = 5
    DISABLE = 6
    STOPPED = 7


class EnumOspfAdjacencyState(enum.Enum):
    DOWN = 1
    INIT = 2
    TWOWAY = 3
    EXSTART = 4
    EXCHANGE = 5
    LOADING = 6
    FULL = 7


class EnumOspfNetworkType(enum.Enum):
    BROADCAST = 0
    P2P = 1


class EnumOspfAuthType(enum.Enum):
    NONE = 0
    SIMPLE = 1
    MD5 = 2


class EnumOspfv2OptionBit(Flag):
    TOSBIT = 0x1
    EBIT = 0x2
    MCBIT = 0x4
    NPBIT = 0x8
    EABIT = 0x10
    DCBIT = 0x20
    OBIT = 0x40
    DNBIT = 0x80


class EnumOspfv2ReasonType(enum.Enum):
    UNKNOWN = 0
    SOFTWARE = 1
    RELOADORUPGRADE = 2
    SWITCH = 3


class EnumOspfv2RouterType(Flag):
    ABR = 0x1
    ASBR = 0x2
    VLE = 0x4


class EnumRouterLsaLinkType(enum.Enum):
    P2P = 1
    TRANSITNETWORK = 2
    STUBNETWORK = 3
    VIRTUALLINK = 4


class EnumExtLsaLsType(enum.Enum):
    ExtLsaLsType1 = 0
    ExtLsaLsType2 = 1


class EnumExtLsaLsMetricType(enum.Enum):
    ExtLsaLsMetricType1 = 0
    ExtLsaLsMetricType2 = 1


class EnumTeTlvType(enum.Enum):
    LsaRouter = 1
    LsaLink = 2


class EnumTeLinkType(enum.Enum):
    LinkP2P = 1
    LinkMultiaccess = 2


class EnumOspfv2WizardTopologyType(enum.Enum):
    NONE = 0
    TREE = 1
    GRID = 2
    FULLMESH = 3
    RING = 4
    HUBSPOKE = 5


class EnumOspfv2WizardGridRouterPositionType(enum.Enum):
    ATTACHEDTOGRID = 0
    MEMBEROFGRID = 1


class EnumOspfv2WizardFullMeshRouterPositionType(enum.Enum):
    ATTACHEDTOMESH = 0
    MEMBEROFMESH = 1


class EnumOspfv2WizardRingRouterPositionType(enum.Enum):
    ATTACHEDTORING = 0
    MEMBEROFRING = 1


class EnumOspfv2WizardHubSpokeRouterPositionType(enum.Enum):
    ATTACHEDTOHUB = 0
    ATTACHEDTOSPOKE = 1
    MEMBERASHUB = 2
    MEMBERASSPOKE = 3


class EnumOspfv2WizardAreaType(enum.Enum):
    REGULAR = 0
    STUB = 1
    STUBNOSUMMARY = 2
    NSSA = 3
    NSSANOSUMMARY = 4


class EnumOspfv2WizardRadioType(enum.Enum):
    NONE = 0
    ALL = 1
    EDGE = 2


class EnumOspfv2WizardDistributionType(enum.Enum):
    FIXED = 0
    LINEAR = 1


class EnumInterSystemLevel(enum.Enum):
    L1 = 1
    L2 = 3


class EnumRouteMeTricType(enum.Enum):
    INTERNAL = 0
    EXTERNAL = 1


class EnumRouterState(enum.Enum):
    NOTSTART = 0
    IDLE = 1
    INIT = 2
    UP = 3
    GR = 4
    GRHELPER = 5
    DISABLE = 6


class EnumThreeWayP2PAdjState(enum.Enum):
    UP = 0
    INIT = 1
    DOWN = 2
    NOTSTART = 3
    NA = 4


class EnumBroadcastAdjState(enum.Enum):
    NOTSTART = 0
    IDLE = 1
    INIT = 2
    DISOTHER = 3
    DIS = 4
    GR = 5
    GRHELPER = 6
    NA = 7


class EnumIpVersion(enum.Enum):
    IPV4 = 0
    IPV6 = 1
    IPV4IPV6 = 2


class EnumLevel(enum.Enum):
    L1 = 1
    L2 = 2
    L1L2 = 3


class EnumNetworkType(enum.Enum):
    BROADCAST = 0
    P2P = 1


class EnumAuthMethod(enum.Enum):
    NONE = 0
    SIMPLE = 1
    MD5 = 54


class EnumMetricMode(enum.Enum):
    NARROW = 0
    WIDE = 1
    NARROWWIDE = 2


class EnumOspfv3OptionBit(Flag):
    V6BIT = 0x1
    EBIT = 0x2
    MCBIT = 0x4
    NBIT = 0x8
    RBIT = 0x10
    DCBIT = 0x20


class EnumOspfv3ReasonType(enum.Enum):
    UNKNOWN = 0
    SOFTWARE = 1
    RELOADORUPGRADE = 2
    SWITCH = 3


class EnumOspfv3RouterType(Flag):
    RouterTypeABR = 0x1
    RouterTypeASBR = 0x2
    RouterTypeVirtype = 0x4


class EnumOspfv3RouteLinkType(enum.Enum):
    P2P = 1
    TRANSITNETWORK = 2
    VIRTUALLINK = 4


class EnumOspfv3PrefixOptionBit(Flag):
    NUBIT = 0x1
    LABIT = 0x2
    MCBIT = 0x4
    PBIT = 0x8


class EnumOspfv3WizardTopologyType(enum.Enum):
    NONE = 0
    TREE = 1
    GRID = 2
    FULLMESH = 3
    RING = 4
    HUBSPOKE = 5


class EnumOspfv3WizardGridRouterPositionType(enum.Enum):
    ATTACHEDTOGRID = 0
    MEMBEROFGRID = 1


class EnumOspfv3WizardFullMeshRouterPositionType(enum.Enum):
    ATTACHEDTOMESH = 0
    MEMBEROFMESH = 1


class EnumOspfv3WizardRingRouterPositionType(enum.Enum):
    ATTACHEDTORING = 0
    MEMBEROFRING = 1


class EnumOspfv3WizardHubSpokeRouterPositionType(enum.Enum):
    ATTACHEDTOHUB = 0
    ATTACHEDTOSPOKE = 1
    MEMBERASHUB = 2
    MEMBERASSPOKE = 3


class EnumOspfv3WizardAreaType(enum.Enum):
    REGULAR = 0
    STUB = 1
    STUBNOSUMMARY = 2
    NSSA = 3
    NSSANOSUMMARY = 4


class EnumOspfv3WizardRadioType(enum.Enum):
    NONE = 0
    ALL = 1
    EDGE = 2


class EnumOspfv3WizardDistributionType(enum.Enum):
    FIXED = 0
    LINEAR = 1


class BfdDiagnosticEnum(enum.Enum):
    NO_DIAGNOSTIC = 0
    CONTROL_DETECTION_TIME_EXPIRED = 1
    ECHO_FUNCTION_FAILED = 2
    NEIGHBOR_SIGNAL_SESSION_DOWN = 3
    FORWARDING_PLANE_RESET = 4
    PATH_DOWN = 5
    CONCATENATED_PATH_DOWN = 6
    ADMINISTRATIVELY_DOWN = 7
    REVERSE_CONCATENATED_PATH_DOWN = 8


class EnumCreateLspLevel(enum.Enum):
    CREATE_L1_LSP = 0
    CREATE_L2_LSP = 1
    CREATE_L1_L2_LSP = 2


class EnumLspTopologyType(enum.Enum):
    NONE = 0
    TREE = 1
    GRID = 2
    FULL_MESH = 3
    RING = 4
    HUB_SPOKE = 5


class EnumTopologyRouterPosition(enum.Enum):
    ATTACHED = 0
    MEMBER = 1


class EnumHubTopologyRouterPosition(enum.Enum):
    ATTACHED_TO_HUB = 0
    ATTACHED_TO_SPOKE = 1
    MEMBERAS_HUB = 2
    MEMBERAS_SPOKE = 3


class EnumSimuRouterAdvertiseType(enum.Enum):
    NONE = 0
    ALL = 1
    EDGE = 2


class EnumPrefixLenDistributionType(enum.Enum):
    FIXED = 0
    LINEAR = 1


class EnumPathAttributeOptionalFlag(enum.Enum):
    WELL_KNOWN = 0
    OPTION = 1


class EnumPathAttributeTransitiveFlag(enum.Enum):
    NONTRANSITIVE = 0
    TRANSITIVE = 1


class EnumPathAttributePartialFlag(enum.Enum):
    COMPLETE = 0
    PARTIAL = 1


class EnumBgpProtocolState(enum.Enum):
    DISABLED = 0
    NOT_START = 1
    RUNNING = 2
    STARTING = 3
    STOPPING = 4


class EnumBgpIpVersion(enum.Enum):
    BOTH = 0
    IPV4 = 1
    IPV6 = 2


class EnumBgpType(enum.Enum):
    EBGP = 0
    IBGP = 1


class EnumBgpSessionIpAddress(enum.Enum):
    INTERFACE_IP = 0
    ROUTE_ID = 1


class EnumBgpRouteRefreshMode(enum.Enum):
    NONE = 0
    ROUTE_REFRESH = 1


class EnumBgpAuthentication(enum.Enum):
    NONE = 0
    MD5 = 1


class EnumBgpRoutesFileType(enum.Enum):
    HUAWEI = 0
    CISCO = 1


class EnumBgpRoutesFileParsingStatus(enum.Enum):
    NONE = 0
    SUCCEEDED = 1
    FAILED = 2


class EnumVtepState(enum.Enum):
    STARTED = 0
    STOPPED = 1


class EnumMulticastType(enum.Enum):
    IGMP = 0
    PIM = 1


class EnumTunnelIpAddress(enum.Enum):
    INTERFACEIP = 0
    ROUTERID = 1


class EnumCommunicationType(enum.Enum):
    UNICAST = 0
    MULTICAST = 1
    BGPEVPN = 2


class EnumVxlanAddressMode(enum.Enum):
    IPv4 = 1


class EnumIGMPVersion(enum.Enum):
    IGMPv2 = 0
    IGMPv3 = 1


class EnumBgpSubAfi(enum.Enum):
    UNICAST = 1
    MULTICAST = 2
    EVPN = 70


class EnumBgpOrigin(enum.Enum):
    IGP = 0
    EGP = 1
    INCOMPLETE = 2


class EnumBgpAsPathType(enum.Enum):
    SET = 1
    SEQUENCE = 2


class EnumBgpCommunityType(enum.Enum):
    AA_NN = 0
    NO_EXPORT = 1
    NO_ADVERTISE = 2
    LOCAL_AS = 3


class EnumBgpAfi(enum.Enum):
    IPV4 = 1
    IPV6 = 2
    L2VPN = 25


class EnumBgpWizardRouteType(enum.Enum):
    IPV4_ROUTES = 0
    IPV6_ROUTES = 1
    IPV4_IPV6 = 2
    NO_ROUTES = 3


class EnumEvpnOrigin(enum.Enum):
    IGP = 0
    EGP = 1


class EnumRouteDistinguisherType(enum.Enum):
    TYPE0 = 0
    TYPE1 = 1
    TYPE2 = 2


class EnumEthernetSegmentType(enum.Enum):
    OPERATOR = 0
    IEEE802 = 1
    BRIDGEDLAN = 2
    MACBASED = 3
    ROUTEID = 4
    AS = 5


class EnumAdRouteType(enum.Enum):
    EVI = 0
    ESI = 1


class EnumActiveStandbyType(enum.Enum):
    ALL = 0
    SINGLE = 1


class EnumPmsiTunnelType(enum.Enum):
    NONE = 0
    RSVP_TE_P2MP_LSP = 1
    MLDP_P2MP_LSP = 2
    PIM_SSM = 3
    PIM_SM = 4
    BIDIR_PIM = 5
    INGRESS_REPLICATION = 6
    MLDP_MP2MP_LSP = 7


class EnumAssociatedIpType(enum.Enum):
    NONE = 0
    IPV4 = 1
    IPV6 = 2


class EnumLdpState(enum.Enum):
    NOT_STARTED = 0
    CONNECTING = 1
    INIT = 2
    OPEN_SENT = 3
    OPEN_REC = 4
    UP = 5
    DOWN = 6


class EnumHelloType(enum.Enum):
    DIRECT = 0


class EnumTransportMode(enum.Enum):
    TEST_IP = 0
    ROUTER_ID = 1
    NONE = 2


class EnumEgressLabel(enum.Enum):
    DEFINED = 0
    IMPLICIT = 1
    EXPLICIT = 2


class EnumFECType(enum.Enum):
    WILDCARD_FEC = 0
    PREFIX_FEC = 1
    HOST_FEC = 2
    CRLSP_FEC = 3
    VC_FEC = 4


class EnumProtocolState(enum.Enum):
    DISABLE = 0
    NOTSTART = 1
    CLOSED = 2
    OPEN = 3
    SUSPENDED = 4


class EnumRipVersion(enum.Enum):
    RIPV1 = 1
    RIPV2 = 2
    RIPNG = 3


class EnumUpdateType(enum.Enum):
    BROADCAST = 0
    MULTICAST = 1
    UNICAST = 2


class EnumRipAuthMethod(enum.Enum):
    NONE = 0
    SIMPLE = 1
    MD5 = 2


class EnumTxType(enum.Enum):
    SINGLE = 0
    MULTIPLE = 1


class EnumTxRate(enum.Enum):
    TXRATE_10_PER_SEC = 0
    TXRATE_1_PER_SEC = 1
    TXRATE_1_PER_MIN = 2
    TXRATE_1_PER_10MIN = 3


class EnumOpMode(enum.Enum):
    IEEE = 0


class EnumMAIDType(enum.Enum):
    PRI_VID = 1
    STRING = 2


class EnumMdLevel(enum.Enum):
    Level0 = 0
    Level1 = 1
    Level2 = 2
    Level3 = 3
    Level4 = 4
    Level5 = 5
    Level6 = 6
    Level7 = 7


class EnumCCPeriod(enum.Enum):
    CC_3MS = 0
    CC_10MS = 1
    CC_100MS = 2
    CC_1S = 3
    CC_10S = 4
    CC_1MIN = 5
    CC_10MIN = 6


class EnumLCKPeriod(enum.Enum):
    LCK_1S = 0
    LCK_1MIN = 1


class EnumMpType(enum.Enum):
    MEP = 0


class EnumRdiValue(enum.Enum):
    AUTO = 0
    OFF = 1
    ON = 2


class EnumDot1agState(enum.Enum):
    DISABLED = 0
    IDLE = 1
    RUNNING = 2


class EnumMaIdFormat(enum.Enum):
    STRING = 1
    PRIMARY_VID = 2


class EnumMdIdFormat(enum.Enum):
    NO_NAME = 1
    STRING = 2


class EnumVlanType(enum.Enum):
    SINGLE = 0
    QinQ = 1


class EnumEthType(enum.Enum):
    TYPE_8100 = 33024
    TYPE_88A8 = 34984
    TYPE_9100 = 37120
    TYPE_9200 = 37376


class EnumOamModeType(enum.Enum):
    PASSIVE = 0
    ACTIVE = 1


class EnumDot3ahLocalState(enum.Enum):
    NONE = 0
    UNSATISFIED = 1
    NOTCOMPLETED = 2
    COMPLETED = 3
    RESERVED = 4
    DISABLED = 5
    IDLE = 6


class EnumTransmitType(enum.Enum):
    SINGLE = 0
    BATCH = 1


class EnumOfpField(enum.Enum):
    InPort = 0
    InPhyPort = 1
    Metadata = 2
    EthDstAddr = 3
    EthSrcAddr = 4
    EthType = 5
    VlanID = 6
    VlanPCP = 7
    IpDscp = 8
    IpEcn = 9
    IpProtocol = 10
    IPv4SrcAddr = 11
    IPv4DstAddr = 12
    TcpSrcPort = 13
    TcpDstPort = 14
    UdpSrcPort = 15
    UdpDstPort = 16
    SctpSrcPort = 17
    SctpDstPort = 18
    ICMPv4Type = 19
    ICMPv4Code = 20
    ArpOpcode = 21
    ArpSpa = 22
    ArpTpa = 23
    ArpSha = 24
    ArpTha = 25
    IPv6SrcAddr = 26
    IPv6DstAddr = 27
    IPv6FlowLabel = 28
    ICMPv6Type = 29
    ICMPv6Code = 30
    IPv6NdTarget = 31
    IPv6NdSll = 32
    IPv6NdTll = 33
    MplsLabel = 34
    MplsTc = 35
    MplsBos = 36
    PbbIsid = 37
    TunnelID = 38
    IPv6ExtHdr = 39


class EnumOfpModifier(enum.Enum):
    NONE = 0
    Intra = 1
    Inter = 2


class EnumOfpAction(enum.Enum):
    Output = 0
    CopyTtlOut = 11
    CopyTtlIn = 12
    SetMplsTtl = 15
    DecMplsTtl = 16
    PushVlan = 17
    PopVlan = 18
    PushMpls = 19
    PopMpls = 20
    SetQueue = 21
    Group = 22
    SetIPv4Ttl = 23
    DecIPv4Ttl = 24
    SetField = 25
    PushPBB = 26
    PopPBB = 27
    Experimenter = 65535


class EnumOfpCmdType(enum.Enum):
    ConfigSwitch = 0
    ConfigTable = 1
    AddFlow = 2
    ModifyFlow = 3
    DeleteFlow = 4
    AddGroup = 5
    ModifyGroup = 6
    DeleteGroup = 7
    AddMeter = 8
    ModifyMeter = 9
    DeleteMeter = 10
    RoleRequest = 11
    PacketOut = 12
    Think = 65532
    LoopBegin = 65534
    LoopEnd = 65535


class EnumOfpRole(enum.Enum):
    Equal = 1
    Master = 2
    Slave = 3


class EnumOfpSessionState(enum.Enum):
    IDLE = 0
    RUNING = 1
    STOPPED = 2
    DISABLED = 3


class EnumOfpConnection(enum.Enum):
    TCP = 0
    TCP_TLS = 1


class EnumOfpRoleDescState(enum.Enum):
    NONE = 0
    CONNECTED = 1


class EnumOfpControllerVersion(enum.Enum):
    v1_3 = 4


class EnumOfpInstruction(enum.Enum):
    GotoTable = 0
    WriteMetadata = 1
    WriteActions = 2
    ApplyActions = 3
    ClearActions = 4
    ApplyMeter = 5
    Experimenter = 65535


class EnumOfpFlowFlags(Flag):
    SEND_FLOW_REM = 0x1
    CHECK_OVERLAP = 0x2
    RESET_COUNTS = 0x4
    NO_PKT_COUNTS = 0x8
    NO_BYT_COUNTS = 0x10


class EnumOfpPacketInAction(enum.Enum):
    ApplyActions = 0
    AddFlow = 1
    ModifyFlow = 2


class EnumOfpTableMiss(enum.Enum):
    Drop = 0
    Continue = 1
    Controller = 2


class EnumOfpGroupTable(enum.Enum):
    All = 0
    Select = 1
    Indirect = 2
    FastFailover = 3


class EnumOfpMeterBand(enum.Enum):
    Drop = 0
    DscpRemark = 1
    Experimenter = 65535


class EnumOfpBandUnit(enum.Enum):
    kb = 0
    pkt = 1


class EnumOfpSwitchVersion(Flag):
    v1_3 = 0x10


class EnumOfpQueue(enum.Enum):
    MinRate = 0
    MaxRate = 1
    Experimenter = 65535


class EnumFlowTableType(enum.Enum):
    BOUND = 0


class EnumFlowActionType(enum.Enum):
    FORWARD_TO_PORT = 0
    DROP = 1


class EnumOvsdbState(enum.Enum):
    STARTED = 0
    STOPPED = 1


class EnumRefreshWay(enum.Enum):
    MANUAL = 0
    PERIODIC = 1


class EnumDatabaseType(enum.Enum):
    HARDWAREVTEP = 0


class EnumTableType(enum.Enum):
    LOCAL = 0
    REMOTE = 1


class EnumRefreshState(enum.Enum):
    REFRESHING = 0
    IDLE = 1


class EnumOvsdbConnectionType(enum.Enum):
    TCP = 0
    TLS = 1
    PASSIVE_TCP = 2
    PASSIVE_TLS = 3


class EnumArchive(enum.Enum):
    TRUE = 0
    FALSE = 1


class EnumStpProtocolType(enum.Enum):
    STP = 0
    RSTP = 1
    MSTP = 2


class EnumStpRootType(enum.Enum):
    SELF = 0
    OTHER = 1


class EnumRootPriority(enum.Enum):
    PRIORITY0 = 0
    PRIORITY4096 = 4096
    PRIORITY8192 = 8192
    PRIORITY12288 = 12288
    PRIORITY16384 = 16384
    PRIORITY20480 = 20480
    PRIORITY24576 = 24576
    PRIORITY28672 = 28672
    PRIORITY32768 = 32768
    PRIORITY36864 = 36864
    PRIORITY40960 = 40960
    PRIORITY45056 = 45056
    PRIORITY49152 = 49152
    PRIORITY53248 = 53248
    PRIORITY57344 = 57344
    PRIORITY61440 = 61440


class EnumPortPriority(enum.Enum):
    PRIORITY0 = 0
    PRIORITY16 = 16
    PRIORITY32 = 32
    PRIORITY48 = 48
    PRIORITY64 = 64
    PRIORITY80 = 80
    PRIORITY96 = 96
    PRIORITY112 = 112
    PRIORITY128 = 128
    PRIORITY144 = 144
    PRIORITY160 = 160
    PRIORITY176 = 176
    PRIORITY192 = 192
    PRIORITY208 = 208
    PRIORITY224 = 224
    PRIORITY240 = 240


class TrillProtocolStateEnum(enum.Enum):
    DISABLED = 0
    NOT_STARTED = 1
    IDLE = 2
    RUNNING = 3


class TrillDRBStateEnum(enum.Enum):
    DOWN = 0
    SUSPENDED = 1
    DRB = 2
    NOT_DRB = 3


class TrillAuthenticationTypeEnum(enum.Enum):
    NONE = 0
    SIMPLE = 1
    HMAC_MD5 = 2


class TrillNetworkTypeEnum(enum.Enum):
    BROADCAST = 0
    P2P = 1


class TrillRBridgeStateEnum(enum.Enum):
    DOWN = 0
    LISTEN = 1
    INIT = 2
    UP = 3


class EnumLacpLinkStatus(enum.Enum):
    DOWN = 0
    UP = 1
    ERROR = 2


class EnumLacpL2HashOption(Flag):
    ETHERNET_SOURCE_MAC = 0x1
    ETHERNET_DESTINATION_MAC = 0x2
    VLAN = 0x4
    MPLS = 0x8


class EnumLacpL3HashOption(Flag):
    ETHERNET_SOURCE_MAC = 0x1
    ETHERNET_DESTINATION_MAC = 0x2
    VLAN = 0x4
    MPLS = 0x8
    IPV4_SOURCE = 0x10
    IPV4_DESTINATION = 0x20
    IPV6_SOURCE = 0x40
    IPV6_DESTINATION = 0x80
    TCP = 0x100
    UDP = 0x200


class EnumLacpTransmotAlgorithm(enum.Enum):
    HASHING = 0
    ROUND_ROBIN = 1


class EnumLacpPortState(enum.Enum):
    DOWN = 0
    UP = 1


class EnumLacpTimeout(enum.Enum):
    LONG = 0
    SHORT = 1


class EnumLacpActivity(enum.Enum):
    ACTIVE = 0
    PASSIVE = 1


class TransportType(enum.Enum):
    TCP = 0
    UDP = 1


class ClientCmdQueryType(enum.Enum):
    QueryType_A = 0
    QueryType_NS = 1
    QueryType_CNAME = 2
    QueryType_SOA = 3
    QueryType_PTR = 4
    QueryType_MX = 5
    QueryType_AAAA = 6


class ClientCmdExpectType(enum.Enum):
    ExpectTypeIPv4 = 0
    ExpectTypeIPv6 = 1
    ExpectypeDomain = 3


class DnsRecordType(enum.Enum):
    A = 0
    AAAA = 1
    CNAME = 2
    NS = 3
    MX = 4
    PTR = 5
    SOA = 6


class EnumLoginMode(enum.Enum):
    PASSIVE = 0
    ACTIVE = 1


class EnumPacketInterval(enum.Enum):
    KEEP = 0
    NONE = 1
    CUSTOM = 2


class EnumCloseType(enum.Enum):
    RSTCli = 0
    RSTSer = 1
    FINCli = 2
    FINSer = 3


class EnumStreamGroupCreationMethodType(enum.Enum):
    ADDRESSFIRST = 0
    PORTFIRST = 1


class EnumTCPTearDown(enum.Enum):
    FIN = 0
    RST = 1


class EnumHttpVersion(enum.Enum):
    HTTP10 = 0
    HTTP11 = 1


class EnumHttpAuthType(enum.Enum):
    NoAuth = 0
    BasicAuth = 1


class EnumConnectionType(enum.Enum):
    TCP = 0
    EnablePipeline = 1
    DisablePipeline = 2


class EnumCmdAbortType(enum.Enum):
    NotAbort = 0
    BeforeRequest = 1
    AfterRequest = 2
    AfterResponse = 3


class EnumHttpPayloadType(enum.Enum):
    Custom = 0
    File = 1
    Range = 2


class EnumDateType(enum.Enum):
    Null = 0
    Static = 1
    Real = 2


class EnumModifyType(enum.Enum):
    Never = 0
    Static = 1


class EnumExpireType(enum.Enum):
    Never = 0
    Static = 1
    AfterRequest = 2
    AfterModify = 3


class EnumPayloadOffsetType(enum.Enum):
    Start = 0
    Middle = 1
    End = 2


class EnumPayloadTextType(enum.Enum):
    ASCII = 0
    Hex = 1


class EnumSSLVersion(Flag):
    SSLv2 = 0x1
    SSLv3 = 0x2
    TLSv1 = 0x4
    TLSv1_2 = 0x8


class EnumPeerAuthType(enum.Enum):
    NoAuth = 0
    OptionalAuth = 1
    MandatoryAuth = 2


class EnumLoadUnit(enum.Enum):
    PERCENT = 0
    FRAME_PER_SECOND = 1
    INTER_FRAME_GAP = 2
    BITS_PER_SEC = 3
    KBITS_PER_SEC = 4
    MBITS_PER_SEC = 5
    BYTES_PER_SEC = 6


class EnumIterationMode(enum.Enum):
    FIXED = 0
    STEP = 1
    CUSTOM = 2


class EnumInterFrameGapMode(enum.Enum):
    MIN = 0
    USER = 1


class EnumFrameSizeType(enum.Enum):
    STREAMBLOCK = 0
    RANDOM = 1
    STEP = 2
    CUSTOM = 3
    FIXED = 4
    IMIX = 5


class EnumLoadMode(enum.Enum):
    FIXED = 0
    STEP = 1
    CUSTOM = 2
    RANDOM = 3


class EnumAdjustStreamTemplateLoad(enum.Enum):
    NONE = 0
    PER_PORT = 1
    DIV_PORT = 2


class EnumSearchMode(enum.Enum):
    STEP = 0
    BINARY = 1
    COMBO = 2


class EnumLatencyType(enum.Enum):
    LIFO = 0
    FIFO = 1
    LILO = 2
    FILO = 3


class EnumAddressLearningMode(enum.Enum):
    L2 = 0
    L3 = 1


class EnumDurationMode(enum.Enum):
    SECOND = 0
    BURST = 1


class EnumAdddressLearningFrequency(enum.Enum):
    LEARNING_ONCE = 0
    LEARNING_EVERY_TRIAL = 1
    LEARNING_EVERY_FRAME_SIZE = 2
    LEARNING_EVERY_ITERATION = 3


class EnumEtherType(enum.Enum):
    CUSTOM = 0
    IPv4 = 1
    IPv6 = 2
    VLAN = 3


class EnumTrialDurationMode(enum.Enum):
    SECONDS = 0
    BURSTS = 1


class EnumDiagramMode(enum.Enum):
    LEARNING = 0
    BROADCAST = 1
    CONGESTION = 2


class EnumMulticastGroupCountMode(enum.Enum):
    FIXED = 0
    STEP = 1
    CUSTOM = 2
    RANDOM = 3


class EnumDeviceConfigurationMode(enum.Enum):
    AUTOMATIC = 0
    MANUAL = 1


class Enum3918AdddressLearningFrequency(enum.Enum):
    LEARNING_EVERY_TOPOLOGY_CHANGE = 1
    LEARNING_EVERY_FRAME_SIZE = 2
    LEARNING_EVERY_ITERATION = 3


class EnumMulticastGroupDist(enum.Enum):
    EVEN = 0
    WEIGHTED = 1


class EnumMulticastClientVersion(enum.Enum):
    IGMPV1 = 0
    IGMPV2 = 1
    IGMPV3 = 2
    MLDV1 = 3
    MLDV2 = 4


class EnumTransportLayerHeaderType(enum.Enum):
    NONE = 0
    TCP = 1
    UDP = 2


class EnumTrafficVerificationFrequency(enum.Enum):
    NONE = 0
    VERIFY_EVERY_TOPOLOGY_CHANGE = 1
    VERIFY_EVERY_FRAME_SIZE = 2
    VERIFY_EVERY_ITERATION = 3


class EnumMulticastPercentageMode(enum.Enum):
    FIXED = 0
    STEP = 1
    CUSTOM = 2
    RANDOM = 3


class EnumConfigTestCommandType(enum.Enum):
    CIR_TEST = 0
    EIR_TEST = 1
    TFP_TEST = 2
    CBS_TEST = 3
    EBS_TEST = 4


class EnumQosType(enum.Enum):
    TOS = 0
    DSCP = 1
    NONE = 2


class EnumL4ProtocolType(enum.Enum):
    TCP = 0
    UDP = 1
    NONE = 2


class EnumY1564LoadUnit(enum.Enum):
    BITS_PER_SEC = 0
    KBITS_PER_SEC = 1
    MBITS_PER_SEC = 2
    BYTES_PER_SEC = 3


class EnumProfileType(enum.Enum):
    NONE_BASED = 0
    IP_TOS_BASED = 1
    IP_DSCP_BASED = 2
    TCP_PORT_BASED = 3
    UDP_PORT_BASED = 4


class EnumMeshType(enum.Enum):
    ELINE = 0
    ELAN = 1


class EnumY1564AdddressLearningFrequency(enum.Enum):
    ONCE_PER_TEST = 0
    ON_TRIAL = 1
    ONCE_PER_SERVICE = 2
    ON_ITERATION = 3


class EnumTestAlgorithm(enum.Enum):
    SERVICE_CONFIG = 0
    PERFORMANCE_CONFIG = 1


class EnumAsymmetricLoadMode(enum.Enum):
    STEP = 1
    CUSTOM = 2
    RANDOM = 3


class EnumProfileAllocation(enum.Enum):
    PER_SIDE = 0
    PER_PORT = 1


class EnumBackOffMode(enum.Enum):
    INDEPENDENT = 0
    ASSOCIATED = 1


class EnumProfileSide(enum.Enum):
    DOWN_STREAM = 0
    UP_STREAM = 1


class EnumMplsLspPingType(enum.Enum):
    CoreTunnelLspPing = 0
    VpnTunnelLspPing = 1


class EnumMplsPadMode(enum.Enum):
    TransmitWithoutPadTlv = 0
    RequestPeerToDropPadTlv = 1
    RequestPeerToCopyPadTlv = 2


class EnumMplsEncapsulationType(enum.Enum):
    IPv4 = 0
    IPv6 = 1


class EnumMplsIgpProtocols(enum.Enum):
    OSPF = 0
    ISIS = 1
    RIP = 2
    None_ = 3


class EnumMplsMplsProtocols(enum.Enum):
    LDP = 0
    None_ = 1


class EnumMplsTopologyType(enum.Enum):
    Tree = 0
    Grid = 1


class EnumMplsTrafficFlowType(enum.Enum):
    None_ = 0
    FullyMeshed = 1
    Customer2Provider = 2
    Provider2Customer = 3
    CustomerProviderBoth = 4


class EnumMplsHostAssignment(enum.Enum):
    HostsOrMacsPerCe = 0
    HostsOrMacsPerVpn = 1
    TotalHostsOrMacs = 2


class EnumMplsRdAssignment(enum.Enum):
    UseRT = 0
    Manual = 1


class EnumMplsVplsVersion(enum.Enum):
    DraftIetfL2vpnVplsBgp00 = 0
    DraftIetfL2vpnVplsBgp02 = 1
    Rfc4761 = 2


class EnumMplsAssignment(enum.Enum):
    RoundRobin = 0
    Sequential = 1


class EnumMplsDistributionSelector(enum.Enum):
    VPNsPerPE = 0
    PEsPerVPN = 1


class EnumMplsPseudowiresEncapsulation(enum.Enum):
    EthernetVlan = 0
    Ethernet = 1
    EthernetVpls = 2


class EnumMplsFecType(enum.Enum):
    FEC128 = 0
    FEC129 = 1


class EnumMplsAgiAssignment(enum.Enum):
    UseRT = 0
    Manual = 1


class EnumMplsCeProtocol(enum.Enum):
    BGP = 0
    RIP = 1
    ISIS = 2
    OSPF = 3
    Mixed = 4


class EnumMplsRouteType(enum.Enum):
    Internal = 0
    External = 1


class EnumMplsLabelMethod(enum.Enum):
    LabelPerSite = 0
    LabelPerRoute = 1


class EnumCheckPlDetail(enum.Enum):
    CAN_CONNECT = 0
    CL_NOT_FOUND = 1
    REACH_MAX_CONNECTION = 2


