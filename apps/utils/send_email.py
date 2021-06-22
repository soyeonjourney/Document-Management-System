import random
from users.models import EmailVerification
from django.core.mail import send_mail
from DMS.settings import EMAIL_HOST_USER


# Generate a random code
def random_code(length=16):
    code = ''
    str_set = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    for i in range(length):
        idx = random.randint(0, len(str_set)-1)
        code += str_set[idx]
    return code


# Send E-mail
def send_register_email(email):
    email_record = EmailVerification()
    # Generate a random code, append to the link
    code = random_code()
    email_record.code = code
    email_record.email = email
    email_record.save()
    # E-mail content
    email_title = "Lilac User Activate"
    email_body = "Thanks for using Lilac!\n" \
        + "To confirm your email and finish your registration," \
        + "please visit the following URL: \n" \
        + "http://127.0.0.1:8000/active/{0}".format(code)
    send_status = send_mail(email_title, email_body, EMAIL_HOST_USER, [email])
    if send_status:
        pass
