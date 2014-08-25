import mcpi.minecraft as minecraft
import mcpi.block as block
import random
from time import sleep
mc = minecraft.Minecraft.create()
while True: #Will keep running until Cntrl-C pressed
    randomx = random.randint(-127, 127)
    randomz = random.randint(-127, 127)
    randomy = mc.getHeight(randomx, randomz)
    randomy += 20
    mc.setBlock(randomx, randomy, randomz, block.GRAVEL)
    sleep(0.1)
