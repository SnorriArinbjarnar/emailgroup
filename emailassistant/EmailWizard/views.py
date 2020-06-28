from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import FormView, FormMixin
from EmailWizard.forms import AddCompanyForm, AddCompanyFormTwo
from EmailWizard.models import EmailGroup, Email

# Create your views here.
class HomeView(ListView):
    template_name = 'emailwizard/index.html'
    queryset = EmailGroup.objects.order_by('-created_at')
    context_object_name = 'emailgroups'

class GroupDetailView(FormMixin, DetailView):
    model = EmailGroup
    template_name = 'emailwizard/group_detail.html'
    form_class = AddCompanyFormTwo

    def get_success_url(self):
        return reverse('group_detail', kwargs={'pk': self.object.pk})

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs) 
        #group = EmailGroup.objects.get(pk = self.object.pk)
        #context['row'] = group.email_set.all().count()
        #return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        emailgroup = EmailGroup.objects.get(pk = self.object.pk)
        instance.emailgroup = emailgroup
        instance.save()
        return super().form_valid(form)
    
