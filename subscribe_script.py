import paho.mqtt.client as mqtt
import time
import sys
import datetime

#The broker resides on the Google cloud VM instance.
broker = "34.67.68.193"
#Default port for MQTT is 1883.
port = 1883
#Subscribing on the topic test.
topic = "test"

#Callback to display the received data on subscription.
def on_message(client, userdata, message):
	print ("Received data is: ")
	print (str(message.payload.decode("utf-8")))
	print ("----------------------------------")

client = mqtt.Client("sarthak")
client.on_message = on_message

print ("Connecting to broker host: {}".format(broker))
print (" On topic {}".format(topic))
client.connect(broker,port)
print ("Waiting for data---")
client.subscribe(topic)

#Continuously check for messages.
while (1):
	client.loop_start()
