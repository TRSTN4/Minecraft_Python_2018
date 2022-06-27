from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

hoogte = 2
blokType = 181

# Zijkanten torenspits: dezelfde hoogte als de variabele hoogte
zijHoogte = hoogte
mc.setBlocks(x + 1, y, z + 1, x + 3, y + zijHoogte - 1, z + 3, blokType)
# Zijkanten torenspits: twee keer zo hoog als de variabele hoogte
puntHoogte = 4
mc.setBlocks(x + 2, y, z + 2, x + 2, y + puntHoogte - 1, z + 2, blokType)

# Zijkanten torenspits: zou de helft moeten zijn van de variabele hoogte
voetHoogte = 1
mc.setBlocks(x, y, z, x + 4, y + voetHoogte - 1, z + 4, blokType)
