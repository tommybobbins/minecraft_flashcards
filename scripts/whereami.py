import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
x = int(pos.x)
y = int(pos.y)
z = int(pos.z)
mc.postToChat("x=%i, y=%i, z=%i" % (x,y,z))
print(x,y,z)
