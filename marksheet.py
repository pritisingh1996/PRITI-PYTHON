s1=int(input("enter the marks of sub 1:"))
s2=int(input("enter the marks of sub 2:"))
s3=int(input("enter the marks of sub 3:"))
s4=int(input("enter the marks of sub 4:"))
s5=int(input("enter the marks of sub 5:"))
s6=int(input("enter the marks of sub 6:"))

total=s1=s2+s3+s4+s5+s6
print("total:",total)

per=total/6
print("percentage:",per)

if per>=70:
    print("result:distinction")

elif per>=60:
    print("result:first class")

elif per>50:
    print("result:second class")

elif per>=40:
    print("result:pass class")

else:
    print("result:fail")