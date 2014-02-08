import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlock(pos.x + 4, pos.y, pos.z , block.WOOL.id, 13) #Green
mc.setBlock(pos.x + 4, pos.y , pos.z + 1 , block.WOOL.id, 0) #White
mc.setBlock(pos.x + 4, pos.y , pos.z + 2 , block.WOOL.id, 14) #Red
mc.setBlock(pos.x + 4, pos.y + 1, pos.z + 1, block.TNT.id, 1) #
#Block is armed.
mc.postToChat("Hit the TNT, then run.")
