

def convtoCM(measure):
    cm = measure * .39370079
    return cm

def convtoIN(measure):
    inch = measure * 2.54
    return inch

units = int(input("What measurement unit use: 1 for cm, 2 for inch: "))
if units == 1:
    length = float(input("Enter the length in cm: "))
    print('The length in inches is', '%2.f' % convtoCM(length))
                 
elif units == 2:
    length = float(input("Enter the length in inches: "))
    print('The length in cetemeters is', '%2.f' % convtoIN(length))
                 
else :
    print('Please enter a valid choice')
    
