#!/usr/bin/python
colourmap = {14 : "red", 13 : "green", 11 : "blue", 1: "orange", 4 : "yellow", 15 : "white" }
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
from time import sleep

def create_lighthouse(x,z,colour):
    # Create a lighthouse at x,z 
    # Red = 14, Blue = 11, Green = 13
    try: 
        woolcolour = colour
    except:
        woolcolour = 14
    height = mc.getHeight(x,z)
    mc.setBlock(x, height, z , block.WOOL.id, 0 )
    mc.setBlock(x, height+1, z , block.WOOL.id, woolcolour )
    mc.setBlock(x, height+2, z , block.WOOL.id, 0 )
    mc.setBlock(x, height+3, z , block.WOOL.id, woolcolour )
    mc.setBlock(x, height+4, z , 20 )
    return(x,height,z)
##############################################################
def destroy_lighthouse(x,y,z):
    height = mc.getHeight(x,z)
    height = y
    mc.setBlocks(x, height, z ,x , height+4, z, block.AIR.id, 0 )
#    mc.postToChat("Cleaning up lighthouse %i %i %i" % (x,y,z))


def light_piglow(colour,rotations):
    colourmap = {14 : "red", 13 : "green", 11 : "blue", 1: "orange", 4 : "yellow", 15 : "white" }
    from piglow import PiGlow
    piglow = PiGlow()
#    piglow.all(0)
    if ( colour != "all" ):
        ledcolour = colourmap[colour]
        for j in range(rotations):
            piglow.colour(ledcolour,j) 
            sleep(0.001*j) # As the intensity increases, sleep for longer periods
    else:
    #    print ("Trying to run all ")
        for j in range(rotations):
            for colour in (colourmap.values()):
                piglow.colour(("%s" % colour), 255)
                sleep(0.2) 
                piglow.colour(colour, 0)
                sleep(0.01)
    piglow.all(0)
