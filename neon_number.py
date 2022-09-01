n = int(input("Enter the number you want to have checked :"))
num = str(n)
sq = n**2
sq_a = str(sq)
p = len(sq_a)
sum = 0
i = 0
j = 0
d = 0
k = 0
list_b = []
while i<p:
    l = sq_a[i]
    list_b.append(l)
    i+=1
list_b = list(map(int, list_b))
while k<p:
    f = list_b[k]
    sum = (sum+f)
    k+=1
if sum == n:
    print("The given number is a neon number")
else:
    print("The number is not a neon number")
