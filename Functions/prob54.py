def check_palin(n):
    pass

n = int(input("Enter a number : "))
org_num = n
rev_num = 0
while n>0:
    digit = n%10
    rev_num=(rev_num*10)+digit
    n = n//10

if rev_num==org_num:
    print("palindrome")
else:
    print("not a palindrome")

