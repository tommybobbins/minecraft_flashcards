import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y + 4, pos.z, block.DIAMOND_BLOCK)
mc.postToChat("Look above you")
