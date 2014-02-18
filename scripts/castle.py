import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
from time import sleep
radius = 7 # Radius of the keep (2 * 7 = 14 blocks wide)
height = radius + 15 # Height of the Keep
outer = radius + 10 # Walls around the keep
tower_width = 7 # Towers around the walls
moat = tower_width + outer + 2 # Moat width
tnt = 46

pos = mc.player.getPos()

def make_walls(x1,y1,z1,x2,y2,z2,material,floormaterial,roofmaterial,crenelations):
    mc.setBlocks(x1, y1, z1, x2, y2, z2, material)
    mc.setBlocks(x1 - 1, y1, z1 + 1, x2 + 1, y2, z2 -1, block.AIR)
    mc.setBlocks(x1 - 1, y1-1, z1 + 1, x2 + 1, y1 -1, z2 -1, floormaterial)
    if (roofmaterial != block.AIR):
        mc.setBlocks(x1 - 1, y2-2, z1 + 1, x2 + 1, y2 -2, z2 -1, roofmaterial)
# Making Crenelations is slow, set to False for rapid building. 
# Add True when you are happy #
    if crenelations: 
        x2 = int(x2) # Make all co-ordinates integers
        x1 = int(x1)
        z1 = int(z1)
        z2 = int(z2)
        mc.postToChat("Making Crenelations")
        for xblock in (range(x2-1,x1+1)): # Check all blocks in x
            for zblock in (range(z1-1,z2+1)): # Check all blocks in z
                block_type = mc.getBlock(xblock,y2,zblock) #Find block type
                if ((block_type != 1)): #If block not air
                    # Set block to air on odd,odd or even,even.
                    if (((xblock % 2 == 0 ) & ( zblock % 2 == 0 )) | (( xblock % 2 == 1 ) & ( zblock % 2 == 1 )) ):
                        mc.setBlock(xblock,y2,zblock, block.AIR)
# End of adding crenelations

def make_moat(x1,y1,z1,x2,y2,z2,material):
    mc.setBlocks(x1, y1, z1, x2, y2, z2, material)
    mc.setBlocks(x1 - 1, y1, z1 + 1, x2 + 1, y2, z2 -1, block.GRASS)

mc.postToChat("Building. Keep Still.")
mc.postToChat("Making Moat")
make_moat(pos.x + moat , pos.y, pos.z - moat, pos.x - moat , pos.y - 1, pos.z + moat, block.WATER)
mc.postToChat("Making Curtain Wall")
make_walls(pos.x + outer , pos.y, pos.z - outer, pos.x - outer , pos.y + (height/2), pos.z + outer, block.STONE_BRICK,block.MOSS_STONE,block.WOOD_PLANKS,True)
mc.postToChat("Making Wall Walk")
make_walls(pos.x + outer - 1 , pos.y, pos.z - outer + 1, pos.x - outer + 1 , pos.y + (height/2) - 2, pos.z + outer - 1, block.STONE_BRICK,block.MOSS_STONE,block.AIR,False)
mc.postToChat("Making Tower1")
make_walls(pos.x + outer + tower_width - 3, pos.y, pos.z + outer - 3, pos.x + outer - 3 , pos.y + (height), pos.z + outer + tower_width - 3, block.STONE_BRICK,block.MOSS_STONE,block.WOOD_PLANKS,True)
mc.postToChat("Making Tower2")
make_walls(pos.x + outer + tower_width - 3, pos.y, pos.z - outer - tower_width + 3, pos.x + outer - 3, pos.y + (height), pos.z - outer + 3 , block.STONE_BRICK,block.MOSS_STONE,block.WOOD_PLANKS,True)
mc.postToChat("Making Tower3")
make_walls(pos.x - outer + 3, pos.y, pos.z + outer - 3, pos.x - outer - tower_width + 3 , pos.y + (height), pos.z + outer + tower_width - 3, block.STONE_BRICK,block.MOSS_STONE,block.WOOD_PLANKS,True)
mc.postToChat("Making Tower4")
make_walls(pos.x - outer + 3, pos.y, pos.z - outer - tower_width + 3, pos.x - outer - tower_width + 3 , pos.y + (height), pos.z - outer + 3, block.STONE_BRICK,block.MOSS_STONE,block.WOOD_PLANKS,True)
mc.postToChat("Making Gate")
mc.setBlocks(pos.x + outer - 2, pos.y , pos.z - 1, pos.x + outer, pos.y + (height/3), pos.z + 1,block.AIR)
mc.postToChat("Making Ladders")
mc.setBlocks(pos.x, pos.y, pos.z + outer - 2, pos.x, pos.y + (height/2) - 2, pos.z + outer - 2 , block.LADDER.id, 2)
mc.setBlocks(pos.x, pos.y, pos.z - outer + 2, pos.x, pos.y + (height/2) - 2, pos.z - outer + 2 , block.LADDER.id, 3)
mc.setBlocks(pos.x + outer - 2 , pos.y, pos.z + (radius/2), pos.x + outer - 2 , pos.y + (height/2) - 2, pos.z + (radius/2), block.LADDER.id, 4)
mc.setBlocks(pos.x - outer + 2 , pos.y, pos.z, pos.x - outer + 2 , pos.y + (height/2) - 2, pos.z, block.LADDER.id, 5)
mc.postToChat("Making Keep")
make_walls(pos.x + radius, pos.y, pos.z - radius, pos.x - radius, pos.y + height, pos.z + radius  , block.STONE_BRICK,block.WOOD_PLANKS,155,True)
mc.postToChat("Making Doorway")
mc.setBlocks(pos.x + radius, pos.y , pos.z - 1, pos.x + radius, pos.y + (height/4), pos.z + 1,block.AIR)
mc.setBlocks(pos.x + radius + 1, pos.y + 2 , pos.z - 2, pos.x + radius + 1, pos.y + 2, pos.z + 2,block.TORCH.id,4)
mc.setBlocks(pos.x + radius + 1, pos.y + (height/3) + 2, pos.z - 3, pos.x + radius + 1, pos.y + (height/3) + 2, pos.z + 3,block.TORCH.id,4)
mc.postToChat("Making Mood Lighting")
mc.setBlocks(pos.x + radius - 1, pos.y + (height/2) , pos.z - radius + 1, pos.x - radius + 1, pos.y + (height/2), pos.z + radius - 1,block.TORCH)
mc.setBlock(pos.x,pos.y+ height - 2,pos.z,block.GLOWSTONE_BLOCK)
mc.postToChat("Finished.")
