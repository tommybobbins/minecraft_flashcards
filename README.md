minecraft_flashcards and scripts
================================

A PDF set of Flashcards for the Raspberry Pi Minecraft API written in LaTeX, together with the scripts to run. Full LaTeX source for the flashcards is provided.

Instructions to install Minecraft on the Raspberry Pi:
http://pi.minecraft.net/

After installing Minecraft Pi, it's easiest to move the Python libraries to a central location:
sudo cp -rp /home/pi/mcpi/api/python/mcpi /usr/local/lib/python2.7/dist-packages/

Python scripts for controlling Minecraft Pi Edition on Raspberry Pi, from the work of Martin O' Hanlon found at mcpipy.com: https://github.com/brooksc/mcpipy
Code and Inspiration taken from Craig Richardson’s Minecraft Pi Book: http://arghbox.wordpress.com/
Craig's book is licensed under the Creative Commons license of Attribution-
NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)

Scripts included with these flashcards are:

    all_blocks.py             - Put all available blocks into a Totem.
    talking.py                - One off chat message.
    look_whos_talking_two.py  - Show how to continually send chat messages.
    rainingrocks.py           - Drop random gravel blocks from the sky. 
    bigjump.py                - Teleport the player into the air.
    midas.py                  - Square below the player turn to gold.
    tower_lava.py             - Simple solid tower. Edit to add lava icing.
    towerblock.py             - Build a towerblock with windows, doorway, floors and roof.
    cuboid.py                 - Cuboid.
    nomoon.py                 - Sphere.                
    whereami_loop.py          - Continually post player location.
    flatten_planet.py         - Remove all terrain.
    place_one_block.py        - Place one block.
    teleport.py               - Teleport the player to a fixed location.
    whereami.py               - Find player location.
    forest.py                 - Create random forest around player.
    pyramid.py                - Create Pytamid.
    tnt_explodes.py           - Create explosive block TNT.
    woolly_world.py           - Create wool totem.
