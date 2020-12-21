from getpass import getpass
from datetime import datetime
import client_functions, database_functions
import sys

# Client Actions
attempts = 0
while(True):
    master_user = input('Enter Master Username: ')
    master_pass = getpass('Enter the Master Password: ')
    if client_functions.check_master(master_user, master_pass):
        print("Welcome!")
        break
    else:
        attempts += 1
        print("Did not Enter Correct Password. {}/3".format(attempts))
        if attempts > 3:
            sys.exit("Exceeded # attempts. Exiting..")

# Database Actions
user_input = 'a'
while(user_input.lower() == 'a' or user_input.lower() == 's'):

    user_input = input("a = Add Password, s = Show Passwords, any other key = Exit: ")

    # Add/Update Password
    if user_input.lower() == "a":
        app = input('Name of Application to add pass: ')
        password = getpass('Password: ')
        password_verify = getpass('Verify Password: ')

        while(password != password_verify):
            print('\n---\nPasswords did NOT match\n---\n')
            password = getpass('Password: ')
            password_verify = getpass('Verify Password: ')

        check_inputs = database_functions.check_inputs(master_user, app, password)

        if check_inputs == 'Update':
            print("\n---\nPassword exists in Application ({})\n---\n".format(app))
            print("Do you want to update for App ({})?".format(app))
            update = input('y/N: ')

            if update.lower() == 'y':
                print(database_functions.update_password(app,password,str(datetime.now().date())))
            else:
                print('Did NOT Update Password')
        elif check_inputs == 'Equal':
            print('Password Already EXISTS for App ({})'.format(app))
        else:
            database_functions.add_row(master_user, app, password, str(datetime.now().date()), str(datetime.now().date()))
            print('Added password for App {}!'.format(app))

    # Delete Password - Implement Later
    #elif user_input.lower() == "d":
    #    print(delete_password(master_user, app, password))

    elif user_input.lower() == "s":
        show = input('s = single (decrypted pass), any other key = table (encrypted pass): ')

        if show.lower() == 's':
            show_app = input('Enter Application to show Password: ')
            print(database_functions.show_password(master_user, show_app))
        else:
            print(database_functions.show_table(master_user))

    # Exit
    else:
        print("Exiting..")