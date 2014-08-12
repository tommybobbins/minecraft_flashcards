import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
mc.setBlocks(-128,40,-128,128,50,128,block.WOOL.id, 0)
