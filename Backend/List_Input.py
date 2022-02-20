print("Hello your list reminder!\nTo get started we need to know if you already have a list in our system.\nIf you already have a list type \"Yes\" if not type \"No\".")

test_trial = 0

#need to add a loop incase the user enters the wrong input, but wants to access the correct information
while(test_trial < 2):
    user_response = input("Please type your response here:")
    #no isn't working, nor the cycle to verify a correct response
    if (user_response ==("Yes" or "No")):
        test_trial = 3
        print("To verify you typed: " + user_response)
        if(user_response == "Yes"):
            print("\nYou have stated that you have a list of reminders store. \nWe are retrieving it now.")
        else:
            print("You will now to redirected to create a new reminder list.")
    else:
        test_trial += 1
        print("Your input did not match either of the acceptable responsese.  Please try again.")

