from django.http import HttpResponse
from django.shortcuts import render, redirect
from portfolio.models import Message, Mail, Test
from random import choice


def home(request):
    return render(request, 'index.html')

def join(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        if not email:
            return HttpResponse("Error")
        try:
            mail = Mail.objects.get(email=email)
            print("FOUND, NOT GONNA ADD!")
        except Mail.DoesNotExist:
            mail = Mail.objects.create(email=email)
        return redirect('home')


def showmsg(request):
    # random_msg = choice(Message.objects.all())
    random_msg = Message.objects.all()[0]

    return render(request, "mail.html", {'message': random_msg})