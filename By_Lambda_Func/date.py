date = input('Enter Year,Month,Date by Giving Space:')

extract = lambda x: (int(x[:4]), int(x[5:7]), int(x[8:]))

year, month, day = extract(date)

print(date)
print(year)
print(month)
print(day)
