#!/usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import pygame
pygame.init()
from piglow import PiGlow
piglow = PiGlow()
piglow.all(0)
mc = minecraft.Minecraft.create()
from time import sleep
import time
import thread
found_lighthouses = 0
lighthouse = 0
lighthouses={}
lighthousered=0
lighthousegreen=0
lighthouseblue=0
colourtuple=(lighthousered,lighthousegreen,lighthouseblue)
woolcolours = ['red', 'green', 'blue']
numLEDs = 16
brightness = 256
pulse_time = 0.4
#piglow.all(0)
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
###############################################################
##### Make the game easier with high number_of_lighthouses_make
##### compared to number_of_lighthouses_find
number_of_lighthouses_find = 12
number_of_lighthouses_make = 16
map_sizea = 55 
map_sizeb = 100
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

def light_piglow(colours,rotations):
    for j in range(rotations):
        print ("Rotating %i " % j)
        piglow.arm(1,255)            # Control the top arm (with PiGlow logo at the top)
        time.sleep(pulse_time)
        piglow.all(0)
        piglow.arm(2,255)            # Control the right arm (with PiGlow logo at the top)
        time.sleep(pulse_time)
        piglow.all(0)
        piglow.arm(3,255)            # Control the left arm (with PiGlow logo at the top)
        time.sleep(pulse_time)
        piglow.all(0)
##############################################################

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
            # blockBelow player is Glass - we make it Gold when lit
            mc.setBlock(pos.x, pos.y - 1 , pos.z , 41 )
            mc.postToChat("On!")
            thread.start_new_thread(light_piglow,(colourtuple,2))
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
    light_piglow(colourtuple,20)
    for key in lighthouses:
        (lhx,lhy,lhz)=lighthouses[key]
        destroy_lighthouse(lhx,lhy,lhz)
    if espeakEnabled:
        sleep(1)
        espeak.synth("Found all lighthouses.")
    mc.postToChat("Removed all lighthouses")
    if (fourthreethree):
        switch_socket('off')
