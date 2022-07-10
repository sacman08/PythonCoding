#Program to counter letters in msg

welcome = 'Welcome to the Character Counting program!'

print(welcome)

msg = input('Please enter a message:')
msg_letter = input('Please enter the letter to be counted.')

msg_count = msg.count(msg_letter)
msg_perc = round((msg_count / len(msg))*100)
print(f'Your letter, {msg_letter}, was counted {msg_count} times: {msg_perc}%')