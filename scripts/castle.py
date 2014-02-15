import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
radius = 5
height = radius + 6
outer = radius + 10
offset = radius 
tnt = 46
Placeblock = 1

pos = mc.player.getPos()

def make_walls(x1,y1,z1,x2,y2,z2,material):
    mc.setBlocks(x1, y1, z1, x2, y2, z2, material)
    mc.setBlocks(x1 - 1, y1, z1 + 1, x2 + 1, y2, z2 -1, block.AIR)
    x2 = int(x2)
    x1 = int(x1)
    z1 = int(z1)
    z2 = int(z2)
    for xblock in (range(x2-1,x1+1)):
#        print xblock
        for zblock in (range(z1-1,z2+1)):
#            print zblock
#            print (xblock, zblock)
            block_type = mc.getBlock(xblock,y2,zblock)
            if ((block_type != 1)):
                if (((xblock % 2 == 0 ) & ( zblock % 2 == 0 )) | (( xblock % 2 == 1 ) & ( zblock % 2 == 1 )) ):
                    mc.setBlock(xblock,y2,zblock, block.AIR)
                    # Set block to air on odd,odd or even,even


make_walls(pos.x + outer , pos.y, pos.z - outer, pos.x - outer , pos.y + (height/2), pos.z + outer, block.STONE_BRICK)
make_walls(pos.x + radius, pos.y, pos.z - radius, pos.x - radius, pos.y + height, pos.z + radius  , block.STONE_BRICK)

