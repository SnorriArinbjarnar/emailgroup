from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView 
from EmailWizard.models import EmailGroup, Email

# Create your views here.
class HomeView(ListView):
    template_name = 'emailwizard/index.html'
    queryset = EmailGroup.objects.order_by('-created_at')
    context_object_name = 'emailgroups'

class GroupDetailView(DetailView):
    model = EmailGroup
    template_name = 'emailwizard/group_detail.html'
    
