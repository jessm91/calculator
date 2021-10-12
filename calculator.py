print("Python Calculator [enter 'q' to quit]")

while True:
    function = input("Would you like to add, subtract, multiply or divide? Please choose one: ")

    if function == 'q':
        break
        
#User enters 2 numbers
    first_numb = input("Enter the first number: ")
    sec_numb = input("Enter the second number: ")

#addition, subtraction, multiply, divide
    if function == 'add':
        answer = int(first_numb) + int(sec_numb)
        print(answer)
    elif function == 'subtract':
        answer = int(first_numb) - int(sec_numb)
        print(answer)
    elif function == 'multiply':
        answer = int(first_numb) * int(sec_numb)
        print(answer)
    elif function == 'divide':
        answer = int(first_numb) / int(sec_numb)
        print(answer)
