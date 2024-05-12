from django.test import TestCase
from django.urls import reverse, resolve

from itmo_hh.views import *


class TestUrls(TestCase):
    def test_index(self):
        '''
        Проверка на корректность отображения главной страницы
        '''
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
    def test_personal_account(self):
        '''
        Проверка на корректность отображения страницы "Личный кабинет"
        '''
        url = reverse('personal_account')
        self.assertEqual(resolve(url).func.view_class, PersonalAccount)
    def test_registration(self):
        '''
        Проверка на корректность отображения страницы "Регистрация"
        '''
        url = reverse('registration')
        self.assertEqual(resolve(url).func, registration)
    def test_startapp(self):
        '''
        Проверка на корректность отображения страницы "Стартовая страница"
        '''
        url = reverse('startapp')
        self.assertEqual(resolve(url).func.view_class, Startapp)
    def test_project(self):
        '''
        Проверка на корректность отображения страницы "Проекты"
        '''
        url = reverse('project')
        self.assertEqual(resolve(url).func.view_class, Projects)
    def test_resume(self):
        '''
        Проверка на корректность отображения страницы "Резюме"
        '''
        url = reverse('resume')
        self.assertEqual(resolve(url).func.view_class, Resume)
    def test_my_projects(self):
        '''
        Проверка на корректность отображения страницы "Мои проекты"
        '''
        url = reverse('my_projects')
        self.assertEqual(resolve(url).func.view_class, MyProjects)
    def test_find_resume(self):
        url = reverse('find_resume')
        self.assertEqual(resolve(url).func.view_class, FindResume)

    def test_resume_project(self):
        url = reverse('resume_project')
        self.assertEqual(resolve(url).func, resume_project)

    def test_resume_person(self):
        url = reverse('resume_person')
        self.assertEqual(resolve(url).func, resume_person)
    def test_page_of_project(self):
        url = reverse('project', args=[1])
        self.assertEqual(resolve(url).func.view_class, PageOfProject)

    def test_my_offers(self):
        url = reverse('my_offers')
        self.assertEqual(resolve(url).func.view_class, MyOffers)

    def test_my_otclics(self):
        url = reverse('my_otclics')
        self.assertEqual(resolve(url).func.view_class, MyOtclics)

    def test_competitions(self):
        url = reverse('competitions')
        self.assertEqual(resolve(url).func.view_class, Competitions)
    def test_resume_page(self):
        url = reverse('resume', args=[1])
        self.assertEqual(resolve(url).func.view_class, ResumePage)
    def test_register(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)
    def test_login(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, LoginUser)
    def test_logout(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)
    def test_update_resume(self):
        url = reverse('update', args=[1])
        self.assertEqual(resolve(url).func.view_class, UpdateResume)

    def test_delete_resume(self):
        url = reverse('delete', args=[1])
        self.assertEqual(resolve(url).func, delete_resume)

    def test_delete_project(self):
        url = reverse('delete-project', args=[1])
        self.assertEqual(resolve(url).func, delete_project)

    def test_update_project(self):
        url = reverse('update-project', args=[1])
        self.assertEqual(resolve(url).func.view_class, UpdateProject)

    def test_otclic_on_project(self):
        url = reverse('otclic_on_project', args=[1])
        self.assertEqual(resolve(url).func, Otclic_on_project)

    def test_resume_invite(self):
        url = reverse('resume_invite', args=[1])
        self.assertEqual(resolve(url).func, resume_invite)

    def test_accept_invitation(self):
        url = reverse('accept_invitation', args=[1, 2])
        self.assertEqual(resolve(url).func, accept_invitation)

    def test_deny_invitation(self):
        url = reverse('deny_invitation', args=[1, 2])
        self.assertEqual(resolve(url).func, deny_invitation)

    def test_accept_application(self):
        url = reverse('accept_application', args=[1, 2])
        self.assertEqual(resolve(url).func, accept_application)

    def test_deny_application(self):
        url = reverse('deny_application', args=[1, 2])
        self.assertEqual(resolve(url).func, deny_application)

    def test_recall_invitation(self):
        url = reverse('recall_invitation', args=[1, 2])
        self.assertEqual(resolve(url).func, recall_invitation)

    def test_recall_application(self):
        url = reverse('recall_application', args=[1, 2])
        self.assertEqual(resolve(url).func, recall_application)