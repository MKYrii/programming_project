from django.test import TestCase
from itmo_hh.forms import *

class TestForms(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.sphere = Sphere.objects.create(name='Мобильные и сетевые технологии')
        self.napravlenie = Napravlenie.objects.create(name='Мобильная разработка')
        self.category = Category.objects.create(name='Конкурс')

    def test_form_addresumeperson_valid_data(self):
        form = AddResumePerson(data={
            'title': 'resume1',
            'FIO': 'RESUME1',
            'sex': 'women',
            'birthday': '2020-01-01',
            'sphere': self.sphere,
            'content': 'content1',
            'napravlenie': self.napravlenie,
            'education_level': 'bakalavriat',
            'experience': 'no_experience',
            'user_id': self.user
        })

        self.assertTrue(form.is_valid())

    def test_form_addresumeproject_valid_data(self):
        form = AddResumeProject(data={
            'user_id': self.user,
            'title': 'pr1',
            'header': 'pr1',
            'sphere': self.sphere,
            'experience': '1-3',
            'education_level': 'bakalavriat',
            'content': 'pr1',
            'category': self.category,
            'applied_users': 5
        })

        self.assertTrue(form.is_valid())

    def test_filter_projects_is_valid(self):
        form = Filter_projects(data={
            'sphere': self.sphere,
            'experience': '1-3',
            'education_level': 'bakalavriat',
        })

        self.assertTrue(form.is_valid())

    def test_filter_projects(self):
        Startapps_and_projects.objects.create(user_id=self.user, title='pr1', header='pr1', sphere=self.sphere,
                                              experience='1-3', education_level='bakalavriat', content='pr1',
                                              category=self.category, applied_users=5)

        Startapps_and_projects.objects.create(user_id=self.user, title='pr2', header='pr2', sphere=self.sphere,
                                              experience='1-3', education_level='bakalavriat', content='pr2',
                                              category=self.category, applied_users=7)

        form = Filter_projects(data={
            'sphere': self.sphere,
            'experience': '1-3',
            'education_level': 'bakalavriat',
        })

        if form.is_valid():
            response_form = Startapps_and_projects.objects.filter(**form.cleaned_data).order_by('id')

            response = Startapps_and_projects.objects.filter(
                sphere=self.sphere,
                experience='1-3',
                education_level='bakalavriat'
            ).order_by('id')

            self.assertQuerysetEqual(response_form, response, transform=lambda x: x)

    def test_filter_resume(self):
        Resumes.objects.create(title='resume1', FIO='RESUME1', sex='women', birthday='2020-01-01',
                               sphere=self.sphere, content='content1', napravlenie=self.napravlenie,
                               education_level='bakalavriat', experience='no_experience',
                               user_id=self.user)

        Resumes.objects.create(title='resume2', FIO='RESUME2', sex='women', birthday='2020-01-01',
                               sphere=self.sphere, content='content2', napravlenie=self.napravlenie,
                               education_level='bakalavriat', experience='1-3',
                               user_id=self.user)

        form = Filter_resumes(data={
            'experience': '1-3',
            'sphere': self.sphere,
            'education_level': 'bakalavriat',
        })

        if form.is_valid():
            response_form = Resumes.objects.filter(**form.cleaned_data).order_by('id')

            response = Resumes.objects.filter(
                experience='1-3',
                education_level='bakalavriat',
                sphere=self.sphere
            ).order_by('id')

            self.assertQuerysetEqual(response_form, response, transform=lambda x: x)

    def test_user_registration_form(self):
        form = UserRegistrationForm(data={
            'username': 'test_user',
            'email': 'test@example.com',
            'password': '12345',
            'password2': '12345',
        })

        self.assertTrue(form.is_valid())