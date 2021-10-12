print("Python Calculator [enter 'q' to quit]")

while True:
    #user input
    function = input("Would you like to add, subtract, multiply or divide? Please choose one: ")

    if function == 'q':
        break

    first_numb = input("Enter the first number: ")
    sec_numb = input("Enter the second number: ")

#addition, subtraction, multiply, divide
    if function == 'add':
        try:
            answer = int(first_numb) + int(sec_numb)
        except ValueError:
            print("Please enter numbers only!")
        else:
            print(answer)
    elif function == 'subtract':
        try:
            answer = int(first_numb) - int(sec_numb)
        except ValueError:
            print("Please enter numbers only!")
        else:
            print(answer)
    elif function == 'multiply':
        try:
            answer = int(first_numb) * int(sec_numb)
        except ValueError:
            print("Please enter numbers only!")
        else:
            print(answer)
    elif function == 'divide':
        try:
            if int(first_numb) == 0:
                answer = 0
            elif int(sec_numb) == 0:
                answer = "Error"
            else:
                answer = int(first_numb) / int(sec_numb)
        except ValueError:
            print("Please enter numbers only!")
        else:
            print(answer)
