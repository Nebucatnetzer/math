#!/usr/bin/env python
#
#Kn=Ko*q^n+r*((q^n-1)/(q-1))
#Kn=80000.-
#Ko=20000.-
#n=18 Jahre=216 Monate
#q=1+((z/100)/12)=1+((1.2%/100)/12)=1.001
#r=250.-

z = 0
Kn = 0
Ko = 0
n = 0
r = 0

def choose_values():                                                    
    Kn = float(input("Wie gross soll der Endbetrag sein?"))
    Ko = float(input("Wie gross ist das Startkapital?"))
    n = float(input("Über wieviele Jahre wird einbezahlt?"))
    z = float(input("Wie hoch ist der Zins?"))
    r = float(input("Wie hoch ist die monatliche Rate?"))


def main():
    choose_values()
    q = 1+((z/100)/12)
    Kn = Ko*q**n+r*((q**n-1)/(q-1))
    print(Kn)

if __name__ == "__main__": main()
