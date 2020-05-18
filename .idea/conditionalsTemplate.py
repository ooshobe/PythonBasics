grade1 = float(input("Type the grade for the first test: "))
grade2 = float(input("Type the grade for the second test: "))
absences = int(input("Type the total numbe of absences: "))
total_Classes = int(input("Type the total number of classes: "))

avg_grade = (grade1 + grade2) / 2
attendance = (total_Classes - absences) / total_Classes

print("Average grade: ", round(avg_grade,2))
print("Attendace rate: ",str(round(( attendance * 100),2))+'%')

#basic if statement Structure
#if (avg_grade >= 6):
#   if (attendance >= 0.8):
#        print("The student has been approved.")
#    else:
#        print("The student has failed to an attendance rate lower than 80%.")
#else:
#    print("The student has failed. ")

if (avg_grade >= 6):
     if (attendance >= 0.8):
       print("The student has been approved.")
     else:
       print("The student has failed to an attendance rate lower than 80%.")
elif(attendance >= 0.8):
    print("The student has failed due to a grade being lower than 6.0.")
else:
    print("The student has failed due to an average grade lower than 6.0 and an attendance rate lower than 80%")