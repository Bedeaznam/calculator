class Calculator:
    def __init__(self):
        print("Welcome to the Enhanced Calculator!")
        self.history = []  # Списък за запазване на историята на операциите

    def add(self, a, b):
        result = a + b
        self._save_history("Add", a, b, result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._save_history("Subtract", a, b, result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._save_history("Multiply", a, b, result)
        return result

    def divide(self, a, b):
        if b != 0:
            result = a / b
            self._save_history("Divide", a, b, result)
            return result
        else:
            return "Error: Division by zero is not allowed."

    def show_history(self):
        if self.history:
            print("\nCalculation History:")
            for record in self.history:
                print(record)
        else:
            print("\nNo calculations yet.")

    def clear_history(self):
        self.history = []
        print("\nHistory cleared.")

    def _save_history(self, operation, a, b, result):
        # Запазва операцията и резултата в списъка history
        self.history.append(f"{operation}: {a} and {b} = {result}")

if __name__ == "__main__":
    calc = Calculator()

    while True:
        print("\nSelect an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Clear History")
        print("7. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == "7":
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

            if choice == "1":
                print("Result:", calc.add(num1, num2))
            elif choice == "2":
                print("Result:", calc.subtract(num1, num2))
            elif choice == "3":
                print("Result:", calc.multiply(num1, num2))
            elif choice == "4":
                print("Result:", calc.divide(num1, num2))
        elif choice == "5":
            calc.show_history()
        elif choice == "6":
            calc.clear_history()
        else:
            print("Invalid choice. Please try again.")
