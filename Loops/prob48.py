# a = int(input("Enter first term : "))
# d = int(input("Enter common diffrence : "))
# n = int(input("number of terms : "))

# sum = 0

# for i in range(n):
#     sum = sum+a
#     a = a+d
# print(sum)

choice = int(input("Enter 1 for Arithmetic, 2 for Geometric: "))

a = int(input("Enter first term: "))
n = int(input("Enter number of terms: "))

sum = 0

if choice == 1:
    d = int(input("Enter common difference: "))

    for i in range(n):
        sum = sum + a
        a = a + d

elif choice == 2:
    r = int(input("Enter common ratio: "))

    for i in range(n):
        sum = sum + a
        a = a * r

print(sum)