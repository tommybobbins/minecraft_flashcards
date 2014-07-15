#!/usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import threeon
from time import sleep
from threeon import switch_socket
mc = minecraft.Minecraft.create()
mc.postToChat("Gold block on. Diamond block off.")
while True:
    pos = mc.player.getTilePos()
    blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if (blockBelow == 41):
#       print ("Block Below is %s" % blockBelow)
        mc.postToChat("On!")
        switch_socket('on')
        sleep(1)
    elif (blockBelow == 57):
        switch_socket('off')
        mc.postToChat("Off!")
        sleep(1)
    else:
       sleep(1)
