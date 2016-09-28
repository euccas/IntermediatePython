import sys
import random

if len(sys.argv) > 1:
    sides = int(sys.argv[1])
else:
    sides = 6

print(random.randint(1, sides))
print(random.randrange(1, sides))
