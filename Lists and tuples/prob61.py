l1 = [10,2,80,60,4,16]
# print(max(l1))
# print(min(l1))
biggest = l1[0]
smallest = l1[0]
for ele in l1:
    if ele>biggest:
        biggest=ele
print(biggest)

for ele in l1:
    if ele<smallest:
        smallest= ele
print(smallest)