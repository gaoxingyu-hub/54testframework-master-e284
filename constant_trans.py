from common.info import SystemLanguage


class  TransConstants:
    if SystemLanguage.LANGUAGE == SystemLanguage.fr_FR:
        TESTNUMBER = ''
        TESTTABLE_ITEM = 'Elément de test'
        TESTTABLE_COND = 'Condition de test'
        TESTTABLE_VALUE = 'Valeur de test'
        TESTTABLE_CONCLU = 'Conclusion de test'
        QMESSAGEBOX_WARN = 'Alerte'
        QMESSAGEBOX_INFO = 'Remarque'
        QMESSAGEBOX_CONTENTS_TEST_FINISH = 'Achèvement de test'
        QMESSAGEBOX_CONTENTS_TEST_NORMAL = 'Test normal'
        QMESSAGEBOX_CONTENTS_TEST_ABNORMAL = 'Panne'
        TESTRESULT_PASS = 'PASS'
        TESTRESULT_FAIL = 'FAIL'

        TESTCONDITION_FREQ = 'Fréquence'
        TESTCONDITION_FREQ_UNIT = 'MHz'
        TESTCONDITION_BAND = 'Largezur de bande:'
        TESTCONDITION_BAND_UNIT = 'MHz'
        TESTCONDITION_POWER = 'Puissance:'
        TESTCONDITION_POWER_UNIT = 'dBm'
        PROCESS_CONTROL_NEXT = 'next'
        PROCESS_CONTROL_FINISH = 'finish'
        CONTENTS_NEXT = 'Étape suivante'
        CONTENTS_NOT = 'Non'
        CONTENTS_OVER = 'Fin de test'
        CONTENTS_YES = 'Oui'
        CONTENTS_NO = 'Non'
        UDP_SEND_CONTENTS = 'test'
        BUTTON_CONTENTS_NEXT = 'Étape suivante'
        BUTTON_CONTENTS_FINISH = 'Fin de test'

        about = "À propos"
        t_help = "Aide"

        test_resource = "Ressources de test"
        name = "Nom"
        type = "Type"
        id = "Numéro / type"
        number = "Quantité"

        test_item = 'Elément de test'
        test_condition = 'Condition de test'
        test_value = 'Valeur de test'
        test_conclusion = 'Conclusion de test'
        test_result = 'Résultats des essais'
        next = "Étape suivante"
        notes = "Notes"
        yes = "Oui"
        no = "Non"
        ip_address = "Adresse ip"
        tip_info = "Information de remarque"
        log = "Journal"
        send = "Envoyer"
        test_ip_address = "Adresse IP de test"
        test_port = "Interface"
        test_configuration = "Configuration de test"
        local_ip = "IP local"
        remote_ip = "IP à distance"
        link = "Connection"

        # 散射高频设备
        high_freq_name = "Haute fréquence troposphérique"
        high_freq_shoufa = "Unité de réception et d'émission "
        high_freq_zaosheng = "Amplificateur à bas bruit"
        high_freq_gongfang = "Amplificateur de puissance "
        high_freq_ouhe = "Coupleur "
        high_freq_zihuan = "Circulateur "
        high_freq_lvbo = "Filtre"
        high_freq_bodao = "Interrupteur de guide d'onde"
        high_freq_jiankong = "Module de surveillance"

        mw_com_xieyikongzhi = "Module de commande et de conversion de protocole"
        mw_com_xieyikongzhitest = "Transformation d’accord et test de contrôle"
        mw_com_test = "Équipement de transmission via Radio FH Ad hoc network"

        sdsl_test = "sdsl test"

        ip_protector = "Équipement de chiffrement IP"
        ip_bit_1 = "Interface 1 de testeur de taux d’erreur de bit IP"
        ip_bit_2 = "Interface 2 de testeur de taux d’erreur de bit IP"

        router_test_module = "Test de module de routeur"
        router = "routeur"

        module_test = "Test de module"

        test = "test"

        network_trans = "Test de version de transformation d’accord de réseau"

        # UI_MainWindow.py
        main_fkj = "FKJ Sous-système de maintenance des communications"
        main_test_module = "Module de test"
        main_tongxin = "Sous-système de communication"
        main_sanshe = "Haute fréquence troposphérique"
        main_mw1500 = "Équipement MW-1500"
        main_ecom1 = "Commutateur type I"
        main_ecom2 = "Commutateur type II"
        main_vhf = "Radio VHF"
        main_zizuwang = "Équipement de communication à micro-ondes auto-organisé"
        main_sdsl = "Équipement SDSL"
        main_ip = "Équipement de chiffrement IP"
        main_tongxin_control = "Équipement de contrôle de transmission"
        main_router = "Routeur"
        main_test_project = "Projet du test"
        previous = "Précédente"
        jiankongcscl = 'Stratégie de test de surveillance'
        qinwuhuacs = 'Stratégie de test de surveillance'
        shoufaxjnbdycs = 'Test d’unité intérieure du récepteur  et de l’émetteur'
        #mw1500
        fashe_frequency = 'fréquence d’émission'
        jieshou_frequency = 'fréquence de réception'
    else:
        TESTNUMBER = ''
        TESTTABLE_ITEM = '测试项目'
        TESTTABLE_COND = '测试条件'
        TESTTABLE_VALUE = '测试值'
        TESTTABLE_CONCLU = '测试结论'
        QMESSAGEBOX_WARN = '警告'
        QMESSAGEBOX_INFO = '提示'
        QMESSAGEBOX_CONTENTS_TEST_FINISH = '测试完成'
        QMESSAGEBOX_CONTENTS_TEST_NORMAL = '测试正常'
        QMESSAGEBOX_CONTENTS_TEST_ABNORMAL = '故障'
        TESTRESULT_PASS = 'PASS'
        TESTRESULT_FAIL = 'FAIL'
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
        remote_ip = "远程IP"
        about = "关于"
        t_help = "帮助"

        test_resource = "测试资源"
        name = "名称"
        type = "类型"
        id = "编号/型号"
        number = "数量"
        test_item = '测试项目'
        test_condition = '测试条件'
        test_value = '测试值'
        test_conclusion = '测试结论'
        test_result = "测试结果"
        next = "下一步"
        notes = "备注"
        yes = "是"
        no = "否"
        ip_address = "ip地址"
        tip_info = "提示信息"
        log = "日志"
        send = "发送"
        test_ip_address = "测试ip地址"
        test_port = "测试端口"
        test_configuration = "测试配置"
        local_ip = "本地ip"
        link = "连接"

        #散射高频设备
        high_freq_name = "散射高频设备"
        high_freq_shoufa = "收/发单元"
        high_freq_zaosheng = "低噪声放大器"
        high_freq_gongfang = "功放"
        high_freq_ouhe = "耦合器"
        high_freq_zihuan = "自环器"
        high_freq_lvbo = "滤波器"
        high_freq_bodao = "波导开关"
        high_freq_jiankong = "监控设备"

        # 自组网微波通信设备
        mw_com_xieyikongzhi = "协议控制和转换模块"
        mw_com_xieyikongzhitest = "协议转换与控制测试"
        mw_com_test = "自组网微博通信设备测试"

        sdsl_test = "sdsl测试"

        ip_protector = "ip保密机"
        ip_bit_1 = "ip误码仪端口1"
        ip_bit_2 = "ip误码仪端口2"

        router_test_module = "路由器模块测试"
        router = "路由器"

        module_test = "模块测试"

        test = "测试"

        network_trans = "网络协议转换板测试"

        # UI_MainWindow.py
        main_fkj = "FKJ通信维修分系统"
        main_test_module = "测试模块"
        main_tongxin = "通信分系统"
        main_sanshe = "散射高频设备"
        main_mw1500 = "MW-1500微波电台"
        main_ecom1 = "ECOM_NS_1型交换机"
        main_ecom2 = "ECOM_NS_2型交换机"
        main_vhf = "VHF电台"
        main_zizuwang = "自组网微波通信设备"
        main_sdsl = "SDSL设备"
        main_ip = "IP保密机"
        main_tongxin_control = "通信控制设备"
        main_router = "路由器"
        main_test_project = "测试项目"
        previous = "上一步"
        jiankongcscl='监控测试策略'
        qinwuhuacs='勤务话测试'
        shoufaxjnbdycs='收发信机内部单元测试'

        #mw1500
        fashe_frequency='发射频率'
        jieshou_frequency='接收频率'
