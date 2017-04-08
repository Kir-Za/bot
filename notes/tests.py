from django.test import TestCase, Client
from django.db import transaction
from django.core.urlresolvers import reverse_lazy
from interface.models import OrdinaryUser
from .models import MyNote

test_user = 'Dummy'
test_password = '123'


class NotesViewTest(TestCase):
    def test_client(self):
        client_obj = Client()
        with transaction.atomic():
            client_obj.login(username=test_user, password=test_password)
        return client_obj

    def setUp(self):
        user = OrdinaryUser.objects.create_user(username=test_user, password=test_password)
        MyNote.objects.create(customer=user, title='Base note', keys='base', text_body='Add base note')

    def test_add_note_pos(self):
        client_obj = self.test_client()
        response = client_obj.post(
            reverse_lazy('note_add'),
            {'title': 'Test note', 'keys': 'note, test, all', 'text_body': 'Try add correct notee'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(MyNote.objects.all()), 2)

    def test_add_note_neg(self):
        client_obj = self.test_client()
        response = client_obj.post(
            reverse_lazy('note_add'),
            {'title': 'Base note', 'keys': 'note, test, all', 'text_body': 'Try add correct notee'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(MyNote.objects.all()), 1)

    def test_note_list(self):
        client_obj = self.test_client()
        response = client_obj.get(reverse_lazy('note_list', args=['last']))
        self.assertEqual(response.status_code, 200)

    def test_serch_api(self):
        client_obj = self.test_client()
        resopnse = client_obj.post(reverse_lazy('serach_api'), {'search_field': 'test'})
        self.assertEqual(resopnse.status_code, 302)

    def test_note_detail_pos(self):
        client_obj = self.test_client()
        note = MyNote.objects.all()[0]
        response = client_obj.get(reverse_lazy('note_detail', args=[note.pk]))
        self.assertEqual(response.status_code, 200)

    def test_note_detail_neg(self):
        client_obj = self.test_client()
        response = client_obj.get(reverse_lazy('note_detail', args=['10']))
        self.assertEqual(response.status_code, 404)

    def test_del_note(self):
        client_obj = self.test_client()
        note = MyNote.objects.all()[0]
        response = client_obj.post(reverse_lazy('note_del', args=[note.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(MyNote.objects.all()), 0)
