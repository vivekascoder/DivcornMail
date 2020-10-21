from portfolio.models import Message, Mail, Test
from django.core.mail import send_mass_mail, send_mail
from random import choice, randint
from django.template.loader import render_to_string
from django.conf import settings

# Sending Mail Functions Goes Here.

def send_random_mail():
    recievers = [i.email for i in Mail.objects.all()]
    random_msg = choice(Message.objects.all())
    html_message = render_to_string('mail.html', context={'message': random_msg})
    send_mail(random_msg.subject, random_msg.message, settings.EMAIL_HOST_USER, ['vivekascoder@gmail.com'], html_message=html_message)


def test_cron():
    Test.objects.create(test="hello" + str())