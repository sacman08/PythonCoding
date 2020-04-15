#Convert Celsius to Fahrenheit

def convert(deg):
    sec = (deg * 1.8) +32
    return '%.1f' % sec


def convert2(deg):
    fahr = (deg-32)/1.8
    return '%.1f' % fahr

deg = float(input("Enter the Celsius temperature to convert:"))
print(convert(deg))


fahr = float(input("Enter the Fahrenheit temperature to convert:"))
print(convert2(fahr))
