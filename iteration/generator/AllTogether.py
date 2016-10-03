# All Together
# Write a function all_together that takes any number of iterables and strings them together.
#
# Example:
#
# >>> list(all_together([1, 2], (3, 4), "hello"))
# [1, 2, 3, 4, 'h', 'e', 'l', 'l', 'o']
# >>> nums = all_together([1, 2], (3, 4))
# >>> list(all_together(nums, nums))
# [1, 2, 3, 4]

def all_together(*iters): # Why use *iters - Any number of iterables
    for i in iters:
        yield from i

    # Notes: yield from i is the shortcut for for x in i: yield x
    #for i in iters:
    #    for x in i:
    #        yield x

print(list(all_together([1,2], [3,4], "hello")))

