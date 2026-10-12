n = int(input("Enter a number : "))
original_num = n
on = n
count = 0
sum = 0

while n>0:
    n = n//10
    count+=1
print(count)

while on>0:
    digits = on%10
    sum = sum + (digits**count)
    on = on//10
print(sum)

if original_num==sum:
    print("Armstrong number")
else:
    print("Not an armstrong number")

