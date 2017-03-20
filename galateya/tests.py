from django.test import TestCase


class TestSelfTest(TestCase):
    def test_common(self):
        self.assertEqual(1+1, 2)
