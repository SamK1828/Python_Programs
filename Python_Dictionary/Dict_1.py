dict_1 = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
print(type(dict_1))
print()
print()
# get keys of dictionary
x = dict_1.keys()
print(x)
for i in x:
    print(i)
# get values of dictionary
y = dict_1.values()
print(y)
for i in y:
    print(i)
# get both keys and values
z = dict_1.items()
for i, j in z:
    print(i, j)
print()
print()

list1 = [10, 20, 40, 20, 40, 60, 30, 20, 10, 60]
d1 = {}

for x in list1:
    c = list1.count(x)  # counting repetition of element and storing as a key
    d1[c] = x  #
print(d1)
