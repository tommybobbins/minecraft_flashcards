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
        switch_socket("on")
        sleep(1)
        mc.postToChat("Timeout!")
        mc.postToChat("10...")
        sleep(1)
        mc.postToChat("9...")
        sleep(1)
        mc.postToChat("8...")
        sleep(1)
        mc.postToChat("7...")
        sleep(1)
        mc.postToChat("6...")
        sleep(1)
        mc.postToChat("5...")
        sleep(1)
        mc.postToChat("4...")
        sleep(1)
        mc.postToChat("3...")
        sleep(1)
        mc.postToChat("2...")
        sleep(1)
        mc.postToChat("1...")
        sleep(1)
        switch_socket("off")
        mc.postToChat("Now. Do NOT Step on the Gold block")
    else:
       sleep(1)
