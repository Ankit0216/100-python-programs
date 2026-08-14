print("enter 1 for addition")
print("enter 2 for substraction")
print("enter 3 for multiplication")
print("enter 4 for division")




a = float(input("Enter number one : "))
b = float(input("Enter number two : "))

c = int(input("Enter the type of operation : "))
if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
    print(a*b)
elif c == 4:
    print(a/b)
else:
    print("invalid input")
