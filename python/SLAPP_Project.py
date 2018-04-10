

import time
import requests
import grovepi
import sys

# A0
# SIG,NC,VCC,GND
air_sensor = 0

url = "http://RossMacbookPro.local:3000"

while True:
    try:
        sensor_value = grovepi.analogRead(air_sensor)

        print(sensor_value)

        payload = { 'airQuality' : sensor_value }

        requests.post(url, data=payload)

        time.sleep(0.1)

    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")
