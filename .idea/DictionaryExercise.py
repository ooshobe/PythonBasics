#Dictionary initialization
person ={"first_name":"John","last_name":"Green","gender":"M","age": 50, "address":"1162 Queen Street East","phone":"119652600"}

user = input("What information would you like to know about this person: ")

result = person.get(user,"That information doesn't exist")

print(result)