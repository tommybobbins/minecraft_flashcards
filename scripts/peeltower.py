#!/usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
from time import sleep
import thread
import time
###############################################
import random
def create_peelt(x,z):
    # Create a lighthouse at x,z
    y1 = mc.getHeight(x,z)
    y1 = 0
    y2 = y1 + 8 # Height of base
    y3 = y2 + 21 # Height of tower
    base_width=12
    tower_width=4
    mc.setBlocks(x, y1, z, x + base_width , y2, z + base_width, block.MOSS_STONE)
    mc.setBlocks(x + 1, y1, z + 1, x + base_width - 1 , y2 - 1, z + base_width -1, 0)
    mc.setBlocks(x + ((base_width-tower_width)/2), y2, z + ((base_width-tower_width)/2), x + tower_width + ((base_width-tower_width)/2) , y3, z + ((base_width-tower_width)/2) + tower_width, block.STONE_SLAB_DOUBLE)
    mc.setBlocks(x + ((base_width-tower_width)/2) + 1, y2, z + ((base_width-tower_width)/2) + 1, x + tower_width + ((base_width-tower_width)/2) -1 , y3 - 1, z + ((base_width-tower_width)/2) + tower_width -1, 0)
#    mc.setBlocks(x + (base_width/2) + 1, y2, z + (base_width/2) +1, x + tower_width + (base_width/2) -1 , y3, z + (base_width/2) + tower_width -1, 0)
    mc.setBlock(x + ((base_width - tower_width)/2) + 1, y1, z + ((base_width - tower_width)/2) +1, block.DOOR_WOOD)
    mc.setBlock(x, y1 + 1, z + ((base_width - tower_width)/2) +1, block.DOOR_WOOD)
    mc.setBlock(x, y1 + 2, z + ((base_width - tower_width)/2) +1, block.DOOR_WOOD)

    mc.setBlocks(x + ((base_width-tower_width)/2), y2 + 2, z + ((base_width - tower_width)/2) +1, x + ((base_width-tower_width)/2), y2 + 3, z + ((base_width - tower_width)/2) +2, block.GLASS)



    mc.setBlocks(x + ((base_width-tower_width)/2), 0, z + ((base_width-tower_width)/2), x + tower_width + ((base_width-tower_width)/2) , y2 - 1, z + ((base_width-tower_width)/2) + tower_width, block.TNT.id,1)
    

if __name__ == "__main__":
    mc.postToChat("Creating Peel Tower power")
    pos = mc.player.getPos()
    create_peelt(pos.x + 10 ,pos.z + 10)
