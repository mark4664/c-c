#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# client_publish_basic.py
# MGB 2/12/21
# This shows a simple example of an MQTT  client publisher.

# Import paho MQTT library
import paho.mqtt.publish as publish

topic='skiddawu3a'
broker='test.mosquitto.org'


publish.single(topic, "Message to subscriber", hostname=broker)

#message=input('Enter a message :')
#publish.single('skiddawu3a', message, hostname=broker)

