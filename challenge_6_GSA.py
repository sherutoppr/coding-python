print("Welcome to the Grade Sorted App")

# initialise the list
grade = []

# get user input
print("Enter 4 numbers : ")
for i in range(4):
    x = int(input("\t" + str(i+1) + " : "))
    grade.append(x)


print("your grade are : " + str(grade))

# sort the list from highest to lowest
grade.sort(reverse=True)
print("your grade from highest to lowest : " + str(grade))

# removing the lowest 2 grade
print("lowest two grade : ")
print(" removed grade = " + str(grade.pop()))
print(" removed grade = " + str(grade.pop()))

print("your remaining grades are : " + str(grade))
print("Nice work!, your highest grade is " + str(grade[0]) + ".")


