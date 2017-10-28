from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.homepage),
    url(r'^createaccount', views.createaccount),
    url(r'^addpayee', views.addpayee),
    url(r'^transfer', views.transfer),
    url(r'^email', views.email),
    url(r'^otp', views.otp),
]