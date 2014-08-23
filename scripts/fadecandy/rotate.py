#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time

numLEDs = 16
brightness = 256
pulse_time = 4
# Bright white
standard_brightness=(brightness,brightness,((3*brightness)/4))
# Yellow
standard_brightness=(brightness,brightness,((brightness)/2))
client = opc.Client('localhost:7890')
leds_forward=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
leds_foneback=(15,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)
leds_reverse=(8,9,10,11,12,13,14,15,0,1,2,3,4,5,6,7)
leds_roneback=(7,8,9,10,11,12,13,14,15,0,1,2,3,4,5,6)
pixels = [ (0,0,0) ] * numLEDs

while True:
   for i in range(numLEDs):
      pixels[leds_forward[i]] = standard_brightness
      pixels[leds_reverse[i]] = standard_brightness
      pixels[leds_foneback[i]] = (0,0,0)
      pixels[leds_roneback[i]] = (0,0,0)
      client.put_pixels(pixels)
      time.sleep(pulse_time)
