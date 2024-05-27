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
        self.factory = RequestFactory()

        self.resume_list_url = reverse('personal_account')

        self.project_list_url = reverse('my_projects')

        self.resume_page_url = reverse('resume', args=[1])

        self.user1 = User.objects.create(username='testuser', password='12345')
        self.user2 = User.objects.create(username='testuser2', password='123452')

        self.sphere = Sphere.objects.create(name='Мобильные и сетевые технологии')
        self.napravlenie = Napravlenie.objects.create(name='Мобильная разработка')
        self.category1 = Category.objects.create(name='Конкурс')
        self.category2 = Category.objects.create(name='Проект')
        self.category3 = Category.objects.create(name='Стартап')

        self.resume1 = Resumes.objects.create(title='resume1', FIO='RESUME1', sex='women', birthday='2020-01-01',
                                              sphere=self.sphere, content='content1', napravlenie=self.napravlenie,
                                              education_level='bakalavriat', experience='no_experience', user_id=self.user1)

        self.project_project = Startapps_and_projects.objects.create(
            user_id=self.user1, title='pr1', header='pr1', sphere=self.sphere, experience='1-3',
            education_level='bakalavriat', category=self.category2, content='pr1', applied_users=5)

        self.project_competition = Startapps_and_projects.objects.create(
            user_id=self.user1, title='pr2', header='pr2', sphere=self.sphere, experience='1-3',
            education_level='bakalavriat', category=self.category1, content='pr2', applied_users=5)

        self.project_startapp = Startapps_and_projects.objects.create(
            user_id=self.user1, title='pr3', header='pr3', sphere=self.sphere, experience='1-3',
            education_level='bakalavriat', category=self.category3, content='pr3', applied_users=5)

        self.other_resume = Resumes.objects.create(title='resume-other', FIO='RESUME-OTHER', sex='women', birthday='2020-01-01',
                                              sphere=self.sphere, content='content1', napravlenie=self.napravlenie,
                                              education_level='bakalavriat', experience='no_experience', user_id=self.user2)
        self.other_project = Startapps_and_projects.objects.create(
            user_id=self.user2, title='pr-other', header='pr3', sphere=self.sphere, experience='1-3',
            education_level='bakalavriat', category=self.category3, content='pr3', applied_users=5)

    # Доделать, когда исправлю класс представления
    def test_my_offers_get(self):
        pass

    # Доделать, когда исправлю класс представления
    def test_my_otclics_get(self):
        pass

    #Тест для PerdonelAccount
    def test_personal_account(self):
        request = self.factory.get(reverse('personal_account'))
        request.user = self.user1
        self.resume2 = Resumes.objects.create(title='resume2', FIO='RESUME2', sex='women', birthday='2020-01-01',
                                              sphere=self.sphere, content='content2', napravlenie=self.napravlenie,
                                              education_level='bakalavriat', experience='no_experience',
                                              user_id=self.user1)
        view = PersonalAccount.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            list(response.context_data['resumes']),
            [repr(self.resume2), repr(self.resume1)],
            transform=repr
        )
        self.assertNotIn(self.other_resume, response.context_data['resumes'])

    # Тесты для MyProjects
    def test_my_projects(self):
        request = self.factory.get(reverse('my_projects'))
        request.user = self.user2
        view = MyProjects.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context_data['projects']), [self.other_project],)

    # Тесты для Startapp
    def test_startapp(self):
        request = self.factory.get(reverse('startapp'))
        request.user = self.user2
        view = Startapp.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context_data['projects']), [self.project_startapp])

    def test_startapp_filtering(self):
        request = self.factory.get(
            reverse('startapp') + '?experience=1-3&education_level=bakalavriat&sphere=Проект')
        request.user = self.user2
        view = Startapp.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        qs = Startapps_and_projects.objects.filter(category_id=3).filter(experience='1-3').filter(
            education_level='bakalavriat').filter(sphere=self.sphere).filter(user_id=self.user1)
        self.assertEqual(list(response.context_data['projects']), list(qs))

    # Тесты для Projects
    def test_projects(self):
        request = self.factory.get(reverse('project'))
        request.user = self.user2
        view = Projects.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context_data['projects']), [self.project_project])

    def test_projects_filtering(self):
        request = self.factory.get(
            reverse('project') + '?experience=1-3&education_level=bakalavriat&sphere=Проект')
        request.user = self.user2
        view = Projects.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        qs = Startapps_and_projects.objects.filter(category_id=2).filter(experience='1-3').filter(
            education_level='bakalavriat').filter(sphere=self.sphere).filter(user_id=self.user1)
        self.assertEqual(list(response.context_data['projects']), list(qs))

    # Тесты для Competitions
    def test_competitons(self):
        request = self.factory.get(reverse('competitions'))
        request.user = self.user2
        view = Competitions.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context_data['projects']), [self.project_competition])

    def test_competitions_filtering(self):
        request = self.factory.get(
            reverse('competitions') + '?experience=1-3&education_level=bakalavriat&sphere=Проект')
        request.user = self.user2
        view = Competitions.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        qs = Startapps_and_projects.objects.filter(category_id=1).filter(experience='1-3').filter(
            education_level='bakalavriat').filter(sphere=self.sphere).filter(user_id=self.user1)
        self.assertEqual(list(response.context_data['projects']), list(qs))

    # Тесты для Resume
    def test_resume(self):
        request = self.factory.get(reverse('resume'))
        request.user = self.user2
        view = Resume.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context_data['resumes']), [self.resume1])

    def test_resume_filtering(self):
        request = self.factory.get(
            reverse('resume') + '?experience=no_experience&education_level=bakalavriat&sphere=Проект')
        request.user = self.user2
        view = Resume.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        qs = Resumes.objects.filter(experience='no_experience').filter(
            education_level='bakalavriat').filter(sphere=self.sphere).filter(user_id=self.user1)
        self.assertEqual(list(response.context_data['resumes']), list(qs))

    # Тесты для PageOfProject
    def test_page_of_project(self):
        request = self.factory.get(reverse('project', kwargs={'project_id': self.project_project.id}))
        request.user = self.user1
        view = PageOfProject.as_view()
        response = view(request, project_id=self.project_project.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['project'], self.project_project)

    def test_page_of_project_is_owner(self):
        request = self.factory.get(reverse('project', kwargs={'project_id': self.project_project.id}))
        request.user = self.user1
        view = PageOfProject.as_view()
        response = view(request, project_id=self.project_project.id)
        self.assertEqual(response.context_data['is_owner'], True)

    def test_page_of_project_applied_resumes(self):
        project_application = ProjectApplication.objects.create(project=self.project_project, resume=self.resume1, status=0)
        request = self.factory.get(reverse('project', kwargs={'project_id': self.project_project.id}))
        request.user = self.user1
        view = PageOfProject.as_view()
        response = view(request, project_id=self.project_project.id)
        self.assertEqual(list(response.context_data['applied_resumes']), [project_application])

    def test_page_of_project_invited_resumes(self):
        project_invitation = ProjectInvitation.objects.create(project=self.project_project, resume=self.resume1, status=0)
        request = self.factory.get(reverse('project', kwargs={'project_id': self.project_project.id}))
        request.user = self.user1
        view = PageOfProject.as_view()
        response = view(request, project_id=self.project_project.id)
        self.assertEqual(list(response.context_data['invited_resumes']), [project_invitation])

    # Тесты для ResumePage
    def test_resume_page(self):
        request = self.factory.get(reverse('resume', kwargs={'resume_id': self.resume1.id}))
        request.user = self.user1
        view = ResumePage.as_view()
        response = view(request, resume_id=self.resume1.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['resume'], self.resume1)

    def test_resume_page_is_owner(self):
        request = self.factory.get(reverse('resume', kwargs={'resume_id': self.resume1.id}))
        request.user = self.user1
        view = ResumePage.as_view()
        response = view(request, resume_id=self.resume1.id)
        self.assertEqual(response.context_data['is_owner'], True)

    def test_resume_page_applied_resumes(self):
        project_application = ProjectApplication.objects.create(resume=self.resume1, project=self.project_project, status=0)
        request = self.factory.get(reverse('resume', kwargs={'resume_id': self.resume1.id}))
        request.user = self.user1
        view = ResumePage.as_view()
        response = view(request, resume_id=self.resume1.id)
        self.assertEqual(list(response.context_data['applied_resumes']), [project_application])

    def test_resume_page_invited_resumes(self):
        project_invitation = ProjectInvitation.objects.create(resume=self.resume1, project=self.project_project, status=0)
        request = self.factory.get(reverse('resume', kwargs={'resume_id': self.resume1.id}))
        request.user = self.user1
        view = ResumePage.as_view()
        response = view(request, resume_id=self.resume1.id)
        self.assertEqual(list(response.context_data['invited_resumes']), [project_invitation])

    # Тесты для delete_resume
    def test_delete_resume(self):
        request = self.factory.post(reverse('delete', kwargs={'resume_id': self.resume1.id}))
        request.user = self.user1
        response = delete_resume(request, resume_id=self.resume1.id)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('personal_account'))
        self.assertFalse(Resumes.objects.filter(id=self.resume1.id).exists())

    # Тесты для delete_project
    def test_delete_project(self):
        request = self.factory.post(reverse('delete-project', kwargs={'project_id': self.project_project.id}))
        request.user = self.user1
        response = delete_project(request, project_id=self.project_project.id)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('personal_account'))
        self.assertFalse(Startapps_and_projects.objects.filter(id=self.project_project.id).exists())

