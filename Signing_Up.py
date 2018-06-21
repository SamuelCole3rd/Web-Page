import time
import random
import sys

code = ''
points = 0
points_earned = 0
name = ''
email = ''

def entered_info(name,email):
    try:
        with open('Save_Data.txt') as f:
            for line in f:
                if name in line:
                    return True
    except FileNotFoundError:
        pass
    return False

def user_name():
    global name
    while True:
        print("Please type in a user name.")
        response = input()
        name = response
        print("Would you like to use that as your user name? [yes] or (no)")
        response = input().lower()
        if response == "yes":
            print("Alright than moving on to the password.")
            password()
        elif response == "no":
            print("Please retry and change the username than.")

def password():
    global code
    while True:
        print("Please type in a password.")
        response = input()
        code = response
        print("Would you like to use this as your password? [yes] or (no)")
        response = input().lower()
        if response == "yes":
            print("Okay than.")
            email_setup()
        elif response == "no":
            print("Please type in a password.")

def email_setup():
    global email
    while True:
        print("Please type in a valid user for your email.")
        response = input()
        print(response+'@rebank.com', "Would you like to this as your email? [yes] or (no)")
        email = response+'@rebank.com'
        response = input().lower()
        if response == "yes":
            print("Alright than.")
            points_generator() 
        elif response == "no":
            print("Please retry and enter a valid user for your email.")

def points_generator():
    global points
    global points_earned
    print("Here we will generate the number of points that you will have.")
    time.sleep(1)
    print("The number of points that you have is...")
    time.sleep(1)
    points = ['5000','5500','6000','6500','7000','7500','8000','8500','9000','9500','10000']
    points_earned = random.choice(points)
    print(points_earned)
    time.sleep(1)
    save()

def save():
    print("Would you like to save your data? [yes] or (no)")
    response = input().lower()
    if response == "yes":
        print("Okay than.")
        time.sleep(1)
        if entered_info(name,email):
            print("I'm sorry but the following info was already entered. Please restart the program and try a different set of info.")
            quit()
        else:
            print("Here you are. Thank you for using this program and have a nice day.")
            f = open('Save_Data.txt', 'a')
            f.write(f"{name}, {email}, {points_earned}, {code}\r\n")
            f.close()
            time.sleep(1)
            quit()
    elif response == "no":
        print("You have reached the end of this program. Thank you and have a nice day.")
        time.sleep(1)
        quit()

print("Hello there. Would you like to start our program? [yes] or (no)")
response = input().lower()
if response == "yes":
    print("Let's get started than.")
    time.sleep(1)
    user_name()
elif response == "no":
    quit()