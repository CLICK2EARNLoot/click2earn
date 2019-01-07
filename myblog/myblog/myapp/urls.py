from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('signup/',views.signup),
    path('sign_up',views.sign_up),
    path('log_in',views.log_in),
    path('login/',views.login),
    path('payout/',views.payout),
    path('about/',views.about),
    path('contact/',views.contact),

]