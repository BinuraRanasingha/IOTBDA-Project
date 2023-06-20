import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import json

# Set the MQTT broker and topic

MQTT_BROKER = "broker.hivemq.com"

MQTT_TOPIC = "PDAControl"
GPIO.setmode(GPIO.BCM)

sensor = Adafruit_DHT.DHT11
pin = 21

# Create an MQTT client object
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(MQTT_BROKER, 1883)
 

try:
    
    while True:
        # Read data from sensor
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

 

        # Print data to console
        if humidity is not None and temperature is not None:
            print(f'Temperature={temperature}*C  Humidity={humidity}%')
            # Create a dictionary to hold the humidity value
            
            payload = {
                            "humidity": round(humidity, 1)
                      }
            client.publish(MQTT_TOPIC, json.dumps(payload))

        else:
            print('Failed to read data from sensor')
 
 
        time.sleep(1)

except RuntimeError as e:
        print("Failed to retrieve data from DHT11 sensor:", e)
        
# Disconnect from the MQTT broker
client.disconnect()

