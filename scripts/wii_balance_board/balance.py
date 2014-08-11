#!/usr/bin/python
import mcpi.minecraft as minecraft
import pygame
pygame.init()
import mcpi.block as block
mc = minecraft.Minecraft.create()
from time import sleep
import time
##############################################################
# Balance board code 
# Initialize the joysticks
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
bb_pos={}
name = joystick.get_name()
print("Joystick name: {%s}" % name )
axes = joystick.get_numaxes()
print("Number of axes: {%s}" % axes )
# Average 8 year old
calibration_factor = 1.02
# Average male adult
calibration_factor = 1.05

if __name__ == "__main__":
    while True:
        pos = mc.player.getTilePos()
        direction_of_travel = "stopped"
        events=pygame.event.get()
        for i in range( axes ):
            bb_pos[i] = float(joystick.get_axis(i))
        forwards_or_backwards = (bb_pos[2] + bb_pos[0])/(bb_pos[3] + bb_pos[1])
        left_or_right = (bb_pos[2] + bb_pos[3])/(bb_pos[0] + bb_pos[1])
        abs_fb = abs(forwards_or_backwards - 1.0)
        abs_lr = abs(left_or_right - 1.0)
        if abs_fb > abs_lr:
#            print ("Mainly trying to move forward backwards")
            if forwards_or_backwards < 1.0/calibration_factor:
                direction_of_travel="Forwards"
                mc.player.setTilePos(pos.x,pos.y,pos.z-1)
            elif forwards_or_backwards > 1.0*calibration_factor:
                direction_of_travel="Backwards"
                mc.player.setTilePos(pos.x,pos.y,pos.z+1)
            else:
                direction_of_travel="Stopped"
        elif abs_fb < abs_lr:
#            print ("Mainly trying to move Left Right")
            if left_or_right < 1.0/calibration_factor:
                direction_of_travel="Left"
                mc.player.setTilePos(pos.x-1,pos.y,pos.z)
            elif left_or_right > 1.0*calibration_factor:
                direction_of_travel="Right"
                mc.player.setTilePos(pos.x+1,pos.y,pos.z)
            else:
                direction_of_travel="Stopped"
        print (direction_of_travel)
