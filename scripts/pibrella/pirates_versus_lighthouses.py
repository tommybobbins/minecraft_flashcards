#!/usr/bin/python
import sys
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
from time import sleep
import time
from math import sqrt
found_lighthouses = 0
lighthouse = 0
lighthouses = {}
(shipx,shipy,shipz) = 0,0,0
colourmap = {14 : "red", 13 : "green", 11 : "blue", 1: "orange", 4 : "yellow", 15 : "white" }
##### Make the game easier with high number_of_lighthouses_make
##### compared to number_of_lighthouses_find
number_of_lighthouses_find = 10
number_of_lighthouses_make = 30
pibrella_enabled = False
espeakEnabled=False
sys.path.append("/home/pi/minecraft_flashcards/scripts/library/")
from lighthouse_setup import create_lighthouse,destroy_lighthouse,make_pirate_ship
###############################################
# To enable the game to speak to the player:
# $ sudo apt-get install python-espeak
# Then uncomment the following lines
#from espeak import espeak
#espeakEnabled=True
###############################################
###############################################
###Uncomment if there is a Pibrella
### $ sudo apt-get install python-pip
### $ sudo pip install pibrella
import pibrella
pibrella_enabled = True
###############################################
import random


def make_it_dark():
######35 is Wool###############
    mc.setBlocks(-125,40,-125,125,41,125,35, 0)
def make_it_light():
######Get rid of Wool##########
    mc.setBlocks(-125,40,-125,125,41,125,0, 0)

def plant_booty(x,z):
    # Create a set of treasure chests at x,z
    height = mc.getHeight(x,z)
    mc.setBlocks(x-5, height, z-5,x+5, height +90 , z+5 , 0 )
    mc.setBlocks(x-3, height-1, z-3,x+3, height -1 , z+3 , 48 )
    mc.setBlocks(x-5, height, z-3,x+5, height , z+8 , 12 )
    mc.setBlocks(x-1, height+1, z-1,x+1, height +1, z+1 , 74 )
    mc.setBlocks(x-1, height+2, z-1,x+1, height +2, z+1 , 89 )
    mc.setBlocks(x-1, height+3, z-1,x+1, height +3, z+1 , 54 )
    return (x,height,z)

def remove_booty(x,z):
    height = mc.getHeight(x,z)
    mc.setBlocks(x-3, height-1, z-3,x+3, height +5 , z+3 , 0 )
    return (x,height,z)

