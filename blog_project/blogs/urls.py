from django.urls import  path
from . import views
urlpatterns = [
    path('<int:category_id>/',views.category_pages,name ='category_pages')
]