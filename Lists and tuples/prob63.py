l1 = [10,2,80,5,60,7,16]

even_count = 0
odd_count = 0

for ele in l1:
    if ele%2==0:
        even_count+=1
    else:
        odd_count+=1


print(even_count)
print(odd_count)