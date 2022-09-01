s = input("Enter the word you want to check")
k = len(s)
j = 0
i = (k-1)
list_a = list(s)
print(list_a)
list_b = list_a                         #OR manually reversing the list
list_b.reverse()                        # while i>=0:
print(list_b)                           #     l = s[i]
if list_a == list_b:                    #     list_b.append(l)
    print("palindrome")                 #     i-=1
else:
    print("not a palindrome")




