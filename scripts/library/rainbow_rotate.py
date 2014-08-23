#!/usr/bin/env python

def rainbow_rotate(rotations):
    # Light each LED in sequence, and repeat.
    import opc, time
    numLEDs = 16
    client = opc.Client('localhost:7890')
    pixels = [ (0,0,0) ] * numLEDs
    rainbow = { "red":(255,0,0), "orange":(255,127,0), "yellow":(255,255,0), "green":(0,255,0), "blue":(0,0,255), "indigo":(75,0,130), "violet":(143,0,255), "white":(255,255,255) } 
    for j in range(rotations):
       for colour in ("red","orange","yellow","green","blue","indigo","violet","white"):
#           print ("%s %s " % (colour, rainbow[colour]))
           for i in range(numLEDs):
               pixels[i] = rainbow[colour]
               client.put_pixels(pixels)
               time.sleep(0.04)
    pixels = [ (0,0,0) ] * numLEDs
    client.put_pixels(pixels)


if __name__ == "__main__":
       rainbow_rotate(3) 
