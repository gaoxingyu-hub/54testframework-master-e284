from common.info import SystemLanguage


class ModuleConstants:
    if SystemLanguage.LANGUAGE == SystemLanguage.fr_FR:
        QMESSAGEBOX_WARN = "Alerte"
        QMESSAGEBOX_INFO = 'Remarque '
        QMESSAGEBOX_WARN_SELECTED_TEST = "Sélectionnez l’élement de test"
        QMESSAGEBOX_WARN_INPUT_PARAMETER_NOT_ENOUGH = "L’entrée des paramètres de test est imcomplète ou le format est incorrect."
        QMESSAGEBOX_WARN_IP_NOT_VALID = "Erreur d’entrée d’adresse IP"
        QMESSAGEBOX_CONTENTS_TEST_FINISH = "Achèvement de test"
        WINDOW_TITLE_MAIN = "ECOM_NS_1 test"
        PROCESS_CONTROL_NEXT = "next"
        PROCESS_CONTROL_FINISH = "finish"
        CONTENTS_NEXT = "Étape suivante"
        CONTENTS_NOT = "'Non"
        CONTENTS_OVER = "Fin de test"
        CONTENTS_YES = "Oui"
        CONTENTS_NO = "'Non"
        UDP_SEND_CONTENTS = "test"
        next= "Étape suivante"
        BUTTON_CONTENTS_FINISH = "Fin de test"
        QMESSAGEBOX_CONTENTS_TEST_ABNORMAL = 'Panne'
        VHF_radio_PowerSource= "courant de la radio VHF"
        Synthesize_Service_module="Module de services intégrés"

        VHF_radio = "la radio VHF"
        VHF_POWER_PANNEL ="Panne de courant de la radio VHF"
        system_load = "Le système est-il chargé avec succès"
        ssm_pannel = "Panne du module d’intégration des services"
        tip = "rapide"
        mianban_caozuo = "Vérifiez si le fonctionnement du panneau est normal"
        two_radio_yuyin = "Exécutez l'appel vocal entre deux stations de radio"

        # TEST7.py
        test_shoubing_qingxi = "Écoutez si le combiné peut produire une tonalité unique claire"
        shoubing_yes = "Oui"
        shoubing_no = "Non"

        # TEST7point2.py
        chezaitonglu_pannel = "La connexion de réception de l'adaptateur à bord est défectueuse"
        tiaoxie_pannel = "Panne du module de syntonisation"

        # TEST7point5.py
        test_shoufa_light = "Observez les changements des voyants de réception et d'émission sur le panneau"
        audio_module_pannel = "Panne du module audio"
        test_tested_radio = "Si la tonalité latérale peut être entendue lors de l'utilisation de la radio testée"
        zhongpin_module_pannel = "Panne du module IF"
        tested_radio_ceyin = "Tonalité latérale de la radio testée"

        # TEST10point2_1
        chezai_small_pannel = "la connexion d'émission à faible puissance de l'adaptateur à bord est défectueuse"
        ditong_5w_pannel = "Panne du filtre passe-bas 5W"

        # TEST10point6_2.py
        pinhe_5w_pannel =" le module de synthétiseur de fréquence est déterminé défectueux, le module d'amplification de puissance 5W est déterminé défectueux"
        gongfang_5w_pannel = "le module d'amplification de puissance 5W est déterminé défectueux"
        ditong_50w_pannel = " il est déterminé que le module passe-bas de 50 W est défectueux"
        gongfang_50w_pannel = "Panne du module d'amplificateur de puissance 50 W"

        # TEST5.py
        diantaifa_30025 = "Mesurez si la fonction d'émission à faible puissance de 55 MHz de la radio est normale"
        frequence = "la fréquence:"
        fuzhi = "Amplitude"
        diantaifa_30025_pass = "Mesure de la fonction basse puissance 30,025 MHz de la station radio"
        diantaifa_30025_pannel = "Mesure de la fonction basse puissance 30,025 MHz de la station radio"

        # TEST9.py
        diantai_xiao = "Mesure de l'émetteur de faible puissance"
        gongneng = "Fonction qualifiée"
        gongneng_pannel = "Panne de fonction"
        tongxin_xiao = "Mesure de la transmission à faible puissance de l'hôte de communication"
        tongxin_zhong = "Mesurer la puissance de l'hôte de communication"
        diantai_zhong = "Mesurer la puissance de la radio"
        vhf_zhong = "Mesurer la puissance de la radio VHF"
        diantai_da = "Mesure de la radio haute puissance"
        gongneng_ = "Fonctions"

        # Ui_TEST6.py
        tiaozhi_fangshi = "le mode de modulation"
        tiaozhi_xinhao = "le signal de modulation est"
        xinhao_fudu = "et l'amplitude du signal est"
        pinpian = "l'écart de fréquence est"
        shiliangxinhaofashengqi ='Générateur de signaux vectoriels Keysight'
        warning='Alerte'
        #
        test_radio_xiaoXGLF55MHz = "Mesurez si la fonction d'émission de faible puissance de 55 MHz de la radio est normale"
        test_radio_xiaoXGLF87MHz = "Mesurez si la fonction d'émission à faible puissance de 87.975 MHz de la radio est normale"
        test_radio_zhongZGLF30MHz = "Mesurez si la fonction d'émission à moyenne puissance de 30.025 MHz de la radio VHF est normale"
        test_radio_daDGLF30MHz = "Mesurez si la fonction d'émission à haute puissance de 30.025 MHz de la radio VHF est normale"
        test_tongxinzhuji_XGLF = "Vérifiez si l'émission à faible puissance de l'unité principale de transmission est normale"
        test_tongxinzhuji_XGLF_30 = "Mesurez si l' émission à faible puissance de 30.025MHz de l'unité principale de transmission est normale'"
        test_tongxinzhuji_XGLF_87 = "'Mesurez si l'émission à faible puissance de 87.975MHz de l'unité principale de transmission est normale'"
        test_tongxinzhuji_ZGLF_87 = "Mesurez si l'émission à moyenne puissance de 87.975MHz de l'unité principale de transmission est normale."
    else:
        QMESSAGEBOX_WARN = "警告"
        QMESSAGEBOX_INFO = '提示'
        QMESSAGEBOX_WARN_SELECTED_TEST = "请选择测试项目"
        QMESSAGEBOX_WARN_INPUT_PARAMETER_NOT_ENOUGH = "测试参数输入不完整"
        QMESSAGEBOX_WARN_IP_NOT_VALID = "输入IP地址有误"
        QMESSAGEBOX_CONTENTS_TEST_FINISH = "测试完成"
        WINDOW_TITLE_MAIN = "ECOM_NS_1交换机测试"
        PROCESS_CONTROL_NEXT = "next"
        PROCESS_CONTROL_FINISH = "finish"
        CONTENTS_NEXT = "下一步"
        CONTENTS_NOT = "不"
        CONTENTS_OVER = "测试结束"
        CONTENTS_YES = "是"
        CONTENTS_NO = "否"
        UDP_SEND_CONTENTS = "test"
        next = "下一步"
        BUTTON_CONTENTS_FINISH = "测试结束"
        QMESSAGEBOX_CONTENTS_TEST_ABNORMAL = '故障'
        VHF_radio_PowerSource = "VHF电台电源"
        Synthesize_Service_module = "综合业务模块"

        VHF_radio = "VHF电台"
        VHF_POWER_PANNEL = "VHF电台电源故障"
        system_load = "系统是否加载成功"
        ssm_pannel = "综合业务模块故障"
        tip = "提示"
        mianban_caozuo = "观察面板操作是否正常"
        two_radio_yuyin = "操作两部电台之间进行语音通话"

        # TEST7.py
        test_shoubing_qingxi = "听手柄能否输出清晰单音"
        shoubing_yes = "是"
        shoubing_no = "否"

        # TEST7point2.py
        chezaitonglu_pannel = "车载适配器收通路故障"
        tiaoxie_pannel = "调谐模块故障"

        # TEST7point5.py
        test_shoufa_light = "观察面板收发指示灯的变化"
        audio_module_pannel = "音频模块故障"
        test_tested_radio = "操作被测电台通话时是否能够听到侧音"
        zhongpin_module_pannel = "中频模块故障"
        tested_radio_ceyin = "被测电台通话时的侧音"

        # TEST10point2_1
        chezai_small_pannel = "车载适配器小功率发射通路故障"
        ditong_5w_pannel = "5W低通滤波器故障"

        # TEST10point6_2.py
        pinhe_5w_pannel = '判定频和模块故障,判定5W功放模块故障'
        gongfang_5w_pannel = "判定5W功放模块故障"
        ditong_50w_pannel = "判定50W低通模块故障"
        gongfang_50w_pannel = "50W功放模块故障"


        # TEST5.py
        diantaifa_30025 = "测量电台小功率发30.025MHz功能是否正常"
        frequence = "频率:"
        fuzhi = "幅值"
        diantaifa_30025_pass = "测量电台小功率发30.025MHz功能合格"
        diantaifa_30025_pannel = "测量电台小功率发30.025MHz功能不合格"

        # TEST9.py
        diantai_xiao = "测量电台小功率发"
        gongneng = "功能合格"
        gongneng_pannel = "功能不合格"
        tongxin_xiao = "测量通信主机小功率发"
        tongxin_zhong = "测量通信主机中功率发"
        diantai_zhong = "测量电台中功率发"
        vhf_zhong = "测量VHF电台中功率发"
        diantai_da = "测量电台大功率发"
        gongneng_ = "功能"

        #Ui_TEST6.py
        tiaozhi_fangshi = "调制方式"
        tiaozhi_xinhao = "调制信号"
        xinhao_fudu = "信号幅度"
        pinpian = "频偏"

        shiliangxinhaofashengqi='矢量信号发生器'
        warning='警告'
        #
        test_radio_xiaoXGLF55MHz="测量电台小功率发55MHz功能是否正常"
        test_radio_xiaoXGLF87MHz = "测量电台小功率发87.975MHz功能是否正常"
        test_radio_zhongZGLF30MHz = "测量VHF电台中功率发30.025MHz功能是否正常"
        test_radio_daDGLF30MHz = "测量VHF电台大功率发30.025MHz功能是否正常"
        test_tongxinzhuji_XGLF='测试通信主机小功率发是否正常'
        test_tongxinzhuji_XGLF_30 = '测量通信主机小功率发30.025MHz是否正常'
        test_tongxinzhuji_XGLF_87 = '测量通信主机小功率发87.975MHz是否正常'
        test_tongxinzhuji_ZGLF_87 = '测量通信主机中功率发87.975MHz是否正常'







