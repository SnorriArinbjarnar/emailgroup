from django.test import TestCase

from ..models import Email, EmailGroup 

class EmailGroupTest(TestCase):

    def test_string_representation(self):
        emailgroup = EmailGroup(title="group1")
        self.assertEqual(str(emailgroup), emailgroup.title)