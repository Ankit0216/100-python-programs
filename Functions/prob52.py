def calc_prime(n):
    i =1
    count = 0

    while i<=n:
        if n%i==0:
            count+=1
        i+=1

    if count==2:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
    

n = int(input("Enter a number here : "))
calc_prime(n)
