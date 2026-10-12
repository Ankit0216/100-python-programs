def my_max(n):
    i = 0
    greatest = l1[0]
    while i<len(l1):
        if l1[i]>greatest:
            greatest = l1[i]
        i+=1
    return greatest




l1 = [10.20,30,40]
print(my_max(l1))

