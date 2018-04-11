import time
import requests
import grovepi
import sys

# A0
# SIG,NC,VCC,GND
air_sensor = 0
ultrasonic_ranger = 4
temp_sensor = 1
light_sensor = 2

url = "http://RossMacbookPro.local:3000"

while True:
    try:
        # Air Sensor
        sensor_value = grovepi.analogRead(air_sensor)
        if sensor_value <= 291:
            air_quality = 'good'
        else:
            air_quality = 'bad'

        print(sensor_value)
        print(air_quality)
        
        # Distance Sensor
        dist_value = grovepi.ultrasonicRead(ultrasonic_ranger)

        print(dist_value)
        
        # Temperature and Humidity Sensor
        
        temp_value = grovepi.temp(temp_sensor, '1.1')
        print("temp =", temp_value)
        
        # Light Sensor
        
        light_value = grovepi.analogRead(light_sensor)
        print("light_value = %d" %(light_value))
        
        # Broadcast Payload
        payload = { 'airQuality' : air_quality, 'airValue' : sensor_value, 'distance' : dist_value, 'tempValue' : temp_value, 'lightValue' : light_value}

        requests.post(url, data=payload)

        time.sleep(.5)

    # Errors
    
    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")
