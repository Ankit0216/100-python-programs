def rev_num(n):
    
    r_num=0

    while n>0:
        digit = n%10
        r_num = (r_num*10)+digit
        n = n//10

    return r_num

n = int(input("Enter a number : "))
print(rev_num(n))

