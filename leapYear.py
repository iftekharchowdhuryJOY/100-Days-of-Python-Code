while True:
    year = int(input("Enter the year: "))

    if year % 4 == 0 and year % 400 == 0 and year % 100 == 0:
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")

    exit = 'y'
    user_exit_input = input("DO you wanna exit? press y ")
    if user_exit_input == exit:
        print("Thank you")
        break