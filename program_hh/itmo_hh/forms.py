from django import forms
from .models import *
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class AddResumePerson(forms.ModelForm):
    class Meta:
        model = Resumes
        fields = ['title', 'FIO', 'sex', 'birthday', 'napravlenie', 'education_level', 'experience', 'sphere', 'content', 'file']

        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }


class AddResumeProject(forms.ModelForm):
    class Meta:
        model = Startapps_and_projects
        fields = ['title', 'photo', 'header', 'sphere', 'experience', 'education_level', 'category', 'content', 'applied_users', 'file']

        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }

class Filter_projects(forms.Form):
    experience_choice = (
        ('none', 'Не имеет значения'),
        ('no_experience', 'Нет опыта'),
        ('1-3', '1-3 года'),
        ('3-5', '3-5 лет'),
        ("5", "5+")
    )
    education_level_choice = (
        ('none', 'Не имеет значения'),
        ('bakalavriat', 'Бакалавриат'),
        ('magistr', 'Магистратура'),
        ('aspirantyra', 'Аспирантура')
    )
    experience = forms.ChoiceField(choices=experience_choice, label='Опыт')
    sphere = forms.ModelChoiceField(queryset=Sphere.objects.all(), label='Сфера разработки', empty_label='Не имеет значения', required=False)
    education_level = forms.ChoiceField(choices=education_level_choice, label='Уровень образования')


class Filter_resumes(forms.Form):
    experience_choice = (
        ('none', 'Не имеет значения'),
        ('no_experience', 'Нет опыта'),
        ('1-3', '1-3 года'),
        ('3-5', '3-5 лет'),
        ("5", "5+")
    )
    education_level_choice = (
        ('none', 'Не имеет значения'),
        ('bakalavriat', 'Бакалавриат'),
        ('magistr', 'Магистратура'),
        ('aspirantyra', 'Аспирантура')
    )
    experience = forms.ChoiceField(choices=experience_choice, label='Опыт')
    sphere = forms.ModelChoiceField(queryset=Sphere.objects.all(), label='Сфера разработки', empty_label='Не имеет значения', required=False)
    education_level = forms.ChoiceField(choices=education_level_choice, label='Уровень образования')


