def all_together(*iters): # Why use *iters
    for i in iters:
        yield from i

print(list(all_together([1,2], [3,4])))

