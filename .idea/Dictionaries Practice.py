#Dictionary initialization
person ={"first_name":"John","last_name":"Green","Birth_year": 1950, "county_of_birth":"Canada"}

#display the properties
print(person)

#changing properties
person["Birth_year"] = 1979

#test
print(person)

#adding a new property
person["Marital_status"]= "Married"

#test2
print(person)

#adding a list to a dictionary
person["children"] =["Natalie","Evan"]

#test3
print(person)

#adding a element to a list
person["children"].append("Eliza")
print(person)


