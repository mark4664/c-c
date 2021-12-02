#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# client_subscribe_basic.py
# MGB 2/12/21
# This shows a simple example of an MQTT  client subscriber.

# Import paho MQTT library
import paho.mqtt.client as mqtt


# This is the callback function used when connecting to the broker
def on_connect(client,userdata,flags,rc):
    print("Connected with result code " + str(rc))
    # Subscribe to a topic
    client.subscribe(topic)

# This is the callback function used when a messages is received
def on_message(client,userdata, msg):
    
    print('Topic ',msg.topic,\n,
          'QOS ', str(msg.qos),\n
          'Message ',str(msg.payload.decode()))
    
# ------------------ Main ---------------------

client = mqtt.Client()   # Create an MQTT client 

client.on_connect = on_connect   # Assign the function to handle the connection
client.on_message = on_message   # Assign the function to handle incomming messages

# Connect to the broker
client.connect(broker, 1883, 60)

client.loop_forever() # Look for messages.

