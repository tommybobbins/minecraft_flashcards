import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
print ("Block Below is %s" % blockBelow)
