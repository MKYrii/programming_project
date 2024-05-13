from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import FileResponse
from django.shortcuts import render, redirect
from itertools import chain

from itmo_hh.forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from itmo_hh.models import *
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'itmo_hh/index.html')


class PersonalAccount(LoginRequiredMixin, ListView):
    '''
    Отображение личного аккаунта
    '''
    login_url = 'login'
    paginate_by = 4
    model = Resumes
    template_name = 'itmo_hh/personal_account.html'
    context_object_name = 'resumes'

    def get_queryset(self):
        r = Resumes.objects.filter(user_id=self.request.user.id).order_by('time_published')
        return r


class MyOffers(LoginRequiredMixin, ListView):
    '''
    Отображает резюме, которые откликнулись на твой проект. Проекты, в которые тебя пригласили
    '''

    login_url = 'login'
    model = ProjectApplication
    paginate_by = 4
    template_name = 'itmo_hh/my_offers.html'
    context_object_name = 'offers_for_my_project'

    def get_queryset(self):
        return ProjectApplication.objects.filter(project__user_id=self.request.user.id)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offers_as_invite'] = ProjectInvitation.objects.filter(resume__user_id=self.request.user.id)
        return context


class MyOtclics(LoginRequiredMixin, ListView):
    '''
    Отображает на какие проекты ты послал свое резюме, какие резюме ты пригласил в проект
    '''

    login_url = 'login'
    paginate_by = 4
    model = ProjectApplication
    template_name = 'itmo_hh/my_otclics.html'
    context_object_name = 'otclics_on_projects'

    def get_queryset(self):
        return ProjectApplication.objects.filter(resume__user_id=self.request.user.id)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offers_to_resumes'] = ProjectInvitation.objects.filter(project__user_id=self.request.user.id)
        return context


class MyProjects(LoginRequiredMixin, ListView):
    '''
    Отображение проектов, которые создал пользователь
    '''
    login_url = 'login'
    paginate_by = 4
    model = Startapps_and_projects
    template_name = 'itmo_hh/my_projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Startapps_and_projects.objects.filter(user_id=self.request.user.id).order_by('time_published')


def registration(request):
    return render(request, 'itmo_hh/registration.html')


class Startapp(ListView):
    '''
    Отображение странички стартапов
    '''

    paginate_by = 15
    paginate_orphans = 3
    model = Startapps_and_projects
    template_name = 'itmo_hh/startapp.html'
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вакансии: стартапы'
        context['form'] = Filter_projects()
        return context

    def get_queryset(self):
        qs = Startapps_and_projects.objects.filter(category_id=3)
        qs = qs.filter(~Q(user_id=self.request.user.id))
        form = Filter_projects(self.request.GET)
        if form.is_valid():
            experience = form.cleaned_data.get('experience')
            education_level = form.cleaned_data.get('education_level')
            sphere = form.cleaned_data.get('sphere')

            if experience != 'none':
                qs = qs.filter(experience=experience)
            if education_level != 'none':
                qs = qs.filter(education_level=education_level)
            if sphere != '' and sphere != None and sphere != 'Не имеет значения':
                qs = qs.filter(sphere=sphere)
        return qs


class Projects(ListView):
    '''
    Отображение странички проектов
    '''

    paginate_by = 15
    paginate_orphans = 3
    model = Startapps_and_projects
    template_name = 'itmo_hh/project.html'
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вакансии: проекты'
        context['form'] = Filter_projects()
        return context

    def get_queryset(self):
        qs = Startapps_and_projects.objects.filter(category_id=2)
        qs = qs.filter(~Q(user_id=self.request.user.id))
        form = Filter_projects(self.request.GET)
        if form.is_valid():
            experience = form.cleaned_data.get('experience')
            education_level = form.cleaned_data.get('education_level')
            sphere = form.cleaned_data.get('sphere')

            if experience != 'none':
                qs = qs.filter(experience=experience)
            if education_level != 'none':
                qs = qs.filter(education_level=education_level)
            if sphere != '' and sphere != None and sphere != 'Не имеет значения':
                qs = qs.filter(sphere=sphere)
        return qs


class Resume(ListView):
    '''
    Отображение странички резюме людей
    '''

    paginate_by = 15
    paginate_orphans = 3
    model = Resumes
    template_name = 'itmo_hh/resume.html'
    context_object_name = 'resumes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Резюме'
        context['form'] = Filter_resumes()
        return context

    def get_queryset(self):
        qs = Resumes.objects.filter()
        qs = qs.filter(~Q(user_id=self.request.user.id))
        form = Filter_resumes(self.request.GET)
        if form.is_valid():
            experience = form.cleaned_data.get('experience')
            education_level = form.cleaned_data.get('education_level')
            sphere = form.cleaned_data.get('sphere')

            if experience != 'none':
                qs = qs.filter(experience=experience)
            if education_level != 'none':
                qs = qs.filter(education_level=education_level)
            if sphere != '' and sphere != None and sphere != 'Не имеет значения':
                qs = qs.filter(sphere=sphere)
        return qs


