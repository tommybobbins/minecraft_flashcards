import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
for x in range(pos.x-3, pos.x+3):
    for y in range (pos.y, pos.y + 4):
        for z in range (pos.z-3, pos.z +3):
            blockType = mc.getBlock(x,y,z)
#            print ("Blocktype = %i" % blockType)
            if (blockType == 41):
                print ("Found Gold")
