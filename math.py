import pension_calculation
from pension_calculation import calculation 
while True:
    print("What would you like to calculate?")
    print("1: Pension Calculation")
    chosen_calculation = int(input("Choose the desired calculation:"))
    if chosen_calculation == 1:
            calculation.calculate_interest()
print("test")
