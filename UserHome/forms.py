from django import forms
from . import form_widget
from . import models

class createaccount(forms.Form):
    attrs = {'class':'custom-select',}
    account_choice = (('', ' --Select Account Type-- '), ('Saving', 'Saving'), ('Current', 'Current'), ('Salary', 'Salary'), ('Pension', 'Pension'),)
    account_name = forms.ChoiceField(choices = account_choice, label="", initial='', widget=form_widget.get_select_widget(attrs))
    
    #hack to add request data in form
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(createaccount, self).__init__(*args, **kwargs)
        
        
    def clean(self):
        allerror = []
        cleaned_data = super(createaccount, self).clean();
        act = cleaned_data.get('account_name')
            
        accountexist = models.user_account.objects.filter(user=self.request.user, account_name__iexact=act).exists()
        
        if accountexist:
            allerror.append(forms.ValidationError(('Account already exist'), code='invalid'))
            
        if allerror:
            raise forms.ValidationError(allerror)

class addpayee(forms.Form):
    name = forms.CharField(min_length=4, max_length=30, help_text='e.g Bill Gates')
    account_no = forms.IntegerField(min_value=1000000, max_value=9999999, help_text='e.g 7218294')
    
    #hack to add request data in form
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(addpayee, self).__init__(*args, **kwargs)
        
    def clean(self):
        allerror = []
        cleaned_data = super(addpayee, self).clean();
        act = cleaned_data.get('account_no')
        accountexist = models.payee_account.objects.filter(user=self.request.user, account_no=act).exists()
        
        if accountexist:
            allerror.append(forms.ValidationError(('Account already exist'), code='invalid'))
            
        if allerror:
            raise forms.ValidationError(allerror)
        
class transfer(forms.Form):
    attrs = {'class':'form-control', 'placeholder': 'e.g sorry, will not attend birthday'}
    sender_text = forms.CharField(30, 5, widget=form_widget.get_text_widget(attrs))
    del attrs['placeholder']
    transfer_date = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'], widget=form_widget.get_date_widget(attrs))
    attrs['placeholder'] = 'e.g. have a good one'
    receiver_text = forms.CharField(30, 5, widget=form_widget.get_text_widget(attrs))
    del attrs['placeholder']
    attrs['class'] = 'custom-control-input'
    agree = forms.BooleanField(widget=form_widget.get_checkbox_widget(attrs))
    
    def clean_transfer_date(self):
        user_date = self.cleaned_data['transfer_date'].strftime('%Y-%m-%d %H:%M')
        if (user_date < self.initial_date):
            raise forms.ValidationError(('Time cannot be in past'), code='invalid')
        return user_date
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.initial_date = kwargs.pop('initial_date', None)
        super(transfer, self).__init__(*args, **kwargs) 
        
        attrs = {'class':'form-control',}
        #get user account       
        from_account_list = []
        user_account_qs = models.user_account.objects.filter(user_id=self.request.user)
        for user_account_row in user_account_qs:
            account_description = "{} - {}".format(user_account_row.account_no, user_account_row.account_name)
            from_account_list.append((user_account_row.account_no, account_description))
        choice_tuple = tuple(from_account_list)
        self.fields['from_account'] = forms.ChoiceField(choices = choice_tuple, label='', initial='', widget=form_widget.get_select_widget(attrs))
        
        #get user account
        to_account_list= []       
        payee_account_qs = models.payee_account.objects.filter(user_id=self.request.user)
        for payee_account_row in payee_account_qs:
            account_description = "{} - {}".format(payee_account_row.account_no, payee_account_row.payee_name)
            to_account_list.append((payee_account_row.account_no, account_description))
        choice_tuple = tuple(to_account_list)
        self.fields['to_account'] = forms.ChoiceField(choices = choice_tuple, label='', initial='', widget=form_widget.get_select_widget(attrs))
        

class email(forms.Form):
    attrs = {'class':'custom-select',}
    subject_choices = (('', '   --Select Subject--   '), 
                      ('cards', 'Cards'), 
                      ('ebanking', 'eBanking'), 
                      ('mbanking', 'Mobile Banking'), 
                      ('others', 'Others'),)
    subject = forms.ChoiceField(choices = subject_choices, label="", initial='', widget=form_widget.get_select_widget(attrs))
    attrs['class'] = 'form-control'
    attrs['rows'] = '10'
    body = forms.CharField(1000, 10, widget = form_widget.get_textarea_widget(attrs))
     

class otp(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(otp, self).__init__(*args, **kwargs) 
        otplabel = '{} - {}'.format('Enter OTP', self.request.session.get('numotp'))
        self.fields['numotp'] = forms.CharField(min_length=8, max_length=8, label=otplabel, help_text=self.request.session.get('numotp'))
        self.fields['numotph'] = forms.CharField(initial=self.request.session.get('numotp'), widget=forms.HiddenInput())
        otplabel = '{} - {}'.format('Enter OTP', self.request.session.get('strotp'))
        self.fields['strotp'] = forms.CharField(min_length=8, max_length=8, label=otplabel, help_text=self.request.session.get('strotp'))
        self.fields['strotph'] = forms.CharField(initial=self.request.session.get('strotp'), widget=forms.HiddenInput())
        otplabel = '{} - {}'.format('Enter OTP', self.request.session.get('alnotp'))
        self.fields['alnotp'] = forms.CharField(min_length=8, max_length=8, label=otplabel, help_text=self.request.session.get('alnotp'))
        self.fields['alnotph'] = forms.CharField(initial=self.request.session.get('alnotp'), widget=forms.HiddenInput())
    
    def clean_numotp(self):
        user_numotp = self.cleaned_data['numotp']
        if user_numotp != self.request.session.get('numotp'):
            raise forms.ValidationError(('Wrong OTP entered'), code='invalid')
    def clean_strotp(self):
        user_strotp = self.cleaned_data['strotp']
        if user_strotp != self.request.session.get('strotp'):
            raise forms.ValidationError(('Wrong OTP entered'), code='invalid')
    def clean_alnotp(self):
        user_alnotp = self.cleaned_data['alnotp']
        if user_alnotp != self.request.session.get('alnotp'):
            raise forms.ValidationError(('Wrong OTP entered'), code='invalid')
            
            