list = []
n = int(input("Enter the total length of the tuple you want to create: "))
for i in range (0, n):
    list.append(int(input(f"enter the {i}th element:  ")))
tup = tuple(list)
print(list, type(list))
print(tup, type(tup))
tup_2 = tup[::-1]
tup3 = tup + tup_2
print(tup3)