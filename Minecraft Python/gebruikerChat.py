from mcpi.minecraft import Minecraft
mc = Minecraft.create()
voorNaam = "Charles"
achterNaam = "Kremer"
print(voorNaam + " " + achterNaam)
print(voorNaam, achterNaam)
print("Hij heet " + voorNaam + " " + achterNaam)
boodschap = input("Typ je boodschap: ")
mc.postToChat(boodschap)
                       

