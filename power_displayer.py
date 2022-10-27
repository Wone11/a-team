
# Awash Bank
# This is day 3 afternoon session - bout Devops

# Write python code that display the power of given list

# function that displays power of lists
def display_list(power):
    numbers=[1,2,3,4,5,6,7,8,9]
    powered_list = []
    for number in numbers:
        powered_list.append(number**power)
    
    print('Original list:', numbers)
    print('Powered list:', powered_list)

# We can accept the length of power from user or 
# Directly pass to the function
display_list(2)   # Directly passing actual value to function
#display_list(3)
