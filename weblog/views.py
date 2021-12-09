from django.shortcuts import render
from . models import Blog

def home(request):
    blogs = Blog.objects.all()
    print(blogs)
    context = { 'blogs': blogs }
    return render(request, 'output.html', context)
