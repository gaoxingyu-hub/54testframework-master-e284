from visa import *
import time
rm=ResourceManager('@py')
inst=rm.open_resource("TCPIP::192.168.1.222::INSTR")
print(inst.query("*IDN?"))
# inst.write("*RST")
# time.sleep(0.1)
# inst.write(":CHANNEL1:DISPLAY ON")
# inst.write(":CHANNEL2:DISPLAY ON")
# time.sleep(0.1)  
# inst.write(":TIMebase:SCALe 1e-8")
# time.sleep(0.1)
# 
# inst.write(":CHANnel1:SCALe 0.1")
# inst.write(":CHANnel1:SCALe 0.5")
# time.sleep(0.1)
# inst.write(":CHANnel1:OFFSet 0.1")
# inst.write(":CHANnel1:OFFSet 0.2")
# time.sleep(0.1)
# inst.write(":SINGle")


