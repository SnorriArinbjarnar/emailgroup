from django.db import models
from django.urls import reverse

# Create your models here.
class EmailGroup(models.Model):
    title = models.CharField(max_length=500)
    # set field to now when created
    created_at = models.DateTimeField(auto_now_add=True)
    # set field to now when updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('group_detail', kwargs={'pk' : self.pk})

class Email(models.Model):
    company = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    # connected with Emailgroup (one to many)
    emailgroup = models.ForeignKey(EmailGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.company + ':' + self.email
    
