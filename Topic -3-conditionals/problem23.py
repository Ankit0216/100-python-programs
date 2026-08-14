a = float(input())
b = float(input())
c = float(input())
# d = b**2 - 4*a*c
# print("discriminant =", d)
# x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
# x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)

# print(x1,x2)



d = b**2-4*a*c
if d>0:
    x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    print(x1,x2)
elif d == 0:
    x = -b / (2*a)
else:
    print("No real roots")
