
from django import forms 
from EmailWizard.models import EmailGroup, Email

class AddCompanyForm(forms.Form):
    companyName = forms.CharField(max_length=100, label='Company Name:')
    companyEmail = forms.EmailField(required=True, label='Company Email Address:')

class AddCompanyFormTwo(forms.ModelForm):
    class Meta:
        model = Email 
        #fields = ['company', 'email', 'emailgroup']
        fields = ['company', 'email']

        def __init__(self, *args, **kwargs):
            self.emailgroup = kwargs.pop('pk')
            #
            #super(AddCompanyFormTwo, self).__init__(*args, **kwargs)
            #self.fields['emailgroup'] = self.emailgroup
            #self.emailgroup = self.kwargs['pk']
            #pass

        def save(self, commit=True):
            instance = super(AddCompanyFormTwo, self).save(commit=False)
            instance.save()
            return instance