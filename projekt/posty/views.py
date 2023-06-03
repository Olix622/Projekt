from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def list_of_post(request):
    post = Post.objects.all()
    template = 'posty/posty.html'
    context = {'post': post}
    return render(request, template, context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    template = 'posty/posty_szczegoly.html'
    context = {'post': post}
    return render(request, template, context)