print('Welcome to the Miles per hour conversion app')

# Get user input
speed_mph = float(input("Enter the spped in mile per hour : "))

# logic
speed_mps = speed_mph * 0.4474
speed_mps = round(speed_mps,2)

# print the result
print("your speed in mile per second is "+str(speed_mps)+".")