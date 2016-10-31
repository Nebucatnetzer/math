import pension.calculate
while True:
    print("What would you like to calculate?")
    print("1: Pension Calculation")
    chosen_calculation = int(input("Choose the desired calculation:"))
    if chosen_calculation == 1:
            pension.calculate.interest()
print("test")
