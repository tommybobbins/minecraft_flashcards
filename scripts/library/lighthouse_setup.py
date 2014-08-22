#!/usr/bin/python
colourmap = {14 : "red", 13 : "green", 11 : "blue", 1: "orange", 4 : "yellow", 15 : "white" }
from piglow import PiGlow
piglow = PiGlow()
piglow.all(0)
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
    from piglow import PiGlow
    piglow = PiGlow()
    piglow.all(0)
    if ( colour != "all" ):
        ledcolour = colourmap[colour]
    intensity = 0
    for j in range(rotations):
#        print ("Rotating %i " % j)
        if (colour == "all"):
#            print ("Trying to run piglow.arm bit %i " % intensity)
            piglow.arm(1,intensity) 
            piglow.arm(3,0) 
            sleep(0.01)
            piglow.arm(2,intensity) 
            piglow.arm(1,0) 
            sleep(0.01)
            piglow.arm(3,intensity) 
            piglow.arm(2,0) 
            sleep(0.01)
        else:
            piglow.colour(ledcolour,intensity)            # Control the top arm (with PiGlow logo at the top)
#            print("j= %i " % j)            # Control the top arm (with PiGlow logo at the top)
            sleep(0.01)
        intensity += 1 
    piglow.all(0)
