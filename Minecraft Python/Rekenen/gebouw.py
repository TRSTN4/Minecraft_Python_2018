from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
breedte = 10
hoogte = 5
lengte = 6
blokType = 155
lucht = 0
water = 8
#mc.setBlocks(x, y, z, x + breedte, y + hoogte, z + lengte, blokType)
#mc.setBlocks(x + 1, y + 1, z + 1 , x + breedte - 1, y + hoogte - 1, z + lengte - 1, lucht)

# Probeer eens een zwembad te genereren!
mc.setBlocks(x, y, z, x + breedte, y + hoogte, z + lengte, blokType)
mc.setBlocks(x + 1, y + 1, z + 1 , x + breedte - 1, y + hoogte, z + lengte - 1, water)

# Grass

