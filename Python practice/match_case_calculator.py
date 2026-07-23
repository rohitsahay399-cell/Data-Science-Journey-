
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operations = input("Enter the operation you want to perform (+,-,*,/): ")
match operations:
      case "+":
         print(f"The sum of {num1} and {num2} is: {num1 + num2}")

      case "-":
          print(f"The difference of {num1} and {num2} is: {num1 - num2}")

      case "*":
          print(f"The product of {num1} and {num2} is: {num1 * num2}")

      case "/":
          if num2 != 0:
              print(f"The division of {num1} and {num2} is: {num1 / num2}")
          else:
               print("Division by zero is not allowed.")

                