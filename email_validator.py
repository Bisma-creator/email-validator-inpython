import re
from email_validator import validate_email, EmailNotValidError

def valid_email_basic_cond(email):
    if email.count('@') != 1:
        print("Invalid Email , Email must contain atleast one @ symbol.") #check if email address have @ symbol
        return False
    
    localpart , domain = email.split('@') #spliting the local part and domain of email address by @

    if not localpart:
        print("Invalid Email , Email must contain a localpart.") #check if loacl part of email address is present or not
        return False

    if not domain:
        print("Invalid Email , Email must contain a domain.") #check if email address contain domain
        return False

    if not '.':
        print("Invalid Email , Email must contain a '.' in the domain.") #check if domain contains 1 dot
        return False

    basic_pattern = r"^[a-zA-Z0-9_.±]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$" #basic pattern for a valid 
                                                                        #email email address structure
    if not re.match(basic_pattern, email):
        print("Invalid Email , Email must have basic pattern")
        return False

    return True

def valid_email_address(email):
    try:
        valid = validate_email(email) #validate the email address using the email_validator module
        print(f"The email '{valid.email}' is valid.") #if email address is valid then return the email address 
    except EmailNotValidError as e:
        print(f"The email '{email}' is not valid: {e}") #else print error message

email = input("Enter Your Email Address: ") #Take email address as input from user

if valid_email_basic_cond(email): #check the email address with basic conditions
    valid_email_address(email) #if basic check pass then email address is valid   