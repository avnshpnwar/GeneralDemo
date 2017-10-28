from django.http.response import HttpResponseRedirect
from django.shortcuts import render


def homepage(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/db/uhome/")
    else:
        return HttpResponseRedirect("/db/auth/")
    
def bad_request(request):
    context = {}
    context['errorcode'] = '400 Bad Request'
    context['errormsg'] = 'Invalid Request!'
    return render(request, 'common/error.html', context)
    return render(request, '')

def permission_denied(request):
    context = {}
    context['errorcode'] = '403 Permission Denied'
    context['errormsg'] = 'Not authorized to view content!'
    return render(request, 'common/error.html', context)
    return render(request, '')

def page_not_found(request):
    context = {}
    context['errorcode'] = '404 Page Not Found'
    context['errormsg'] = 'Requested page not found!'
    return render(request, 'common/error.html', context)

def server_error(request):
    context = {}
    context['errorcode'] = '500 Server Internal Error'
    context['errormsg'] = 'Something wrong with server!'
    return render(request, 'common/error.html', context)
    return render(request, '')
