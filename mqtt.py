import Adafruit_DHT
import json
import paho.mqtt.client as mqtt

 

    # Set the MQTT broker and topic

 

MQTT_BROKER = "broker.hivemq.com"

 

MQTT_TOPIC = "PDAControl"

 

 # Set the pin that the DHT11 sensor is connected to
DHT_PIN = 21

 

 # Create an MQTT client object
client = mqtt.Client()

 

 # Connect to the MQTT broker
client.connect(MQTT_BROKER, 1883)

 

# Read the humidity from the DHT11 sensor
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_PIN)

 

 # Create a dictionary to hold the humidity value
data = {"humidity": humidity}

 

 # Convert the dictionary to a JSON string
json_data = json.dumps(data)

 

 # Publish the JSON string to the MQTT broker
client.publish(MQTT_TOPIC, json_data)

 

 # Disconnect from the MQTT broker
client.disconnect()