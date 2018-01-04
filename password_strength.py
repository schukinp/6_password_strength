import re


def get_passsword_lenght(password):
    if len(password) > 6:
        return 2
    else:
        return 0


def check_upper_chars(password):
    if re.search('[A-Z]', password):
        return 2
    else:
        return 0


def check_lower_chars(password):
    if re.search('[a-z]', password):
        return 2
    else:
        return 0


def check_digits(password):
    if re.search('\d', password):
        return 2
    else:
        return 0


def check_special_chars(password):
    if re.search('[^A-Za-z\d]', password):
        return 2
    else:
        return 0


def get_password_strength(password):
    score = sum([
        int(get_passsword_lenght(password)),
        int(check_upper_chars(password)),
        int(check_lower_chars(password)),
        int(check_digits(password)),
        int(check_special_chars(password))
        ])
    return score


if __name__ == '__main__':
    password = input('Please enter password: ')
    while len(password) == 0:
        print('Password must be at least 1 characters long!')
        password = input('Please enter password: ')
    if len(password) == 1:
        print('Your password strength is: 1')
    else:
        print('Your password strength is: {}'.format(get_password_strength(password)))




