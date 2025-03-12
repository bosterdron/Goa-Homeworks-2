def calculator():
	try:
		num1 = float(input("Enter first number: "))
		operation = input("Enter operation (+, -, *, /): ")
		num2 = float(input("Enter second number: "))

		if operation == '+':
			result = num1 + num2
		elif operation == '-':
			result = num1 - num2
		elif operation == '*':
			result = num1 * num2
		elif operation == '/':
			result = num1 / num2
		else:
			return "Invalid operation"

		return f"The result is: {result}"
	except ValueError:
		return "Invalid input"

print(calculator())