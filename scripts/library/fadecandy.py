#!/usr/bin/env python
numLEDs = 16
import opc, time
client = opc.Client('localhost:7890')
pixels = [ (0,0,0) ] * numLEDs
numLEDs = 16
brightness = 256
pulse_time = 0.04
leds_forward=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
leds_foneback=(15,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)
leds_reverse=(8,9,10,11,12,13,14,15,0,1,2,3,4,5,6,7)
leds_roneback=(7,8,9,10,11,12,13,14,15,0,1,2,3,4,5,6)
pixels = [ (0,0,0) ] * numLEDs

def rainbow_rotate(rotations):
    # Light each LED in sequence, and repeat.
    rainbow = { "red":(255,0,0), "orange":(255,127,0), "yellow":(255,255,0), "green":(0,255,0), "blue":(0,0,255), "indigo":(75,0,130), "violet":(143,0,255), "white":(255,255,255), "black":(0,0,0) } 
    for j in range(rotations):
       for colour in ("red","orange","yellow","green","blue","indigo","violet","white","black"):
#           print ("%s %s " % (colour, rainbow[colour]))
           for i in range(numLEDs):
               pixels[i] = rainbow[colour]
               client.put_pixels(pixels)
               time.sleep(0.04)

def light_neopixelring(colours,rotations):
    pixels = [ (0,0,0) ] * numLEDs
    client.put_pixels(pixels)
    for j in range(rotations):
        for i in range(numLEDs):
           pixels[leds_forward[i]] = colours
           pixels[leds_reverse[i]] = colours
           pixels[leds_foneback[i]] = (0,0,0)
           pixels[leds_roneback[i]] = (0,0,0)
           client.put_pixels(pixels)
           time.sleep(pulse_time)

if __name__ == "__main__":
       rainbow_rotate(3) 
