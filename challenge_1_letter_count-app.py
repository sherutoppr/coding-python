
print("Welcome to the Letter count app")

# Get user input
name = input("Enter your name, Please : ")
print("hello "+name+"!")
print("I will count the number of times a letter occurs ina message.")
message = input("Please enter a message : ")
letter = input("which letter u would like to count :")

# lower case of message
message = message.lower()
letter = letter.lower()

# Get the count and print the result
letter_count = message.count(letter)
print("\n" + name + ", your message has " + str(letter_count) + " " + letter + "'s in it.")