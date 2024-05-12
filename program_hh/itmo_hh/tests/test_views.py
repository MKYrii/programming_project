from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from itmo_hh.views import *
from django.urls import reverse
from itmo_hh.models import *

class TestViewsPersonalAccount(TestCase):
    def setUp(self):
        '''
        Инициализация переменных
        '''

        self.client = Client()

        self.resume_list_url = reverse('personal_account')

        self.project_list_url = reverse('my_projects')

        self.resume_page_url = reverse('resume', args=[1])

        self.user = User.objects.create(username='testuser', password='12345')

        self.sphere = Sphere.objects.create(name='Мобильные и сетевые технологии')

        self.napravlenie = Napravlenie.objects.create(name='Мобильная разработка')

        self.resume1 = Resumes.objects.create(title='resume1', FIO='RESUME1', sex='women', birthday='2020-01-01',
                                              sphere=self.sphere, content='content1', napravlenie=self.napravlenie,
                                              education_level='bakalavriat', experience='no_experience', user_id=self.user)
    # Заебався
    # def test_personal_account_resume_list_get(self):
    #     self.client.login(username='testuser', password='12345')
    #     self.resume2 = Resumes.objects.create(title='resume2', FIO='RESUME2', sex='women', birthday='2020-01-01',
    #                                           sphere=self.sphere, content='content1', napravlenie=self.napravlenie,
    #                                           education_level='bakalavriat', experience='no_experience',
    #                                           user_id=self.user)
    #
    #     response = self.client.get(self.resume_list_url)
    #     self.assertEqual(response.status_code, 302)
    #
    #     print(self.resume1.user_id.id)
    #     print(self.resume2.user_id.id)
    #     print(self.user.id)
    #     self.assertIn('resumes', response.context)
    #     response_data = response.context['resumes']  # Данные запроса для сравнения
    #
    #     # Убедиться, что выводимые объекты равны url хозяина
    #     self.assertEqual(response_data[0], self.resume1)
    #     self.assertEqual(response_data[1], self.resume2)

        # Проверить пагинацию?

    # Доделать, когда исправлю класс представления
    def test_my_offers_get(self):
        pass

    # Доделать, когда исправлю класс представления
    def test_my_otclics_get(self):
        pass

    # def test_my_projects_project_list_get(self):
    #     response = self.client.get(self.project_list_url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(Startapps_and_projects.objects.filter(user_id=self.user.id), response)

    def test_resume_page_get(self):
        '''
        Проверка шаблона страницы резюме
        '''

        response = self.client.get(self.resume_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'itmo_hh/resume_page.html')

