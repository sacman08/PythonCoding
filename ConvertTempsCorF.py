# Convert Celsius to Fahrenheit

def convert_F_to_C(deg):
    cent = (deg * 1.8) + 32
    return '%.1f' % cent


def convert_C_to_F(deg):
    fahr = (deg - 32) / 1.8
    return '%.1f' % fahr


which_temp_to_convert = input("What type of temp to convert? (C or F)")

if which_temp_to_convert == "f" or which_temp_to_convert == "F":
    deg_in_F = float(input("Enter the Fahrenheit temp:"))
    print(f'{deg_in_F} F converts to', convert_C_to_F(deg_in_F), "C.")
elif which_temp_to_convert == "c" or which_temp_to_convert == "C":
    deg_in_C = float(input("Enter the Celsius temp:"))
    print(f'{deg_in_C} C converts to ', convert_F_to_C(deg_in_C), "F.")