class Competitions(ListView):
    '''
    Отображение странички конкурсов
    '''

    paginate_by = 15
    paginate_orphans = 3
    model = Startapps_and_projects
    template_name = 'itmo_hh/competitions.html'
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Команды: конкурсы'
        context['form'] = Filter_projects()
        return context

    def get_queryset(self):
        qs = Startapps_and_projects.objects.filter(category_id=1)
        qs = qs.filter(~Q(user_id=self.request.user.id))
        form = Filter_projects(self.request.GET)
        if form.is_valid():
            experience = form.cleaned_data.get('experience')
            education_level = form.cleaned_data.get('education_level')
            sphere = form.cleaned_data.get('sphere')

            if experience != 'none':
                qs = qs.filter(experience=experience)
            if education_level != 'none':
                qs = qs.filter(education_level=education_level)
            if sphere != '' and sphere != None and sphere != 'Не имеет значения':
                qs = qs.filter(sphere=sphere)
        return qs


class FindResume(ListView):
    '''
    Отображение страницы для поиска резюме
    '''
    paginate_by = 15
    paginate_orphans = 3
    model = Resumes
    template_name = 'itmo_hh/find_resume.html'
    context_object_name = 'resumes'

    def get_queryset(self):
        return Resumes.objects.filter(~Q(user_id=self.request.user.id)).order_by('time_published')


