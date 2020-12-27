#Use the password policy in first section to verify the password in second section 
#Example: 2-5 j: durjwejdfkn  (First uses j 2 to 5 times, password valid)
#How many passwords are valid according to their policy?
#from random import randint
#open raw data file to read
with open('PassList.txt') as pass_file:
  #Create a dictionary variable for storing key and values
  pass_list1 = []
  #assign key and values to dictionary
  #Loop through file to strip the "\n", and split on the ":" into keys and values
  #o = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '1','2','3','4','5','6','7','8','9','0']
  
  for line in pass_file:
    #o_rand = randint(0,35)
    stripped_line = line.strip()
    pass_list1 = stripped_line.split(":")
    #pass_list1[key+' '+o[o_rand]] = val
    
  #Close file to release it  
  pass_file.close

key_policy = []

total_compliant = 0

for pass_str in pass_list1:
  #find the policy by split at the '-' to get start and stop count
  key_policy = pass_str[0].split("-")
  print(key_policy)
  #change the start str to int (i.e '1' to 1)
  key_start = (int(key_policy[0]))
  #key_start = int(key_start)
  #set the stop string
  key_stop = key_policy[1]
  #slice out the number as int ( i.e '5 j' to 5) 
  key_stop = int(key_stop[0:2])
  #Grab the key char and slice out for each password (i.e '5 j' to 'j')
  key_id = key_policy[1]
  key_id = key_id[2:4]
  key_id = key_id.strip()
  
  value = pass_list1[key]
    #Grab the key character and count in values
  pass_count = value.count(key_id)
    #Compare the count the require min and max, add up correct
  print(key, total_compliant, key_id, key_start, key_stop, key_policy, pass_count, value)
  if pass_count > key_start and pass_count < key_stop:
    total_compliant += 1
    continue
  elif pass_count == key_start and pass_count < key_stop:
    total_compliant += 1
    continue
  elif pass_count == key_stop and pass_count > key_start:
    total_compliant += 1
    continue
  elif pass_count == key_start and pass_count == key_stop:
    total_compliant += 1
    continue
