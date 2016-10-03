fruit = dict()
i = iter(fruit)
fruit['apple'] = 'red'
print(next(i))

#>>> RuntimeError: dictionary changed size during iterator

# Iterators don't work when Dictionary changes, because elements do not have a constant order in Dictionary (hash, rehash might happen)

