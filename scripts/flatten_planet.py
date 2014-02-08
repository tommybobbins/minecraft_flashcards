import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
mc.setBlocks(-128,0,-128,128,64,128,block.AIR)# Air above
mc.setBlocks(-128,0,-128,128,-1,128,block.WATER)# Water below
mc.postToChat("Waterworld in 5 minutes. Take a break.")
