import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
mc.setBlocks(-150,0,-150,150,80,150,block.AIR)# Air above
mc.setBlocks(-150,0,-150,150,-1,150,block.WATER)# Water below
mc.postToChat("Waterworld in 5 minutes. Take a break.")
