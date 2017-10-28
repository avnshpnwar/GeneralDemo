from django import forms
from Auth import form_widget
from django.contrib.auth.models import User
import re
from django.core.validators import RegexValidator

class Logon(forms.Form):
    attrs = {"class":"form-control", "placeholder": "username", "autofocus":""}
    uid = forms.CharField(max_length=10, min_length=4, widget=form_widget.get_text_widget(attrs))
    del attrs["autofocus"]
    
    attrs["placeholder"] = "password"
    pwd = forms.CharField(max_length=10, min_length=4, widget=form_widget.get_pwd_widget(attrs))
    
class Registration(forms.Form):
    attrs = {"class":"form-control", "placeholder": "username", "autofocus":""}
    uid = forms.CharField(validators=[RegexValidator(regex='^[a-z]+$',message='No space in UserId'),], 
                        max_length=10, min_length=4, widget=form_widget.get_text_widget(attrs))
    del attrs["autofocus"]
    
    attrs["placeholder"] = "enter password"
    pwda = forms.CharField(max_length=10, min_length=4, widget=form_widget.get_pwd_widget(attrs))
    
    attrs["placeholder"] = 'confirm password'
    pwdb = forms.CharField(max_length=10, min_length=4, widget=form_widget.get_pwd_widget(attrs))
    
    def clean(self):
        cleaned_data = super(Registration, self).clean();
        userid = cleaned_data.get('uid')
        pwda = cleaned_data.get('pwda')
        pwdb = cleaned_data.get('pwdb')
        allerror = []
        if (pwda != pwdb):
            allerror.append(forms.ValidationError(('Password do not match'), code='invalid'))
        
        #check if user already exist
        is_user_exist = User.objects.filter(username=userid).exists()
        if is_user_exist:
            allerror.append(forms.ValidationError(('User already exist'), code='invalid'))
        if allerror:
            raise forms.ValidationError(allerror)
        