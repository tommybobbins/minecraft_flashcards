import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
radius = 4
height = radius + 16
pos = mc.player.getPos()
#mc.setBlocks(pos.x + height, pos.y, pos.z, pos.x + radius, pos.y + height, pos.z + radius , block.STONE_BRICK.id, 18)
mc.setBlocks(pos.x + height, pos.y, pos.z, pos.x + radius, pos.y + height, pos.z + radius , block.GLOWING_OBSIDIAN)
# If you want Lava icing remove the comment (#) from the line below
#mc.setBlocks(pos.x + height, pos.y + height + 1, pos.z, pos.x + radius, pos.y + height + 1, pos.z + radius , block.LAVA)
