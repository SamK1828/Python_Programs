list1 = [10, 21, 30, 43, 66, 78, 33]
list2 = list(map(lambda x: x * 10, list1))
print(list2)

for i in list2:
    print(i, end=' ')
