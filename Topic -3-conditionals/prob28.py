a = float(input())
b = float(input())
c = float(input())

# if a+b+c == 180:
#     print("These values can form a triangle")
# else:
#     print("These values can not form a triangle")

if a+b>c and a+c>b and b+c>a:
    print("These values can form a triangle")
else:
    print("These values cannot form a triangle")