import random 
from django.conf import settings
from django.core.mail import send_mail


def generate_otp():

    list = '0123456789'

    otp = ''.join(random.choice(list) for _ in range(6))
    return otp

def sendEmail(otp,email):

    subject = 'Your Email Verification Code'
    message = f'Hi ,\n\nYour OTP for email verification is:  {otp}\n\nPlease enter this code to verify your email address.\n\nThank you!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


