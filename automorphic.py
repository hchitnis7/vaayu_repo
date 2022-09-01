n = int(input("Enter the number which you would like to check :"))
sq = n**2
l1 = (n%10)
l2 = (sq%10)
if l1==l2:
    print("The entered number is Automorphic")
else:
    print("The entered number is not Automorphic")