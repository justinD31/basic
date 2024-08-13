import re

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the result of subtracting y from x."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the result of dividing x by y. Raise an exception for division by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def evaluate_expression(expression):
    """Evaluate a mathematical expression and return the result. Handles basic arithmetic operations."""
    # Regular expression to match the operators and operands
    pattern = r'^(\d+\.?\d*)\s*([+\-*/])\s*(\d+\.?\d*)$'
    match = re.match(pattern, expression.strip())
    
    if not match:
        raise ValueError("Invalid expression format. Please use the format 'number operator number'.")

    x, operator, y = match.groups()
    x = float(x)
    y = float(y)

    if operator == '+':
        return add(x, y)
    elif operator == '-':
        return subtract(x, y)
    elif operator == '*':
        return multiply(x, y)
    elif operator == '/':
        return divide(x, y)
    else:
        raise ValueError("Unsupported operator. Use +, -, *, or /.")

def main():
    """Main function to run the calculator."""
    print("Welcome to the Simple Calculator!")
    print("You can perform basic arithmetic operations (addition, subtraction, multiplication, division).")
    print("Type 'exit' to quit the calculator.")
    
    while True:
        expression = input("Enter your expression: ")
        if expression.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        try:
            result = evaluate_expression(expression)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
