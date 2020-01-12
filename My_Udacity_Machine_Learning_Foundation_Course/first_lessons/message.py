names =  input("Provide list of names: >").title().split(",") # get and process input for a list of names
assignments =  input("Provide list of count of missed assignments: >").split(",") # get and process input for a list of the number of assignments
grades =  input("Provide list of grades: >").split(",") # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assignment, grade in zip(names, assignments, grades):
    final_grade = int(grade) + 2*int(assignment)
    print(message.format(name, assignment, grade, final_grade))