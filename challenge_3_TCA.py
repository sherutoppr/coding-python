print("Welcome to Temperature Conversion App")

# Get user input
Fahrenheit = float(input("Enter the temperature in celsius : "))

# converting to celsius and kelvin
celsius = (Fahrenheit-32)*(5/9)
kelvin = Fahrenheit + 273.15

# rounding the temperature to 4 decimal digit
Fahrenheit = round(Fahrenheit, 4)
celsius = round(celsius, 4)
kelvin = round(kelvin, 4)

# summary table
print("Fahrenheit : "+str(Fahrenheit))
print("Celsius : "+str(celsius))
print("Kelvin : "+str(kelvin))

