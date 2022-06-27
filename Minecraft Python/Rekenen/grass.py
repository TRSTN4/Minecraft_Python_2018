from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
breedte = 100
hoogte = 1
lengte = 100
blokType = 2
lucht = 0
water = 8
mc.setBlocks(x, y, z, x + breedte, y + hoogte, z + lengte, blokType)
