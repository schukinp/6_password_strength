import re
from getpass import getpass


def get_passsword_lenght(password):
    min_strenght_len = 6
    return bool(len(password) > min_strenght_len)


def check_upper_chars(password):
    return bool(re.search('[A-Z]', password))


def check_lower_chars(password):
    return bool(re.search('[a-z]', password))


def check_digits(password):
    return bool(re.search('\d', password))


def check_special_chars(password):
    return bool(re.search('\W', password))


def get_password_strength(password):
    score = sum([
        get_passsword_lenght(password)*2,
        check_upper_chars(password)*2,
        check_lower_chars(password)*2,
        check_digits(password)*2,
        check_special_chars(password)*2
        ])
    return score


if __name__ == '__main__':
    password = getpass('Enter password: ')
    min_password_len = 1
    if not password:
        print('Password must be at least 1 characters long!')
    elif len(password) == min_password_len:
        print ('Your password strenght is: {}'.format(min_password_len))
    else:
        print('Your password strength is: {}'.format(get_password_strength(password)))






