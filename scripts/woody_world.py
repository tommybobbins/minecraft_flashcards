import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
x = pos.x
z = pos.z+4
height = mc.getHeight(x,z)

for number in range(0,3):
    mc.setBlock(x, height, z , block.WOOD.id, number )
    mc.setBlock(x, height + 3, z , block.LEAVES.id, number )
    height += 1
