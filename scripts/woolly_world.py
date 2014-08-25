import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
x = pos.x
z = pos.z+4
height = mc.getHeight(x,z)

for number in range(0,15):
    mc.setBlock(x, height, z , block.WOOL.id, number )
    height += 1
