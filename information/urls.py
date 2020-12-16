from django.contrib import admin
from django.urls import path, include
import information.views
import information.forms
# import account.views

urlpatterns = [
    path('search/', information.views.SearchFormView.as_view(), name='search'),
]
