def get_oldest(date1, date2):
    date1_list = date1.split('/')
    #print(date1_list)
    num1 = 0
    for s in date1_list:
        i = int(s)
        num1 += i

    date2_list = date2.split('/')
    #print(date2_list)
    num2 = 0
    for s in date2_list:
        i = int(s)
        num2 += i

    if num1 < num2:
        return date1
    else:
        return date2

def get_oldest2(date1, date2):
    date1_list = date1.split('/')
    print(date1_list[-1])
    print(date1_list[:2])
    date1_a = [date1_list[-1]] + date1_list[:2]
    print(date1_a)

print(get_oldest('01/27/1832', '01/27/1756'))

print(get_oldest2('01/27/1832', '01/27/1756'))