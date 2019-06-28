#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pybleno import *
import sys
import signal
from LightService import *
import RPi.GPIO as gpio

def gpioSetup():
	#Set in numbering to Broadcom scheme
	gpio.setmode(gpio.BCM)

	#Set GPIO21 (pin 40) as an output pin
	gpio.setup(21, gpio.OUT)
	gpio.output(21, gpio.LOW)

bleno = Bleno()
primaryService = LightService()

def onStateChange(state):
	if (state == 'poweredOn'):
		print("bluetooth power on")
		bleno.startAdvertising('led service', ['FF10'])

bleno.on('stateChange', onStateChange)

def onAdvertisingStart(err):
	if not err:
		def on_setServiceError(error):
			print('setServices: %s' % ('error ' + error if error else 'success'))

		bleno.setServices([
			primaryService
		], on_setServiceError)
		print("start advertise")

bleno.on('advertisingStart', onAdvertisingStart)

gpioSetup()
bleno.start()
print("peripheral start")

print ('Hit <ENTER> to disconnect')

if (sys.version_info > (3, 0)):
	input()
else:
	raw_input()

bleno.stopAdvertising()
bleno.disconnect()
gpio.output(21, gpio.LOW)
gpio.cleanup()

print ('terminated.')
sys.exit(1)
