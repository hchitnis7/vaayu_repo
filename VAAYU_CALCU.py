key = "y"
key_2 = "NO"


def calc_sum(x, y):
    return x + y


def calc_diff(x, y):
    return x - y


def calc_quo(x, y):
    return x / y


def calc_prod(x, y):
    return x * y


def calc_mod(x, y):
    return x % y


def calc_percent(x, y):
    percent = (x / 100) * y
    return percent


def is_prime(x):
    flag = False
    for i in range(2, x):
        if (x % i) == 0:
            flag = True
            break
    if flag:
        return False
    else:
        return True


a, b = 0, 0
while True:
    if key_2 != "YES":
        a = int(input("Enter the 1st operand: \n"))
        print("Which operation would you like to perform?")
        c = input("addition: + \nsubtraction: - \ndivision: / \nmultiplication: * \nmodulus: mod \npercentage: % \nprime number check: prime \n")
        b = int(input("Enter the 2nd operand: \n"))
    else:
        print("Which operation would you like to perform?")
        c = input("addition: + \nsubtraction: - \ndivision: / \nmultiplication: * \nmodulus: mod \npercentage: % \nprime number check: prime \n")
    c = c.lower()
    if c == "+":
        out = calc_sum(a, b)
        print("The sum of the two numbers is: ", out)
    elif c == "-":
        out = calc_diff(a, b)
        print("The difference of the two numbers is: ", out)
    elif c == "*":
        out = calc_prod(a, b)
        print("The difference of the two numbers is: ", out)
    elif c == "/":
        out = calc_quo(a, b)
        print("The difference of the two numbers is: ", out)
    elif c == "mod":
        out = calc_mod(a, b)
        print("The difference of the two numbers is: ", out)
    elif c == "%":
        per = calc_percent(a, b)
        print(per)
    elif c == "prime":
        out = is_prime(a)
        if out is False:
            print(a, " is not a prime number")
        else:
            print(a, "is a prime number")
        out = is_prime(b)
        if out is False:
            print(b, " is not a prime number")
        else:
            print(b, "is a prime number")
    else:
        print("invalid option entered, try again \n")
    key = input("Do you want to run again? y/n \n")
    if key == "y":
        key_2 = input("if you want to run the calculator with different operation but same operands enter YES \n")
        key_2 = key_2.upper()
        continue
    else:
        break
