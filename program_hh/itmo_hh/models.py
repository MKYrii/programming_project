from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Resumes(models.Model):
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
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)  # ? в модели user добавить Forenkey на эту модель
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    time_published = models.DateTimeField(auto_now_add=True)
    FIO = models.CharField(max_length=255, verbose_name='ФИО')
    sex = models.CharField(choices=(('women', 'Женский'), ('men', 'Мужской')), max_length=30, verbose_name='Пол')
    birthday = models.DateField(verbose_name='День рождения', blank=True, null=True)
    napravlenie = models.ForeignKey('Napravlenie', on_delete=models.PROTECT, verbose_name='Направление обучения')
    education_level = models.CharField(max_length=100, choices=education_level_choice,
                                       verbose_name='Уровень образования')
    experience = models.CharField(max_length=30, choices=experience_choice, verbose_name='Опыт')
    sphere = models.ForeignKey('Sphere', on_delete=models.PROTECT, verbose_name='Сфера деятельности')
    content = models.TextField(blank=True, null=True, verbose_name='Описание')
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True, verbose_name='Файл')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resume', kwargs={'resume_id': self.pk})


class Startapps_and_projects(models.Model):
    experience_choice = (
        ('no_experience', 'Нет опыта'),
        ('1-3', '1-3 года'),
        ('3-5', '3-5 лет'),
        ("5", "5+ лет")
    )
    education_level_choice = (
        ('bakalavriat', 'Бакалавриат'),
        ('magistr', 'Магистратура'),
        ('aspirantyra', 'Аспирантура')
    )
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    time_published = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    photo = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True, verbose_name='Фото')
    header = models.CharField(max_length=255, verbose_name='Руководитель')
    sphere = models.ForeignKey('Sphere', on_delete=models.PROTECT, verbose_name='Сфера деятельности')
    experience = models.CharField(max_length=30, choices=experience_choice, verbose_name='Необходимый опыт работы')
    education_level = models.CharField(max_length=100, choices=education_level_choice, verbose_name='Требуемый уровень образования')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    content = models.TextField(blank=True, verbose_name='Описание')
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True, verbose_name='Файл')
    applied_users = models.IntegerField(blank=True, null=True, verbose_name='Количество человек')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project', kwargs={'project_id': self.pk})


class Category(models.Model):
    # 3-стартап, 2-проект, 1-конкурс
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})


class Sphere(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sphere', kwargs={'sphere_id': self.pk})


class Napravlenie(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('napravlenie', kwargs={'napravlenie_id': self.pk})

# Можно удалить
class My_otclics_and_offers(models.Model):
    id_offer_user = models.ForeignKey(User, related_name='offer_user', on_delete=models.CASCADE)
    id_to_whom_user = models.ForeignKey(User, related_name='to_whom_user', on_delete=models.CASCADE)
    time_published = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id_offer_user} - {self.id_to_whom_user}'

    def get_absolute_url(self):
        return reverse('otof', kwargs={'otof_id': self.pk})

class ProjectApplication(models.Model):
    '''
    Здесь хранятся данные об откликах резюме на проект. Все по id
    '''

    project = models.ForeignKey('Startapps_and_projects', related_name='projects_application', on_delete=models.CASCADE)
    resume = models.ForeignKey('Resumes', related_name='resumes_application', on_delete=models.CASCADE)
    status_choices = (
        (0, 'В рассмотрении'),
        (1, 'Принято'),
        (2, 'Отклонено')
    )
    status = models.IntegerField(default=0)
    time_published = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('project_application', kwargs={'project_id': self.project})
class ProjectInvitation(models.Model):
    '''
    Здесь хранятся приглашения резюме в проект. Все по id
    '''

    project = models.ForeignKey('Startapps_and_projects', related_name='projects_invitation', on_delete=models.CASCADE)
    resume = models.ForeignKey('Resumes', related_name='resumes_invitation', on_delete=models.CASCADE)
    status_choices = (
        (0, 'В рассмотрении'),
        (1, 'Принято'),
        (2, 'Отклонено')
    )
    status = models.IntegerField(default=0)
    time_published = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Love(models.Model):
    id_love_res = models.ForeignKey('Resumes', on_delete=models.CASCADE)
    id_love_proj = models.ForeignKey('Startapps_and_projects', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('love', kwargs={'love_id': self.pk})
