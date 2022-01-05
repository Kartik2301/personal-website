from django.shortcuts import render, HttpResponse
from .models import Project
import smtplib
from datetime import datetime

# Create your views here.


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


def about_me(request):
    age = 21
    return render(request, 'portfolio/about_me.html', {'age': age})


def do_something(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    my_email = 'manesuresh010@gmail.com'
    password = 'hjdr8963'
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Message Received on Personal Portfolio Website from {email}\n\n{email} sent you the following message :- \n{message}")

    return HttpResponse('Return data to ajax call')
