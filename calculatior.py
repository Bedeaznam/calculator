class calculator:
    def __init__(self):
        print("Welcome to coldculator")


    def devide(self, a , b):
        if b != 0:
         return a/b

    def multiply(self, a ,b):
        return a*b

    def minus(self, a, b):
        return a - b

    def plus (self, a, b):
      return a+b


if __name__ == "__main__":
    calc = calculator()

while True:
    print("\nSelect an operation:")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exit")

    coice = input("Enter your choice: ")


    if coice == "5":
        print("Goodbye!")
        break


    num1: float = float(input("Enter first number: "))
    num2: float = float(input("Enter second number: "))

    if coice == "1":
        print(calc.plus(num1,num2))
    elif coice == "2":
        print(calc.minus(num1,num2))
    elif coice == "3":
        print(calc.multiply(num1,num2))
    elif coice == "4":
        print(calc.divide(num1,num2))
    else:
        print("Invalid input")



