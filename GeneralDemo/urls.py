"""GeneralDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls import handler400, handler403, handler404, handler500  # @UnusedImport


urlpatterns = [
    url(r'^$',views.homepage),
    url(r'^db/$',views.homepage),
    url(r'^db/auth/',include('Auth.urls')),
    url(r'^db/uhome/',include('UserHome.urls')),
    url(r'^db/admin/', admin.site.urls),
]

handler400 = 'GeneralDemo.views.bad_request'
handler403 = 'GeneralDemo.views.permission_denied'
handler404 = 'GeneralDemo.views.page_not_found'
handler500 = 'GeneralDemo.views.server_error'