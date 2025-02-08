import art

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def divide(n1,n2):
    return n1 / n2

def multiply(n1,n2):
    return n1 * n2

operations = {"/":divide,
              "*":multiply,
              "+":add,
              "_":subtract}
def calculator():
    print(art.logo)
    continue_calculation = True
    n1 = float(int(input("what's the 1st number:")))
    while continue_calculation:
        operation = input("/\n*\n+\n-\nchoose a mathematical operation:")
        n2 = float(int(input("what's the 2nd number:")))
        for key in operations:
            if operation == key:
                calculate = operations[key]
                result = calculate(n1, n2)
                print(result)
        further = input(f"type y to continue calculating with {result} or type 'n' to start a new calculation:")
        if further == "y":
            n1 = result
        elif further == "n":
            continue_calculation = False
            print("\n" * 20)
            calculator()
        else:
            print("Check the input you gave")
calculator()


