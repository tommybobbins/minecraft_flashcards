import mcpi.minecraft as minecraft
import mcpi.block as block
import random

""" draw a building

    @author: goldfish"""

def drawBuilding( locx, locy, locz, floors, width, depth, floorheight, wallmaterial, floormaterial, roofmaterial ):
    topx = locx+width
    topy = locy+((floorheight+1)*floors)
    topz = locz+depth
    #draw building shell
    mc.setBlocks( locx, locy, locz, topx, topy, topz, wallmaterial )
    mc.setBlocks( locx+1, locy+1, locz+1, topx-1, topy-1, topz-1, block.AIR )
    #draw floors
    if( floors > 1 ):
        for i in range( floors -1 ):
            floorYloc = locy+( (floorheight+1)*(i+1) )
            mc.setBlocks( locx+1, floorYloc, locz+1, topx-1, floorYloc, topz-1, floormaterial )
    #draw door
    doorloc = random.randint( 1, width-2 )
    mc.setBlock( locx, locy+1, locz+doorloc, block.AIR )
    mc.setBlock( locx, locy+2, locz+doorloc, block.AIR )
    #draw front windows
    if( floors > 1 ):
        for i in range( floors-1 ):
            windowYloc = locy+2+( (floorheight+1)*(i+1) )
            for j in range( floorheight-1 ):
                mc.setBlocks( locx, windowYloc+j , locz+1, locx, windowYloc+j, locz+(width-1), block.GLASS_PANE )
    #draw back windows
    if( floors > 1 ):
        for i in range( floors-1 ):
            windowYloc = locy+2+( (floorheight+1)*(i+1) )
            for j in range( floorheight-1 ):
                mc.setBlocks( locx+depth, windowYloc+j , locz+1, locx+depth, windowYloc+j, locz+(width-1), block.GLASS_PANE )
    #connect levels with ladder
    #mc.setBlocks( topx-1, locy+1, topz-1, topx-1, topy-1, topz-1, block.LADDER )
#   Add width block height Pyramid on top for tiles
    height = width
    level = 1
    while level <= height:
        mc.setBlocks( locx - level + width/2 , topy + 5  - level, locz - level + depth/2, locx + level + width/2, topy + 5 - level, locz + level + depth/2, roofmaterial, 1 )
#    mc.setBlocks( x - level, height - level, z - level, x + level, height - level, z + level, block.TNT.id, 1 )
        level = level + 0.5
#####End of Pyramid tiles


if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    pos = mc.player.getPos()
    x = int(pos.x + 20)
    z = int(pos.z + 15)
    y = int(mc.getHeight(x,z))
    #   x,y,z, width, depth, floors, heighfloor, wallsmaterial, floormaterial, roofmaterial
    drawBuilding( x, y, z, 10, 10, 10, 3, block.BRICK_BLOCK, block.WOOD_PLANKS, block.STONE_BRICK )
