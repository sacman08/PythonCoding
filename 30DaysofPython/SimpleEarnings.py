# Simple earnings application
# Ask for their name, hourly wage, how many hours were worked.
# Calculate the money made.
# NOTE: Added looping with while and try statements to correct information entered.


def earnings_info():
    while True:
        name = input("What is your name: ")
        hourly_wage = input("What is your hourly wage: ")
        hours_worked = input("How many hours did you work this week: ")
        try:
            if name == "" or hourly_wage == "" or hours_worked == "":
                print("Please enter valid information!")
                continue
            elif float(hours_worked) < 5 or float(hours_worked) > 120:
                print("Please enter reasonable hours worked!")
                continue
            elif float(hourly_wage) < 7.5:
                print("Are you working for pennies? Please enter a reasonable wage!")
                continue
            elif float(hourly_wage) > 50:
                print("Are you REALLY making all that cash? Please enter a normal wage!")
                continue
            else:
                wage_earned = float(hourly_wage) * float(hours_worked)
                print(f'{name.title()}\'s gross pay is ${wage_earned:.2f} this week!')
                break
        except Exception as e:
            print(e)


print("""
    Welcome to the Simple Earnings application!
    Please enter the relevant information to 
    calculate your wages! """)
earnings_info()
