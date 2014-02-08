import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

radius = 4

pos = mc.player.getPos()

for x in range(-(radius),radius):
	for y in range(-(radius), radius):
		for z in range(-(radius),radius):
			if x**2 + y**2 + z**2 < radius**2:
				mc.setBlock(pos.x + x - radius -10 , pos.y + y + radius, pos.z - z , block.COBBLESTONE)
