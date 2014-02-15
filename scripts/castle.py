import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
from time import sleep
radius = 5
height = radius + 6
outer = radius + 10
moat = outer + 2
tnt = 46

pos = mc.player.getPos()

def make_walls(x1,y1,z1,x2,y2,z2,material,floormaterial):
    mc.setBlocks(x1, y1, z1, x2, y2, z2, material)
    mc.setBlocks(x1 - 1, y1, z1 + 1, x2 + 1, y2, z2 -1, block.AIR)
    mc.setBlocks(x1 - 1, y1-1, z1 + 1, x2 + 1, y1 -1, z2 -1, floormaterial)
    x2 = int(x2)
    x1 = int(x1)
    z1 = int(z1)
    z2 = int(z2)
    mc.postToChat("Making Crenelations")
    for xblock in (range(x2-1,x1+1)):
        for zblock in (range(z1-1,z2+1)):
            block_type = mc.getBlock(xblock,y2,zblock)
            if ((block_type != 1)):
                # Set block to air on odd,odd or even,even.
                if (((xblock % 2 == 0 ) & ( zblock % 2 == 0 )) | (( xblock % 2 == 1 ) & ( zblock % 2 == 1 )) ):
                    mc.setBlock(xblock,y2,zblock, block.AIR)
                    sleep(0.1)

def make_moat(x1,y1,z1,x2,y2,z2,material):
    mc.setBlocks(x1, y1, z1, x2, y2, z2, material)
    mc.setBlocks(x1 - 1, y1, z1 + 1, x2 + 1, y2, z2 -1, block.GRASS)

mc.postToChat("Making Moat")
make_moat(pos.x + moat , pos.y, pos.z - moat, pos.x - moat , pos.y - 1, pos.z + moat, block.WATER)
mc.postToChat("Making Curtain Wall")
make_walls(pos.x + outer , pos.y, pos.z - outer, pos.x - outer , pos.y + (height/2), pos.z + outer, block.STONE_BRICK,block.MOSS_STONE)
mc.postToChat("Making Keep")
make_walls(pos.x + radius, pos.y, pos.z - radius, pos.x - radius, pos.y + height, pos.z + radius  , block.STONE_BRICK,block.WOOD_PLANKS)

