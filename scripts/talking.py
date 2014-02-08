import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
while True:
    message = raw_input("Write here to chat:")
    mc.postToChat(message)
