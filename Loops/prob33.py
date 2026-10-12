# n = int(input("Whats n : "))
# fact = 1

# for i in range(1,n+1):
#     fact*=i
# print(fact)

n = int(input("Whats n : "))

i = 1
fact = 1

while i<=n:
    fact*=i
    i+=1
print(fact)
