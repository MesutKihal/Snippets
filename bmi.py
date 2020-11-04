def BMI_Calc(weight, height):
    bmi = weight / ((height/100) ** 2)

    if 18.5 <= bmi <= 25:
        output = 'You are within the ideal weight range.'

    if bmi < 18.5:
        output = 'You are underweight. You should see your doctor.'

    if bmi > 25:
        output = 'You are overweight. You should see your doctor.'

    return f'Your BMI is {round(bmi)}.\n{output}'



result = BMI_Calc(int(input('What is your body weight, in kilograms(Kg). ')),
                  float(input('What is your height, in centmeters(cm) ')))

print(result)
