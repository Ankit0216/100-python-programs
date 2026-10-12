n = int(input("what's n : "))

sum = 0
while n>0:
    digits = n%10
    sum = sum+digits
    n = n//10
print(sum)
