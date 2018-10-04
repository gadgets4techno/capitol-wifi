#!/usr/bin/python
# -*- coding: utf-8 -*-

# MQTT extended library

# Import necessary libraries
import paho.mqtt.client as mqtt
from time import sleep as sleep

#MQTT Protocol configuation
server = "test.mosquitto.org"
server_port = 1883
clientid = "ibm_cloud"
password = "ibm_cloud_pass"
server_sub_topic = "/discord"
server_qos = 0
client = mqtt.Client(clientid)

# Define necessary variables
connected = False
payload = None

# Connect to the broker
def init():
 global connected
 m = ""
 try:
  client.on_message = on_message
  client.on_publish = on_publish
  client.on_disconnect = on_disconnect
  client.on_connect = on_connect
#  client.message_callback_add(discovery_topic, add_system)
#  client.connect(server)
  connect()
  client.loop_start()
  connected = True
 except Exception as m:
  connected = False
  print("init(): " + str(m))

def send(str = None):	#publishes provided message to pre-defined topic
 client.publish(server_sub_topic, str)

def connect():	#connects to broker
 client.connect(server)
def disconnect():	#disconnects from broker
 client.disconnect()

def close():	#function to facilitate terminating broker connection
# client.unsubscribe()
 client.disconnect()
 client.loop_stop()

def check():	#function to ensure broker connectivity
 global connected
 if (not connected):
  client.disconnect()
  sleep(1)
  client.connect(server, port=server_port)
  connected = True
  print("MQTT connected...")
 else:
  return True

# Callback functions
def on_message(client, userdata, message):	#do smth when message
 global payload
 payload = str(message.payload.decode("utf-8"))

def on_publish(client, userdata, mid):	#do smth when publishing message
# print("Result: " + str(userdata) + "," + str(mid))
 m=1

def on_disconnect(client, userdata, rc=0):	#do smth when disconnecting from broker
 print("Disconnected result code "+str(rc))
 global connected
 connected = False

def on_connect(client, userdata, flags, rc):	#do smth when connecting to broker
 global connected
 if (rc == 0):
  print("connected OK Returned code = " + str(rc))
  client.subscribe(server_sub_topic, qos = 0)
  connected = True
 else:
  print("Bad connection Returned code = " + str(rc))
  connected = False


