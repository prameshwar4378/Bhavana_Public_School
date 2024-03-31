
from django import forms
from django.contrib.auth.forms  import AuthenticationForm
from .models import DB_Alumni, DB_Enqueries,DB_Career
class login_form(AuthenticationForm):
    username=forms.CharField(label='username',widget=forms.TextInput(attrs={'class':'form-control radius','placeholder':'Enter Username'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control radius','placeholder':'Enter Password'}))


class Enquiry_form(forms.ModelForm):
    class Meta:
        model = DB_Enqueries
        fields = '__all__'



class Career_form(forms.ModelForm):
    class Meta:
        model = DB_Career
        fields = '__all__'


class Alumni_form(forms.ModelForm):
    class Meta:
        model = DB_Alumni
        fields = '__all__'

