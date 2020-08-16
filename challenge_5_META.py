print("Welcome to the Multiplication/Exponential Table App")

# Get user input
name = input("Enter your name : ")
num = float(input("Enter the number u would like to work with : "))

message = name.title() + ", Math is cool!"

# printing the multiplication table
print("Multiplication Table for " + str(num))
for i in range(1,10):
    print("\n\t "+str(i)+" * "+str(num)+" = "+str(round(i*num, 4)))

# print the exponential table
print("\nExponential Table for " + str(num))
for i in range(1,10):
    print("\n\t " + str(i) + " ** " + str(num) + " = " + str(round(num**i, 4)))

# final message
print("\n" + message)
print("\n\t" + message.lower())
print("\n\t\t" + message.title())
print("\n\t\t\t" + message.upper())

