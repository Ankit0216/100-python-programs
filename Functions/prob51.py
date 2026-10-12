def fact_calc(n):
    i = 1
    fact = 1
    while i<=n:
        fact*=i
        i+=1
    return fact


n = int(input("Enter a number : "))
print(fact_calc(n))
