import math
a = -3
b = 2
g = a
f = b
#g = a / 360 * math.pi * 2
if a < 0:
    a = -a
while b:
    a, b = b, a % b
#if (a == 0) or (b == 0):
#    nod = 0
#else:
    nod = a
sin = math.sin(g)
#sin = round(math.sin(g), 4)
f = math.factorial(f)
print(nod)
print(f)
c = ((sin * nod) ** f)
c = round(c, 2)
print(c)