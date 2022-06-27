# Maak verbinding met Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# Maak x, y en z variabelen om coordinaten in te stellen
x = -74
y = 65
z = 22

# Verander de positie van de speler
mc.player.setTilePos(x, y, z)

# Wacht x seconden
time.sleep(2)

# Maak x, y en z variabelen om coordinaten in te stellen
x = -58
y = 65
z = 14

# Verander de positie van de speler
mc.player.setTilePos(x, y, z)

# Wacht x seconden
time.sleep(2)

# Maak x, y en z variabelen om coordinaten in te stellen
x = -44
y = 65
z = 3

# Verander de positie van de speler
mc.player.setTilePos(x, y, z)

