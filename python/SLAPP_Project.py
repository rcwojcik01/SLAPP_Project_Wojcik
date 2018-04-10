import time
import requests
import grovepi
import sys

# A0
# SIG,NC,VCC,GND
air_sensor = 0
ultrasonic_ranger = 4

url = "http://RossMacbookPro.local:3000"

while True:
    try:
        if grovepi.analogRead(air_sensor)<= 40:
            sensor_value = 'good'
        else:
            sensor_value = 'bad'

        print(sensor_value)

        dist_value = grovepi.ultrasonicRead(ultrasonic_ranger)

        print(dist_value)

        payload = { 'airQuality' : sensor_value, 'distance' : ultrasonic_ranger}

        requests.post(url, data=payload)

        time.sleep(0.1)

    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")
