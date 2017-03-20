from django.test import TestCase


class DBTest(TestCase):
    def test_db_exist(self):
        self.assertEqual(1+1, 2)
