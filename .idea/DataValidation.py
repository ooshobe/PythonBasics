data_valid = False

while data_valid == False:
    grade1 = float(input("Type the grade for the first test: "))
    if grade1 < 0 or grade1 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    grade2 = float(input("Type the grade for the second test: "))
    if grade2 < 0 or grade2 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    total_Classes = int(input("Type the total number of classes: "))
    if total_Classes <= 0 :
        print("The number of classes can't be zero or less")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    absences = int(input("Type the total numbe of absences: "))
    if absences < 0 or absences > total_Classes :
        print("The number of abscences can't be less than zero or greater than the number of total classes.")
        continue
    else:
        data_valid = True




avg_grade = (grade1 + grade2) / 2
attendance = (total_Classes - absences) / total_Classes

print("Average grade: ", round(avg_grade,2))
print("Attendace rate: ",str(round(( attendance * 100),2))+'%')


if (avg_grade >=6  and attendance >= 0.8 ):
    print("The student has been approved.")
elif(avg_grade < 6 and attendance < 0.8):
        print("The student has failed due to an average grade lower than 6.0 and an attendance rate lower than 80%.")
elif(attendance >= 0.8):
    print("The student has failed due to a grade being lower than 6.0.")
else:
    print("The student has failed due to an average grade lower than 6.0 and an attendance rate lower than 80%")