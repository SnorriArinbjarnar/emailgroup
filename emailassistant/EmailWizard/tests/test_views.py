from django.test import TestCase 
from EmailWizard.models import EmailGroup, Email
from django.urls import reverse

class HomeViewTestCase(TestCase):
    """ Test wether email groups show up on page """
    def test_no_emailgroup(self):
        response = self.client.get('/emailForMe', follow=True)
        self.assertContains(response, 'No emailgroups added...')
    def test_one_emailgroup(self):
        EmailGroup.objects.create(title='1-title')
        response = self.client.get('/emailForMe', follow=True)
        self.assertContains(response, '1-title')

    def test_two_emailgroups(self):
        EmailGroup.objects.create(title='1-title')
        EmailGroup.objects.create(title='2-title')

        response = self.client.get('/emailForMe', follow=True)
        self.assertContains(response, '1-title')
        self.assertContains(response, '2-title')

class GroupListTest(TestCase):
    def setUp(self):
        self.group = EmailGroup.objects.create(title='1-title')
    def test_basic_view(self):
        response = self.client.get(self.group.get_absolute_url())
        self.assertEqual(response.status_code, 200)
    def test_title(self):
        response = self.client.get(self.group.get_absolute_url())
        self.assertContains(response, self.group.title)

class GroupDetailTest(TestCase):
    def setUp(self):
        self.group = EmailGroup.objects.create(title='1-title')
       # self.response = self.client.get(self.group.get_absolute_url(), follow=True)
        self.response = self.client.get(reverse('group_detail', args=(self.group.id,)))
    def test_no_emails(self):
        self.assertContains(self.response, 'No companies added yet')
    def test_one_email(self):
        email = Email(company="Arcana", email="arcana@arcana.is", emailgroup=self.group)
        email.save()
        response = self.client.get(reverse('group_detail', args=(self.group.id,)))
        self.assertContains(response, email.company + ':' + email.email)


    


