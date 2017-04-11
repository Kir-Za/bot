from django.test import TestCase, Client
from django.db import transaction
from django.core.urlresolvers import reverse_lazy, reverse
from interface.models import OrdinaryUser


class InterfaceViewTest(TestCase):
    def setUp(self):
        OrdinaryUser.objects.create_user(username='Dummy', password='123')

    def test_main_view_neg(self):
        client_obj = Client()
        response = client_obj.post(reverse_lazy('login_page'), {'main_field': 'bad_user'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login_page'))

    def test_main_view_pos(self):
        client_obj = Client()
        response = client_obj.post(reverse_lazy('login_page'), {'main_field': 'Dummy'})
        self.assertEqual(response.status_code, 200)

    def test__main_view_pos_next(self):
        client_obj = Client()
        response = client_obj.post(reverse_lazy('login_page'), {'main_field': '123', 'ex_user_name': 'Dummy'})
        self.assertEqual(response.url, reverse('note_list'))

    def test_menu_login_pos(self):
        client_obj = Client()
        with transaction.atomic():
            client_obj.login(username='Dummy', password='123')
        response = client_obj.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)

    def test_menu_login_neg(self):
        client_obj = Client()
        response = client_obj.get(reverse('note_list'))
        self.assertEqual(response.status_code, 302)
