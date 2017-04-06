from django.test import TestCase, Client, utils
from django.db import transaction
from interface.models import OrdinaryUser


class InterfaceRedirectTest(TestCase):
    def setUp(self):
        user = OrdinaryUser.objects.create_user(username='Dummy', password='123')

    def test_main_view_neg(self):
        client_obj = Client()
        response = client_obj.post('/login/', {'main_field': 'bad_user'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/')

    def test_main_view_pos(self):
        client_obj = Client()
        response = client_obj.post('/login/', {'main_field': 'Dummy'})
        self.assertEqual(response.status_code, 200)

    def test__main_view_pos_next(self):
        client_obj = Client()
        response = client_obj.post('/login/', {'main_field': '123', 'ex_user_name': 'Dummy'})
        self.assertEqual(response.url, '/menu/')

    def test_menu_login_pos(self):
        client_obj = Client()
        with transaction.atomic():
            client_obj.login(username='Dummy', password='123')
        response = client_obj.get('/menu/')
        self.assertEqual(response.status_code, 200)

    def test_menu_login_neg(self):
        client_obj = Client()
        response = client_obj.get('/menu/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/?next=/menu/')
