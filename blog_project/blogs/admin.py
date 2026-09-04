from django.contrib import admin
from .models import Blog, category
# Register your models here.
admin.site.register(category)

class blogadmin_display(admin.ModelAdmin):
    prepopulated_fields ={'slug':('title',)}
    search_fields = ('id','title','category__category_name','status')
    list_display = ('title','category','status','is_featured')
    list_editable = ('is_featured',)



admin.site.register(Blog,blogadmin_display)
