import mcpi.minecraft as minecraft
import mcpi.block as block
import math
mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
a = 4 
b = 15 
pi = math.pi
theta = 0
height = 3
while theta <= (2*pi):
    x = round(a * (math.cos(theta)),0)
    z = round(b * (math.sin(theta)),0)
    mc.setBlocks(pos.x + x , pos.y , pos.z + z, pos.x - x, pos.y + height, pos.z - z , 5)   
    mc.setBlocks(pos.x + x - 1 , pos.y + 1, pos.z + z, pos.x - x + 1, pos.y + height + 1, pos.z - z , 0)    
#        print ("%i %i" % (x,z))
    
    theta += (pi/32)
mc.setBlocks(pos.x + (a/2) , pos.y + height , pos.z + (b - 1), pos.x - (a/2), pos.y + (height + 3), pos.z + (b/2) , 5)    

#### BOW SPIRIT #####################################
mc.setBlocks(pos.x , pos.y + height , pos.z - b , pos.x, pos.y + height, pos.z - b - 10  , 5)    

#### MAST############################################
mc.setBlocks(pos.x , pos.y , pos.z + 1, pos.x, pos.y + (height + 15), pos.z + 1 , 5)    
mc.setBlocks(pos.x - 5 , pos.y + height + 12 , pos.z + 1, pos.x + 5, pos.y + height + 12, pos.z + 1 , 5)    

#### SAIL############################################
mc.setBlocks(pos.x - 5 , pos.y + 4 , pos.z , pos.x - 5, pos.y + (height + 12), pos.z , 35,0)    
mc.setBlocks(pos.x - 4 , pos.y + 4 , pos.z , pos.x - 4, pos.y + (height + 12), pos.z , 35,14)    
mc.setBlocks(pos.x - 3 , pos.y + 4 , pos.z , pos.x - 3, pos.y + (height + 12), pos.z , 35,0)    
mc.setBlocks(pos.x - 2 , pos.y + 4 , pos.z , pos.x - 2, pos.y + (height + 12), pos.z , 35,14)    
mc.setBlocks(pos.x - 1 , pos.y + 4 , pos.z , pos.x - 1, pos.y + (height + 12), pos.z , 35,0)    
mc.setBlocks(pos.x - 0 , pos.y + 4 , pos.z , pos.x - 0, pos.y + (height + 12), pos.z , 35,14)    
mc.setBlocks(pos.x + 1 , pos.y + 4 , pos.z , pos.x + 1, pos.y + (height + 12), pos.z , 35,0)    
mc.setBlocks(pos.x + 2 , pos.y + 4 , pos.z , pos.x + 2, pos.y + (height + 12), pos.z , 35,14)    
mc.setBlocks(pos.x + 3 , pos.y + 4 , pos.z , pos.x + 3, pos.y + (height + 12), pos.z , 35,0)    
mc.setBlocks(pos.x + 4 , pos.y + 4 , pos.z , pos.x + 4, pos.y + (height + 12), pos.z , 35,14)    
mc.setBlocks(pos.x + 5 , pos.y + 4 , pos.z , pos.x + 5, pos.y + (height + 12), pos.z , 35,0)    
mc.player.setPos(pos.x , pos.y + height + 5, pos.z + 2 )    
