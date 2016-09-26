# Running Mean
# Create a generator function running_mean that takes an iterable and yields the current running mean.
#
# For example:
#
# >>> numbers = [8, 4, 3, 1, 3, 5]
# >>> list(running_mean(numbers))
# [8.0, 6.0, 5.0, 4.0, 3.8, 4.0]

def running_mean(numbers):
    #average = []
    sum = 0
    for i, num in enumerate(numbers):
        sum += num
        #average.append(sum/(i*1.0))
        yield sum/((i+1)*1.0)

numbers = [8, 4, 3, 1, 3, 5]
print(list(running_mean(numbers)))
