from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'itmo_hh/index.html')
