# Make a function, power_list, that accepts a list of numbers and returns a new list that contains each number raised to the i-th power where i is the index of that number in the given list. For example:
#
# >>> power_list([3, 2, 5])
# [1, 2, 25]
# >>> numbers = [78, 700, 82, 16, 2, 3, 9.5]
# >>> power_list(numbers)
# [1, 700, 6724, 4096, 16, 243, 735091.890625]

def power_list(nums):
    result = []
    for i, n in enumerate(nums):
        result.append(n ** i)

    return result

def power_list_2(nums):
    return [
        n ** i
        for i, n in enumerate(nums)
    ]

nums = [3, 2, 5]
print(power_list(nums))
print(power_list_2(nums))
