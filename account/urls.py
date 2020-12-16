from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
import information.views

app_name = "account"
urlpatterns = [
    path('login/', LoginView.as_view(template_name ='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name ='account/logout.html'), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('register/done/', UserCreateDoneTV.as_view(), name='register_done'),
    path('', information.views.main, name="main"),
]
