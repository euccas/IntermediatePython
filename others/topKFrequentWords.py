def topKFrequentWords(words, k):
    dict = {}
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    p = []
    for key, value in dict.items():
        p.append((value, key))

    p.sort(cmp=cmp)
    result = []
    for i in range(k):
        result.append(p[i][1])

    return result

def cmp(a, b):
    if a[0] > b[0] or a[0] == b[0] and a[1] < b[1]:
        return -1
    elif a[0] == b[0] and a[1] == b[1]:
        return 0
    else:
        return 1

print(topKFrequentWords(["abc", "abc", "hello"], 1))