import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
mc.postToChat("x=%i, y=%i, z=%i" % (x,y,z))
