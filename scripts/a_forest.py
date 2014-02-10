import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
import random
number_trees = 0
max_trees = 20

def makeTree(x,z):
    y = mc.getHeight(x,z)
    mc.setBlock(x,y-1,z,block.GRASS.id)
    mc.setBlocks(x,y,z,x,y+3,z,block.WOOD.id,2)
    mc.setBlocks(x-2,y+4,z-2,x+2,y+5,z+2,block.LEAVES.id,3)
    mc.setBlocks(x-1,y+6,z-1,x+1,y+7,z+1,block.LEAVES.id,3)
    mc.setBlock(x-1,y+7,z-1,block.AIR.id)
    mc.setBlock(x+2,y+5,z-2,block.AIR.id)
    mc.setBlock(x+2,y+4,z+2,block.AIR.id)
    mc.setBlocks(x+1,y+6,z-1,x+1,y+7,z-1,block.AIR.id)
    mc.setBlocks(x+1,y+6,z+1,x+1,y+7,z+1,block.AIR.id)
    mc.setBlocks(x-1,y+6,z+1,x-1,y+7,z+1,block.AIR.id)

# Main body
pos = mc.player.getPos()
x = pos.x
z = pos.z

while number_trees < max_trees:
    x = pos.x + random.randint((-1 * max_trees),max_trees )
    z = pos.z + random.randint(-1 * max_trees,max_trees)
    makeTree(x,z)
    number_trees += 1

