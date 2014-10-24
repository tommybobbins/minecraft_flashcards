import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
import math
pi = math.pi
exp = math.exp
x = pos.x
y = pos.y
z = pos.z
tower_width=20
internal_width=3
last_stage = 0
tower_height=50 # Should be 159m, but mcpi max height is 50 blocks.
height = mc.getHeight(x,z)
maximum_block_height = 0
height = 0

def create_air(x,y,z):
    mc.setBlocks(x-5*tower_width, y, z+5*tower_width , x+5*tower_width, y+tower_height+20, z-5*tower_width, block.AIR )

create_air(x,height,z) # Clear some space

#####Create square around the outside#############
#####Needs tidying to two concentric##############
#####squares######################################
mc.setBlocks(x+tower_width,height,z+tower_width,x+tower_width,height,z-tower_width,112)
mc.setBlocks(x-tower_width,height,z+tower_width,x-tower_width,height,z-tower_width,112)
mc.setBlocks(x+tower_width,height,z+tower_width,x-tower_width,height,z+tower_width,112)
mc.setBlocks(x+tower_width,height,z-tower_width,x-tower_width,height,z-tower_width,112)

##### Make the X
for i in range(internal_width,tower_width):
    try:
        block_height =  tower_height/i
        if (block_height > maximum_block_height):
            maximum_block_height = block_height
    except:
        block_height = tower_height
    mc.setBlock(x+i,height,z+i,112)
    mc.setBlocks(x+i,block_height,z+i, x+i, block_height - 1, z+i, block.WOOL.id, 4)
    mc.setBlock(x-i,height,z+i,112)
    mc.setBlocks(x-i,block_height,z+i, x-i, block_height - 1, z+i, block.WOOL.id, 4)
    mc.setBlock(x+i,height,z-i,112)
    mc.setBlocks(x+i,block_height,z-i, x+i, block_height - 1, z-i, block.WOOL.id, 4)
    mc.setBlock(x-i,height,z-i,112)
    mc.setBlocks(x-i,block_height,z-i, x-i, block_height - 1, z-i, block.WOOL.id, 4)


mc.setBlocks(x-internal_width,maximum_block_height,z-internal_width, x+internal_width, tower_height, z+internal_width, block.WOOL.id, 5)
mc.player.setTilePos(x,tower_height+1,z)
