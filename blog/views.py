from django.shortcuts import render
from . models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5]
    
    return render(request, 'blogs/all_blogs.html', {'blogs':blogs})