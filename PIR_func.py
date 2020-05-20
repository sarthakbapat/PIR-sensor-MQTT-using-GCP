import RPi.GPIO as GPIO
import time

#Set GPIO 17 to get input to Pi from PIRs output.
#Set GPIO 27 for external LED when Pi receives a signal on its pin.
PIR_OUT = 17 
LED = 27

#Function to initialize the GPIOs.
#PIR_OUT --> Input pin.
#LED --> Output pin.
def GPIO_init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_OUT, GPIO.IN)
    GPIO.setup(LED, GPIO.OUT)

#Function to return the sensor data.
def sensor_data():
    sense = GPIO.input(PIR_OUT)

    try:
        if sense == 1:
            GPIO.output(LED,1)
            print('Sensor is sensing: {} \n'.format(sense))
            time.sleep(2)

        elif sense == 0:
            GPIO.output(LED,0)
            print('Sensor is not sensing: {}\n'.format(sense))
            time.sleep(2)
            
        return sense

    except:
        GPIO.cleanup()
        return -1
    
