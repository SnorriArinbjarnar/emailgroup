from django.test import TestCase 
from EmailWizard.models import EmailGroup

class HomeViewTestCase(TestCase):
    """ Test wether email groups show up on page """
    def test_no_emailgroup(self):
        response = self.client.get('/emailForMe', follow=True)
        self.assertContains(response, 'No emailgroups added...')
    def test_one_emailgroup(self):
        EmailGroup.objects.create(title='1-title')
        response = self.client.get('/emailForMe', follow=True)
        self.assertContains(response, '1-title')

    def test_one_emailgroup(self):
        EmailGroup.objects.create(title='1-title')
        EmailGroup.objects.create(title='2-title')

        response = self.client.get('/emailForMe', follow=True)
        self.assertContains(response, '1-title')
        self.assertContains(response, '2-title')

class GroupViewTest(TestCase):
    def setUp(self):
        self.group = EmailGroup.objects.create(title='1-title')
    def test_basic_view(self):
        response = self.client.get(self.group.get_absolute_url())
        self.assertEqual(response.status_code, 200)
    def test_title(self):
        response = self.client.get(self.group.get_absolute_url())
        self.assertContains(response, self.group.title)
