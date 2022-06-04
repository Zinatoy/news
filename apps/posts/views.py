from django.shortcuts import render
from apps.posts.models import News, Category

# Create your views here.
def index(request):
    news = News.objects.all()
    category = Category.objects.all()
    
    context = {
        'news': news,
        'categories': category,
    }
    return render(request,'index.html',context)

def  category_detail(request, id):
    news = News.objects.get(id=id)
    category = Category.objects.get(id=id)
    context = {
        'news': news,
        'category': category
    }
    return render(request, 'category.html', context)