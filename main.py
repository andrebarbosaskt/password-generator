from lib.func import *
from time import sleep
from sys import exit

password_length = 0

password_list = list()

again = ''

generate_header('Password Generator v1.0')

while True:
    try:
        start = str(input('Generate a passoword?: Y/n ')).strip().upper()[0]
        if start == 'N':
            print("You've choose to not generate a password.")
            print("Goodbye.")
            sleep(1)
            exit()
        elif start == 'Y':
            break
        else:
            error_message()
            print('\033[1;31mInvalid input.\033[m Please enter Y  or N')
    except (ValueError, TypeError, IndexError):
        error_message()
        print('\033[1;31mInvalid input.\033[m Please enter Y or N')
    except KeyboardInterrupt:
        print('The user has stopped the program before the password has been generated.')
        print('Goodbye.')
        exit()

while True:
    try:
        password_length = int(input('Length of the password: '))
    except (ValueError, TypeError, IndexError):
        print('\033[1;31mInvalid input.\033[m Please enter a number for the length of the password.')
    except KeyboardInterrupt:
        print('The user has stopped the program.')
        print('Goodbye')
        exit()
    finally:
        if password_length < 5:
            generate_header('\033[1mWarning\033[m')
            print("Can't generate a password with less than 5 characters.")
            print("Please enter a number greater than 5")
        elif password_length > 99:
            generate_header('\033[1mWarning\033[m')
            print("Too long lentgh for the password!")
            print("Please try again with a lower number")
        else:
            print('The password has been generated successfully.')
            my_password = password_generator(password_length)
            password_list.append(my_password)

            try:
                again = str(input("Generate another password?: Y/n ")).strip().upper()[0]
            except (ValueError, TypeError, IndexError):
                error_message()
                print('\033[1;31mInvalid input.\033[m Please enter Y or N')
            except KeyboardInterrupt:
                print('The user has stoppe the program.')
                print('Goodbye.')
                exit()
            finally:
                if again == 'N':
                    break
                elif again == 'Y':
                    continue
                else:
                    error_message()
                    print('\033[1;31mInvalid input.\033[m Please enter Y or N')

generate_header(f"You've generated {len(password_list)} passwords.")
print(f'{"N°":<30}{"Passwords":>3}')
print()
for number, item in enumerate(password_list):
    print(f'\033[1m#{number+1:<30}\033[m{item:>3}')
print(generate_line())
