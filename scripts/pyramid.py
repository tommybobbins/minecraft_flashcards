import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
[x,y,z] = mc.player.getTilePos()
# Set some variables to customize your pyramid
height = 4
material = block.TNT
level = 1
# Execute the loop, building from the top down
while level <= height:
    print level
    mc.setBlocks( x - level, height - level, z - level, x + level, height - level, z + level, material )
    level = level + 0.5;

