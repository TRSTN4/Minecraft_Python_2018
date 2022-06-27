from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
y = y - 1
blokType = 10
mc.setBlock(x, y, z, blokType)
