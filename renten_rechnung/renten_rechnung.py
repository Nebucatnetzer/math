#!/usr/bin/env python
# Todo: n muss noch in Monate umgerechnet werden
#Kn=Ko*q^n+r*((q^n-1)/(q-1))
#Kn=80000.-
#Ko=20000.-
#n=18 Jahre=216 Monate
#q=1+((z/100)/12)=1+((1.2%/100)/12)=1.001
#r=250.-

z = 1 
Kn = 1
Ko = 1 
n = 1
r = 1

def choose_values():                                                    
    Kn = float(input("Wie gross soll der Endbetrag sein?"))
    Ko = float(input("Wie gross ist das Startkapital?"))
    n = float(input("Über wieviele Jahre wird einbezahlt?"))
    z = float(input("Wie hoch ist der Zins?"))
    r = float(input("Wie hoch ist die monatliche Rate?"))


def main():
    choose_values()
    q = 1+((z/100)/12)
    Kn = (Ko*q**n+r*((q**n-1)/(q-1)))
    print(Kn)
    print(Ko)
    print(n)
    print()
    print()
    print()

if __name__ == "__main__": main()
