from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#blokType = 15
blokType = int(input("Voer een bloktype in: "))
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
mc.setBlock(x, y, z, blokType)

