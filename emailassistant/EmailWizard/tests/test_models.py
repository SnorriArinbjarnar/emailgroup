from django.test import TestCase

from ..models import Email, EmailGroup 

class EmailGroupTest(TestCase):

    def test_string_representation(self):
        # Making sure we have changed __str__
        # so it gives somethinb better than Object object 
        emailgroup = EmailGroup(title="group1")
        self.assertEqual(str(emailgroup), emailgroup.title)

    def test_get_absolute_url(self):
        group = EmailGroup.objects.create(title='Initial Title')
        self.assertIsNotNone(group.get_absolute_url())