import random

random.seed(10)
a = random.random()
random.seed(10)
b = random.random()

random.seed(11)
c = random.random()
random.seed(11)
d = random.random()

print(a, b, c, d)
