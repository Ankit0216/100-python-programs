a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

hcf = 1
if a<b:
    smaller = a
else:
    smaller = b

for i in range(1,smaller+1):
    if a%i ==0 and b%i==0:
        hcf = i
print(hcf)

