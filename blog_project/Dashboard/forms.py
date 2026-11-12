from django import forms
from blogs.models import category,Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields =['title','category','featured_image','short_description','blog_body','is_featured']  

class userForm(UserCreationForm):
    class Meta:
        model= User
        fields =['username','first_name','last_name','email','is_active','is_staff','is_superuser','groups','user_permissions']     
