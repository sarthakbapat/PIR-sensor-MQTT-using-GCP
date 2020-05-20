import paho.mqtt.client as mqtt
import os
import time
import datetime
import PIR_func

#MQTT broker is the Google cloud VM instance.
#The ip address would change for every new start of the VM instance.
broker = "34.67.68.193"

#Default MQTT port number is 1883.
port = 1883

#MQTT topic for publish
topic = "test"

def on_publish(client, userdata, result):
    print ("Published data is: ")
    pass

client = mqtt.Client("cli")
client.on_publish = on_publish
client.connect(broker,port,keepalive = 60)

#Initialize the GPIOs using the function in PIR_func.py file
PIR_func.GPIO_init()

while(1):
    #Get the sensor data using the function in PIR_func.py file.
    sensed_op = PIR_func.sensor_data()
    payload = "{"
    payload += "Sensor data is: "+ str(sensed_op)
    payload += "}"
    
    #Publish the data on the defined topic.
    ret = client.publish(topic,payload)
    print (payload)
    print ('Check the data on the subscriber code\n')
    time.sleep(2)
    