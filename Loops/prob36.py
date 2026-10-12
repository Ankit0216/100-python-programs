n = int(input("Whats n : "))
o_num = n 

r_num = 0

while n>0:
    digits = n%10
    r_num = r_num*10+digits
    n = n//10
if o_num == r_num:
    print("palindrome")
else:
    print("not a palindrome")

