from django import forms
from .models import Event, Comment
from django.contrib.auth.models import User
from django.contrib.admin import widgets   
from django.utils import timezone
                             


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('Name', 'Email', 'Body')


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Enter password'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Enter password again'}))
    
    class Meta:
        model = User
        fields = {
            'username',
            'first_name', 
            'last_name',  
            'email',
        }

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")
        return confirm_password

from django.forms.widgets import DateTimeInput

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name','description','img', 'start_time','category','appointment_time']
        widgets = {
            'appointment_time': DateTimeInput(attrs={'type': 'date'}),
            'start_time': DateTimeInput(attrs={'type': 'time'}),
            
        }
    
    def clean(self):
        super().clean()
        print(self.cleaned_data)