import math
import sympy as sp

class Calculator:
    def _init_(self):
        # Initialize the calculator with some symbolic variables for advanced use
        self.x, self.y = sp.symbols('x y')

    # Basic arithmetic operations
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

    # Advanced operations
    def modulus(self, a, b):
        return a % b

    def power(self, a, b):
        return a ** b

    def sqrt(self, a):
        if a < 0:
            return "Error: Cannot compute the square root of a negative number."
        return math.sqrt(a)

    def log(self, a, base=math.e):
        try:
            return math.log(a, base)
        except ValueError:
            return "Error: Logarithm domain error."

    def sin(self, a):
        return math.sin(math.radians(a))  # Input should be in degrees

    def cos(self, a):
        return math.cos(math.radians(a))

    def tan(self, a):
        return math.tan(math.radians(a))

    # Symbolic operations using SymPy
    def symbolic_solve(self, equation):
        # Example input: "x**2 - 4"
        eq = sp.sympify(equation)
        solutions = sp.solve(eq, self.x)
        return solutions

    # Menu display
    def print_menu(self):
        print("\n--- Developer Calculator ---")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power (x^y)")
        print("7. Square root")
        print("8. Logarithm")
        print("9. Sine")
        print("10. Cosine")
        print("11. Tangent")
        print("12. Solve symbolic equation")

    # Run calculator interaction loop
    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice: ")

            if choice in ['1', '2', '3', '4', '5', '6']:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                self.perform_basic_operation(choice, a, b)

            elif choice == '7':  # Square root
                a = float(input("Enter a number: "))
                print(f"Result: {self.sqrt(a)}")

            elif choice == '8':  # Logarithm
                a = float(input("Enter the number for log: "))
                base = input("Enter the base (default is e): ")
                base = float(base) if base else math.e
                print(f"Result: {self.log(a, base)}")

            elif choice in ['9', '10', '11']:  # Trigonometric functions
                a = float(input("Enter the angle (in degrees): "))
                if choice == '9':
                    print(f"sin({a}) = {self.sin(a)}")
                elif choice == '10':
                    print(f"cos({a}) = {self.cos(a)}")
                elif choice == '11':
                    print(f"tan({a}) = {self.tan(a)}")

            elif choice == '12':  # Symbolic equation solver
                equation = input("Enter the equation (in terms of 'x'): ")
                solutions = self.symbolic_solve(equation)
                print(f"Solutions: {solutions}")

            else:
                print("Invalid choice. Please select a valid operation.")

            # Continue or Exit
            next_calc = input("Do you want to perform another calculation? (yes/no): ")
            if next_calc.lower() != 'yes':
                print("Goodbye!")
                break

    # Perform basic operations based on user's choice
    def perform_basic_operation(self, choice, a, b):
        if choice == '1':
            print(f"Result: {self.add(a, b)}")
        elif choice == '2':
            print(f"Result: {self.subtract(a, b)}")
        elif choice == '3':
            print(f"Result: {self.multiply(a, b)}")
        elif choice == '4':
            print(f"Result: {self.divide(a, b)}")
        elif choice == '5':
            print(f"Result: {self.modulus(a, b)}")
        elif choice == '6':
            print(f"Result: {self.power(a, b)}")

if _name_ == "_main_":
    calc = Calculator()
    calc.run()
