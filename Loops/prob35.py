# Reverse a number (e.g. 123 → 321)
n = int(input("Whats n : "))

r_num = 0

while n>0:
    digit = n%10
    r_num = r_num*10+digit
    n = n//10
print(r_num)

# n = int(input("Whats n : "))

# r_num = 0

# for i in range(len(str(n))):
#     digits = n%10
#     r_num = r_num*10+digits
#     n = n//10
# print(r_num)