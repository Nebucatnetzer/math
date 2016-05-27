#!/usr/bin/env python
# Todo: n muss noch in Monate umgerechnet werden
#Kn=Ko*q^n+r*((q^n-1)/(q-1))
#Kn=80000.-
#Ko=20000.-
#n=18 Jahre=216 Monate
#q=1+((z/100)/12)=1+((1.2%/100)/12)=1.001
#r=250.-

values_chosen = False

def choose_values():
    global values_chosen
    values.desired_capital = float(input("Wie gross soll der Endbetrag sein? "))
    values.start_capital = float(input("Wie gross ist das Startkapital? "))
    values.period_in_years = float(input("Über wieviele Jahre wird einbezahlt? "))
#    values.interest = float(input("Wie hoch ist der Zins? "))
    values.rate = float(input("Wie hoch ist die monatliche Rate? "))
    values_chosen = True

def calculate_compounding_factor():
    print("Calculating the compounding factor")
    values.compounding_factor = 1 + ((values.interest / 100) / 12)
    print(values.compounding_factor)

def years_to_months():
    print("Calculating years into months")
    values.period_in_months = values.period_in_years * 12
    print(values.period_in_months)

def calculate_pension():
    #print("Calculating Pension")
    values.calculated_capital = (values.start_capital * 
    values.compounding_factor ** values.period_in_months + values.rate * 
    ((values.compounding_factor ** values.period_in_months - 1) / 
    (values.compounding_factor - 1)))
    #print(values.calculated_capital)

def increase_interest():
    #print("Increasing interest")
    values.interest += 0.0001
    #print(values.interest)
    


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

values = Calculation(interest=0.0001, desired_capital=1, start_capital=0, 
        period_in_years=0, period_in_months=0, rate=0, 
        compounding_factor=0, calculated_capital=0) 

def main():
    while values.calculated_capital < values.desired_capital:
        if not values_chosen:
            choose_values()
            years_to_months()
            calculate_compounding_factor()
            calculate_pension()
        increase_interest()
        calculate_pension()
    print(values.rate)

if __name__ == "__main__": main()
