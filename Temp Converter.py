temp = float(input("Enter the temperature: "))
unit = input("Enter the unit of temperature C or F  :")
if unit== "C":
    print("The input temperature will be converted from Celcius to Farenheit")
elif unit== "F":
    print("The input temperature will be converted from Farenheit to Celsius")
elif unit== "C":
    print("Invalid unit for conversion")

if unit == "C":
    result = str(temp*(9/5)+32) + " farenheit"
elif unit == "F":
    result = str((5/9)*(temp-32)) + " celsius"
print(result)
print ("Conversion completed. Thank you for using this tool.")


