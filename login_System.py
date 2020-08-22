import csv
import sys


def main():
    with open("user_details.txt") as files:
        file_reader = csv.reader(files)
        user_finder(file_reader)
        files.close()


def welcome_message():
    print("Welcome to the portal page")
    print("1. Existing user")
    print("2. New user, register a login")
    user_input = int(input("1, 2 or 3 to quit" + "\n"))
    if user_input == 1:
        main()
    elif user_input == 2:
        new_user()
    elif user_input == 3:
        print("Thanks for your time, Bye!")
        print("Do you like to restart?" + "\n")
        restart_input = raw_input("y/n ?")
        if restart_input == "y":
            welcome_message()
        elif restart_input == "n":
            print('Thanks for your time again!')
            sys.exit()
    else:
        print("Invalid value and start again!")
        welcome_message()


def user_finder(files):
    user = raw_input("Enter your username: ")
    for row in files:
        if row[0] == user:
            print("Email found:" + " " + user)
            user_found = [row[0], row[1]]
            pass_check(user_found)
            portal_page(user_found)
            break
    else:
        print("Email not found")
        print("1. Quit" + "\n" + "2. Re-enter Email" + "\n" + "3.Go back to Welcome page")
        not_found_input = int(input("Choose one: "))
        if not_found_input == 1:
            sys.exit()
        elif not_found_input == 2:
            user_finder(files)
        elif not_found_input == 3:
            welcome_message()
        else:
            print("Invalid input!")
            welcome_message()


def pass_check(user_found):
    user = raw_input("Enter your password: ")
    if user_found[1] == user:
        print("password correct!")
        portal_page(user_found)
    else:
        print("password incorrect")


def new_user():
    new_username = raw_input("Enter new username?: ")
    new_password = raw_input("Enter new password?: ")
    confirm_new_password = raw_input("Confirm password?: ")

    if confirm_new_password == new_password:
        new_details = new_username, confirm_new_password
        save_new_details = open('user_details.txt', 'w')
        save_new_details.write(str(new_details)[1:-1].replace("'", "").replace(" ", ""))
        save_new_details.close()
        print("Registration success!")
    else:
        print("Doesn't match new password.")
        print("Do you like to restart registration or quit?" + "\n" + "1. Restart" + "\n" + "2. Quit")
        not_match_pass_option = int(input("Choose one: "))
        if not_match_pass_option == 1:
            new_user()
        elif not_match_pass_option == 2:
            sys.exit()
        else:
            print("Invalid value!")
            sys.exit()


def portal_page(user_found):
    print("Welcome to your portal page, " + user_found[0])
    print("What will you like to do today? ")
    print("1. Check the e-Library")
    print("2. Calculator")
    user_found_answer = int(input("Choose one: "))
    if user_found_answer == 1:
        e_library()
    elif user_found_answer == 2:
        calculator()
    else:
        print("Invalid value!")
        sys.exit()


def e_library():
    print("Welcome to e-library")
    with open('Library.txt') as f:
        line = f.readline()
        cnt = 1
        while line:
            print("Book {}: {}".format(cnt, line.strip()))
            line = f.readline()
            cnt += 1
    print("Press 1 to go back to welcome or 2 to quit ")
    e_lib_opt = int(input("Choose: "))
    if e_lib_opt == 1:
        welcome_message()
    elif e_lib_opt == 2:
        sys.exit()
    else:
        print("Invalid value")
        sys.exit()


def calculator():
    print("Welcome to calculator")
    print("1. Addition" + "\n" + "2. Subtraction" + "\n" + "3. Division" + "\n" + "4.Multiple")
    cal_input = int(input("Choose one of the following"))
    if cal_input == 1:
        print("Start adding!")
        add_first = int(input("Enter your first value: "))
        add_second = int(input("Enter your second value: "))
        answer = add_first + add_second
        print("Your answer is" + " " + str(answer))
    elif cal_input == 2:
        print("Start subtracting")
        add_first = int(input("Enter your first value: "))
        add_second = int(input("Enter your second value: "))
        answer = add_first - add_second
        print("Your answer is" + " " + str(answer))
    elif cal_input == 3:
        print("Start dividing!")
        add_first = int(input("Enter your first value: "))
        add_second = int(input("Enter your second value: "))
        answer = add_first / add_second
        print("Your answer is" + " " + str(answer))
    elif cal_input == 4:
        print("Start multiplying")
        add_first = int(input("Enter your first value: "))
        add_second = int(input("Enter your second value: "))
        answer = add_first * add_second
        print("Your answer is" + " " + str(answer))
    else:
        print("Invalid value" + "\n" + "Start again!")
        calculator()


welcome_message()
