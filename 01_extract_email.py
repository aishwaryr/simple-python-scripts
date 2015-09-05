
user_input = raw_input('Enter the string: ')


#checks if a string is a valid Email address
def is_valid_address(some_string):
    pos_at  = some_string.find('@')
    pos_dot = some_string.find('.')
    if pos_at is -1 and pos_dot is -1:
        return False
    if pos_at > pos_dot:
        return False
    if (pos_dot - pos_at) == 1:
        return False
    if some_string.count('@') > 1:
        return False
    if pos_at == 0 or pos_dot == len(some_string)-1:
        return False

    return True

#user input
#this space is added to take care of the case where the first string is the Email address.
if user_input[-1] == '.':
    user_input = user_input[:-1]
    user_input = ' '+user_input+' '
    # print ('Removed fullstop.\n')
 
if '@' not in user_input or (user_input.count(' ',user_input.find('@') , user_input.find('.'))) > 0 :
    #Or part checks if ther spaces in email address. If yes gives error.
    print ('No valid email address found.')
elif ' ' not in user_input:
    if is_valid_address(user_input):
        print ('The email address is ' + user_input)
    else:
        print ('No valid email address found.')
#case when user inputs a string with spaces in between
else:
    at = 0
    while True:
        start = user_input.find(' ' , at)
        end = user_input.find(' ' , start + 1)
        # print ('start = ' + str(start) + ' and end = ' + str(end))
        if is_valid_address(user_input[start:end]):
            print ('Address is : ' + user_input[start:end])
            break
        else:
            at = end
            if at == -1:
                print ('No valid email address found.')
                break