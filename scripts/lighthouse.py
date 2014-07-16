#!/usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
from time import sleep
import time
found_lighthouses = 0
lighthouse = 0
number_of_lighthouses = 10
###############################################
###Enable if there is a 433 Transmitter
#import threeon
#from threeon import switch_socket
fourthreethree = False
###############################################
import random
def create_lighthouse(x,z):
    height = mc.getHeight(x,z)
    mc.setBlock(x, height, z , block.WOOL.id, 0 )
    mc.setBlock(x, height+1, z , block.WOOL.id, 14 )
    mc.setBlock(x, height+2, z , block.WOOL.id, 0 )
    mc.setBlock(x, height+3, z , block.WOOL.id, 14 )
    mc.setBlock(x, height+4, z , 57 )

if __name__ == "__main__":
    try: 
        while (lighthouse < number_of_lighthouses):
            xlighthouse=random.randint(-126,126)
            zlighthouse=random.randint(-126,126)
            create_lighthouse(xlighthouse,zlighthouse)
            mc.postToChat("Created lighthouse %i" % lighthouse)
            lighthouse += 1
    except (KeyboardInterrupt, SystemExit):
        exit()
    try: 
        mc.postToChat("Land on top of the lighthouses!")
        start_game = time.time()
        while (found_lighthouses < number_of_lighthouses):
            pos = mc.player.getTilePos()
            blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
            if (blockBelow == 57):
                # blockBelow player is Diamond 
                mc.setBlock(pos.x, pos.y - 1 , pos.z , 41 )
                mc.postToChat("On!")
                if (fourthreethree):
                    switch_socket('on')
                found_lighthouses += 1
                mc.postToChat("Found %i lighthouses" % found_lighthouses)
                sleep(1)
                if (fourthreethree):
                    switch_socket('off')
            else:
                sleep(0.5)
    except (KeyboardInterrupt, SystemExit):
        exit()
    end_game = time.time()
    elapsed = end_game - start_game 
    mc.postToChat("Found all lighthouses in %s seconds" % elapsed)
    if (fourthreethree):
        switch_socket('off')
