year = int(input("Enter year : "))

if (year%400==0):
    print("this is a leap year")
elif(year%4==0 and year%100!=0):
    print("this ia a leap year")
elif(year%100==0 and year%400!=0):
    print("This is not a leap year")
elif(year%4!=0):
    print("not a leap yaer")