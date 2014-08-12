import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
blockBelow = mc.getBlock(pos.x, pos.y,  pos.z)
mc.setBlocks(-128,pos.y,-128,128,50,128,block.WOOL.id, 0)
mc.setBlocks(-127,pos.y,-127,127,49,127, 0)
