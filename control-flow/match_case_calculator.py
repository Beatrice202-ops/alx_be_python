num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
user = input("Choose the operation (+, -, *, /): ")

match user:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("error: division by zero is not allowed" )
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("invalid calculation")

        
    
    

    