def run_game():
    found_lighthouses = 0
    toldtoPressTNT = False
    indeepwater = False
    mc.postToChat("Find deep water and push the blue button" )
    lighthouse = 0
    # Build initial set of lighthouses at random positions on the map
    while (indeepwater == False):
        if pibrella.button.read() == 1:
            # Check squares below player
            pos = mc.player.getTilePos()
            blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
            block2Below = mc.getBlock(pos.x, pos.y - 2, pos.z)
            # If we are on at least two blocks deep water
            if (blockBelow == 9) and (block2Below == 9):
                (shipx,shipy,shipz)=make_pirate_ship(4,15,3)
                indeepwater = True
            # Or we are on a pre-existing pirate ship 
            elif (blockBelow == 247):
                indeepwater = True
                (shipx,shipy,shipz) = (pos.x,pos.y,pos.z)
            else:
                mc.postToChat("Block below = %i, %i" % (blockBelow, block2Below))
                mc.postToChat("Find deep water and push the button" )

    while (lighthouse < number_of_lighthouses_make):
        xlighthouse=random.randint(-110,110)
        zlighthouse=random.randint(-110,110)
        random_colour=random.choice(colourmap.keys())
        lighthouses[lighthouse]=create_lighthouse(xlighthouse,zlighthouse,random_colour)
        (currx,curry,currz) = lighthouses[lighthouse]
        mc.setBlock(currx, curry+4, currz , 41 )
        #print ("%i %i %i" % (x,y,z) )
        #        mc.postToChat("Created lighthouse %i" % lighthouse)
        lighthouse += 1
    #    make_it_dark()
    #    mc.postToChat("Making it dark....")
    xbooty=random.randint(-50,50)
    ybooty=random.randint(-50,50)
    (bootyx,bootyy,bootyz)=plant_booty(xbooty,ybooty)
    #

    mc.postToChat("Plant TNT on top of %i lighthouses!" % number_of_lighthouses_find)
    # Main game starts here
    start_game = time.time()
    while (found_lighthouses < number_of_lighthouses_find):
        if (pibrella_enabled):
            if (found_lighthouses >= number_of_lighthouses_find):
                pibrella.light.all.on()
            elif (found_lighthouses > 7):
                pibrella.light.red.on()
                pibrella.light.amber.on()
                pibrella.light.green.pulse(0.5,0.5,2,2)
            elif (found_lighthouses > 4):
                pibrella.light.red.on()
                pibrella.light.amber.pulse(0.5,0.5,2,2)
            elif (found_lighthouses > 1):
                pibrella.light.red.pulse(0.5,0.5,2,2)
            else:
                pibrella.light.off()
            frequency = 1.0+(0.25 * (found_lighthouses))
            pibrella.buzzer.buzz(frequency)
        pos = mc.player.getTilePos()
        blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
        if (blockBelow == 41):
            if (toldtoPressTNT == False):
                mc.postToChat("Press button to plant TNT!")
                toldtoPressTNT = True
            landed_on_lighthouse=True
            # blockBelow player is Gold - we make it TNT
            if pibrella.button.read() == 1:
                mc.setBlock(pos.x, pos.y-1, pos.z, block.TNT.id,1)
                found_lighthouses += 1
                number_of_lighthouses_left = number_of_lighthouses_find - found_lighthouses
                mc.postToChat("Found %i lighthouses, %i to go" % (found_lighthouses,number_of_lighthouses_left))
                toldtoPressTNT = False
                if espeakEnabled:
                    espeak.synth("%i to go" % number_of_lighthouses_left)
        else:
            sleep(0.01)
    bootyAvailable = True
    mc.postToChat("Find the booty me hearty")
    pibrella.light.off()
    mc.postToChat("When the three lanterns be lit, ")
    mc.postToChat("near to the treasure ye sit, ")
    mc.postToChat("the tick-tocker stops it... ")
    toldToLandBooty=False
    while (bootyAvailable == True):
        pos = mc.player.getTilePos()
        blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
        distance_to_booty = sqrt((pos.x - bootyx)**2 + (pos.y - bootyy)**2 + (pos.z - bootyz)**2)
        pibrella.buzzer.buzz((distance_to_booty+1.0)/10)
        if (distance_to_booty > 200):
            pibrella.light.off()
        elif (distance_to_booty > 100):
            pibrella.light.red.on()
            pibrella.light.amber.off()
            pibrella.light.green.off()
        elif (distance_to_booty >= 50):
            pibrella.light.red.on()
            pibrella.light.amber.on()
            pibrella.light.green.off()
        elif (distance_to_booty > 0):
            pibrella.light.red.on()
            pibrella.light.green.on()
            pibrella.light.amber.on()
            if (toldToLandBooty == False):
                mc.postToChat("Land on the booty. ")
                toldToLandBooty = True
        #mc.postToChat("Distance to booty = %f " % distance_to_booty)
        if (blockBelow == 54):
            mc.postToChat("Found the booty")
            mc.postToChat("YOHOHO")
            bootyAvailable = False
    remove_booty(xbooty,ybooty)
    mc.postToChat("Now back to the ship")
    netherAvailable = True
    toldToLandNether=False
    while (netherAvailable == True):
        pos = mc.player.getTilePos()
        blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
        distance_to_ship = sqrt((pos.x - shipx)**2 + (pos.y - shipy)**2 + (pos.z - shipz)**2)
        pibrella.buzzer.buzz((distance_to_ship+1.0)/10)
        if (distance_to_ship > 200):
            pibrella.light.off()
        elif (distance_to_ship > 100):
            pibrella.light.red.on()
            pibrella.light.amber.off()
            pibrella.light.green.off()
        elif (distance_to_ship >= 50):
            pibrella.light.red.on()
            pibrella.light.amber.on()
            pibrella.light.green.off()
        elif (distance_to_ship > 0):
            pibrella.light.red.on()
            pibrella.light.green.on()
            pibrella.light.amber.on()
            if (toldToLandNether == False):
                mc.postToChat("Go into The Captain's Cabin.")
                toldToLandNether = True
        #mc.postToChat("Distance to booty = %f " % distance_to_booty)
        if (blockBelow == 247):
            mc.postToChat("You won me hearty")
            mc.postToChat("YOHOHO")
            netherAvailable = False
    end_game = time.time()
    elapsed = end_game - start_game
    if pibrella_enabled:
        pibrella.buzzer.off()
        pibrella.buzzer.success()
        pibrella.buzzer.off()
    mc.postToChat("Completed game in %s seconds" % elapsed)
    for key in lighthouses:
        (lhx,lhy,lhz)=lighthouses[key]
        destroy_lighthouse(lhx,lhy,lhz)
    #     make_it_light()
    if espeakEnabled:
        espeak.synth("Found all lighthouses.")

if __name__ == "__main__":
    mc.postToChat("----HELP THE PIRATES----")
    mc.postToChat("Destroy 10 lighthouses, then find the booty ")
    run_game()
