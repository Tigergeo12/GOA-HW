operator = input("Enter an operator (+ - * /): ")
num1 = input("Enter the 1st number: ")
num2 = input("Enter the 2nd number: ")

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)