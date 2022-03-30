#!/usr/bin/python3

#import find_user.py
#import add_to_database.py
import re


def minLength(pwInput):
    if len(pwInput) >= 8:
        return True
    else:
        return False

def reqChars(pwInput):
    reqLetter = re.search("(?=.*\d)(?=.*[a-zA-Z])", pwInput)
    reqNum = re.search("\d", pwInput)    
    if (reqLetter == None) or (reqNum == None):
        return False
    else:
        return True


def testInput(pwInput1):
    if (minLength(pwInput1) == True) and (reqChars(pwInput1) == True):
        return True
    elif minLength(pwInput1) != True:
        print("\nPasswords must be a minimum of eight characters long.")
    else:
        print("\nPasswords must contain at least one number and one letter.")


def testMatch(pwInput1, pwInput2):
    if pwInput1 == pwInput2:
        return True
    else:
        return False

#Note: The input for this will eventually come from user input at the webpage rather than through the terminal.
def passwordInput():
    pwTries = 0
    while(pwTries < 2):
        
        #Allows user to exit new password dialogue.
        if (pwTries > 0):
            retryInput = input("\nEnter q to quit or t to try again:\n")
            if (retryInput == 't'):
                pwTries = 0
                continue
            elif (retryInput == 'q'):
                print("\nReturning to login screen.")
                break
            else:
                continue
        
        pwInput1 = input("\nPlease enter a new password.\nPasswords must be a minimum of eight characters long and contain at least one number and one letter:\n")
        pwSyntaxTest = testInput(pwInput1)
        
        if (pwSyntaxTest == True):
            pwInput2 = input("\nPlease re-enter your password:\n")
            pwMatchTest = testMatch(pwInput1, pwInput2)
            
            if (pwMatchTest == True):
                #This will ultimately result in the entered password being hashed and entered into the database along with the new user information.
                print("\nPassword accepted.")
                break
            else:
                print("\nThe passwords entered do not match.")
                pwTries +=1
                continue

        else:
            pwTries +=1
            continue

def main():
	passwordInput()

if __name__ == "__main__":
	main()