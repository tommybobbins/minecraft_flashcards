import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
x = pos.x
z = pos.z+4
height = mc.getHeight(x,z) + 1

print ("x=%i, y=%i, z = %i" % (x,height,z))

allblocks=[
  block.AIR,
  block.STONE,
  block.GRASS,
  block.DIRT,
  block.COBBLESTONE,
  block.WOOD_PLANKS,
  block.SAPLING,
  block.BEDROCK,
  block.WATER_STATIONARY,
  block.LAVA_STATIONARY,
  block.SAND,
  block.GRAVEL,
  block.GOLD_ORE,
  block.IRON_ORE,
  block.COAL_ORE,
  block.WOOD,
  block.LEAVES,
  block.GLASS,
  block.LAPIS_LAZULI_ORE,
  block.LAPIS_LAZULI_BLOCK,
  block.SANDSTONE,
  block.BED,
  block.COBWEB,
  block.GRASS_TALL,
  block.WOOL,
  block.FLOWER_YELLOW,
  block.FLOWER_CYAN,
  block.MUSHROOM_BROWN,
  block.MUSHROOM_RED,
  block.GOLD_BLOCK,
  block.IRON_BLOCK,
  block.STONE_SLAB_DOUBLE,
  block.STONE_SLAB,
  block.BRICK_BLOCK,
  block.TNT,
  block.BOOKSHELF,
  block.MOSS_STONE,
  block.OBSIDIAN,
  block.TORCH,
  block.FIRE,
  block.STAIRS_WOOD,
  block.CHEST,
  block.DIAMOND_ORE,
  block.DIAMOND_BLOCK,
  block.CRAFTING_TABLE,
  block.FARMLAND,
  block.FURNACE_INACTIVE,
  block.FURNACE_ACTIVE,
  block.DOOR_WOOD,
  block.LADDER,
  block.STAIRS_COBBLESTONE,
  block.DOOR_IRON,
  block.REDSTONE_ORE,
  block.SNOW,
  block.GLOWSTONE_BLOCK,
  block.ICE,
  block.SNOW_BLOCK,
  block.STONE_BRICK,
  block.CACTUS,
  block.MELON,
  block.SUGAR_CANE,
  block.GLOWING_OBSIDIAN,
  block.FENCE,
  block.NETHER_REACTOR_CORE,
  block.GLASS_PANE,
  block.NETHER_REACTOR_CORE,
  block.WATER_FLOWING,
            ]

#  block.LAVA_FLOWING,
#  block.LAVA,
#  block.WATER,
#   block.CLAY,

for BLOCKTYPE in allblocks:
    height += 1 
#    print BLOCKTYPE
#    print ("x=%i, y=%i, z = %i" % (x,height,z))
    mc.setBlock(x, height, z , BLOCKTYPE.id )
