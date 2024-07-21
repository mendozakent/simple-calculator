from calculator import add, subtract, multiply, divide,validate_number, round_result

print(r"""
 _____       _            _       _             
/  __ \     | |          | |     | |            
| /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| \__/\ (_| | | (__| |_| | | (_| | || (_) | |   
 \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                    """)
print("""
 This is a calculator that performs basic arithmetic calculations.
 
 To begin please follow the steps below.
                    """)

while True:
    try:
        num1 = validate_number(input("Enter the first number: "))
        num2 = validate_number(input("Enter the second number: "))

        operation = input("""
Available Operations include:
            
    [+] -- To Add
            
    [-] -- To Subtract
            
    [*] -- To Multiply
            
    [/] -- To Divide

Enter an Operation:  """)

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            print('Invalid Operation')
            continue
        result = round_result(result)
        print(f'\nResult: {result}')

    except ValueError as e:
        print(f'Error: {e}')

    tryAgain = input('\nDo you want to perform another calculation? (Yes/No): ')
    if tryAgain.lower() != 'yes':
        break

