f = open('Demo.txt', 'r')

lines = f.readlines()
print(lines)
for each in lines:
    print(each)
f.close()
