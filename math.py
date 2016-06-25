import pension_calculation
from pension_calculation import pension_calculation
while True:
    print("What would you like to calculate?")
    print("1: Pension Calculation")
    chosen_calculation = int(input("Choose the desired calculation:"))
    if chosen_calculation == 1:
            pension_calculation.calculate_interest()
print("test")
