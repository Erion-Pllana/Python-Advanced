while True:
    user_input = input("Enter a apositive number: ")

    if user_input.isnumeric():
        number = int(user_input)

        if number > 0:
            break

        print ("Invalid input, Please try again.")

print("You entered a valid positive number which is: ",number)