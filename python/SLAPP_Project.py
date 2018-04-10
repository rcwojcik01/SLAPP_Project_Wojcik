import time
import requests
import grovepi
import sys

# A0
# SIG,NC,VCC,GND
air_sensor = 0
dist_sensor = 4

url = "http://10.10.90.78:3000"

while True:
    try:
        if grovepi.analogRead(air_sensor) <= 500:
            sensor_value = 'Good'
        else:
            sensor_value = 'Bad'
            
        
    #    dist_value = grovepi.analogRead(dist_sensor)

     #   print(sensor_value)

        payload = { 'airQuality' : sensor_value}

        requests.post(url, data=payload)

        time.sleep(1)

    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")
