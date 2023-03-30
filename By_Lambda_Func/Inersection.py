list1 = [1, 2, 3, 5, 7, 8, 9, 10]
list2 = [1, 2, 4, 8, 9]

set1 = set(list1)
set2 = set(list2)

# set3 = list(map(lambda x: x.intersection(set2), filter(lambda y: y in set2, set1)))

print(set1.intersection(set2))
