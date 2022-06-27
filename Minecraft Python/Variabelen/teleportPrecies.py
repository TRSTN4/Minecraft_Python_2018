# Maak verbinding met Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# Maak x, y en z variabelen om coordinaten in te stellen
x = -73.510
y = 65.0
z = 22.455

# Verander de positie van de speler
mc.player.setPos(x, y, z)

# Wacht 10 seconden
time.sleep(10)



