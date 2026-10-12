def converter(n,choice):
    if choice == 1:
        fahrenheit = (n*9/5)+32
        return fahrenheit
    elif choice == 2:
        celsius = (n-32)*(5/9)
        return celsius

    


n = float(input("Enter temperature : "))
choice = float(input("Enter 1 for celsius to fahrenheit and 2 for fahrenheit to celcius : "))
if choice == 1:
    print(converter(n,choice))
elif choice == 2:
    print(converter(n,choice))



