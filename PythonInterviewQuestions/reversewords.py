# Ask the user for a sentence. Sort the sentence and then
# return the sentence backwards.
# use a lambda function in this process

# Get our sentence and split on the words
our_sent = input("Please enter a sentence to reverse: ").split()
# Print the words sorted reverse by the last letter of the word
print(sorted(our_sent, key=lambda words: words[::-1]))
# OR just print the words in reverse from how they were entered
print(our_sent[::-1])
