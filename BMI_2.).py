while True:

    height = float(input("Enter your height: "))

    weight = int(input("Enter your weight: "))

    bmi_cal = weight / (height*height)

    if bmi_cal < 18:
        print(f"Your BMI is {bmi_cal}, you are underweight")
    elif bmi_cal <=22:
        print(f"Your BMI is {bmi_cal}, you have a normal weight.")
    elif bmi_cal <29:
        print(f"Your BMI is {bmi_cal}, you are slightly overweight")
    elif bmi_cal < 33:
        print(f"Your BMI is {bmi_cal}, you are obese")
    else:
        print(f"Your BMI is {bmi_cal}, you are clinically obese")
    print(f"your bmi {bmi_cal}")
    exit = 'y'
    user_exit_input = input("DO you wanna exit? press y ")
    if user_exit_input == exit:
        print("Thank you")
        break