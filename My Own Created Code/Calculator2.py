def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b

def MOD(a,b):
    return a % b

def DIV(a,b):
    return a // b

def EXP(a,b):
    return a**b

print("Please enter an integer")
a = int(input())
print("Please enter another integer")
b = int(input())

print("Please enter the operation from +,-,*,/,MOD,DIV,EXP")
operation = input()

if operation == "+":
    c = addition(a,b)
    print(a,"+",b,"=",c)

elif operation == "-":
    c = subtraction(a,b)
    print(a,"-",b,"=",c)

elif operation == "*":
    c = multiplication(a,b)
    print(a,"*",b,"=",c)

elif operation == "/":
    c = division(a,b)
    print(a,"/",b,"=",c)

elif operation == "MOD":
    c = MOD(a,b)
    print(a,"%",b,"=",c)

elif operation == "DIV":
    c = DIV(a,b)
    print(a,"//",b,"=",c)

elif operation == "EXP":
    c = EXP(a,b)
    print(a,"**",b,"=",c)