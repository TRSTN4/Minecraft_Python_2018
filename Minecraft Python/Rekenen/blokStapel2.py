from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -55
y = 63
z = 22
blokType = 4
up = 1
mc.setBlock(x, y, z, blokType)
mc.setBlock(x, y + up, z, blokType)
