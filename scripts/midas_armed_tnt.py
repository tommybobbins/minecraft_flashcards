import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
from time import sleep
water = 9 # Declare a variable
air = 0 # Declare a variable
while True:
    pos = mc.player.getTilePos()
    blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if blockBelow != air and blockBelow != water:
        mc.setBlock(pos.x, pos.y - 1, pos.z, block.TNT.id,1)
    else:
        mc.postToChat("Not placing block. Over water or air")
        sleep(1)
    sleep(0.1)

