from mcpi.minecraft import Minecraft
mc = Minecraft.create()
boodschap = "Dit is de standaard boodschap"
mc.postToChat(boodschap)
boodschap = "Tweede boodscap is ook standaard"
mc.postToChat(boodschap)                        

