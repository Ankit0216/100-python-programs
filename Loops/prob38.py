n = int(input("What's n : "))

count = 0

while n>0:
    n = n//10
    count+=1
print(count)