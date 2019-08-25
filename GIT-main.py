#!/usr/bin/env python

import RPi.GPIO as GPIO
import distance
import i2c_lcd1602
import time
import paho.mqtt.client as mqtt
#import 20180922mqtt-pub

screen = i2c_lcd1602.Screen(bus=1, addr=0x27, cols=16, rows=2)


broker_address = "test.mosquitto.org"
print("creating new instance")
client = mqtt.Client("pub5") #create new instance

print("connecting to broker")
client.connect(broker_address) #connect to broker

def destory():
	GPIO.cleanup()

def loop():
	while True:
		screen.cursorTo(0, 0)
		screen.println(line)
		t = distance.checkdist()
		t = round(t, 1)
		m = '%f' %t
		m = m[:5]
		screen.cursorTo(1, 0)
		screen.println(' Dist: ' + m + ' cm ')
		screen.clear()
		print 'Distance: ' + m + 'cm'
		client.publish("topic",m)#type the topic
		time.sleep(0.5)      

if __name__ == '__main__':
	print 'SummerMealTime'
	line = " SummerMealTime "
	screen.enable_backlight()
	screen.clear()
	try:
		distance.setup()
		loop()
	except KeyboardInterrupt:
		destory()
