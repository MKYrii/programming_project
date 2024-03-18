from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'itmo_hh/index.html')

def personal_account(request):
    return render(request, 'itmo_hh/personal_account.html')

def registration(request):
    return render(request, 'itmo_hh/registration.html')

def startapp(request):
    return render(request, 'itmo_hh/startapp.html')

def project(request):
    return render(request, 'itmo_hh/project.html')

def summary(request):
    return render(request, 'itmo_hh/summary.html')

def resume_project(request):
    return render(request, 'itmo_hh/resume_project.html')

def resume_person(request):
    return render(request, 'itmo_hh/resume_person.html')

def page_of_project(request):
    return render(request, 'itmo_hh/page_of_project.html')