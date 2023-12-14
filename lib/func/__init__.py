import secrets
import string


def password_generator(length=10):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    selection_list = letters + digits + symbols


    password = ""

    for i in range(length):
        password += ''.join(secrets.choice(selection_list))

    return password


def generate_line(length=50):
    return '-' * length


def generate_header(msg):
    print(generate_line())
    print(msg.center(50))
    print(generate_line())


def error_message(msg='Error'):
    print(generate_line())
    print(f'\033[1;31m{msg}\033[m'.center(50))
    print(generate_line())


