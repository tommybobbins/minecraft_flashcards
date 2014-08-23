#!/usr/bin/python
import sys
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
from time import sleep
import time
import thread
found_lighthouses = 0
lighthouse = 0
lighthouses={}
colourmap = {14 : "red", 13 : "green", 11 : "blue" }
lighthousered=0
lighthousegreen=0
lighthouseblue=0
sys.path.append("/home/pi/minecraft_flashcards/scripts/library/")
from lighthouse_setup import create_lighthouse,destroy_lighthouse
from fadecandy import rainbow_rotate, light_neopixelring

###############################################################
##### Make the game easier with high number_of_lighthouses_make
##### compared to number_of_lighthouses_find
number_of_lighthouses_find = 12
number_of_lighthouses_make = 24
map_sizea = 55 
map_sizeb = 100
espeakEnabled=False
###############################################
# To enable the game to speak to the player:
# $ sudo apt-get install python-espeak
# Then uncomment the following lines
from espeak import espeak
espeakEnabled=True
###############################################
import random


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

if __name__ == "__main__":
        # Build initial set of lighthouses at random positions on the map
    while (lighthouse < number_of_lighthouses_make):
        xlighthouse=random.randint(-map_sizeb,map_sizea)
        zlighthouse=random.randint(-map_sizea,map_sizeb)
        random_colour=random.choice(colourmap.keys())
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
        blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
        if (blockBelow == 20):
            block2Below = mc.getBlockWithData(pos.x, pos.y - 2, pos.z)
            # blockBelow player is Glass - we make it Gold when lit
            mc.setBlock(pos.x, pos.y - 1 , pos.z , 41 )
            mc.postToChat("On!")
            (lighthousered,lighthousegreen,lighthouseblue)=light_lighthouse(block2Below.data,lighthousered,lighthousegreen,lighthouseblue)
            colourtuple=(lighthousered,lighthousegreen,lighthouseblue)
            thread.start_new_thread(light_neopixelring,(colourtuple,2))
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
    rainbow_rotate(5)
    for key in lighthouses:
        (lhx,lhy,lhz)=lighthouses[key]
        destroy_lighthouse(lhx,lhy,lhz)
    if espeakEnabled:
        sleep(1)
        espeak.synth("Found all lighthouses.")
    mc.postToChat("Removed all lighthouses")
