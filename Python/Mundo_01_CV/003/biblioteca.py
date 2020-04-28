# import math
from math import sqrt, floor
import random
import emoji
num = random.randint(1, 10)
# raiz = math.sqrt(num)
raiz = sqrt(num)
print("A raiz de {} é igual a {:.6f}".format(num, raiz))
print(emoji.emojize("Olá :angry:", use_aliases=True))