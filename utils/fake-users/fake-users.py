import random
import string
import hashlib
import csv

def generator_str(user_min, user_max):
    user_len = random.randint(user_min, user_max)
    user_range = ''
    for i in range(1, 3):
        user_range += string.ascii_letters + string.digits
    username = ''.join(random.sample(user_range, user_len))
    return username

def hash_pwd(pwd, salt='lilac4cvpr'):
    return hashlib.sha256(salt.encode() + pwd.encode()).hexdigest()

def generator_email():
    email_first = generator_str(3, 8)
    email_suffix = ['163', '126', 'qq', 'gmail', 'outlook']
    choose = random.randint(0,4)
    suffix = email_suffix[choose]
    return email_first + '@' + suffix + '.com'

def generator_date(year):
    date_first = str(year)
    date_second = '{:0>2d}'.format(random.randint(1,12))
    date_third = '{:0>2d}'.format(random.randint(1,28))
    date = date_first + '-' + date_second + '-' + date_third
    return date

if __name__ == '__main__':
    with open('fake-users.csv', 'a', newline='') as user_csv:
        csv_writer = csv.writer(user_csv, delimiter=',')
        csv_writer.writerow(['name', 'password', 'email', 'is_active', 'join_time'])
    for i in range(200):
        username = generator_str(3, 8)  # Unername
        pwd = generator_str(8, 16)  # Password
        encry_pwd = hash_pwd(pwd)  # Encrypted Password
        email = generator_email()  # E-mail Address
        is_active = random.randint(0,1)
        join_time = generator_date(2021)
        with open('fake-users.csv', 'a', newline='') as user_csv:
            csv_writer = csv.writer(user_csv, delimiter=',')
            csv_writer.writerow([username, encry_pwd, email, is_active, join_time])
