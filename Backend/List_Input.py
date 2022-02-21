#import find_user.py

#intro statement
print("Hello your list reminder!\nTo get started we need to know if you already have a list in our system.\nIf you already have a list type \"Yes\" if not type \"No\".")

#database to store users and their txt files
master_user_database = {}

#class list and variables
class user_profile:

    def __init__(user):
        user.phonenumber = ""
        user.reminder_list.txt

# initial list finding or new list creation
test_trial = 0
while(test_trial < 2):
    user_response = input("Please type your response here:")    
    print("To verify you typed: " + user_response)
    if(user_response == "Yes"):
        print("\nYou have stated that you have a list of reminders stored. \nPlease enter your phone number so we can retrieve it.\n")
        user_phonenumber = input("Please type in your ten digit phone number:")
        test_trial = 3
    elif (user_response == "No"):
        print("You will now to redirected to create a new reminder list.  \nPlease enter a phonenumber to be associated with your acocunt:")
        user_phonenumber = input("Please type in your ten digit phone number: ")
        test_trial = 3
    else:
        test_trial += 1
        print("Your input did not match either of the acceptable responsese.  You have two attempts before the program closes.  Please try again.")

#Call to Database using the phone number as the unique identifier
def find_user(user_phonenumber)

