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




def make_pirate_ship(a,b,height):
    import math
    pos = mc.player.getPos()
    a = 4 
    b = 15 
    height = 3
    pi = math.pi
    theta = 0
    while theta <= (2*pi):
        x = round(a * (math.cos(theta)),0)
        z = round(b * (math.sin(theta)),0)
    #   Oak planks to build body of ship around elipse
        mc.setBlocks(pos.x + x , pos.y , pos.z + z, pos.x - x, pos.y + height, pos.z - z , 5)   
    #   Fences around the outside
        mc.setBlocks(pos.x + x , pos.y + height + 1, pos.z + z, pos.x - x, pos.y + height + 1, pos.z - z , 85)    
    #   Hollow out the inside of the boat
        mc.setBlocks(pos.x + x - 1 , pos.y + 1, pos.z + z, pos.x - x + 1, pos.y + height + 1, pos.z - z , 0)    
    #        print ("%i %i" % (x,z))
    
        theta += (pi/32)

    #

    #### CAPTAINS CABIN##################################
    # Main box
    mc.setBlocks(pos.x + (a/2) , pos.y + height , pos.z + (b - 1), pos.x - (a/2), pos.y + (height + 4), pos.z + (b/2) , 5)    
    # Air box inside
    mc.setBlocks(pos.x + (a/2) - 1 , pos.y + height + 1  , pos.z + (b - 2), pos.x - (a/2) + 1, pos.y + (height + 3), pos.z + ((b/2) - 2) , 0)    
    # Aft section
    mc.setBlocks(pos.x + (a - 1) , pos.y + height , pos.z + (b - 1), pos.x - (a - 1), pos.y + height, pos.z + (b - ((3*b)/4)) , 5)    
    # Forecastle
    mc.setBlocks(pos.x + (a - 2) , pos.y + height , pos.z - (b - 1), pos.x - (a - 2), pos.y + height, pos.z - (b - ((1*b)/2)) , 5)    
    # Doors windows etc
    # Glass
    mc.setBlocks(pos.x + (a/2 - 1),pos.y + height + 1, pos.z + (b/2), pos.x - (a/2 - 1), pos.y + height +3, pos.z + (b/2), 5 ) 
    mc.setBlocks(pos.x + (a/2 - 1),pos.y + height + 2, pos.z + (b/2), pos.x - (a/2 - 1), pos.y + height +2, pos.z + (b/2), 20 ) 
    # Door
    mc.setBlocks(pos.x,pos.y + height + 1, pos.z + (b/2),pos.x,pos.y + height + 2, pos.z + (b/2), 0 ) 
    mc.setBlock(pos.x,pos.y + height + 1, pos.z + (b/2), 64 ) 
    mc.setBlock(pos.x,pos.y + height + 2, pos.z + (b/2), 64 ) 
    # Nether reactor used to detect when player is in ship
    mc.setBlock(pos.x,pos.y + height, pos.z + (b/2) + 2, 247 ) 

    #### BOW SPIRIT #####################################
    mc.setBlocks(pos.x , pos.y + height , pos.z - b , pos.x, pos.y + height, pos.z - b - 5  , 5)    

    #### PLUG HOLE AT FRONT AND BACK
    mc.setBlocks(pos.x , pos.y , pos.z - b , pos.x, pos.y + 3, pos.z - b  , 5)    
    mc.setBlocks(pos.x , pos.y - 1 , pos.z + b , pos.x, pos.y + 3, pos.z + b  , 5)    


    #### MAST############################################
    mc.setBlocks(pos.x , pos.y , pos.z + 1, pos.x, pos.y + (height + 17), pos.z + 1 , 5)    
    mc.setBlocks(pos.x - 5 , pos.y + height + 12 , pos.z + 1, pos.x + 5, pos.y + height + 12, pos.z + 1 , 5) 

    #### FLAG############################################   
    mc.setBlocks(pos.x, pos.y + height + 13, pos.z + 6, pos.x, pos.y + height + 17, pos.z + 2 , 35,15)    
    # Skull and crossbones
    mc.setBlock(pos.x, pos.y + height + 16, pos.z + 3 , 35,0)    
    mc.setBlock(pos.x, pos.y + height + 16, pos.z + 4 , 35,0)    
    mc.setBlock(pos.x, pos.y + height + 16, pos.z + 5 , 35,0)    
    mc.setBlock(pos.x, pos.y + height + 15, pos.z + 3 , 35,0)    
    mc.setBlock(pos.x, pos.y + height + 15, pos.z + 5 , 35,0)    
    mc.setBlock(pos.x, pos.y + height + 14, pos.z + 4 , 35,0)    
    mc.setBlock(pos.x, pos.y + height + 13, pos.z + 3 , 35,0)    
    mc.setBlock(pos.x, pos.y + height + 13, pos.z + 5 , 35,0)    

    #### SAIL############################################
    mc.setBlocks(pos.x - 5 , pos.y + height + 2, pos.z , pos.x - 5, pos.y + (height + 12), pos.z , 35,0)    
    mc.setBlocks(pos.x - 4 , pos.y + height + 2, pos.z , pos.x - 4, pos.y + (height + 12), pos.z , 35,14)    
    mc.setBlocks(pos.x - 3 , pos.y + height + 2, pos.z , pos.x - 3, pos.y + (height + 12), pos.z , 35,0)    
    mc.setBlocks(pos.x - 2 , pos.y + height + 2, pos.z , pos.x - 2, pos.y + (height + 12), pos.z , 35,14)    
    mc.setBlocks(pos.x - 1 , pos.y + height + 2, pos.z , pos.x - 1, pos.y + (height + 12), pos.z , 35,0)    
    mc.setBlocks(pos.x - 0 , pos.y + height + 2, pos.z , pos.x - 0, pos.y + (height + 12), pos.z , 35,14)    
    mc.setBlocks(pos.x + 1 , pos.y + height + 2, pos.z , pos.x + 1, pos.y + (height + 12), pos.z , 35,0)    
    mc.setBlocks(pos.x + 2 , pos.y + height + 2, pos.z , pos.x + 2, pos.y + (height + 12), pos.z , 35,14)    
    mc.setBlocks(pos.x + 3 , pos.y + height + 2, pos.z , pos.x + 3, pos.y + (height + 12), pos.z , 35,0)    
    mc.setBlocks(pos.x + 4 , pos.y + height + 2, pos.z , pos.x + 4, pos.y + (height + 12), pos.z , 35,14)    
    mc.setBlocks(pos.x + 5 , pos.y + height + 2, pos.z , pos.x + 5, pos.y + (height + 12), pos.z , 35,0)    
    mc.player.setPos(pos.x,pos.y + height + 1, pos.z + (b/2) + 2, 247 ) 
    pos = mc.player.getPos()
    return (pos.x, pos.y, pos.z)
