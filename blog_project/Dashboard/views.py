from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
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

    if req.method == 'POST':
        form = CategoryForm(req.POST)
        
        if form.is_valid():
            form.save()
            return redirect('categories')
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    return render(req,'Dashboard/add_categories.html',{'form':form})


def edit_category(req,pk):
    cat = get_object_or_404(category,id=pk)

    if req.method == 'POST':
      form = CategoryForm(req.POST,instance=cat)
      if form.is_valid():
         form.save()
         return redirect('categories')
      else:
          print(form.errors)
    else:
      
        form = form = CategoryForm(instance=cat)



    return render(req,'Dashboard/editCategory.html',{'form':form,'cat':cat})


def delete_category(req,pk):
    obj = get_object_or_404(category,pk=pk)
    obj.delete()
    return redirect('categories')