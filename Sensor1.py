import datetime
from subprocess import Popen

f = open("Output/temp2.txt","a")
now = datetime.datetime.now()
now = str(now)
f.write(now + ', ')

tfile = open("/sys/bus/w1/devices/28-000004abecbf/w1_slave")
text = tfile.read()
tfile.close()
temperature_data = text.split()[-1]
temperature = fload(temperature_data[2:])
temperature = temperature / 1000
temperature = temperature*1.8+32
print temperature
f.write(str(temperature)+', ')

f.write('\n')