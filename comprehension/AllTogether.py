def all_together(*iterables):
    for i in iterables:
        yield from i

def all_together_2(*iterables):
    return (
        i
        for iter in iterables
        for i in iter
    )

print(list(all_together([1, 2], (3, 4), "hello")))
print(list(all_together_2([1, 2], (3, 4), "hello")))

nums = all_together_2([1, 2], (3, 4))
print(list(all_together_2(nums, nums)))
