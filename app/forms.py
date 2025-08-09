from django import forms
from .models import *

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email','phone', 'service', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Lead.objects.filter(email=email).count() > 5:
            raise forms.ValidationError("Too many entries with this email.")
        return email