@login_required(login_url='login')
def resume_project(request):
    '''
    Создание личного резюме
    '''

    if request.method == "POST":
        form = AddResumeProject(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user_id = request.user
            resume.save()
            return redirect('my_projects')
    else:
        form = AddResumeProject()
    return render(request, 'itmo_hh/resume_project.html', {'form': form, 'title': 'Создать новый проект'})


@login_required(login_url='login')
def resume_person(request):
    '''
    Создание резюме проекта
    '''

    if request.method == "POST":
        form = AddResumePerson(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user_id = request.user
            resume.save()
            return redirect('personal_account')
    else:
        form = AddResumePerson()
    return render(request, 'itmo_hh/resume_person.html', {'form': form, 'title': 'Создать резюме/ личное резюме'})


# @login_required(login_url='login')
class PageOfProject(DetailView):
    '''
    Страница конкретного проекта
    '''

    model = Startapps_and_projects
    template_name = 'itmo_hh/page_of_project.html'
    context_object_name = 'project'
    pk_url_kwarg = 'project_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()

        # Проверка на то, что текущий пользователь создал проект
        if project.user_id.id == self.request.user.id:
            context['is_owner'] = True
        else:
            context['is_owner'] = False

        context['applied_resumes'] = ProjectApplication.objects.filter(project=project)
        context['invited_resumes'] = ProjectInvitation.objects.filter(project=project)

        return context


# @login_required(login_url='login')
class ResumePage(DetailView):
    '''
    Страница конкретного резюме
    '''

    model = Resumes
    template_name = 'itmo_hh/resume_page.html'
    context_object_name = 'resume'
    pk_url_kwarg = 'resume_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resume = self.get_object()

        # Проверка на то, что текущий пользователь создал проект
        if self.request.user.id == resume.user_id.id:
            context['is_owner'] = True
        else:
            context['is_owner'] = False

        context['applied_resumes'] = ProjectApplication.objects.filter(resume=resume)
        context['invited_resumes'] = ProjectInvitation.objects.filter(resume=resume)

        return context


# @login_required(login_url='login')
class UpdateResume(UpdateView):
    '''
    Редактирование личного резюме
    '''

    model = Resumes
    template_name = 'itmo_hh/update_resume_person.html'
    context_object_name = 'resume'
    pk_url_kwarg = 'resume_id'
    form_class = AddResumePerson


# @login_required(login_url='login')
class UpdateProject(UpdateView):
    '''
    Редактирование проекта
    '''

    model = Startapps_and_projects
    template_name = 'itmo_hh/update_project.html'
    context_object_name = 'project'
    pk_url_kwarg = 'project_id'
    form_class = AddResumeProject


# @login_required(login_url='login')
def delete_resume(request, resume_id):
    '''
    Удаление резюме
    '''

    resume = Resumes.objects.get(id=resume_id)
    resume.delete()
    return redirect('personal_account')


# @login_required(login_url='login')
def delete_project(request, project_id):
    '''
    Удаление прокта
    '''

    project = Startapps_and_projects.objects.get(id=project_id)
    project.delete()
    return redirect('personal_account')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'itmo_hh/register.html', {'user_form': user_form, 'title': 'регистрацияя'})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'itmo_hh/login.html'
    context_object_name = 'login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'логин'
        return context

    def get_success_url(self):
        return 'personal_account'


def Otclic_on_project(request, project_id):
    '''
    Отклик резюме на проект
    '''

    if request.method == 'POST':

        # Проверка на то, что этот пользователь уже откликнулся на проект
        if ProjectApplication.objects.filter(project_id=project_id, resume_id=1).exists():

            messages.error(request, 'Вы уже откликнулись на этот проект')
            return redirect('project', project_id=project_id)

        else:
            # resume_id = request.POST.get('resume_id')
            project_application = ProjectApplication(project_id=project_id, resume_id=1,
                                                     status=0)
            project_application.save()
            return redirect('project', project_id=project_id)
    else:
        pass


def resume_invite(request, resume_id):
    '''
    Приглашение резюме в проект
    '''

    if request.method == 'POST':
        if ProjectInvitation.objects.filter(resume_id=resume_id, project_id=1).exists():
            messages.error(request, 'Вы уже пригласили это резюме')
            return redirect('resume', resume_id=resume_id)
        else:
            # project = request.POST.get('project_id')
            project_invitation = ProjectInvitation(project_id=1, resume_id=resume_id, status=0)
            project_invitation.save()
            return redirect('resume', resume_id=resume_id)
    else:
        pass


def accept_invitation(request, resume_id, project_id):
    '''
    Когда ты принимаешь приглашение от проекта, то в твоем резюме меняется статус
    :param resume_id: Номер твоего резюме
    :param project_id: Номер проекта, который тебя пригласил
    :return: Изменяет статус проекта на 1 - принято
    '''
    all = ProjectInvitation.objects.filter(resume_id=resume_id)
    needed_record = all.get(project_id=project_id)
    needed_record.status = 1
    needed_record.save()
    return redirect('resume', resume_id=resume_id)


def deny_invitation(request, resume_id, project_id):
    '''
    Когды ты отказываешь в приглашении проекта, то в твоем резюме меняется статус
    :param resume_id: Номер твоего резюме
    :param project_id: Номер проекта, который тебя пригласил
    :return: Изменяет статус проекта на 2 - отказано
    '''
    all = ProjectInvitation.objects.filter(resume_id=resume_id)
    needed_record = all.get(project_id=project_id)
    needed_record.status = 2
    needed_record.save()
    return redirect('resume', resume_id=resume_id)


def accept_application(request, project_id, resume_id):
    '''
    Когда ты принимаешь откликнувшееся резюме в проект, у тебя меняется статус
    :param project_id: Номер твоего проекта
    :param resume_id: Номер откликнувшегося резюме
    :return: Изменяет статус на 1 - принято
    '''
    all = ProjectApplication.objects.filter(project_id=project_id)
    needed_resord = all.get(resume_id=resume_id)
    needed_resord.status = 1
    needed_resord.save()
    return redirect('project', project_id=project_id)


def deny_application(request, project_id, resume_id):
    '''
    Когда ты отказываешь откликнувшемуся резюме в проект, у тебя меняется статус
    :param project_id: Номер твоего проекта
    :param resume_id: Номер откликнувшегося резюме
    :return: Изменяет статус на 2 - отказано
    '''
    all = ProjectApplication.objects.filter(project_id=project_id)
    needed_resord = all.get(resume_id=resume_id)
    needed_resord.status = 2
    needed_resord.save()
    return redirect('project', project_id=project_id)


def recall_invitation(request, project_id, resume_id):
    '''
    Когда ты отзываешь приглашение для резюме, оно удаляется из бд
    '''
    all = ProjectInvitation.objects.filter(project_id=project_id)
    needed_resord = all.get(resume_id=resume_id)
    needed_resord.delete()
    return redirect('project', project_id=project_id)


def recall_application(request, resume_id, project_id):
    '''
    Когда ты отзываешь свой отклик на проект, он удаляется из бд
    '''
    all = ProjectApplication.objects.filter(resume_id=resume_id)
    needed_record = all.get(project_id=project_id)
    needed_record.delete()
    return redirect('resume', resume_id=resume_id)


LogoutView.template_name = 'itmo_hh/logout.html'
