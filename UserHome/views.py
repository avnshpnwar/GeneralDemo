from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models.aggregates import Max
from django.shortcuts import render

from . import forms
from . import models



# Create your views here.
@login_required
def homepage(request):
    return render(request,'UserHome/index.html')

@login_required
def createaccount(request):
    if request.method == 'POST':
        form = forms.createaccount(request.POST, request=request)
        postdic = request.POST
        if form.is_valid():
            latest_account_dict = models.user_account.objects.all().aggregate(Max('account_no'))
            latest_account_no = 1000001
            if latest_account_dict['account_no__max'] is not None:
                latest_account_no = latest_account_dict['account_no__max'] + 1
            ua = models.user_account(user=request.user, account_no = latest_account_no, account_name = postdic.get('account_name'))
            try:
                ua.save()
                context = {}
                context['msgtype'] = 's'
                context['title'] = 'Congrats!!!'
                context['text'] = 'Account Created Successfully'
                context['url'] = '/db/uhome/'
                return render(request, 'common/alert.html', context)
            except Exception as e:
                context = {}
                context['msgtype'] = 'f'
                context['title'] = 'Ooops!!!'
                context['text'] = 'Account creation failed. Cause - ' + str(e)
                context['url'] = '/db/uhome/'
                return render(request, 'common/alert.html', context)
        else:
            context = {}
            context['form'] = form
            return render(request, 'UserHome/createaccount.html', context)
    else:
        context = {}
        context['form'] = forms.createaccount()
        context['account_list'] = models.user_account.objects.filter(user=request.user)
        return render(request, 'UserHome/createaccount.html', context)
    
@login_required
def addpayee(request):
    if request.method == 'POST':
        form = forms.addpayee(request.POST, request=request)
        postdic = request.POST
        if form.is_valid():
            payee = models.payee_account(user=request.user, payee_name=postdic.get('name'), account_no=postdic.get('account_no'),)
            try:
                payee.save()
                context = {}
                context['msgtype'] = 's'
                context['title'] = 'Congrats!!!'
                context['text'] = 'Payee Added Successfully'
                context['url'] = '/db/uhome/'
                return render(request, 'common/alert.html', context)
            except Exception as e:
                context = {}
                context['msgtype'] = 'f'
                context['title'] = 'Ooops!!!'
                context['text'] = 'Cannot add payee. Cause - ' + str(e)
                context['url'] = '/db/uhome/'
                return render(request, 'common/alert.html', context)
        else:
            context = {}
            context['form'] = form
            context['payee_list'] = models.payee_account.objects.filter(user=request.user)
            return render(request, 'UserHome/addpayee.html', context)
    else:
        context = {}
        context['form'] = forms.addpayee()
        context['payee_list'] = models.payee_account.objects.filter(user=request.user)
        return render(request, 'UserHome/addpayee.html', context)
    
@login_required 
def transfer(request):
    if request.method == 'POST':
        initial_date = request.session.get('initial_date')
        form = forms.transfer(request.POST, request=request, initial_date=initial_date)
        postdic = request.POST
        if form.is_valid():
            context = {}
            context['formdata'] = postdic
            return render(request, 'common/formtest.html', context)
        else:
            context = {}
            context['form'] = form
            context['showform'] = True
            return render(request, 'UserHome/transfer.html', context)
            
    else:
        #check if user have account, and have atleast one payee account
        user_account_count = models.user_account.objects.filter(user_id=request.user).count()
        payee_account_count = models.user_account.objects.filter(user_id=request.user).count()
        if 0 in (user_account_count, payee_account_count):
            context = {}
            context['showform'] = False
            return render (request, 'UserHome/transfer.html', context)
        else:
            request.session['initial_date'] = datetime.now().strftime('%Y-%m-%d %H:%M')
            initial_date = request.session.get('initial_date')
            form = forms.transfer(initial={'transfer_date': initial_date}, request=request)
            context = {}
            context['showform'] = True
            context['form'] = form
            return render (request, 'UserHome/transfer.html', context)
        
@login_required 
def email(request):
    if request.method == 'POST':
        form = forms.email(request.POST)
        postdic = request.POST
        if form.is_valid():
            context = {}
            context['formdata'] = postdic
            return render(request, 'common/formtest.html', context)
        else:
            context = {}
            context['form'] = form
            return render(request, 'UserHome/email.html', context)
    else:
        form = forms.email()
        context = {}
        context['form'] = form
        return render (request, 'UserHome/email.html', context)
    
@login_required 
def otp(request):
    if request.method == 'POST': 
        form = forms.otp(request.POST, request=request)
        postdic = request.POST
        if form.is_valid():
            context = {}
            context['formdata'] = postdic
            return render(request, 'common/formtest.html', context)
        else: #form is invalid, send error back
            context = {}
            context['form'] = form 
            return render (request, 'UserHome/otp.html', context)
    else:
        context = {}
        from . import utils
        numotp = utils.get_random_numeric_string(length=8)
        strotp = utils.get_random_alphabetic_string(length=8)
        alnotp = utils.get_random_alphanumeric_string(length=8)
        request.session['numotp'] = numotp
        request.session['strotp'] = strotp
        request.session['alnotp'] = alnotp
        context['numotp'] = numotp
        context['strotp'] = strotp
        context['alnotp'] = alnotp
        form = forms.otp(request=request)
        context['form'] = form
        return render (request, 'UserHome/otp.html', context)