from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class UserCreateView(CreateView):
    template_name = 'account/signup.html'
    form_class=UserCreationForm
    success_url=reverse_lazy('account:register_done')

class UserCreateDoneTV(TemplateView):
    template_name='account/register_done.html'

def main(request):
    return render(request, 'information/main.html')
