#!/usr/bin/python
import mcpi.minecraft as minecraft
import pygame
pygame.init()
import mcpi.block as block
mc = minecraft.Minecraft.create()
from time import sleep
import opc
import time
import thread
found_lighthouses = 0
lighthouse = 0
lighthouses={}
lighthousered=0
lighthousegreen=0
lighthouseblue=0
woolcolours = ['red', 'green', 'blue']
numLEDs = 16
brightness = 256
pulse_time = 0.04
client = opc.Client('localhost:7890')
leds_forward=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
leds_foneback=(15,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)
leds_reverse=(8,9,10,11,12,13,14,15,0,1,2,3,4,5,6,7)
leds_roneback=(7,8,9,10,11,12,13,14,15,0,1,2,3,4,5,6)
pixels = [ (0,0,0) ] * numLEDs

##############################################################
# Balance board code 
# Initialize the joysticks
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
bb_pos={}
name = joystick.get_name()
print("Joystick name: {%s}" % name )
axes = joystick.get_numaxes()
print("Number of axes: {%s}" % axes )
# Average 8 year old
#calibration_factor = 1.02
# Average Adult
calibration_factor = 1.05
###############################################################
##### Make the game easier with high number_of_lighthouses_make
##### compared to number_of_lighthouses_find
number_of_lighthouses_find = 12
number_of_lighthouses_make = 30
map_sizea = 55 
map_sizeb = 192
fourthreethree = False
espeakEnabled=False
###############################################
###Uncomment if there is a 433 Transmitter
#from fourthreethree_transmitter.threeon import switch_socket
#fourthreethree = True
###############################################
###############################################
# To enable the game to speak to the player:
# $ sudo apt-get install python-espeak
# Then uncomment the following lines
from espeak import espeak
espeakEnabled=True
###############################################
import random
def create_lighthouse(x,z,colour):
    # Create a lighthouse at x,z 
    # Red = 14, Blue = 11, Green = 13
    if (colour == "red"):
       woolcolour = 14
    elif (colour == "blue"):
       woolcolour = 11
    elif (colour == "green"):
       woolcolour = 13
    else:
       woolcolour = 14
    height = mc.getHeight(x,z)
    mc.setBlock(x, height, z , block.WOOL.id, 0 )
    mc.setBlock(x, height+1, z , block.WOOL.id, woolcolour )
    mc.setBlock(x, height+2, z , block.WOOL.id, 0 )
    mc.setBlock(x, height+3, z , block.WOOL.id, woolcolour )
    mc.setBlock(x, height+4, z , 20 )
    return(x,height,z)

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
##############################################################
# Balance board code 


def light_lighthouse(colour,lighthousered,lighthousegreen,lighthouseblue):
    # Red = 14, Blue = 11, Green = 13
    if (colour == 11):
        lighthouseblue += 64
        if (lighthouseblue > 256):
            lighthouseblue = 256
    elif (colour == 13):
        lighthousegreen += 64
        if (lighthousegreen > 256):
            lighthousegreen = 256
    elif (colour == 14):
        lighthousered += 64
        if (lighthousered > 256):
            lighthousered = 256
    else:
        print ("No incoming colour")
    mc.postToChat("Current colour = %i,%i,%i " % (lighthousered, lighthousegreen, lighthouseblue))
    return (lighthousered,lighthousegreen, lighthouseblue)

def destroy_lighthouse(x,y,z):
    height = mc.getHeight(x,z)
    height = y
    mc.setBlocks(x, height, z ,x , height+4, z, block.AIR.id, 0 )
#    mc.postToChat("Cleaning up lighthouse %i %i %i" % (x,y,z))

if __name__ == "__main__":
        # Build initial set of lighthouses at random positions on the map
    while (lighthouse < number_of_lighthouses_make):
        xlighthouse=random.randint(-map_sizeb,map_sizea)
        zlighthouse=random.randint(-map_sizea,map_sizeb)
        random_colour=random.choice(woolcolours)
        lighthouses[lighthouse]=create_lighthouse(xlighthouse,zlighthouse,random_colour)
#        mc.postToChat("Created lighthouse %i" % lighthouse)
        lighthouse += 1
    mc.postToChat("Land on top of %i lighthouses!" % number_of_lighthouses_find)
    if espeakEnabled:
        espeak.synth("Ready.")
        sleep(1)
        espeak.synth("Steady.")
        sleep(1)
        espeak.synth("Go")
    # Main game starts here
    start_game = time.time()
    while (found_lighthouses < number_of_lighthouses_find):
        pos = mc.player.getTilePos()
        direction_of_travel = "stopped"
        events=pygame.event.get()
        for i in range( axes ):
            bb_pos[i] = float(joystick.get_axis(i))
        forwards_or_backwards = (bb_pos[2] + bb_pos[0])/(bb_pos[3] + bb_pos[1])
        left_or_right = (bb_pos[2] + bb_pos[3])/(bb_pos[0] + bb_pos[1])
        abs_fb = abs(forwards_or_backwards - 1.0)
        abs_lr = abs(left_or_right - 1.0)
        if abs_fb > abs_lr:
            print ("Mainly trying to move forward backwards")
            if forwards_or_backwards < 1.0/calibration_factor:
                direction_of_travel="Forwards"
                mc.player.setTilePos(pos.x,pos.y,pos.z+1)
            elif forwards_or_backwards > 1.0*calibration_factor:
                direction_of_travel="Backwards"
                mc.player.setTilePos(pos.x,pos.y,pos.z-1)
            else:
                direction_of_travel="Stopped"
        elif abs_fb < abs_lr:
            print ("Mainly trying to move Left Right")
            if left_or_right < 1.0/calibration_factor:
                direction_of_travel="Left"
                mc.player.setTilePos(pos.x+1,pos.y,pos.z)
            elif left_or_right > 1.0*calibration_factor:
                direction_of_travel="Right"
                mc.player.setTilePos(pos.x-1,pos.y,pos.z)
            else:
                direction_of_travel="Stopped"
        print (direction_of_travel)
        blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
        if (blockBelow == 20):
            block2Below = mc.getBlockWithData(pos.x, pos.y - 2, pos.z)
            # blockBelow player is Glass - we make it Gold when lit
            mc.setBlock(pos.x, pos.y - 1 , pos.z , 41 )
            mc.postToChat("On!")
            (lighthousered,lighthousegreen,lighthouseblue)=light_lighthouse(block2Below.data,lighthousered,lighthousegreen,lighthouseblue)
            colourtuple=(lighthousered,lighthousegreen,lighthouseblue)
            thread.start_new_thread(light_neopixelring,(colourtuple,2))
            if (fourthreethree):
                switch_socket('on')
                sleep(1)
                switch_socket('off')
            found_lighthouses += 1
            number_of_lighthouses_left = number_of_lighthouses_find - found_lighthouses
            mc.postToChat("Found %i lighthouses, %i to go" % (found_lighthouses,number_of_lighthouses_left))
            if espeakEnabled:
                espeak.synth(" %i to go" % number_of_lighthouses_left)
        else:
            sleep(0.01)
    end_game = time.time()
    elapsed = end_game - start_game 
    mc.postToChat("Found all lighthouses in %s seconds" % elapsed)
    light_neopixelring(colourtuple,20)
    for key in lighthouses:
        (lhx,lhy,lhz)=lighthouses[key]
        destroy_lighthouse(lhx,lhy,lhz)
    if espeakEnabled:
        sleep(1)
        espeak.synth("Found all lighthouses.")
    mc.postToChat("Removed all lighthouses")
    if (fourthreethree):
        switch_socket('off')
