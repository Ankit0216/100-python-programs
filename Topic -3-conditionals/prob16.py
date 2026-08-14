a = float(input("Enter number one : "))
b = float(input("Enter number two : "))
c = float(input("Enter number three : "))

if(a>=b and a>=c):
    print("The greater number is ", a)
elif(b>=a and b>=c):
    print("The greater number is " , b)
else:
    print("The greater number is " , c)

