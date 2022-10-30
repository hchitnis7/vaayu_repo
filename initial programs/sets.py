list_in = []
n = int(input("Enter the total length of the tuple you want to create: "))
for i in range (0, n):
    list_in.append(int(input(f"enter the {i}th element:  ")))
set_1 = set(list_in)
print(set_1)
ch = input("do you want to add a value to the existing set? Y/N")
if ch == "y" or ch == "Y":
    k = int(input("Enter the value you wish to add : "))
    set_1.add(k)
    print(set_1)
else:
    print(set_1)
set_2 = {"hello", "world", "vaayu"}
set_3 = set_1|set_2         # can also be written as set_3 = set_1.union(set_2)
print(set_3)