# Luhn Algorithm
# Remove right most digit
# Reverse the digits
# Take the even digits (0,2,4,6, etc.) and double it
# If any double digit > 9 then subtract 9 from it
# Add together all the digits
# If the total results is divisible by 10 means it's a valid card number

def luhn_algorithm(card_number):
    card_number = str(card_number)
    card_number = map(int, card_number)
    card_number = list(card_number)  # convert number to a mutable list
    end_digit = card_number.pop(15) # Drop the last digit
    card_number.reverse()  # reverse the numbers
    for number in range(0, 15, 2):  # take our even digits, double them and subtract 9
        card_number[number] = (card_number[number] * 2)
        if card_number[number] > 9:
            card_number[number] = (card_number[number] - 9)
    card_number.append(end_digit)  # put our end digit back on
    if sum(card_number) % 10 == 0:  # if the sum of our numbers is dividable by 10 then true, else false.
        check_value = True
    else:
        check_value = False
    return check_value


print(luhn_algorithm())
