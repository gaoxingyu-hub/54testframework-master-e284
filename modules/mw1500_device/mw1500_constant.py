from common.info import SystemLanguage


class ModuleConstants:
    TESTNUMBER=''
    TESTTABLE_ITEM = '测试项目'
    TESTTABLE_COND = '测试条件'
    TESTTABLE_VALUE = '测试值'
    TESTTABLE_CONCLU = '测试结论'
    IP_SG = "192.168.1.141"
    IP_SA = "192.168.1.142"
    IP_NA = "192.168.1.143"
    IP_PM = "192.168.1.145"
    QMESSAGEBOX_WARN = '警告'
    QMESSAGEBOX_WARN_SELECTED_TEST = '请选择测试项目'
    QMESSAGEBOX_WARN_INPUT_PARAMETER_NOT_ENOUGH = '测试参数输入不完整或格式不正确'
    QMESSAGEBOX_WARN_IP_NOT_VALID = '输入IP地址有误'
    QMESSAGEBOX_WARN_INSTR_NOT_VALID = '仪表连接错误！'
    QMESSAGEBOX_INFO = '提示'
    QMESSAGEBOX_INFO_FREQ_SET = '请将被测设备发射频率设为'
    QMESSAGEBOX_CONTENTS_TEST_FINISH = '测试完成'
    QMESSAGEBOX_CONTENTS_TEST_NORMAL = '测试正常'
    QMESSAGEBOX_CONTENTS_TEST_ABNORMAL = '故障'
    WINDOW_TITLE_MAIN = '散射通信高频设备'
    TESTITEM_TR_T = '收发信机/发射单元'
    TESTITEM_TR_R = '收发信机/接收单元'
    TESTITEM_LNA = '低噪声放大器'
    TESTITEM_PA = '功放'
    TESTITEM_LOOP = '自环器'
    TESTITEM_FILTER = '滤波器'
    TESTITEM_SWITCH = '波导开关'
    TESTITEM_COUPLER = '耦合器'
    TESTITEM_MONITOR = '监控模块'
    TESTRESULT_PASS = 'PASS'
    TESTRESULT_FAIL = 'FAIL'
    TESTRESULT_MONITOR_V2_NORM = '监控供电正常'
    TESTRESULT_MONITOR_V2_ABNORM = '监控供电异常，需要排查监控+5V供电情况'
    TESTRESULT_MONITOR_V3_NORM = '监控单元程序运行正常'
    TESTRESULT_MONITOR_V3_ABNORM = '监控单元没有程序运行'
    TESTRESULT_MONITOR_V8_NORM = '物理连接正常'
    TESTRESULT_MONITOR_V8_ABNORM = '物理连接异常'
    TESTRESULT_MONITOR_V9_NORM = '100Mbps传输速率'
    TESTRESULT_MONITOR_V9_ABNORM = '10Mbps传输速率'
    TESTRESULT_MONITOR_V10_NORM = '全双工'
    TESTRESULT_MONITOR_V10_ABNORM = '半双工'
    TESTRESULT_MONITOR_V11_NORM = '数据冲突'
    TESTRESULT_MONITOR_V11_ABNORM = '数据正常'
    TESTRESULT_MONITOR_V12_NORM = '收数据正常'
    TESTRESULT_MONITOR_V12_ABNORM = '收数据异常'
    TESTRESULT_MONITOR_V13_NORM = '发数据正常'
    TESTRESULT_MONITOR_V13_ABNORM = '发数据异常'
    TESTCONDITION_FREQ = '频率:'
    TESTCONDITION_FREQ_UNIT = 'MHz'
    TESTCONDITION_BAND = '带宽:'
    TESTCONDITION_BAND_UNIT = 'MHz'
    TESTCONDITION_POWER = '功率:'
    TESTCONDITION_POWER_UNIT = 'dBm'
    PROCESS_CONTROL_NEXT = 'next'
    PROCESS_CONTROL_FINISH = 'finish'
    CONTENTS_NEXT = '下一步'
    CONTENTS_NOT = '不'
    CONTENTS_OVER = '测试结束'
    CONTENTS_YES = '是'
    CONTENTS_NO = '否'
    UDP_SEND_CONTENTS = 'test'
    BUTTON_CONTENTS_NEXT = '下一步'
    BUTTON_CONTENTS_FINISH = '测试结束'

    if SystemLanguage.LANGUAGE == SystemLanguage.fr_FR:
        tip = "rapide"
        t1 = "Le dispositif détecté surveille et reçoit les instructions du poste D 'essai"
        t2 = "l’unité de surveillance est normale"
        t3 = "l’unité de surveillance est en panne"

        # Test2.py
        qinwuhua = "EOW"
        qinwuhua_normal = "EOW est normal"
        qinwuhua_panne = "EOW est en panne"

        # Test11.py
        zihuanqi = "circulateur"
        zihuanqi_normal = "normale de circulaateur"
        zihuanqi_panne = "panne de circulaateur"
        test_all_normal = "Tous les tests sont normaux"

        # Test13.py
        pinpuyi = "spectographe"
        pinpuyi_normal = "spectographe est normale"
        shuanggong_panne = "il faut faire les étapes suivantes"

        # Ui_TEST1:
        anormal = "anormal"
        normal = "normal"
        send_frequence = "Fréquence d'émission"
        recivice_frequence = "Fréquence d'acceptation"
        next = "Suivant"

        # Ui_TEST11:
        shuchu_frequence = "Fréquence de sortie"
        shuchu_dianping = "Niveau de sortie"
        zhongxin_pinlv = "Fréquence centrale"
        cankao_dianping = "Niveau de référence"
        daikuan = "bande passante"

        # Ui_TEST12:
        qishi_pinlv = "Fréquence de départ"
        zhongzhi_pinlv = "Fréquence d'arrêt"
        saomiao_bujin = "Étape de numérisation"
        shuchu_gonglv = "Puissance de sortie"
    else:
        # Test1.py
        tip = "提示"
        t1 = "被测设备监控接收到测试分机指令"
        t2 = "监控单元正常"
        t3 = "监控单元故障"

        #Test2.py
        qinwuhua = "勤务话"
        qinwuhua_normal = "勤务话正常"
        qinwuhua_panne = "勤务话故障"

        #Test11.py
        zihuanqi = "自环器"
        zihuanqi_normal = "自环器正常"
        zihuanqi_panne = "自环器故障"
        test_all_normal = "测试值全部正常"

        #Test13.py
        pinpuyi = "频谱仪"
        pinpuyi_normal = "频谱仪正常"
        shuanggong_panne = "双工器故障"

        # Ui_TEST1:
        anormal = "不正常"
        normal = "正常"
        send_frequence = "发射频率"
        recivice_frequence = "接受频率"
        next = "下一步"

        # Ui_TEST11:
        shuchu_frequence = "输出频率"
        shuchu_dianping = "输出电平"
        zhongxin_pinlv = "中心频率"
        cankao_dianping = "参考电平"
        daikuan = "带宽"

        # Ui_TEST12:
        qishi_pinlv = "起始频率"
        zhongzhi_pinlv = "终止频率"
        saomiao_bujin = "扫描步进"
        shuchu_gonglv = "输出功率"

