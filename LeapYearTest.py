leapyear = []

def check_for_leap(leapyear):
    #Quick and dirty check, not looking for the /100 or /400.
    if leapyear % 4 == 0:
        if leapyear % 400 == 0:
            print('Leap year.')
        elif leapyear % 100 == 0:
            print('Not a leap year.')
    else:
        print('Not a leap year.')


check_for_leap(int(input('Please enter a year to check for leap year:')))
