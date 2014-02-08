import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
print ("Hold down Ctrl and Press C to stop")
while True:
    message = raw_input("Write here to chat:")
    mc.postToChat(message)
