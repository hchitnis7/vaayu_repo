fruits = ["apple", "cherry", "banana", "papaya", "watermelon", 1, 2, 3, 4, 5, 6, 7, 6.9, 69.420]
i= 0
l = len(fruits)
while i < l:
    if fruits[i] == "cherry":
        print(i)
    i+=1
fruits.append("meow")
print(fruits)
fruits.pop(4)
print(fruits)
print(fruits[4:11])
list = fruits[4:11]
print(list[::-1])
print(list[::3])
