import mcpi.minecraft as minecraft
from time import sleep
mc = minecraft.Minecraft.create()
while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.postToChat("x=%i, y=%i, z=%i" % (x,y,z))
    sleep(1)
