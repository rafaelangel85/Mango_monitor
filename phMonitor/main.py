'''
Created on 26 jun. 2019

@author: jrangel
'''

import time
import read_ph
import read_rasp_temp


#Wait at least 60seconds so the rasp can connect to the Wifi

time.sleep(60)

# Run until you get a ctrl^c
try:
    while True:
        read_ph .   getMangoHumidity()
        read_rasp_temp      .   getRaspTemp()
except KeyboardInterrupt:
    pass
