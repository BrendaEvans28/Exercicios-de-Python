x1 = int(input('Digite um valor'))
y1 = int(input('Digite um valor'))
x2 = int(input('Digite um valor'))
y2 = int(input('Digite um valor'))

import math

raiz = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if raiz >= 10:
    print('Longe')
else:
    print('Perto')
