from django.shortcuts import render, get_object_or_404, redirect
from .models import Information
from django.contrib import messages
from django.db.models import Q
from .forms import CommentForm
from .forms import SearchForm
from django.views.generic.edit import FormView

# Create your views here.

def main(request):
    return render(request, 'main.html')

def info(request):
    informations=Information.objects
    return render(request, 'information.html', {'informations':informations})

def event(request):
    return render(request, 'event.html')

def calendar(request):
    return render(request, 'mycalendar.html')

def search(request):
    information=Information.objects.all()
    query=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        if query:
            information=information.filter(Q(title__icontains=query)|Q(info_data__icontains=query))
    return render(request, 'search.html', {'information' : information, 'query' : query})



def detail(request, blog_id):
    blog_object=get_object_or_404(Information, pk=blog_id)
    return render(request, 'detail.html', {'information':blog_object})

def add_comment(request, blog_id):
    blog=get_object_or_404(Information, pk=blog_id)
    
    if request.method == "POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=blog
            comment.save()
            return redirect('detail', blog_id)
    else:
        form=CommentForm()
        return render(request, 'review.html', {'form':form})