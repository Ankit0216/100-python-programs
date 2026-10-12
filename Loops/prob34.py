# n = int(input("Whats n : "))
# a = 0
# b = 1
# for i in range(n):
#     c = a+b
#     a=b
#     b=c

n = int(input("Whats n : "))

a = 0
b = 1
i = 0
while i<=n:
    print(a)
    c = a+b
    a = b
    b = c
    i+=1