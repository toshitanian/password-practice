import os
import argparse
import getpass
import uuid
import hashlib
PASSWORD_PATH = os.path.expanduser('~/.password_practice')
INIT_ERROR = 'ERROR: password not found Consider using --configure parameter to create one.'


def practice():
    with open(PASSWORD_PATH) as f:
        salt, hashed_password = f.read().strip().split(":")
    succsss_count = 0
    max_count = 5
    for i in xrange(max_count):
        p = getpass.getpass(prompt='[{count}/{max_count}]input password:'.format(
            count=(i+1), max_count=max_count
        ))
        judge = hash_password(p, salt) == hashed_password
        print judge
        if judge:
            succsss_count += 1
    success_rate = int(float(succsss_count) / float(max_count) * 100)
    print 'Success: {}%'.format((success_rate))


def hash_password(p, salt):
    s = '{salt}:{p}'.format(salt=salt, p=p)
    h = hashlib.sha512()
    h.update(s)
    p = h.hexdigest()
    return p


def set_password():
    print 'password will be hashed...'
    p = getpass.getpass(prompt='password:')
    p2 = getpass.getpass(prompt='password(confirm):')
    if p != p2:
        print "ERROR: passwords doesn' match"
        exit(1)
    salt = str(uuid.uuid4())
    hashed_password = hash_password(p, salt)
    with open(PASSWORD_PATH, 'w') as f:
        f.write('{salt}:{hashed_password}'.format(
            salt=salt, hashed_password=hashed_password
        ))
    print 'finish saving hashed password;'


def does_password_exist():
    if not os.path.exists(PASSWORD_PATH):
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--configure', action='store_true')
    args = parser.parse_args()

    if args.configure:
        set_password()
    elif not does_password_exist():
        print INIT_ERROR
    else:
        practice()

if __name__ == '__main__':
    main()
