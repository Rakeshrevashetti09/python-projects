print("  WELCOME TO THE PYTHON BASED CALCULATOR")

Number_1 = int (input( "Enter Number_1:"))
Number_2 = int (input( "Enter Number_2:"))

choice = input("Enter the operation needed Sum or Sub or Multiplication or Division:")

if choice == "Sum":
    Sum = Number_1 + Number_2
    print(" the sum of two numbers:" , Sum)

if choice == "Sub":
    Sub = Number_1 - Number_2
    print(" the sub of two numbers:" , Sub)

if choice == "Multi":
    Multiplication = Number_1 * Number_2
    print(" the multiplication of two numbers:" , Multiplication)

if choice == "div":
    Division = Number_1 / Number_2
    print(" the division of two numbers:" , Division)
else:
    print("Invalid Choice")
#print("Sum of two numbers is:", Sum)
#print("Substraction of two number is:" ,Sub)
#print("Multiplication of two numbers is:", Multiplication)
#print("Division of two numbers is:", Division)