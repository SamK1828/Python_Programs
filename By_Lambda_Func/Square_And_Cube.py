list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = list(map(lambda x: x ** 2, list1))
list3 = list(map(lambda x: x ** 3, list1))

print(list2)
print(list3)