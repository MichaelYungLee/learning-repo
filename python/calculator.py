import operator
import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def clear():
    os.system("clear")

def evaluate_expression(op1, oper, op2):
    return ops[oper](op1, op2)

def main():
    print(logo)
    op1 = None
    while True:
        if not op1:
            op1 = float(input("What's the first number?: "))
        for op in ops:
            print(op)
        oper = input("Pick an operation: ")
        op2 = float(input("What's the next number?: "))

        result = evaluate_expression(op1, oper, op2)
        print(f'{op1} {oper} {op2} = {result}')
        
        response = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calcuation: ")
        if response == 'y':
            op1 = result
        else:
            op1 = None
            clear()

if __name__ == "__main__":
    main()