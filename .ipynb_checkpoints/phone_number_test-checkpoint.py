#!/usr/bin/python3

def correct_length(phone_number):
    length_of_phonenumber = len(phone_number)
    
    if(length_of_phonenumber) == 10:
        return True
    else:
        return False

def only_digits(phone_number):
    valid = phone_number.strip().isdigit()

    if valid:
        return True
    else:
        return False