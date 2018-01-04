import re


def get_password_strength(password):
    score = 0
    if len(password) == 1:
        score +=1
        return score
    if len(password) > 6:
        score += 2
    if re.search('[A-Z]', password):
        score += 2
    if re.search('[a-z]', password):
        score += 2
    if re.search('\d', password):
        score += 2
    if re.search('[^A-Za-z\d]', password):
        score += 2
    return score


if __name__ == '__main__':
    password = input('Please enter password: ')
    while len(password) == 0:
        print('Password must be at least 1 characters long!')
        password = input('Please enter password: ')
    print('Your password strength is: {}'.format(get_password_strength(password)))




