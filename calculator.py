print("Python Calculator [enter 'q' to quit]")

while True:
    function = input("Would you like to add, subtract, multiply or divide? Please choose one: ")

#User enters 2 numbers
    first_numb = input("Enter the first number: ")
    sec_numb = input("Enter the second number: ")

    if function == 'q' or first_numb == 'q' or sec_numb == 'q':
        break

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
