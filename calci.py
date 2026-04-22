class Calculator:
    """A professional calculator with multiple operations."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        return a ** b

    def modulus(self, a, b):
        return a % b


def display_menu():
    print("\n===== Advanced Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("7. Exit")


def get_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return None, None


def main():
    calc = Calculator()

    while True:
        display_menu()
        choice = input("Select operation (1-7): ")

        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break

        a, b = get_numbers()
        if a is None:
            continue

        try:
            if choice == '1':
                result = calc.add(a, b)
            elif choice == '2':
                result = calc.subtract(a, b)
            elif choice == '3':
                result = calc.multiply(a, b)
            elif choice == '4':
                result = calc.divide(a, b)
            elif choice == '5':
                result = calc.power(a, b)
            elif choice == '6':
                result = calc.modulus(a, b)
            else:
                print("Invalid choice! Try again.")
                continue

            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()