# Maak verbinding met Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Maak x, y en z variabelen om coordinaten in te stellen
x = -61
y = 62
z = 22
#blokType = 138
#mc.setBlock(x, y, z, blokType)

#y = y + 1
#blokType = 95
#mc.setBlock(x, y, z, blokType)
 
count = 0
while (count < 1000):
    z = z - 1
    blokType = 138
    mc.setBlock(x, y, z, blokType)
    count = count + 1

y = 63
z = 22

count = 0
while (count < 1000):
    z = z - 1
    blokType = 95
    mc.setBlock(x, y, z, blokType)
    count = count + 1

y = 61
z = 22
ax = -60
bx = -62
count = 0
while (count < 1000):
    z = z - 1
    blokType = 42
    mc.setBlock(x, y, z, blokType)
    mc.setBlock(ax, y, z, blokType)
    mc.setBlock(bx, y, z, blokType)
    count = count + 1

