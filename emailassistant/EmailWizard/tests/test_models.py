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

class CompanyEmailTest(TestCase):
    def setUp(self):
        # connect with an emailgroup
        self.emailgroup = EmailGroup.objects.create(
            title='test-emailgroup'
        )
        
    def test_string_representation(self):
        email = Email(company="Arcana", email="arcana@arcana.is", emailgroup=self.emailgroup)
        self.assertEqual(str(email), "Arcana:arcana@arcana.is")
    