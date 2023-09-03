# Worry about overheating your hardware?
# 
# Forget about it! Now your hardware will know, when to shutdown! 
# Especially useful with broken cooler or something like that...
# 
# 
# Do not forget to run Open Hardware Monitor, otherwise code below won't work.
# just make exe, then task scheduler... 
# 
# 
# I have X570 chipset, so other ways (like pyspectator) did not work for me. And psutil is for Linux...

import os
import wmi
import time

def shutdown():
    return os.system("shutdown /s /t 1")
def get_cpu_temperature():
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")

    temperature_infos = w.Sensor()
    names=[]
    temps=[]

    # Credit to: https://stackoverflow.com/questions/3262603/accessing-cpu-temperature-in-python
    for sensor in temperature_infos:   

        if sensor.SensorType==u'Temperature':

            names.append(sensor.Name)

            temps.append(float(sensor.Value))
    index=0
    for i in range(len(names)):
        if names[i]=="CPU Package":
            index=i
            break

    cpu_temperature=temps[index]
        
    return cpu_temperature

while True:
    time.sleep(2)
    temp = get_cpu_temperature()
    if temp>=70:
        shutdown()
