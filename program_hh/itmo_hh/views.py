from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from itmo_hh.forms import *
from django.views.generic import ListView, DetailView

def index(request):
    return render(request, 'itmo_hh/index.html')

class PersonalAccount(ListView):
    model = Resumes
    template_name = 'itmo_hh/personal_account.html'
    context_object_name = 'resumes'

    # Для отображения только тех резюме, что создал пользователь
    #def get_queryset(self):
     #   return Resumes.objects.filter(user_id=self.request.user.id)

class MyOffers(ListView):
    '''
    Отображает резюме, которые откликнулись на твой проект
    '''
    model = My_otclics_and_offers
    template_name = 'itmo_hh/my_offers.html'
    context_object_name = 'offers'
    def get_queryset(self):
        return My_otclics_and_offers.objects.filter(id_to_whom_user=self.request.user.id)

class MyOtclics(ListView):
    '''
    Отображает на какие проекты ты послал свое резюме
    '''
    model = My_otclics_and_offers
    template_name = 'itmo_hh/my_otclics.html'
    context_object_name = 'otclics'
    def get_queryset(self):
        return My_otclics_and_offers.objects.filter(id_offer_user=self.request.user.id)

def registration(request):
    return render(request, 'itmo_hh/registration.html')

class Startapp(ListView):
    model = Startapps_and_projects
    template_name = 'itmo_hh/startapp.html'
    context_object_name = 'projects_s'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'стартапы'
        return context
    def get_queryset(self):
        return Startapps_and_projects.objects.filter(category_id=3)

class Projects(ListView):
    model = Startapps_and_projects
    template_name = 'itmo_hh/project.html'
    context_object_name = 'projects'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'проекты'
        return context
    def get_queryset(self):
        return Startapps_and_projects.objects.filter(category_id=2)

class Competitions(ListView):
    model = Startapps_and_projects
    template_name = 'itmo_hh/competitions.html'
    context_object_name = 'projects'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'конкурсы'
        return context
    def get_queryset(self):
        return Startapps_and_projects.objects.filter(category_id=1)


def summary(request):
    return render(request, 'itmo_hh/summary.html')

def resume_project(request):
    return render(request, 'itmo_hh/resume_project.html')
@login_required
def resume_person(request):
    if request.method == "POST":
        form = AddResumePerson(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user_id = request.user
            resume.save()
            return redirect('personal_account')
    else:
        print('eror2')
        form = AddResumePerson()
    return render(request, 'itmo_hh/resume_person.html', {'form': form, 'title': 'Создать резюме/ личное резюме'})

class PageOfProject(DetailView):
    model = Startapps_and_projects
    template_name = 'itmo_hh/page_of_project.html'
    context_object_name = 'project'
    pk_url_kwarg = 'project_id'

class ResumePage(DetailView):
    model = Resumes
    template_name = 'itmo_hh/resume_page.html'
    context_object_name = 'resume'
    pk_url_kwarg = 'resume_id'