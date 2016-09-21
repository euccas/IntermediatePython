fruit = ['apple', 'orange']
i = iter(fruit)
print(next(i))
#>>> apple

fruit.insert(0, 'banana')
print(next(i))
#>>> apple

# Iterators still work when list changes, because list keeps the order