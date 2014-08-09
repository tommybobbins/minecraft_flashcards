#!/usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
from time import sleep
import time
found_lighthouses = 0
lighthouse = 0
##### Make the game easier with high number_of_lighthouses_make
##### compared to number_of_lighthouses_find
number_of_lighthouses_find = 10
number_of_lighthouses_make = 30
fourthreethree = False
###############################################
###Uncomment if there is a 433 Transmitter
#from fourthreethree_transmitter.threeon import switch_socket
#fourthreethree = True
###############################################
import random
def create_lighthouse(x,z):
    # Create a lighthouse at x,z 
    height = mc.getHeight(x,z)
    mc.setBlock(x, height, z , block.WOOL.id, 0 )
    mc.setBlock(x, height+1, z , block.WOOL.id, 14 )
    mc.setBlock(x, height+2, z , block.WOOL.id, 0 )
    mc.setBlock(x, height+3, z , block.WOOL.id, 14 )
    mc.setBlock(x, height+4, z , 20 )

if __name__ == "__main__":
        # Build initial set of lighthouses at random positions on the map
    while (lighthouse < number_of_lighthouses_make):
        xlighthouse=random.randint(-126,126)
        zlighthouse=random.randint(-126,126)
        create_lighthouse(xlighthouse,zlighthouse)
        mc.postToChat("Created lighthouse %i" % lighthouse)
        lighthouse += 1
    mc.postToChat("Land on top of %i lighthouses!" % number_of_lighthouses_find)
    # Main game starts here
    start_game = time.time()
    while (found_lighthouses < number_of_lighthouses_find):
        pos = mc.player.getTilePos()
        blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
        if (blockBelow == 20):
            # blockBelow player is Glass - we make it Gold when lit
            mc.setBlock(pos.x, pos.y - 1 , pos.z , 41 )
            mc.postToChat("On!")
            if (fourthreethree):
                switch_socket('on')
                sleep(1)
                switch_socket('off')
            found_lighthouses += 1
            number_of_lighthouses_left = number_of_lighthouses_find - found_lighthouses
            mc.postToChat("Found %i lighthouses, %i to go" % (found_lighthouses,number_of_lighthouses_left))
        else:
            sleep(0.5)
    end_game = time.time()
    elapsed = end_game - start_game 
    mc.postToChat("Found all lighthouses in %s seconds" % elapsed)
    if (fourthreethree):
        switch_socket('off')
