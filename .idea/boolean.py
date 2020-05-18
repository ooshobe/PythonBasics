myBoolean = True
print(type(myBoolean))

num1 = 8
num2 = 4

#greater than
print(num1 > num2)

#less than
print(num1 < num2)

#less than or equal to
print(num1 <= num2)

#greater than or equal to
print(num1 >= num2)

#not equal to
print(num1 != num2)

num3 = float (input("Type the first file number: "))
num4 = float(input("Type the second number: "))

if (num3 > num4):
    print(num3, "is greater than ", num4)
elif(num3 == num4):
    print(num3, "is equal to ", num4)
else:
    print(num3, "is less than ", num4)



