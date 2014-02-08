import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y + 4, pos.z, block.GOLD_BLOCK)
mc.player.setPos(pos.x,pos.y+10, pos.z)
