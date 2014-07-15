#!/usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import threeon
from time import sleep
from threeon import switch_socket
mc = minecraft.Minecraft.create()
mc.postToChat("Step on the Gold block")
while True:
    pos = mc.player.getTilePos()
    blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if (blockBelow == 41):
#       print ("Block Below is %s" % blockBelow)
        switch_socket()
        mc.postToChat("Timeout!")
        sleep(10)
        mc.postToChat("Step on the Gold block")
    else:
       sleep(0.1)
