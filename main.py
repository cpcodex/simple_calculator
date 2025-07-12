def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "ERROR: Cannot Divide by zero."
    return num1 / num2

def options(opt, num1, num2):
    if opt == 1:
        result = add(num1,num2)
        print(result)
    elif opt == 2:
        result = subtract(num1,num2)
        print(result)
    elif opt == 3:
        result = multiply(num1,num2)
        print(result)
    elif opt == 4:
        result = divide(num1,num2)
        print(result)
    else:
        print('Invalid input')
  
def seperator():
    print("=" * 24)

def questions():
    print("1.) Add\n2.) Subtract\n3.) Multiply\n4.) Divide")
    seperator()

# intro
print("\nWelcome to The Simple-Calculator!\n")
while True:   
    # inputs
    num1_input = input("Please enter a number (or type 'exit' to quit): ")
    if num1_input.lower() == 'exit':
        break
    num1 = int(num1_input)
    
    num2_input = input("Please enter a number (or type 'exit' to quit): ")
    if num2_input.lower() == 'exit':
        break
    num2 = int(num2_input)
    seperator()
    
    # prompt
    questions()
    option = int(input())
    seperator()
    
    # answer
    print('Answer:')
    options(option, num1, num2)