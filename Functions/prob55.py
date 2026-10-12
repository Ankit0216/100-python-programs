def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def div(a,b):
    return a/b

def prod(a,b):
    return a*b

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = input("enter operation + , - , / , *: ")

if c == '+':
    print(add(a,b))
elif c == "-":
    print(subtract(a,b))
elif c == "/":
    print(div(a,b))
elif c == "*":
    print(prod(a,b))
else:
    print("Invalid input")
