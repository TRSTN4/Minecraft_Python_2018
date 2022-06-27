from mcpi.minecraft import Minecraft
mc = Minecraft.create()

positie = mc.player.getTilePos()
x = positie.x
y = positie.y
z = positie.z

x = x + 5
y = y + 100
mc.player.setTilePos(x, y, z)

#health = 20
#health = health - 10
