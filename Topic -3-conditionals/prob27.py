a = int(input("Units used : "))

if a <= 100:
    x = a*2
    print("Charges for units used : " , x)
elif a<=200:
    x = 100*2 + (a-100)*3
    print("Charges for units used : " , x)
else:
    x = 100*2 + 100*3 + (a-200)*5
    print("Charges for units used : " , x)