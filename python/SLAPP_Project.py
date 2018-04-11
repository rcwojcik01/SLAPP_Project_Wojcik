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
        sensor_value = grovepi.analogRead(air_sensor)
        if sensor_value <= 291:
            air_quality = 'good'
        else:
            air_quality = 'bad'

        print(sensor_value)
        print(air_quality)

        dist_value = grovepi.ultrasonicRead(ultrasonic_ranger)

        print(dist_value)

        payload = { 'airQuality' : air_quality, 'airValue' : sensor_value, 'distance' : dist_value}

        requests.post(url, data=payload)

        time.sleep(.5)

    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")
