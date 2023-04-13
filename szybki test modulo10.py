print("type a number, I'll tell you if its multiplied by 10: ")
input_number = ""
while input_number != 'quit':
    input_number = input(print)
    if input_number.isdigit():
        input_number =int(input_number)
        if (input_number %10) == 0:
            print('yes')
        else:
            print('no')
    else:
        print('please type in an integer')