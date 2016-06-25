import renten_rechnung.renten_rechnung

while True:
    print("What would you like to calculate?")
    print("1: Renten Rechnung")
    chosen_calculation = int(input("Choose the desired calculation:"))
    if chosen_calculation == 1:
            renten_rechnung.main()
print("test")
