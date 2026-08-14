m1 = int(input())
# m2 = int(input())
# m3 = int(input())
# m4 = int(input())

# if m1>=90 and m1<=100:
#     print("Grade point : 10")
# elif m1 >=70 and m1<90:
#     print("Grade point : 9")
# elif m1>=60 and m1<70:
#     print("Grade point : 8")
# elif m1>=50 and m1<60:
#     print("Grade point : 7")
# else:
#     print("Grade point : 0")

if m1<0 or m1>100:
    print("Invalid input")
elif m1>=90:
    print("grade point : 10")
elif m1>=70:
    print("grade point : 9")
elif m1>=50:
    print("grade point : 8")
else:
    print("grade point : 0")