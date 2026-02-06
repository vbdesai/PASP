def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error! Division by zero."
def power(x, y): return x ** y

def calculator():
    print("--- Python Calculator ---")
    print("Operations: +, -, *, /, ^ (power)")
    
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            choice = input("Enter operation (+, -, *, /, ^): ")
            num2 = float(input("Enter second number: "))

            if choice == '+':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '-':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '*':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '/':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == '^':
                print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")
            else:
                print("Invalid operator!")

            # Check if user wants another calculation
            next_calc = input("\nDo another calculation? (y/n): ").lower()
            if next_calc != 'y':
                break
        except ValueError:
            print("Invalid input! Please enter numeric values.")

calculator()
