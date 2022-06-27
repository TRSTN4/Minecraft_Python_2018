# Maak verbinding met Minecraft
from mcpi.minecraft import Minecraft
# mc = Minecraft.create()

# Maak x, y en z variabelen om coordinaten in te stellen
x = -74
 y = 65
z = 22

# Verander de positie van de speler
mc.player.setTilePos(x, y, z)
