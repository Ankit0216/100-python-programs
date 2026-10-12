a = int(input("Enter a number"))
b = int(input("Enter another number"))
lcm = 0

if a>b:
    larger = a
else:
    larger = b

for i in range(1,a*b+1):
    if i%a==0 and i%b==0:
        lcm = i
        break
print(lcm)
