# take parameter s in a function that will right_justify() to a 70 column display

def right_justify(word):
    padded_word = " "
    for w in range(69 - len(word)):
        padded_word = padded_word + " "
    final = padded_word + word
    return final


which_word = input("What word would you like to right justify? ")
print(right_justify(which_word))
