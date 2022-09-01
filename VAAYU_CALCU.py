key = "y"
key_2 = "NO"
key_3 = "NO"
key_1 = "NEW"
c = " "
out = 0


def calc_sum(x, y):
    return x + y


def calc_diff(x, y):
    return x - y


def calc_quo(x, y):
    try:
        quo = x/y
        return quo
    except ZeroDivisionError:
        print("Youre trying to divide by zero")
        return "NA"


def calc_prod(x, y):
    return x * y


def calc_mod(x, y):
    try:
        rem = x % y

    except ZeroDivisionError:
        print("Youre trying to divide by zero")
        return "NA"
    else:
        return rem


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


out = 0
while True:
    if key_1 == "NEW":
        a = int(input("Enter the 1st operand: \n"))
        print("Which operation would you like to perform?")
        c = input("addition: + \nsubtraction: - \ndivision: / \nmultiplication: * \nmodulus: mod \npercentage: % \nprime number check: prime \n")
    if key_3 == "SAME":
        print("Which operation would you like to perform?")
        c = input(" meow 1 addition: + \nsubtraction: - \ndivision: / \nmultiplication: * \nmodulus: mod \npercentage: % \nprime number check: prime \n")
    c = c.lower()
    if key_2 == "ANSWER":
        a = out
        print("Which operation would you like to perform?")
        c = input(" meow 2 addition: + \nsubtraction: - \ndivision: / \nmultiplication: * \nmodulus: mod \npercentage: % \nprime number check: prime \n")
    if c == "+":
        b = int(input("Enter the 2nd operand: \n"))
        out = calc_sum(a, b)
        print("The sum of the two numbers is: ", out)
    elif c == "-":
        b = int(input("Enter the 2nd operand: \n"))
        out = calc_diff(a, b)
        print("The difference of the two numbers is: ", out)
    elif c == "*":
        b = int(input("Enter the 2nd operand: \n"))
        out = calc_prod(a, b)
        print("The product of the two numbers is: ", out)
    elif c == "/":
        b = int(input("Enter the 2nd operand: \n"))
        out = calc_quo(a, b)
        print("The quotient of the division is: ", out)
    elif c == "mod":
        b = int(input("Enter the 2nd operand: \n"))
        out = calc_mod(a, b)
        print("The remainder of the division is: ", out)
    elif c == "%":
        b = int(input("Enter the 2nd operand: \n"))
        per = calc_percent(a, b)
        print(per)
    elif c == "prime":
        out = is_prime(a)
        if out is False:
            print(a, " is not a prime number")
        else:
            print(a, "is a prime number")
    else:
        print("invalid option entered, try again \n")
    key = input("Do you want to run again? y/n \n")
    if key == "y":
        key_1 = input("If you want to start the run a-fresh enter NEW/NO")
        key_1 = key_1.upper()
        if key_1 != "NEW":
            key_2 = input("if you want to run the calculator with the answer from the last run enter ANSWER/NO \n")
            if key_2 == "ANSWER":
                key_2 = key_2.upper()
            else:
                key_3 = input("if you want to run the calculator with the same values and a different operation enter SAME/NO \n")
                key_3 = key_3.upper()
        continue
    else:
        break
