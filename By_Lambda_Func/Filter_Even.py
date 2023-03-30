list1 = [10, 21, 30, 43, 66, 78, 33]
list2 = list(filter(lambda x: x % 2 == 0, list1))  # Even Elements will accept...

print(list2)

print('Elements Filtered or Accepted: ')
for x in list2:
    print(x, end=' ')
