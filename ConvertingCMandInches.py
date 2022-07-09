def convert_to_centimeters(measure):
    cm = measure * .39370079
    return cm


def convert_to_inches(measure):
    inch = measure * 2.54
    return inch


units = int(input("What measurement unit use: 1 for cm, 2 for inch: "))
if units == 1:
    length = float(input("Enter the length in cm: "))
    print(f'{length} cm in inches is', '%2.f' % convert_to_centimeters(length))

elif units == 2:
    length = float(input("Enter the length in inches: "))
    print(f'{length} inches in centimeters is', '%2.f' % convert_to_inches(length))

else:
    print('Please enter a valid choice')
