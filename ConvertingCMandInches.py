from fraction import Fraction


def convtoFrac(measure):
    fract = Fraction(measure)
    return '%.2f' % fract

def convtoCM(measure):
    cm = measure * 2.54
    return cm

def convtoIN(measure):
    inch = measure * .39370079
    return inch

units = int(input("What measurement unit use: 1 for cm, 2 for inch"))
if units == 1:
    length = int(input("Enter the length in cm:"))
    print(convtoCM(length))
                 
elif units == 2:
    length = int(input("Enter the length in inches:"))
    print('The length in inches is', convtoFrac(convtoIN(length)))
                 
else :
    print('Please enter a valid choice')
    
