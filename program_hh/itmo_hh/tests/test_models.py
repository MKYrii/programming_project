from django.test import TestCase
from itmo_hh.models import *
from django.test import Client

class TestModels(TestCase):
    def setUp(self):
        client = Client()
        self.user = User.objects.create(username='testuser', password='12345')
        self.sphere = Sphere.objects.create(name='Мобильные и сетевые технологии')
        self.napravlenie = Napravlenie.objects.create(name='Мобильная разработка')
        self.category = Category.objects.create(name='Конкурс')

        self.resume1 = Resumes.objects.create(title='resume1', FIO='RESUME1', sex='women', birthday='2020-01-01',
                                              sphere=self.sphere, content='content1', napravlenie=self.napravlenie,
                                              education_level='bakalavriat', experience='no_experience',
                                              user_id=self.user)

        self.pr = Startapps_and_projects.objects.create(user_id=self.user, title='pr1', header='pr1', sphere=self.sphere,
                                                        experience='1-3', education_level='bakalavriat', content='pr1',
                                                        category=self.category, applied_users=5)
    def test_url_resume(self):
        self.client.force_login(user=self.user)
        w = self.resume1
        response = self.client.get(reverse('resume', args=[w.pk, ]))
        self.assertEqual(response.status_code, 200)

    def test_url_startapps_and_projects(self):
        self.client.force_login(user=self.user)
        w = self.pr
        response = self.client.get(reverse('project', args=[w.pk, ]))
        self.assertEqual(response.status_code, 200)
