from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import category, Blog
from django.db.models import Q
# Create your views here.
def home(req):
   Blog_Details = Blog.objects.filter(is_featured=True)
   

   Blog_non_featured = Blog.objects.filter(is_featured=False)
  
   

   return render(req,'home.html',{'Blog_Details':Blog_Details,'Blog_non_featured':Blog_non_featured})




def category_pages(req,category_id):
  try:

      context = Blog.objects.filter(category = category_id)
      print(context)
      category_ids = Blog.objects.get(pk=category_id)
      
      
      return render(req,'category_pages.html',{'context':context,'category_ids':category_ids})
  except:
      return render(req,'category_pages.html')
    


def single_blog(req,slug):
    # title_data = Blog.objects.filter(pk=slug)
    slug_data = get_object_or_404(Blog,slug=slug)
    return render(req,'blogs.html',{'slug_data':slug_data})
def search_field(req):
   keyword =req.GET.get('keyword')
   search_matching = Blog.objects.filter(Q(title__icontains = keyword)|Q(short_description__icontains = keyword)|Q( blog_body__icontains = keyword))

   context={
      'keyword':keyword,
      'search_matching':search_matching
   }
   
   return render(req,'search.html',context)