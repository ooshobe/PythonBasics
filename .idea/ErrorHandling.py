number = input("Type a number: ")

try:
    number = float(number)
    print("This number is: ", number)
except:
    print("Invalid number")