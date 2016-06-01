import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
mc.setBlocks(-150,0,-150,150,80,150,block.AIR)# Air above
mc.setBlocks(-150,0,-150,150,-1,150,block.WATER)# Water below
mc.player.setTilePos(0, 1, 0)
mc.setBlock(0,0,0,block.DIRT)# Dirt
mc.postToChat("Waterworld created")
