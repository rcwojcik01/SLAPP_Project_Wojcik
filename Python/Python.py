import time
import requests
import grovepi
import sys

# A0
# SIG,NC,VCC,GND
air_sensor = 0
ultrasonic_ranger = 4
dht11_port = 8
light_sensor = 3

url = "http://RossMacbookPro.local:3000"

while True:
    try:
        # Air Sensor
        sensor_value = grovepi.analogRead(air_sensor)
        if sensor_value <= 300:
            air_quality = 'good'
        else:
            air_quality = 'bad'

        print('Air Sensor Value',sensor_value)
        print('Air Quality',air_quality)
        
        # Distance Sensor
        dist_value = grovepi.ultrasonicRead(ultrasonic_ranger)

        print('Distance',dist_value)

        # Temperature and Humidity Sensor
        
        [temp, humi] = grovepi.dht(dht11_port, 0)
        print(temp, "C")
        print(humi, "%")
        
        # Light Sensor
        
        light_value = grovepi.analogRead(light_sensor)
        print("light_value = %d" %(light_value))

        print("Done")
        
        # Broadcast Payload
        payload = { 'airQuality' : air_quality, 'airValue' : sensor_value, 'distance' : dist_value, 'humi' : humi, 'temp' : temp, 'lightValue' : light_value}

        requests.post(url, data=payload)

        time.sleep(1)

    # Errors
    
    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")
