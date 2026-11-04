from django.shortcuts import render

from blogs.models import category,Blog
from .forms import CategoryForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = 'login')
def dashboard(req):
    categories = category.objects.all().count()
    posts = Blog.objects.all().count()

    context ={
        'categories': categories,
        'posts': posts
    }
    
    return render(req,'Dashboard/dashboard.html',{'context':context})

def categories(req):
    return render(req,'Dashboard/DashCategories.html')


def add_categories(req):

    form = CategoryForm()
    return render(req,'Dashboard/add_categories.html',{'form':form})