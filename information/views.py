from django.shortcuts import render, get_object_or_404, redirect
from .models import Information
from django.contrib import messages
from django.db.models import Q
from .forms import CommentForm

# Create your views here.

def main(request):
    return render(request, 'main.html')

def info(request):
    informations=Information.objects
    return render(request, 'information.html', {'informations':informations})

def search(request):
    
    informations=None
    query=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        informations = Informations.objects.all().filter(Q(title__icontains=q) | Q(info_data__icontaions=q)).distinct()
        return render(request, 'search.html', {'informatinos' : informations, 'query' : query})
    
    else:
        return render(request, 'search.html')

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