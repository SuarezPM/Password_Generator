import string
import random

def password_generator():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars)
                  for i in range (10))


def run ():
    password = password_generator()
    print("You secure password is: {}".format(password))

if __name__ == '__main__':
    run()
