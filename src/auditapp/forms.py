from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import AuditStandard, AuditRequirements, Checklist, CRA




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateAuditStandardForm(ModelForm):
    class Meta:
        model = AuditStandard
        fields = '__all__'

class CreateAuditRequirementsForm(ModelForm):
    class Meta:
        model = AuditRequirements
        fields = '__all__'
class CreateChecklistForm(ModelForm):
    class Meta:
        model = Checklist
        fields = '__all__'

class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget = forms.Textarea)

class CRAForm(ModelForm):
    class Meta:
        model = CRA
        fields = '__all__'
