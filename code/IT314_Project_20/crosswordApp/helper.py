from django.core.mail import send_mail
from datetime import datetime
from django.utils import timezone

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.conf import settings


def send_forget_password_mail(email, token):
    subject = 'Your forget password link'
    message = f'Hi , click on the link to reset your password http://127.0.0.1:8000/change-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True


def send_mail(receiver_address, subject, mail_content):
    sender_address = 'crosswordmanagement@gmail.com'  # add sender's email address here
    sender_pass = 'zkgxfsduhuvebiki'  # add sender's passsword address here

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject

    message.attach(MIMEText(mail_content, 'plain'))

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()


import uuid
import datetime

import bson


class User:
    id: uuid
    username = ""
    email = ""
    password = ""

    def __init__(self, username, email, password):
        # unique_id = uuid.uuid4()

        # print("unique_id: " + str(unique_id))
        # self.id = unique_id
        self.username = username
        self.email = email
        self.password = password

        self.dateOfJoining = datetime.datetime.now()

        # print("")

    def __str__(self):
        return f"User: {self.username}"
