def split_in_half(list):
    mid = len(list) // 2
    result = [list[:mid], list[mid:]]
    print(result)

test_list = [1,2,3,4]
split_in_half(test_list)
split_in_half([])
split_in_half([1])
split_in_half("Hello Wolrd!")
split_in_half((1,2))