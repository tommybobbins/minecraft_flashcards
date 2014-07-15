#!/usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import threeon
from time import sleep
from threeon import switch_socket
mc = minecraft.Minecraft.create()
mc.postToChat("Do NOT Step on the Gold block")
while True:
    pos = mc.player.getTilePos()
    blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if (blockBelow == 41):
#       print ("Block Below is %s" % blockBelow)
        mc.postToChat("Bang!")
        switch_socket('on')
        sleep(1)
    elif (blockBelow == 57):
        switch_socket('off')
        mc.postToChat("Kaput!")
        sleep(1)
    else:
       sleep(1)
