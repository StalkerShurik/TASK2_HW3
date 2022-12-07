from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from urllib.parse import urlencode
from django.shortcuts import redirect
from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import View

from .forms import CVForm


def start_page(request):
    context = {}
    return render(request, 'TASK2-HW3-templates/start.html', context)


def register_page(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            response = redirect('/login')
            return response
        else:
            messages.error(request, "Incorrect input data format")

    context = {'form': form}
    return render(request, 'TASK2-HW3-templates/register.html', context)


def login_page(request):
    form = AuthenticationForm()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect('/user')
            return response
        else:
            messages.error(request, "Incorrect Password")

    context = {'form': form}
    return render(request, 'TASK2-HW3-templates/login.html', context)


def cv_page(request):
    name = request.GET.get('name')
    date = request.GET.get('date')
    education = request.GET.get('education')
    soft_skills = request.GET.get('soft')
    hard_skills = request.GET.get('hard')
    job = request.GET.get('job')
    exp = request.GET.get('exp')

    context = {"name": name, "date": date, "education": education, "soft": soft_skills, "hard": hard_skills, "job": job,
               "exp": exp}

    return render(request, 'TASK2-HW3-templates/cv.html', context)


def user_page(request):
    form = CVForm()

    if request.method == "POST":
        name = request.POST['your_name']
        date = request.POST['your_birth_date']
        education = request.POST['your_education']
        soft_skills = request.POST['your_soft_skills']
        hard_skills = request.POST['your_hard_skills']
        job = request.POST['your_job']
        exp = request.POST['your_exp']

        base_url = '/cv_page?name=' + name + "&date=" + date + "&education=" + education + "&soft=" + soft_skills + "&hard=" + hard_skills + "&job=" + job + "&exp=" + exp
        return redirect(base_url)

    context = {'form': form}
    return render(request, 'TASK2-HW3-templates/user.html', context)


def logout_page(request):
    logout(request)
    response = redirect('/login')
    return response
