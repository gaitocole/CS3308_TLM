#!/usr/bin/python3

#Import List
#import find_user.py
import Testing.phone_number_test as phone_number_test
import add_to_database

#intro statement
print("\nHello your list reminder!\nTo get started we need to know if you already have a list in our system.\nIf you already have a list, type \"Yes\" if not type \"No\".")

#database to store users and their txt files
#master_user_database = {}

#Basic Function Definitions
def test(phonenumb):
    if (phone_number_test.correct_length(phonenumb) and phone_number_test.only_digits(phonenumb)):
        return True
    elif(phone_number_test.only_digits(phonenumb) != True ):
        print("\nPlease type your phone number without delinations such as ( or ) or -.")
    else:
        print("\nPlease type in 10 numbers.")

def last_try(cycle):
    if cycle > 2:
        print("This is your last entry prior to the program closing.")

    


# initial list finding or new list creation
test_trial = 0
inner_test_trial = 1
while(test_trial < 3):
    user_response = input("\nPlease type your response here:")    
    print("\nTo verify you typed: " + user_response)
    if(user_response == "Yes"):
        while inner_test_trial < 4:
            last_try(inner_test_trial)
            print("\nYou have stated that you have a list of reminders stored. \nPlease enter your phone number so we can retrieve it.")
            user_phonenumber = input("\nPlease type in your ten digit phone number without any delinations:")
            if(test(user_phonenumber)):
                add_to_database.find_existing_list(user_phonenumber)
                inner_test_trial = 4
            else:
                inner_test_trial += 1
        test_trial = 3
    elif (user_response == "No"):
        while inner_test_trial < 4:
            last_try(inner_test_trial)
            print("\nYou will now to redirected to create a new reminder list.  \nPlease enter a phonenumber to be associated with your acount:")
            user_phonenumber = input("Please type in your ten digit phone number: ")
            if(test(user_phonenumber)):
                add_to_database.create_new_list(user_phonenumber)
                inner_test_trial = 4
            else:
                inner_test_trial += 1
        test_trial = 3
    else:
        last_try(test_trial)
        test_trial += 1
        print("Your inputs did not match either of the acceptable responsese.  You have three attempts before the program closes.  Please try again.")


#Call to Database using the phone number as the unique identifier
#def find_user(user_phonenumber)

