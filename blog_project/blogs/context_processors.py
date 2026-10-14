
from .models import Blog,category



     
def get_categories(request):
    categories = category.objects.all()
    return dict(categories=categories)

def searching(request):
    keyword = request.GET.get('keyword')
    print(keyword)
    return dict(keyword = keyword)