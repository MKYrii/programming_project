from django import forms
from .models import *

class AddResumePerson(forms.Form):
    experience_choice = (
        ('no_experience', 'Нет опыта'),
        ('1-3', '1-3 года'),
        ('3-5', '3-5 лет'),
        ("5", "5+")
    )
    education_level_choice = (
        ('bakalavriat', 'Бакалавриат'),
        ('magistr', 'Магистратура'),
        ('aspirantyra', 'Аспирантура')
    )
    name = forms.CharField(max_length=255, label='ФИО')
    sex = forms.MultipleChoiceField(label='Пол', choices=(('men', 'Мужчина'), ('women', 'Женщина')),
                                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-inside'}))

    borth = forms.DateField(label='День рождения',
                            input_formats=['%d/%m/%Y', '%d/%m/%y', '%d.%m.%Y', '%d.%m.%y'])

    photo = forms.ImageField(required=False, label='Фото')
    napravlenie = forms.CharField(label='Направление обучения')  #forms.ModelChoiceField queryset=Napravlenie.objects.all()
    education_level = forms.ChoiceField(choices=education_level_choice, label='Уровень образования')
    experience = forms.ChoiceField(choices=experience_choice, label='Опыт')
    sphere = forms.CharField(label='Сфера деятельности')  #forms.ModelChoiceField queryset=Sphere.objects.all()
    context = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Описание')
    files = forms.FileField(required=False, label='Прикрепите файлы')
