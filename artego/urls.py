"""artego URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import information.views
import information.forms
# import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', information.views.main, name="main"),
    path('info/', information.views.info, name="info"),
    path('info/<int:blog_id>', information.views.detail, name="detail"),
    path('info/comment/<int:blog_id>', information.views.add_comment, name="add_comment"),
    path('search/', information.views.search, name="search"),
    path('account/', include('account.urls')),
]
