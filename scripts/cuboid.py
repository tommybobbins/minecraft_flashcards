import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
radius = 4
height = radius + 6

pos = mc.player.getPos()
mc.setBlocks(pos.x + height, pos.y, pos.z, pos.x + radius, pos.y + height, pos.z + radius  , block.WOOL.id, 18)
#mc.setBlocks(pos.x + height, pos.y, pos.z, pos.x + radius, pos.y + height, pos.z + radius  , block.LAVA)
