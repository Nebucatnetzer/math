#!/usr/bin/env python

# This is the calculation the function is based on.
# Kn=Ko*q^n+r*((q^n-1)/(q-1))
# Kn= calculated_capital
# Ko= start_capital
# n= period_in_months
# q= compounding_factor = 1+((z/100)/12)=1+((1.2%/100)/12)=1.001
# r= monthly payment rate
# z= interest

# global variable to lock the choose_values function after it ran once
values_chosen = False


# function to enter the values to calculate with
def choose_values():
    global values_chosen
    values.desired_capital = float(input("Wie gross soll der Endbetrag sein? "))
    values.start_capital = float(input("Wie gross ist das Startkapital? "))
    values.period_in_years = float(input("Über wieviele Jahre wird einbezahlt? "))
    values.rate = float(input("Wie hoch ist die monatliche Rate? "))
    values_chosen = True


# function to calculate the compounding factor from the interest
def calculate_compounding_factor():
    # print("Calculating the compounding factor")
    values.compounding_factor = 1 + ((values.interest / 100) / 12)
    # print(values.compounding_factor)


# convert period_in_years variable into months
def years_to_months():
    # print("Calculating years into months")
    values.period_in_months = values.period_in_years * 12
    # print(values.period_in_months)


# the main pension formula in python
def calculate_pension():
    # print("Calculating Pension")
    values.calculated_capital = (values.start_capital *
                                 values.compounding_factor ** values.period_in_months + values.rate *
                                 ((values.compounding_factor ** values.period_in_months - 1) /
                                  (values.compounding_factor - 1)))
    # print(values.calculated_capital)


# function to increase the interest by a small amount
def increase_interest():
    # print("Increasing interest")
    values.interest += 0.000001
    # print(values.interest)


# main class
class Calculation(object):
    def __init__(self, interest, desired_capital, start_capital, period_in_years,
                 period_in_months, rate, compounding_factor, calculated_capital):
        self.interest = interest
        self.desired_capital = desired_capital
        self.start_capital = start_capital
        self.period_in_years = period_in_years
        self.period_in_months = period_in_months
        self.rate = rate
        self.compounding_factor = compounding_factor
        self.calculated_capital = calculated_capital


# initializing the values
values = Calculation(interest=0.0001, desired_capital=1, start_capital=0,
                     period_in_years=0, period_in_months=0, rate=0,
                     compounding_factor=0, calculated_capital=0)


# Beginning of the main function
# if the calculated capital is smaller than the desired capital it will
# increase the interest and try again until the calculated capital is
# larger than the desired capital then it prints the calculated capital
# and the interest which reached that capital.n
def main():
    while values.calculated_capital < values.desired_capital:
        if not values_chosen:
            choose_values()
            years_to_months()
            calculate_compounding_factor()
            calculate_pension()
        increase_interest()
        calculate_compounding_factor()
        calculate_pension()
    print("Bei einem Zins von ", values.interest, " erhalten sie nach ",
          values.period_in_years, " Jahren")
    print(values.calculated_capital, " Franken")


if __name__ == "__main__": main()
