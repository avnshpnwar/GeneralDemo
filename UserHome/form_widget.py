from django import forms

def get_text_widget(attrs):
    custom_widget = forms.TextInput(attrs=attrs)
    return custom_widget

def get_number_widget(attrs):
    custom_widget = forms.NumberInput(attrs=attrs)
    return custom_widget
    
def get_pwd_widget(attrs):
    custom_widget = forms.PasswordInput(attrs=attrs)
    return custom_widget 
    
def get_email_widget(attrs):
    custom_widget = forms.EmailInput(attrs=attrs)
    return custom_widget

def get_date_widget(attrs): 
    custom_widget = forms.DateInput(attrs=attrs)
    return custom_widget

def get_multiple_box_widget(attrs):
    custom_widget = forms.SelectMultiple(attrs=attrs)
    return custom_widget

def get_radio_widget(attrs):
    custom_widget = forms.RadioSelect(attrs=attrs)
    return custom_widget

def get_select_widget(attrs):
    custom_widget = forms.Select(attrs=attrs)
    return custom_widget

def get_checkbox_widget(attrs):
    custom_widget = forms.CheckboxInput(attrs=attrs)
    return custom_widget 

def get_textarea_widget(attrs):
    custom_widget = forms.Textarea(attrs= attrs)
    return custom_widget
